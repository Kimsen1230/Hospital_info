import streamlit as st

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFacePipeline
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, CSVLoader, JSONLoader
from transformers import pipeline

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Hospital AI Assistant",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 Hospital AI Assistant")
st.write("Ask about doctors, treatments, costs, schedules, and facilities.")

# ---------------------------
# Load RAG Chain (Cached)
# ---------------------------
@st.cache_resource
def load_rag_chain():

    # 1️⃣ Load documents
    docs = []
    docs += TextLoader("doctors_list.txt").load()
    docs += TextLoader("hospital_facilities.txt").load()
    docs += TextLoader("services_list.txt").load()
    docs += TextLoader("hospital_faqs.txt").load()
    docs += TextLoader("disease_doctor_mapping.txt").load()
    docs += CSVLoader("doctor_specialization.csv").load()
    docs += CSVLoader("treatment_costs.csv").load()
    docs += JSONLoader(
        file_path="doctor_schedule.json",
        jq_schema=".[]",
        text_content=True
    ).load()

    # 2️⃣ Split documents
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(docs)

    # 3️⃣ Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # 4️⃣ FAISS
    vectorstore = FAISS.from_documents(chunks, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # 5️⃣ LLM
    hf_pipeline = pipeline(
        "text2text-generation",
        model="google/flan-t5-base",
        max_new_tokens=128,
        temperature=0.0,
        do_sample=False
    )
    llm = HuggingFacePipeline(pipeline=hf_pipeline)

    # 6️⃣ Prompt
    prompt = ChatPromptTemplate.from_template(
        """You are a hospital assistant.

Use ONLY the information given in the context.
Do NOT guess or invent numbers.
DO NOT output only numbers.
DO NOT change currency.
Do NOT add extra details.
If answer is not present say: I dont know.

If the treatment cost is present, respond EXACTLY in this format:
"This treatment will cost you $<cost>."

If the cost is not found, respond:
"I don't know the cost of this treatment".

Context:
{context}

Question: {question}
Answer:
"""
    )

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    # 7️⃣ RAG Chain
    rag_chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain


rag_chain = load_rag_chain()

# ---------------------------
# Initialize Chat History
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------
# Display Chat History
# ---------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------------------
# Chat Input (NO refresh needed)
# ---------------------------
user_query = st.chat_input("Ask your question...")

if user_query:
    # Store user message
    st.session_state.messages.append(
        {"role": "user", "content": user_query}
    )

    with st.chat_message("user"):
        st.markdown(user_query)

    # Generate answer
    with st.spinner("Thinking..."):
        answer = rag_chain.invoke(user_query)

    # Store assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant"):
        st.markdown(answer)


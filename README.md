# 🏥 AI Medical Receptionist (RAG + Streamlit)

An AI-powered Medical Receptionist application built using **Retrieval-Augmented Generation (RAG)**, **LangChain**, and **Streamlit**.  
The system answers hospital and clinic-related queries such as doctor availability, treatments, costs, and services using local data sources.

---

## 📌 Project Overview

Many hospitals and clinics lack efficient digital reception systems. This project aims to solve that problem by providing an intelligent AI assistant that can respond to patient queries in real time.

The application retrieves relevant information from local documents and generates accurate, context-aware responses using a Large Language Model. A simple Streamlit-based UI allows users to interact with the system easily.

This project is developed mainly for **learning, experimentation, and portfolio purposes**, focusing on real-world GenAI use cases.

---

## ✨ Features

- Retrieval-Augmented Generation (RAG) architecture  
- Doctor availability and specialization queries  
- Treatment and cost information lookup  
- Hospital facilities and services information  
- Local document-based knowledge (no web dependency)  
- Simple and interactive Streamlit UI  

---

## 🛠 Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **FAISS** (Vector Database)
- **HuggingFace Transformers**
- **Sentence Transformers**

---

## 📂 Project Structure

Hospital_info/
│── app.py
│── requirements.txt
│── data/
│── src/
│── README.md

yaml
Copy code

---

## 🚀 How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Kimsen1230/Hospital_info.git
cd Hospital_info
2️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Run the application
bash
Copy code
streamlit run app.py
🌐 Live Demo
👉 Deployed on Streamlit Cloud
(Add your Streamlit Cloud URL here once deployed)

arduino
Copy code
https://your-app-name.streamlit.app

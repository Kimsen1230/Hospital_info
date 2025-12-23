import streamlit as st 
st.header("This is header")
#st.write("Hi i am saif!")
st.title("This is my World!")
#st.write(7860)
#st.text("Welcome all to my dreamland")
#st.markdown("List your dream here")
#st.success("Whoope your dream is great")
#st.info('Do not share if your dream is personal')
#st.warning('Your dream is not good!!!')
#st.error('Sorry!! Your dream have bad things')
#name = st.text_input("Enter Your message")
#st.write("Hello",name)
#if st.button('click me'):
#    st.write("Button is clicked")
#age = st.slider("Your age",20,35,40)
#st.write('Select your age',age)
#choice = st.selectbox("Pick one",['A','B','C'])
#st.write('You choose',choice)
#if st.checkbox("Show/Hide"):
 #   st.text('Showing the data')
#status = st.radio("Select Gender:",['Male',['Female']])
#if status=='Male':
 #   st.success('Your gender is male')
#else:
 #   st.success("Your gender is female")

#st.sidebar.title("Users Settings")
#name = st.sidebar.text_input("Enter your name")
#age = st.sidebar.slider("select your age",18,25,30)
#st.write("Your name is :",name)
#st.write("Your age is :",age)
#st.subheader("This is Sub-header")

#st.title("We are creating columns")
#col1,col2 = st.columns(2)
#with col1:
 #  st.header("Column 1")
  #  st.write("This is first column")
#with col2:
  #  st.header("Column 2")
  #  st.write("This is Second Column")

#st.title("Simple form creation")
#with st.form("User_registration_form"):
 #   name = st.text_input("Enter your name:")
  #  age = st.number_input("Enter your age:",min_value=1)
  #  submitted = st.form_submit_button('Submit')
#if submitted:
 #   st.write("Name",name)
  #  st.write("Age",age)

#st.title('Session State Example')
#if 'count' not in st.session_state:
 #   st.session_state.count = 0
#if st.button("Increase"):
 #   st.session_state.count +=1
#st.write('Count value:',st.session_state.count)

#with st.chat_message('User'):
 #   st.write('Hello!')
#with st.chat_message('Assistant'):
 #   st.write("Hi! How i can help you?")

st.title("Simple Chat App")
if 'messages' not in st.session_state:
    st.session_state.messages=[]
for msg in st.session_state.messages:
    with st.chat_message(msg['role']):
        st.write(msg['content'])
user_input = st.chat_input("Say Something")

if user_input:
    st.session_state.messages.append(
        {'role':'user','content':user_input}
    )
    st.session_state.messages.append(
        {'role':'Assistant','content':"You Said"+user_input}
    )

    st.rerun()
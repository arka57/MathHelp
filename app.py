import streamlit as st
import openai
from decouple import config

api_key=config("OPENAI_API_KEY")

openai.api_key=api_key

def ask_math_question(question):
  #create conversation
  conversation=[
      {"role":"system","content": "You are a math tutor."},
      {"role":"user","content":question}
  ]

    #create response
  response=openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=conversation
  )
  reply=response['choices'][0]['message']['content']
  return reply


def main():
  st.title("MathGPT-User Assistant")
  
  user_profile={
    "language":"English"
  }
  st.sidebar.header("User profie Setting")
  user_profile['language'] =st.selectbox("Language",['English','Spanish','French'])

  #user input button
  st.subheader("Ask a Math question")

  question=st.text_area("Write your question here..",height=150,key="math_questions")

  if st.button("Submit"):
    answer=ask_math_question(question)

    #display the answer
    st.write(f"**Answer:**{answer}")


if __name__=='__main__':
  main()
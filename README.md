MathHelp

It is a user friendly tool for solving any mathematical problems.
User can ask any maths related question and the tool will return the answer 

Developed the  application using Langchain framework and GPT 3.5 

Features:

--User can enter any mathematical query 
--Query is sent to GPT 3.5 model and answer is returned

Execution Steps:

1)Clone the repository
Project repo: https://github.com/arka57/MathHelp

2) Create a virtual environment after opening the repository
conda create -n mchatbot python=3.8 -y
conda activate mchatbot

3) Install the requirements
pip install -r requirements.txt

4)Create a .env file in the root directory and add your OpenAI credentials as follows:
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


5)Run streamlit run app.py

6)Give the query and answer will be returned


Example

Technologies Used:

--Langchain
--GPT 3.5
--Python
--Streamlit
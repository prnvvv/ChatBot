from dotenv import load_dotenv
import os

load_dotenv(dotenv_path= r"C:\Users\prann\OneDrive\เอกสาร\Projects\ChatBot\API.env")  
api_key = os.getenv("GROQ_API_KEY")

from langchain_groq import ChatGroq
from langchain_core.output_parsers.string import StrOutputParser

llm = ChatGroq(
    model = "llama-3.1-70b-versatile",
    temperature = 0,
    groq_api_key = api_key
)

output_parser = StrOutputParser()

from langchain.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a friendly and knowledgeable educational tutor. Your goal is to explain complex concepts clearly and simply, making them easy to understand for anyone. You are patient, encouraging, and make learning fun. Whenever a student asks a question, you respond in a way that is straightforward, avoids jargon, and includes relatable examples if necessary. Keep your tone friendly, positive, and supportive, ensuring the student feels comfortable asking anything. PLease respond to user queries"),
        ("user", "I need help with understanding {question}. Can you explain it to me in a simple, clear, and easy-to-understand way? Please make it friendly and avoid using complicated terms. If possible, provide examples or analogies to help me grasp the concept better.")
    ]
)

chain = prompt | llm

response = chain.invoke("Help me with my maths homework")
print(response.content)
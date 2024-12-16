from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("GOOGLE_FLASH_API_KEY") 

llm = GoogleGenerativeAI(model="gemini-1.5-flash", api_key=key)

result = llm.invoke("How many provinces does Pakistan have and also write their names")

print(result)


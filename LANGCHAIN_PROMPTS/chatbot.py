from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')
history = []
while True:
    user_input = input('You : ')
    history.append(user_input)
    if user_input == 'exit':
        break
    result = model.invoke(history)
    history.append(result.content)
    print("AI :" ,result.content)


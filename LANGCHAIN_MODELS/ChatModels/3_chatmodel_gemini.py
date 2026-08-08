from langchain_google_genai import ChatGoogleGenerativeAI

# Use the 2026 stable name
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-8b", 
    google_api_key="AIzaSyDtQqMSJbp_ZAHMq3MQgCG_YdrXFxXusqY"
)

result = model.invoke("What is the Capital of India?")
print(result.content)

import google.generativeai as genai
import os

# Replace with your actual key or ensure your ENV variable is set
api_key = os.getenv("AIzaSyDtQqMSJbp_ZAHMq3MQgCG_YdrXFxXusqY") 
genai.configure(api_key=api_key)

print("--- Models available for your API Key ---")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"Model ID: {m.name}")
except Exception as e:
    print(f"Error fetching models: {e}")
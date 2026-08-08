from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


review_schema = {
    "title": "ReviewAnalysis",
    "description": "Analyze customer review in structured JSON format",
    "type": "object",
    "properties": {
        "summary": {
            "type": "string",
            "description": "Concise summary of the review"
        },
        "sentiment": {
            "type": "string",
            "description": "Positive, Negative, or Neutral"
        },
        "sentiment_score": {
            "type": "number",
            "description": "Score between -1 and 1"
        },
        "pros": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Positive aspects mentioned"
        },
        "cons": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Negative aspects mentioned"
        }
    },
    "required": ["summary", "sentiment", "pros", "cons"]
}

structured_model = model.with_structured_output(
    review_schema,
    method="json_schema"
)

review_text = """
The hardware is great, but the software feels bloated.
Too many pre-installed apps and the UI looks outdated.
"""

result = structured_model.invoke(review_text)

print(result)          
print(result["summary"])  
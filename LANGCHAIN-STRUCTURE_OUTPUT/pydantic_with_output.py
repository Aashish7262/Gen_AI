from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel , Field


load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

class ReviewAnalysis(BaseModel):
    summary: str = Field(description="Concise summary of the review")
    sentiment: str = Field(description="Overall sentiment: Positive, Negative, or Neutral")
    sentiment_score: float = Field(description="Sentiment score range from -1 to 1")
    pros: List[str] = Field(description="List of positive aspects mentioned in the review")
    cons: List[str] = Field(description="List of negative aspects mentioned in the review")
    key_issues: List[str] = Field(description="Main problems highlighted by the user")
    improvement_suggestions: List[str] = Field(description="Suggested improvements based on review")


structured_model = model.with_structured_output(ReviewAnalysis)

review_text = """
The hardware is great, but the software feels bloated.
There are too many pre-installed apps that I can't remove.
Also the UI looks outdated compared to other brands.
Hoping for a software update to fix this.
"""


result = structured_model.invoke(review_text)


print(result)


print("\nSummary:", result.summary)
print("Sentiment:", result.sentiment)
print("Score:", result.sentiment_score)
print("Pros:", result.pros)
print("Cons:", result.cons)
print("Issues:", result.key_issues)
print("Suggestions:", result.improvement_suggestions)
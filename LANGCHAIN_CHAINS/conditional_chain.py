from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

feedback = "The product quality is very bad and I am disappointed."

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(
        description="Sentiment of the feedback"
    )


parser = PydanticOutputParser(pydantic_object=Feedback)


prompt = PromptTemplate(
    template="""
    Classify the sentiment of the following feedback.
    {format_instructions}
    
    Feedback: {feedback}
    """,
    input_variables=['feedback'],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

 
chain = prompt | model | parser
result = chain.invoke({'feedback': feedback})

print("Sentiment:", result.sentiment)

if result.sentiment == 'negative':
    prompt2 = PromptTemplate(
        template="Write a polite apology email to the customer for this negative feedback:\n{feedback}",
        input_variables=['feedback']
    )
else:
    prompt2 = PromptTemplate(
        template="Write a thank you email to the customer for this positive feedback:\n{feedback}",
        input_variables=['feedback']
    )

final_chain = prompt2 | model
final_response = final_chain.invoke({'feedback': feedback})

print("\nFinal Response:\n")
print(final_response.content)
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser , ResponseSchema


load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    temperature=0.7,
    max_new_tokens=512
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name = 'fact_1',description = 'Fact 1 obout the topic '),
    ResponseSchema(name = 'fact_2',description = 'Fact 2 obout the topic')
]

parser = StructuredOutputParser.from_response_schema(schema)
template = PromptTemplate(
    template = 'Give me 3 facts obout {topic}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
prompt = template.invoke({'topic':'black-hole'})
result = model.invoke(prompt)
fina_result = parser.parse(result.content)
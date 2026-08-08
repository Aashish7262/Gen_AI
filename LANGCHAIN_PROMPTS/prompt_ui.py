from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3
)

st.set_page_config(page_title="Research Tool", page_icon="🔬")
st.header("🔬 Dynamic Research Tool (Dropdown Prompts)")


task = st.selectbox(
    "Select Task",
    ["Summarize", "Explain", "Generate Notes", "Compare Concepts"]
)

tone = st.selectbox(
    "Select Tone",
    ["Simple", "Academic", "Technical"]
)

format_type = st.selectbox(
    "Output Format",
    ["Bullet Points", "Paragraph", "Key Points"]
)


user_input = st.text_area(
    "Enter your research text or topic:",
    height=200,
    placeholder="Example: Word2Vec, Transformers, Semantic Search, etc."
)


def build_prompt(task, tone, format_type, text):
    prompt = f"""
    You are an AI Research Assistant.

    Task: {task}
    Tone: {tone}
    Output Format: {format_type}

    Instructions:
    - If input is a topic, explain it clearly.
    - If input is a paragraph, process it based on the selected task.
    - Keep the response well-structured and clear.
    - Maintain the selected tone.
    - Follow the selected output format strictly.

    User Input:
    {text}
    """
    return prompt



if st.button("🚀 Generate Response"):
    if user_input.strip() == "":
        st.warning("Please enter some text or topic.")
    else:
        with st.spinner("Processing with Gemini..."):
            final_prompt = build_prompt(task, tone, format_type, user_input)
            response = llm.invoke(final_prompt)

            st.subheader("📄 AI Response:")
            st.write(response.content)

            
            with st.expander("🧠 View Generated Prompt"):
                st.code(final_prompt)
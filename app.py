import streamlit as st
import time


def call_llm(question):
    responses = {
        "What does the eligibility verification agent (EVA) do?": "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections.",
        "What does the claims processing agent (CAM) do?": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements.",
        "How does the payment posting agent (PHIL) work?": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden.",
        "Tell me about Thoughtful AI's Agents.": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others.",
        "What are the benefits of using Thoughtful AI's agents?": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting.",
    }

    return responses.get(
        question, "I'm sorry, I don't have an answer to that question."
    )


# Sidebar Section
with st.sidebar:
    st.session_state.model = st.selectbox(
        "AI model:", options=["distilbert-base-uncased-distilled-squad"]
    )

# Main Section
st.title("Thoughtful.AI Support Chat")

# User input
user_input = st.text_input("Ask your question:")

# Placeholder for messages
message_placeholder = st.empty()

if user_input:
    message_placeholder.write("Thinking...")
    time.sleep(2)
    response = call_llm(user_input)
    message_placeholder.write(response)

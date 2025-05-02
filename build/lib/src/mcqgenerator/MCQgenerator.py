import os
import json
import traceback
import pandas as pd

from dotenv import load_dotenv

# Custom utility and logging modules
from src.mcqgenerator.utils import read_file, get_table_data
from src.mcqgenerator.logger import logging

# Importing necessary packages from LangChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.callbacks import get_openai_callback

# Load environment variables
load_dotenv()
KEY = os.getenv("openai_api_key")  # Retrieve OpenAI API key from .env

# Define your input variables
TEXT = """
Photosynthesis is the process by which green plants use sunlight to synthesize food from carbon dioxide and water.
It generally involves the green pigment chlorophyll and generates oxygen as a by-product.
"""

NUMBER = 5  # Number of questions to generate
SUBJECT = "Biology"
TONE = "educational"
response_json = {
    "1": {
        "mcq": "Which process helps plants make their food?",
        "options": {
            "A": "Respiration",
            "B": "Photosynthesis",
            "C": "Transpiration",
            "D": "Digestion"
        },
        "correct": "B"
    }
}

llm = ChatOpenAI(
    openai_api_key=KEY,          
    model_name="gpt-4",          
    temperature=0.3
)

template = """
Text: {text}

You are an expert MCQ maker. Given the above text, it is your job to
create a quiz of {number} multiple choice questions for {subject} students in a {tone} tone.

Make sure the questions are not repeated and check all the questions to be conforming to the text as well. 
Make sure to format your response like RESPONSE_JSON below and use it as a guide.

Ensure to make {number} MCQs.

### RESPONSE_JSON
{response_json}
"""
quiz_generation_prompt = PromptTemplate(
    input_variables=["text", "number", "subject", "tone", "response_json"],
    template=template
)


quiz_chain = LLMChain(
    llm=llm,
    prompt=quiz_generation_prompt,
    output_key="quiz",  # <--- important
    verbose=True
)

template2 = """
You are an expert English grammarian and writer. Given a Multiple Choice Quiz for {subject} students,
you need to evaluate the complexity of the questions and give a complete analysis of the quiz. 
Use at most 50 words for the analysis.

If the quiz is not aligned with the cognitive and analytical abilities of the students, update the quiz questions that need to be changed, 
and adjust the tone to perfectly fit the students.

Quiz_MCQs:
{quiz}

Check and update the above quiz as an expert English writer.
"""

quiz_evaluation_prompt = PromptTemplate(
    input_variables=["subject", "quiz"],
    template=template2
)

review_chain = LLMChain(
    llm=llm,  # Ensure 'llm' is defined earlier as your language model (e.g., OpenAI)
    prompt=quiz_evaluation_prompt,
    output_key="review",
    verbose=True
)


generator_evaluate_chain = SequentialChain(
    chains=[quiz_chain, review_chain],
    input_variables=["text", "number", "subject", "tone", "response_json"],
    output_variables=["quiz", "review"],
    verbose=True
)


# Running the chain with token usage tracking
with get_openai_callback() as cb:
    response = generator_evaluate_chain({
        "text": TEXT,  # Use the variable TEXT defined above
        "number": NUMBER,
        "subject": SUBJECT,
        "tone": TONE,
        "response_json": json.dumps(response_json)
    })

    print("Generated Quiz:\n", response["quiz"])
    print("Evaluation:\n", response["review"])
    print(f"Tokens used: {cb.total_tokens}, Cost: ${cb.total_cost:.4f}")

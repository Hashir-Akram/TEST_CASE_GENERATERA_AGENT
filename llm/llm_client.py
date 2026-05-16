from openai import OpenAI

from config.settings import (
    OPENAI_API_KEY,
    OPENAI_BASE_URL,
    MODEL_NAME
)


client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL
)


def generate_response(prompt):

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert QA Automation Engineer "
                    "specialized in pytest and Selenium."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0  # 0 natural language, 1 creative, 2 very creative
    )

    return response.choices[0].message.content
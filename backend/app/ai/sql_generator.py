import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


api_key = os.getenv("OPENAI_API_KEY")

print("API KEY EXISTS:", api_key is not None)


client = OpenAI(
    api_key=api_key
)


def generate_sql(question, schema):

    prompt = f"""
You are a PostgreSQL expert.

Database schema:

{schema}

Convert this user question into SQL.

Rules:
- Return ONLY SQL.
- No explanation.
- Use PostgreSQL syntax.

Question:
{question}
"""


    try:

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )


        return response.choices[0].message.content


    except Exception as e:

        print("OPENAI ERROR:", e)

        return {
            "error": str(e)
        }
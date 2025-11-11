# generate_email.py
import openai
from openai import OpenAI

# Reads OPENAI_API_KEY from env
client = OpenAI()

def generate_in_style(style, topic="a quick update", audience="the team"):
    prompt = f"""
You are writing an email in this EXACT style:
- Formality: {style['formality']}
- Uses emoji: {style['uses_emoji']}
- Average length: ~{style['avg_words']} words
- Greeting: {style['greeting']}
- Closing: {style['closing']}

Write a short, friendly email about: {topic}
Audience: {audience}
Keep it under 50 words.
"""

    # Use the REAL OpenAI endpoint
    response = client.chat.completions.create(
        model="gpt-4o-mini",          # ← public, fast, cheap
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].message.content.strip()
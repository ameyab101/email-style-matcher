# generate_email_langchain.py
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

def generate_in_style(style, topic="a quick update", audience="the team"):
    # 1. Build a reusable LangChain prompt template
    prompt_template = PromptTemplate.from_template(
        """You are writing an email in this EXACT style:
- Formality: {formality}
- Uses emoji: {uses_emoji}
- Average length: ~{avg_words} words
- Greeting: {greeting}
- Closing: {closing}

Write a short, friendly email about: {topic}
Audience: {audience}
Keep it under 50 words."""
    )

    # 2. Fill the template
    prompt = prompt_template.format(
        formality=style['formality'],
        uses_emoji=style['uses_emoji'],
        avg_words=style['avg_words'],
        greeting=style['greeting'],
        closing=style['closing'],
        topic=topic,
        audience=audience
    )

    # 3. Call OpenAI via LangChain
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
    response = llm.invoke(prompt)

    # 4. Return clean text
    return response.content.strip()
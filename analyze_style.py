import pandas as pd

#Tested styles: Super Casual + Emoji, Friendly Professional, Formal Corporate, Concise (Engineer)
def extract_style(df: pd.DataFrame) -> dict:
    # Handle quoted bodies with \n
    bodies = []
    for body in df['body'].dropna():
        text = str(body)
        # Replace literal \n with actual newline
        text = text.replace('\\n', '\n').strip()
        if text:
            bodies.append(text)

    if not bodies:
        return {"formality": "casual", "uses_emoji": False, "avg_words": 15,
                "greeting": "Hi", "closing": "Best"}

    text = " ".join(bodies)

    style = {
        "formality": "casual" if any(g in text for g in ["Hey", "Hi", "Cheers", "Yo", "Sup"]) else "formal",
        "uses_emoji": any(e in text for e in ["🚀", "😊", "👍", "☕", "🎉", "🔥", "💯", "😎", "🤘"]),
        "avg_words": sum(len(b.split()) for b in bodies) // len(bodies),
        "greeting": next((g for g in ["Hey", "Hi", "Hello", "Yo", "Sup"] if g in text), "Hi"),
        "closing": next(
            (c for c in ["Cheers", "Let me know", "Thanks", "Best", "Talk soon", "Catch you later"] if c in text),
            "Best")
    }
    return style

import pandas as pd

def extract_style(df):
    bodies = df['body'].tolist()
    text = " ".join(bodies)
    
    style = {
        "formality": "casual" if any(g in text for g in ["Hey", "Hi", "Cheers"]) else "formal",
        "uses_emoji": any(e in text for e in ["🚀", "☕", "😊", "👍"]),
        "avg_words": sum(len(b.split()) for b in bodies) // len(bodies),
        "greeting": next((g for g in ["Hey", "Hi", "Hello"] if g in text), "Hi"),
        "closing": next((c for c in ["Cheers", "Best", "Thanks", "Let me know"] if c in text), "Best")
    }
    return style

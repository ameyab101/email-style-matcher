from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import pandas as pd
from analyze_style import extract_style
from generate_email import generate_in_style
import io

app = FastAPI(title="Email Style Matcher")

@app.post("/match-style")
async def match_style(
    file: UploadFile = File(...),
    topic: str = "a quick update",
    audience: str = "the team"
):
    content = await file.read()
    df = pd.read_csv(io.BytesIO(content))
    style = extract_style(df)
    email = generate_in_style(style, topic, audience)
    return {"your_style": style, "generated_email": email}

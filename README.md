# Email Style Matcher (Personal Project)

**Goal**: Upload 3 of your past emails -> **ChatGPT writes future ones in your exact voice**.

**Why**  
- Never sound "off" in emails again  
- Perfect for marketing, job apps, or just fun  
- **No ML training** - just **smart prompting + OpenAI API**

**Stack**:
- Python + FastAPI
- OpenAI (gpt-3.5-turbo)
- Pandas
- LangChain (optional)

---

### How It Works
1. Upload **3–5 of your real emails** (CSV)  
2. Script detects:  
   - Formality (Hi vs. Hello)  
   - Emoji use  
   - Sentence length  
   - Greeting/closing  
3. **Prompts ChatGPT**: “Write in this exact style.”  
4. Returns **perfectly matched email**

---

### Run Locally
```bash
pip install -r requirements.txt
uvicorn app:app --reload

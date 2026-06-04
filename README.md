# Groq Chatbot

A simple terminal chatbot I built using Groq's API and LLaMA 3.1. It's fast and gets the job done.

---

## Getting Started

```bash
pip install groq python-dotenv
```

Create a `.env` file and put your API key there:

```
GROQ_API_KEY=your_key_here
```

Then just run it:

```bash
python Ayan.py
```

---

## How it works

You type something, the bot replies. Type `exit` to quit. Pretty straightforward.

---

## One important thing

Don't hardcode your API key in the code. I learned this the hard way when GitHub flagged it. Use environment variables instead:

```python
import os
from dotenv import load_dotenv
load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
```

Also add `.env` to your `.gitignore`.

---

Made by **Ayan Ghosh**


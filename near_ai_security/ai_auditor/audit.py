from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

client = InferenceClient(model="HuggingFaceH4/zephyr-7b-beta", token=HF_TOKEN)

def audit_contract(code):
    prompt = f"Check this contract code for bugs:\n{code[:1000]}"

    response = client.chat_completion(messages=[{"role": "user", "content": prompt}], max_tokens=200)
    return response.choices[0].message.content

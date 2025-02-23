import openai
from near_api import NearRpcClient

NEAR_RPC = "https://rpc.testnet.near.org"

def analyze_contract(contract_code):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Analyze this NEAR smart contract for vulnerabilities."},
                  {"role": "user", "content": contract_code}]
    )
    return response["choices"][0]["message"]["content"]



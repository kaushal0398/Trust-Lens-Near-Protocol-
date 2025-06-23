import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ai_auditor.audit import audit_contract

if len(sys.argv) < 2:
    print("Usage: python run_audit.py path/to/contract.rs")
    sys.exit(1)

with open(sys.argv[1], "r") as f:
    code = f.read()

result = audit_contract(code)

print("\n=== AI Audit Result ===\n")
print(result)

# 🔢 Extract trust score (temporary basic version)
# In future you can use regex or better parsing logic
score = 75  # placeholder score

# 📄 Save to latest_audit.json
with open("latest_audit.json", "w") as outfile:
    json.dump({
        "contract_id": "sample-contract.near",
        "score": score,
        "summary": result
    }, outfile, indent=4)

print("\n✅ Saved audit result to latest_audit.json")

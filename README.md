# 🔍 Trust-Lens — AI-Powered Smart Contract Auditor for NEAR

**Trust-Lens** is an autonomous AI agent that audits NEAR smart contracts for vulnerabilities and assigns on-chain reputation scores to both contracts and users. It aims to enhance **security**, **transparency**, and **trust** across the NEAR ecosystem by automating smart contract analysis and incentivizing safe development practices.

> Built with NEAR Protocol, powered by AI — Trust-Lens bridges smart security and on-chain reputation.


---

## 🧠 Features

- 📦 Upload or input NEAR smart contract code (Rust or .wasm)
- 🤖 Uses AI (OpenAI or local model) to detect vulnerabilities
- 🧮 Calculates a reputation/trust score
- 🌐 Optional: Stores results on NEAR testnet via smart contract
- 🖥️ Simple CLI interface for local use or automation

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/kaushal0398/Trust-Lens-Near-Protocol-.git
cd Trust-Lens-Near-Protocol-
```

### 2. Setup Python & JS Dependencies

#### Python

```bash
pip install -r requirements.txt
```

#### JavaScript

```bash
cd near_integration
npm install
```

### 3. Configure Environment

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key
NEAR_ACCOUNT_ID=your_testnet_account.near
NEAR_PRIVATE_KEY=ed25519:xxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 💡 Usage

### Run Audit Locally

```bash
python cli/run_audit.py path/to/contract.rs
```

You’ll get a vulnerability report and trust score.

### Push to NEAR Blockchain (optional)

```bash
node near_integration/reputation_writer.js
```

This sends the audit results to a smart contract on NEAR testnet.

---

## 🛠️ Smart Contract (Optional)

If you want on-chain storage:

1. Navigate to `contracts/`
2. Compile with:

```bash
cargo build --target wasm32-unknown-unknown --release
```

3. Deploy using:

```bash
near dev-deploy --wasmFile target/wasm32-unknown-unknown/release/reputation.wasm
```

---

## 📚 Future Improvements

* UI Dashboard for uploading contracts & viewing scores
* Support for more vulnerability types (overflow, reentrancy, etc.)
* Multi-chain support via NEAR B.O.S. & intents
* Use of Zero-Knowledge proofs for audit verification

---

## 👥 Credits

Developed by [Kaushal](https://github.com/kaushal0398)

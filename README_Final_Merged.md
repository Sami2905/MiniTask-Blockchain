# 🧱 Mini Task 1: Build & Explain a Simple Blockchain

## 🎯 Objective

Understand blockchain fundamentals, simulate a mini blockchain with linked blocks, and compare consensus mechanisms (PoW, PoS, DPoS) through code.

---

## 🧠 Theoretical Part

### ✅ Blockchain Basics

**Definition:**  
Blockchain is a decentralized, immutable ledger that records transactions across a distributed network. Each block links to the previous block using a cryptographic hash, forming a secure chain of data. This ensures transparency, trust, and data integrity without the need for central authorities.

**Real-Life Use Cases:**
- **Supply Chain:** Track product journey for transparency.
- **Digital Identity:** Allow secure identity verification and self-ownership of data.

---

### ✅ Block Anatomy

- **Components of a Block:**
  - `Data`
  - `Timestamp`
  - `Nonce`
  - `Previous Hash`
  - `Merkle Root`

_Refer to diagram in submitted document._

**Merkle Root Explanation:**  
The Merkle root summarizes all transactions in a block by combining their hashes recursively. Changing even one transaction alters the root, enabling quick and secure data integrity checks.

---

### ✅ Consensus Mechanisms

- **Proof of Work (PoW):**  
  Miners solve computational puzzles to validate blocks. Energy-intensive but secure.

- **Proof of Stake (PoS):**  
  Validators are chosen based on the amount of cryptocurrency they stake. More eco-friendly.

- **Delegated Proof of Stake (DPoS):**  
  Stakeholders vote for a few trusted delegates who validate transactions. Faster and democratic.

---

## 💻 Practical Part

### 1. `blockchain_simulation.py`

Simulates a 3-block blockchain.

- Each block contains index, data, timestamp, nonce, and hashes.
- Demonstrates tampering: editing a block’s data breaks the chain integrity.

➡️ **Run:**  
```bash
python blockchain_simulation.py
```

---

### 2. `mining_simulation.py`

Simulates Proof-of-Work mining using nonce.

- Adjusts `nonce` until a hash starts with a given number of `0`s.
- Measures number of attempts and time taken.

➡️ **Run:**  
```bash
python mining_simulation.py
```

---

### 3. `consensus_demo.py`

Simulates consensus mechanisms:

- **PoW:** Selects validator with highest random `power`.
- **PoS:** Selects validator with highest `stake`.
- **DPoS:** Elects delegate based on mock vote counts.

➡️ **Run:**  
```bash
python consensus_demo.py
```

---

## 📁 Files Included

```
📦 MiniTask-Blockchain
 ┣ 📄 blockchain_simulation.py
 ┣ 📄 mining_simulation.py
 ┣ 📄 consensus_demo.py
 ┣ 📄 README.md
```

---

## ✅ Submission Notes

- All tasks follow the instructions from the mini project guidelines.
- Theoretical parts are well-documented and supported with code demonstrations.
- Ready for review or deployment in GitHub classroom.

---

🔗 **Created for educational purposes. Learn. Build. Validate.**

---

## 🔍 Additional Theoretical Details (As per assignment requirements)

### Merkle Root Example

If a block has four transactions (T1, T2, T3, T4), the Merkle root is calculated as follows:

- H1 = SHA256(T1)
- H2 = SHA256(T2)
- H3 = SHA256(T3)
- H4 = SHA256(T4)

Pairing:
- H12 = SHA256(H1 + H2)
- H34 = SHA256(H3 + H4)

Merkle Root = SHA256(H12 + H34)

Any modification to a single transaction alters the entire root, thus ensuring data integrity.

---

### Detailed Validator Selection Logic

- **Proof of Work (PoW):**  
  Each validator is assigned a random "power" value. The validator with the highest power is selected as the block producer. This simulates competitive computation.

- **Proof of Stake (PoS):**  
  Validators are assigned a "stake" (random value). The one with the highest stake is chosen, reflecting the economic commitment to the network.

- **Delegated Proof of Stake (DPoS):**  
  Simulates 3 user accounts voting for delegates. The candidate with the highest vote count is elected as the validator.

---

### Submission Requirements Checklist

- ✅ Blockchain basics explained clearly.
- ✅ Two real-world use cases provided.
- ✅ Detailed block structure included with Merkle root explanation.
- ✅ All three consensus mechanisms explained.
- ✅ Python scripts simulate blockchain, mining, and consensus processes.
- ✅ Code outputs include explanations and sample print/log statements.
- ✅ All files organized and ready for submission.

---

## 📌 Notes

- This project is structured to meet all guidelines outlined in the assignment document.
- Visual diagrams (e.g., block structure) are included separately as per submission requirements.
- For execution, ensure Python 3.7+ is installed.

---

*End of README Extension*

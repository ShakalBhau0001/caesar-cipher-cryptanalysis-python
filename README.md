# 🔐 Caesar Cipher Cryptanalysis (Python)

An educational **Python implementation of Caesar Cipher brute-force cryptanalysis.**
This project demonstrates how classical encryption can be broken using **exhaustive search and simple English frequency scoring.**

It is designed as a **learning and academic project** to understand why classical ciphers are insecure and how attackers analyze encrypted text — not as a real-world attack tool.

---

## 🧱 Project Structure

```bash
caesar-cipher-cryptanalysis-python/
│
├── assets/               # Screenshots
├── app.py                # Brute-force Basic CLI Version
├── interactive.py        # Rich-powered CLI
├── requirements.txt      # Dependencies
├── LICENSE               # Project license
└── README.md             # Project documentation
```

---

## ✨ Features

### 🔍 Full Brute-Force Search
- Tests all 25 possible Caesar shifts
- Supports both:
  - `L` → Left shift
  - `R` → Right shift
- Automatically evaluates all possible plaintext candidates

### 🧠 English Scoring System
- Uses frequency-based heuristic scoring
- Prioritizes common English letters (E, T, A, O, I, N, etc.)
- Rewards spaces and readable structure
- Ranks outputs automatically

### 📊 Auto-Ranked Results
- Sorts plaintext candidates by likelihood
- Displays top possible decryptions
- Removes mirror duplicate results

### 🧮 Educational Focus
- Demonstrates cryptanalysis workflow
- Shows weakness of classical substitution ciphers
- Reinforces modular arithmetic concepts
- Clean and modular Python implementation

### 🎨 Rich CLI (Interactive Mode)
- Beautiful colored terminal UI using Rich
- Displays key matrix in a structured table 🔥
- Interactive prompts with validation
- Clean and readable output panels

### ⚡ Dual Mode Support
- 🧼 Basic CLI → Lightweight, no dependencies
- 🎨 Rich CLI → Enhanced UI with colors and structured display

---

## 🛠 Technologies Used


| Technology             | Role                                |
| ---------------------- | ----------------------------------- |
| **Python 3**           | Core programming language           |
| **ord() / chr()**      | Character-to-ASCII conversion       |
| **Modular Arithmetic** | Circular alphabet shifting (`% 26`) |
| **Heuristic Scoring**  | English-likeness evaluation         |
| **Rich**               | Styled CLI, colors, panels          |

---

## 📌 Purpose of This Project

This project is built to:
- Understand Caesar Cipher weaknesses
- Learn brute-force cryptanalysis
- Explore basic frequency analysis concepts
- Simulate attacker perspective ethically
- Strengthen Python logic and modular design skills

> ⚠️ This project is intended strictly for educational and cybersecurity learning purposes.

---

## ▶️ How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/ShakalBhau0001/caesar-cipher-cryptanalysis-python.git
```

### 2️⃣ Navigate to the project folder
```bash
cd caesar-cipher-cryptanalysis-python
```

### 3️⃣ Install Dependencies

```bash
pip install rich
```

**OR**

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Running the Project

#### 🧼 Basic CLI Version

```bash
python app.py
```

#### 🎨 Rich Interactive Version

```bash
python interactive.py
```

### 5️⃣ Follow the prompts for Basic CLI Version
- Provide any Caesar-encrypted message
- View automatically ranked possible plaintexts
- Analyze shift and direction results

---

## 🔎 Example

```bash
Enter Caesar cipher text: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD

Top Possible Plaintexts:

Shift  3 | Dir R | Score  72 | THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
Shift 23 | Dir L | Score  72 | THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
...
```

---

## ⚠️ Limitations
- English scoring is heuristic-based (not statistical-grade)
- Works only for Caesar Cipher
- Not designed for real-world encrypted systems
- CLI-based interaction only

---

## 🌟 Future Improvements
- Implement full frequency distribution comparison
- Add dictionary-based validation
- Support file input
- Add support for other classical ciphers
- Convert into reusable Python module
- Add Rich tables for result visualization

---

## ⚠️ Disclaimer

This project is created **for educational and cybersecurity learning purposes only.**
It demonstrates the inherent weakness of classical substitution ciphers such as Caesar Cipher.
It must not be used for unauthorized access, malicious activity, or real-world security attacks.

---

## 📸 Preview

![Rich CLI Preview](assets/screenshot.png)

---

## 🪪 Author

> **Shakal Bhau**

> **GitHub: [ShakalBhau0001](https://github.com/ShakalBhau0001)**

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

---

# 🧠 Keyboard Auto Suggestion NLP Project

An NLP-based keyboard auto-suggestion system built using Python.  
This project predicts and suggests the most probable correct word based on similarity and word frequency.

---

## 🚀 Project Overview

This project implements an auto-correction and word suggestion system using:

- Jaccard Similarity
- Word Frequency Probability
- NLP Text Processing
- Python Libraries (NumPy, Pandas, TextDistance)

The system compares a given input word with a vocabulary built from a text corpus and suggests the top most similar words.

---

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- TextDistance
- Regular Expressions (re)
- Collections (Counter)

---

## 📂 Project Structure
Keyboard-Auto-Suggestion-NLP-Python-Project/
│
├── main.py
├── autocorrect book.txt
├── Autocorrect with Python How It Works.ipynb
├── words suggestions.ipynb
├── README.md
---

## ⚙️ How It Works

1. Reads a large text file (`autocorrect book.txt`)
2. Cleans and tokenizes the text
3. Builds vocabulary
4. Calculates word frequency probability
5. Uses Jaccard similarity (bi-grams)
6. Returns top 10 most similar words sorted by:
   - Similarity score
   - Word probability

---

## ▶️ How to Run

### 1️⃣ Install Dependencies

```bash
pip install numpy pandas textdistance
```

### 2️⃣ Run the Script

```bash
python main.py
```

### 3️⃣ Example Usage

```python
print(autocorrect('whe'))
```

---

## 📊 Output Example

The system returns:

- Word suggestions  
- Similarity score  
- Word probability  

---

## 🎯 Key Features

- NLP-based word suggestion  
- Probability-based ranking  
- Jaccard similarity matching  
- Text preprocessing pipeline  
- Clean modular code  

---

## 📌 Future Improvements

- Implement Levenshtein distance  
- Add GUI interface  
- Deploy as Web App  
- Improve performance using optimized search  

---

## 👩‍💻 Author

**Varshitha Kerlopalli**  
Integrated M.Tech Software Engineering Student  
VIT Vellore  

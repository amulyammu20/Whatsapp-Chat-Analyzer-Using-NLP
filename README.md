
# 📱 WhatsApp Chat Analyzer for Insider Threat Detection

This project is a Python-based tool that analyzes exported WhatsApp `.txt` chat files to detect potential **insider threats**, such as data leaks, sharing of confidential information, or emotionally negative content. It uses **AI techniques like Natural Language Processing (NLP)** and **Regex** to scan messages, flag suspicious ones, and visualize patterns with a word cloud.

---

## 🔍 Features

- ✅ Detects suspicious messages using custom keyword matching
- 😠 Flags messages with strong negative sentiment (using NLTK VADER)
- ☁️ Generates WordCloud of most used terms
- 📊 Displays top 10 most frequent words
- 🖥️ Includes a user-friendly GUI built with Tkinter

---

## 🛠 Technologies Used

- Python 3.7+
- [NLTK](https://www.nltk.org/) – for sentiment analysis
- [Regex](https://docs.python.org/3/library/re.html) – for pattern matching
- [WordCloud](https://pypi.org/project/wordcloud/) – for visual text analysis
- [Matplotlib](https://matplotlib.org/) – to display word cloud
- [Tkinter](https://docs.python.org/3/library/tk.html) – for GUI

---

## 📁 Folder Structure

```
project/
├── gui_chat_analyzer.py          # Main GUI-based app
├── main.py                       # Optional terminal version
├── suspicious_keywords.txt       # List of keywords to detect
├── sample_chat.txt               # Example WhatsApp exported chat
├── README.md                     # This file
```

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/whatsapp-chat-analyzer.git
cd whatsapp-chat-analyzer
```

### 2. Install Required Libraries
```bash
pip install nltk wordcloud matplotlib
```

### 3. Download NLP Lexicon (run once)
```python
import nltk
nltk.download('vader_lexicon')
```

---

## 🚀 Running the App

### GUI Version:
```bash
python gui_chat_analyzer.py
```

- A Tkinter window will appear.
- Upload an exported WhatsApp `.txt` file.
- View suspicious messages, sentiment flags, word frequency, and word cloud.

---

## 📦 Deployment (Optional)

To convert to a standalone executable (Windows):
```bash
pip install pyinstaller
pyinstaller --onefile gui_chat_analyzer.py
```

---

## 🔮 Future Scope

- Real-time WhatsApp Web monitoring  
- Multi-language NLP support  
- Export results to PDF/CSV  
- Advanced AI models (e.g., BERT for deeper context)  
- Threat scoring and alert system

---

## 📚 References

- NLTK: https://www.nltk.org  
- VADER Sentiment: https://github.com/cjhutto/vaderSentiment  
- WordCloud: https://pypi.org/project/wordcloud  
- Matplotlib: https://matplotlib.org  
- Tkinter Docs: https://docs.python.org/3/library/tk.html  
- WhatsApp Chat Export Info: https://faq.whatsapp.com/

---

## 🙌 Acknowledgements

Thanks to open-source contributors and mentors for guidance in building this project.  
Special thanks to libraries like NLTK, WordCloud, and the Python community!

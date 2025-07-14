import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

# Download the VADER sentiment model (only needed once)
nltk.download('vader_lexicon')

# === Load suspicious keywords from file ===
def load_keywords(file_path):
    with open(file_path, 'r') as f:
        return [line.strip().lower() for line in f if line.strip()]

# === Load WhatsApp chat file ===
def load_chat(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

# === Extract only the message part (remove name/timestamp) ===
def extract_messages(lines):
    messages = []
    for line in lines:
        match = re.search(r"\d{1,2}/\d{1,2}/\d{2,4}, \d{1,2}:\d{2} (AM|PM) - .*?: (.+)", line)
        if match:
            messages.append(match.group(2))
    return messages

# === Detect suspicious messages by keyword match ===
def detect_suspicious(lines, keywords):
    flagged = []
    for line in lines:
        lower_line = line.lower()
        for keyword in keywords:
            if re.search(rf"\b{re.escape(keyword)}\b", lower_line):
                flagged.append(line)
                break
    return flagged

# === Analyze sentiment using VADER ===
def analyze_sentiment(messages):
    sia = SentimentIntensityAnalyzer()
    negative_msgs = []
    for msg in messages:
        score = sia.polarity_scores(msg)
        if score['compound'] < -0.3:
            negative_msgs.append((msg, score))
    return negative_msgs

# === Generate WordCloud from messages ===
def generate_wordcloud(messages):
    text = " ".join(messages)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Cloud of WhatsApp Chat")
    plt.show()

# === Count top N words ===
def count_common_words(messages, top_n=10):
    all_words = ' '.join(messages).lower().split()
    words = [word for word in all_words if word.isalpha()]
    return Counter(words).most_common(top_n)

# === MAIN ===
if __name__ == "__main__":
    print("📥 Loading data...")
    chat_lines = load_chat("sample_chat.txt")
    suspicious_keywords = load_keywords("suspicious_keywords.txt")
    messages = extract_messages(chat_lines)

    print("\n🔍 Suspicious Messages:")
    flagged = detect_suspicious(chat_lines, suspicious_keywords)
    if flagged:
        for msg in flagged:
            print("⚠️", msg)
    else:
        print("✅ No suspicious messages found.")

    print("\n🧠 Negative Sentiment Messages:")
    negative_msgs = analyze_sentiment(messages)
    if negative_msgs:
        for msg, score in negative_msgs:
            print(f"😠 {msg} [Sentiment Score: {score['compound']}]")
    else:
        print("✅ No strongly negative messages found.")

    print("\n📊 Top 10 Common Words:")
    for word, count in count_common_words(messages):
        print(f"{word}: {count}")

    print("\n☁️ Generating Word Cloud...")
    generate_wordcloud(messages)

# Semantic Search Engine

## 🚀 Overview
This project is a **semantic search engine** that utilizes **Elasticsearch**, **Universal Sentence Encoder (USE)**, and **Flask** to index and search through Kaggle's Stack Overflow dataset. The search engine supports both **keyword-based** and **semantic similarity-based** queries, returning the top 10 most relevant results.

## 📌 Features
- **Full-Text Search** using **Elasticsearch**
- **Semantic Search** using **Universal Sentence Encoder (USE)**
- **Hybrid Ranking** combining **TF-IDF & Cosine Similarity**
- **REST API** powered by **Flask**
- **Dockerized Deployment** for easy setup


## 📦 Installation
### 🔹 1. Clone the Repository
```bash
git clone
cd semantic-search-engine
```

### 🔹 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 🔹 3. Run with Docker
```bash
docker-compose up -d --build
```

---

## ⚙️ Configuration
All configurations are stored in `config.py` and environment variables:

```python
ES_HOST = os.getenv("ES_HOST", "http://elasticsearch:9200")
USE_PATH = os.getenv("USE_PATH", "/models/USE4")
INDEX_NAME = "questions-index"
```

---

## 🔍 Search API
### **1️⃣ Endpoint:** `/api/search?query=<search_text>`

### **2️⃣ Example Request:**
```bash
curl -X GET "http://localhost:5000/api/search?query=how+to+use+flask" -H "Content-Type: application/json"
```

### **3️⃣ Example Response:**
```json
[
  {"type": "Keyword", "score": 12.34, "title": "How to use Flask with Elasticsearch?"},
  {"type": "Semantic", "score": 11.78, "title": "Using Flask and Elasticsearch together"}
]
```

---

## 📜 Explanation of Key Concepts
### 🔹 **Elasticsearch**
A powerful **search and analytics engine** that enables efficient **keyword** and **vector-based searches**.

### 🔹 **Universal Sentence Encoder (USE)**
A **pre-trained model** by Google that converts text into a **512-dimensional vector representation** for **semantic similarity** calculations.

### 🔹 **Cosine Similarity**
Measures the similarity between two **vector representations**:
\[ \text{cosine similarity} = \frac{A \cdot B}{||A|| \times ||B||} \]

### 🔹 **TF-IDF (Term Frequency-Inverse Document Frequency)**
Ranks documents based on how relevant a **keyword** is in a document:
\[ \text{TF-IDF} = \text{TF} \times \text{IDF} \]

---

## 🛠️ Development
### Start Backend (Without Docker)
```bash
python app.py
```


## 🖥️ Deployment
To deploy this search engine on a cloud server:
1. Ensure **Docker & Docker Compose** are installed.
2. Clone the repository.
3. Run `docker-compose up -d --build`.
4. Expose port `5000` for API access.




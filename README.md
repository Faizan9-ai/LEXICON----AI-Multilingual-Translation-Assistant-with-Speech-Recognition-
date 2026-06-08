
# 🌍 AI Multilingual Translation Assistant

## Overview

AI Multilingual Translation Assistant is an intelligent translation application built using **Streamlit**, **LangChain**, and **Groq LLMs**. The application enables users to translate text and documents across multiple languages while supporting voice input, audio output, automatic language detection, translation history tracking, and downloadable results.

The project demonstrates the integration of Generative AI with speech processing and document handling to create a complete multilingual communication solution.

---

## Features

### 🌐 Text Translation

* Translate text between multiple languages.
* Powered by Groq Large Language Models.
* Fast and accurate AI-based translations.

### 🔍 Automatic Language Detection

* Detects the source language automatically.
* Eliminates the need for manual language selection.

### 🎤 Speech-to-Text

* Speak instead of typing.
* Converts voice input into text using Speech Recognition.

### 🔊 Text-to-Speech

* Generates audio for translated content.
* Listen to translations directly within the application.

### 📄 Document Translation

* Upload and translate:

  * TXT files
  * PDF files
  * DOCX files

### 📜 Translation History

* Stores previous translations using SQLite.
* Displays recent translations in the sidebar.

### 📥 Download Translations

* Download translated text.
* Save translated documents for future use.

### 🎨 User-Friendly Interface

* Clean and responsive Streamlit UI.
* Simple workflow for both text and document translation.

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI & NLP

* LangChain
* Groq API

### Database

* SQLite

### Speech Processing

* SpeechRecognition
* gTTS (Google Text-to-Speech)

### Document Processing

* PyPDF
* python-docx

---

## Project Structure

```text
ai-multilingual-translator/
│
├── app.py
├── requirements.txt
├── .env
│
├── chains/
│   └── translation_chain.py
│
├── services/
│   ├── file_reader.py
│   └── history_db.py
│
├── utils/
│   ├── helpers.py
│   ├── languages.py
│   ├── speech.py
│   └── tts.py
│
├── database/
│   └── translations.db
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/ai-multilingual-translator.git

cd ai-multilingual-translator
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Running the Application

```bash
streamlit run app.py
```

Application will start at:

```text
http://localhost:8501
```

---

## Usage

### Text Translation

1. Select source language.
2. Select target language.
3. Enter text or use voice input.
4. Click **Translate Text**.
5. View translation.
6. Download or listen to the translated result.

### Document Translation

1. Open the Document Translation tab.
2. Upload a TXT, PDF, or DOCX file.
3. Click **Translate Document**.
4. View translated content.
5. Download the translated document.

---

## Future Enhancements

* Translation Analytics Dashboard
* Multi-LLM Support (Groq, Gemini, OpenAI)
* Real-Time Conversation Translation
* Translation Quality Scoring
* User Authentication
* Cloud Deployment
* Translation API Endpoint

---

## Learning Outcomes

This project demonstrates:

* Generative AI Integration
* Prompt Engineering
* LangChain Workflows
* LLM Application Development
* Streamlit Development
* Database Management
* Speech Recognition
* Text-to-Speech Systems
* Document Processing
* API Integration

---

## Author

**Mohammed Faizan Sayeed**



AI/ML Solutions Engineer | Data Analyst | 

---



import streamlit as st

st.set_page_config(
    page_title="AI Multilingual Translator",
    page_icon="🌍",
    layout="wide"
)

from chains.translation_chain import translate_text
from services.file_reader import extract_text
from utils.languages import LANGUAGES
from utils.helpers import detect_language
from utils.speech import speech_to_text
from utils.tts import text_to_audio
from services.history_db import save_translation, get_history


if "input_text" not in st.session_state:
    st.session_state.input_text = ""

if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""

if "audio_file" not in st.session_state:
    st.session_state.audio_file = None

if "translated_doc" not in st.session_state:
    st.session_state.translated_doc = ""

if "doc_audio_file" not in st.session_state:
    st.session_state.doc_audio_file = None


st.sidebar.title("📜 Translation History")

history = get_history()

for row in history[:10]:
    st.sidebar.write(f"{row[3]} ➜ {row[4]}")

st.title("🌍 AI Multilingual Translation Assistant")
st.write("Translate text and documents using LangChain + Groq API.")

source_language = st.selectbox("Source Language", LANGUAGES)

target_language = st.selectbox(
    "Target Language",
    LANGUAGES[1:],
    index=1
)

tab1, tab2 = st.tabs(["Text Translation", "Document Translation"])


# -------------------------
# TEXT TRANSLATION
# -------------------------

with tab1:

    if st.button("🎤 Click & Speak"):
        spoken_text = speech_to_text()
        st.session_state.input_text = spoken_text

    user_text = st.text_area(
        "Enter text",
        value=st.session_state.input_text,
        height=180
    )

    if st.button("Translate Text"):
        if not user_text.strip():
            st.warning("Please enter text.")
        else:
            if source_language == "Auto Detect":
                detected_lang = detect_language(user_text)
                st.info(f"Detected Language: {detected_lang}")

            with st.spinner("Translating..."):
                translated = translate_text(
                    user_text,
                    source_language,
                    target_language
                )

                st.session_state.translated_text = translated
                st.session_state.audio_file = None

                save_translation(
                    user_text,
                    translated,
                    source_language,
                    target_language
                )

    if st.session_state.translated_text:
        st.subheader("Translated Output")

        st.text_area(
            "Translation",
            st.session_state.translated_text,
            height=200
        )

        col1, col2 = st.columns(2)

        with col1:
            st.download_button(
                label="Download Translation",
                data=st.session_state.translated_text,
                file_name="translation.txt",
                mime="text/plain"
            )

        with col2:
            if st.button("🔊 Generate Audio"):
                st.session_state.audio_file = text_to_audio(
                    st.session_state.translated_text,
                    lang="hi"
                )

        if st.session_state.audio_file:
            st.audio(
                st.session_state.audio_file,
                format="audio/mp3"
            )


# -------------------------
# DOCUMENT TRANSLATION
# -------------------------

with tab2:

    uploaded_file = st.file_uploader(
        "Upload TXT, PDF, DOCX",
        type=["txt", "pdf", "docx"]
    )

    if uploaded_file:
        extracted_text = extract_text(uploaded_file)

        st.subheader("Extracted Text")

        st.text_area(
            "Document Content",
            extracted_text,
            height=250
        )

        if st.button("Translate Document"):
            with st.spinner("Translating document..."):
                translated_doc = translate_text(
                    extracted_text,
                    source_language,
                    target_language
                )

                st.session_state.translated_doc = translated_doc
                st.session_state.doc_audio_file = None

        if st.session_state.translated_doc:
            st.subheader("Translated Document")

            st.text_area(
                "Translation",
                st.session_state.translated_doc,
                height=250
            )

            st.download_button(
                label="Download Document",
                data=st.session_state.translated_doc,
                file_name="translated_document.txt",
                mime="text/plain"
            )

            if st.button("🔊 Generate Document Audio"):
                st.session_state.doc_audio_file = text_to_audio(
                    st.session_state.translated_doc,
                    lang="hi"
                )

            if st.session_state.doc_audio_file:
                st.audio(
                    st.session_state.doc_audio_file,
                    format="audio/mp3"
                )
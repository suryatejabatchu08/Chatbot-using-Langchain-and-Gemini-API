# Chatbot using Langchain and Gemini API

A Python-based chatbot project that leverages [Langchain](https://github.com/hwchase17/langchain) and the [Gemini API](https://ai.google.dev/gemini-api/docs) to deliver intelligent conversational experiences. This repository demonstrates how to build, customize, and extend a chatbot using modern language model frameworks and APIs.

## Features

- **Natural Language Understanding**: Utilizes Langchain to manage conversation flow, context, and memory.
- **Gemini API Integration**: Connects to Google's Gemini API for robust language generation and comprehension.
- **Extensible Pipeline**: Easily add new tools, retrievers, or chain logic to enhance chatbot capabilities.
- **Fully in Python**: The entire codebase is written in Python for ease of use and modification.

## Getting Started

### Prerequisites

- Python 3.8 or newer
- Gemini API Key (get from [Google AI Gemini Console](https://ai.google.dev/))
- (Optional) Virtual environment tool such as `venv` or `conda`

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/suryatejabatchu08/Chatbot-using-Langchain-and-Gemini-API.git
    cd Chatbot-using-Langchain-and-Gemini-API
    ```

2. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set your Gemini API key as an environment variable:
    ```bash
    export GEMINI_API_KEY="your-api-key-here"
    ```

### Usage

Run the chatbot with:

```bash
python main.py
```

You may need to adjust the entry point if your main script is named differently.

## Configuration

- To change the chatbot prompt, modify the prompt template in the code.
- Extend with new chains or tools by modifying or adding Python files as needed.

## Project Structure

```
├── app.py
├── chatbot.py
├── requirements.txt
└── README.md
```

## Acknowledgments

- [Langchain](https://github.com/hwchase17/langchain)
- [Google Gemini API](https://ai.google.dev/)

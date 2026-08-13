# RAG Chatbot — Document QnA

An intelligent Document Question & Answer chatbot that allows users to upload PDF documents and ask questions about their content using natural language.

The project uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from uploaded documents and generate accurate, context-aware answers.

## 🚀 Features

- 📄 Upload multiple PDF documents
- 🔍 Search documents using semantic similarity
- 💬 Ask questions in natural language
- 🧠 Maintain conversation context
- ⚡ Fast document retrieval using FAISS
- 🤖 Generate answers using OpenAI models
- 🖥️ Simple and interactive Streamlit interface

## 🔄 How It Works

```
PDF Documents
      ↓
Extract Text
      ↓
Create Embeddings
      ↓
FAISS Vector Store
      ↓
Retrieve Relevant Content
      ↓
LLM + Conversation History
      ↓
Generate Answer
```

## 🧠 RAG Pipeline

### 1. Upload PDFs
Upload one or more PDF documents to the application.

### 2. Extract Text
The application extracts text from the uploaded PDF documents and divides it into smaller chunks.

### 3. Create Embeddings
The text chunks are converted into vector embeddings using the `all-MiniLM-L6-v2` model from Hugging Face.

### 4. Store Embeddings
FAISS is used as the vector store to efficiently store and search the document embeddings.

### 5. Retrieve Relevant Content
When a user asks a question, the system searches the vector store and retrieves the most relevant parts of the documents.

### 6. Generate Answer
The retrieved information and conversation history are provided to an OpenAI language model, which generates the final answer.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web interface |
| LangChain | RAG application framework |
| FAISS | Vector similarity search |
| Hugging Face | Text embeddings |
| `all-MiniLM-L6-v2` | Embedding model |
| OpenAI API | Answer generation |

## 📦 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Shivam46789/RAG_Chatbot.git
cd RAG_Chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up the OpenAI API Key

Set your OpenAI API key as an environment variable.

**Linux / macOS**

```bash
export OPENAI_API_KEY="your-api-key"
```

**Windows**

```cmd
setx OPENAI_API_KEY "your-api-key"
```

> **Important:** Never commit your API key to GitHub.

### 4. Run the Application

```bash
streamlit run app.py
```

The application will be available at: `http://localhost:8501`

## 💡 Use Cases

This chatbot can be used to:

- Ask questions about research papers
- Summarize PDF documents
- Search information across multiple PDFs
- Understand technical documentation
- Find specific information quickly
- Ask follow-up questions while maintaining conversation context

## 📁 Project Structure

```
ChatPDF/
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
└── ...
```

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Push your changes.
6. Open a pull request.

## 📄 License

This project is licensed under the Apache License. See the `LICENSE` file for more information.

## 🙏 Acknowledgments

This project uses the following open-source and third-party technologies:

- [FAISS](https://github.com/facebookresearch/faiss) for vector similarity search
- [Hugging Face](https://huggingface.co/) for the embedding model
- [Streamlit](https://streamlit.io/) for the web interface
- [OpenAI](https://openai.com/) for language model capabilities
- [LangChain](https://www.langchain.com/) for building the RAG pipeline

---

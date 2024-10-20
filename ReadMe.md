# INVESTORY

## Overview

INVESTORY offers two key features:

1. **AI-Powered Financial Insights**: Extracts and analyzes financial data from images using Llama3.2.
2. **Stock Summary App**: Summarizes stock information using RAG with a MySQL database and LLM insights.

Both features are accessible through a Streamlit web interface.

---

## Setup

### Prerequisites

- Python
- MySQL database server (local or cloud)
- API keys for Groq and Llama3.2 models
- Required Python packages (see `requirements.txt`)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Set up a virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure MySQL:
   - Create a new database
   - Update database credentials in `sample.py`

4. Create a `.env` file with your API key:
   ```plaintext
   GROQ_API_KEY=<your_groq_api_key>
   ```

---

## Usage

1. **Financial Insights Feature**:
   ```bash
   cd groq
   streamlit run main.py
   ```
   Upload financial document images (PNG/JPEG) to extract data and receive insights.

2. **Stock Summary Feature**:
   ```bash
   cd app
   streamlit run sample.py
   ```
   Enter stock names to retrieve information and summaries.

---

## Features

### AI-Powered Financial Insights
- Image upload and analysis
- Financial data extraction
- Insight generation using Llama3.2
- User-friendly Streamlit interface

### Stock Summary App
- MySQL database integration
- Stock search functionality
- LLM-powered stock summarization
- Automatic database population with example data

---

## Technologies

- Python
- Streamlit
- Groq API (Llama3.2-11b vision model)
- Llama3.2 (via Langchain)
- MySQL
- SQLAlchemy
- Dotenv

---

## Contributing

1. Fork the repository
2. Create a new feature branch
3. Submit a pull request with detailed change information

---

For any questions or issues, please open a GitHub issue or contact the maintainers.

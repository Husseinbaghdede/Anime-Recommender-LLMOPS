# Anime Recommendation System

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28-red.svg)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)](https://langchain.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://docker.com)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Deployed-orange.svg)](https://kubernetes.io)

An intelligent anime recommendation system powered by advanced vector similarity search and large language models (LLMs). Get personalized anime suggestions based on natural language queries describing your preferences.

## 🚀 Features

- **Natural Language Processing**: Describe your preferences in plain English
- **Vector-Based Search**: Utilizes semantic similarity for accurate recommendations
- **LLM-Powered Responses**: Generates detailed explanations for each recommendation
- **Interactive Web Interface**: Clean, user-friendly Streamlit application
- **Containerized Deployment**: Docker and Kubernetes ready
- **Scalable Architecture**: Modular design for easy maintenance and expansion

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Streamlit     │    │   Pipeline       │    │  Vector Store   │
│   Frontend      │───▶│   Controller     │───▶│   (ChromaDB)    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │   LLM Service    │
                       │   (Groq API)     │
                       └──────────────────┘
```

## 📋 Prerequisites

- Python 3.10 or higher
- Docker (optional, for containerized deployment)
- Kubernetes cluster (optional, for K8s deployment)
- Groq API key for LLM integration

## 🛠️ Installation

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd anime-recommender
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -e .
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   MODEL_NAME=mixtral-8x7b-32768
   ```

5. **Prepare the data**
   Ensure your anime dataset files are in the `data/` directory:
   - `anime_with_synopsis.csv`
   - `anime_updated.csv`

6. **Build the vector store**
   ```bash
   python pipeline/build_pipeline.py
   ```

7. **Run the application**
   ```bash
   streamlit run app/app.py
   ```

### Docker Deployment

1. **Build the Docker image**
   ```bash
   docker build -t anime-recommender:latest .
   ```

2. **Run the container**
   ```bash
   docker run -p 8501:8501 --env-file .env anime-recommender:latest
   ```

### Kubernetes Deployment

1. **Create secrets for environment variables**
   ```bash
   kubectl create secret generic llmops-secrets \
     --from-literal=GROQ_API_KEY=your_api_key \
     --from-literal=MODEL_NAME=mixtral-8x7b-32768
   ```

2. **Deploy to Kubernetes**
   ```bash
   kubectl apply -f llmops-k8s.yaml
   ```

## 📁 Project Structure

```
anime-recommender/
├── app/
│   ├── __init__.py
│   └── app.py                 # Streamlit web interface
├── pipeline/
│   ├── __init__.py
│   ├── build_pipeline.py      # Vector store construction
│   └── pipeline.py            # Main recommendation pipeline
├── src/
│   ├── __init__.py
│   ├── data_loader.py         # Data processing utilities
│   ├── vector_store.py        # Vector database management
│   ├── recommender.py         # LLM-based recommendation logic
│   └── prompt_template.py     # LLM prompt templates
├── utils/
│   ├── __init__.py
│   ├── logger.py              # Logging configuration
│   └── custom_exception.py    # Exception handling
├── config/
│   └── config.py              # Configuration settings
├── data/                      # Dataset files
├── logs/                      # Application logs
├── Dockerfile                 # Container configuration
├── llmops-k8s.yaml           # Kubernetes manifests
├── requirements.txt           # Python dependencies
├── setup.py                  # Package setup
└── README.md                 # Project documentation
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `GROQ_API_KEY` | API key for Groq LLM service | Required |
| `MODEL_NAME` | LLM model identifier | `mixtral-8x7b-32768` |

### Data Requirements

The system expects two CSV files in the `data/` directory:

1. **anime_with_synopsis.csv**: Original dataset with columns:
   - `Name`: Anime title
   - `Genres`: Comma-separated genres
   - `sypnopsis`: Plot synopsis

2. **anime_updated.csv**: Processed dataset (generated automatically)

## 🚀 Usage

### Web Interface

1. Navigate to `http://localhost:8501` after starting the application
2. Enter your anime preferences in natural language
   - Example: "light hearted anime with school settings"
   - Example: "dark fantasy anime with complex characters"
3. Receive three personalized recommendations with detailed explanations

### API Usage

The system can be extended to provide API endpoints. The core recommendation logic is accessible through:

```python
from pipeline.pipeline import AnimeRecommendationPipeline

# Initialize the pipeline
pipeline = AnimeRecommendationPipeline()

# Get recommendations
recommendations = pipeline.recommend("your query here")
print(recommendations)
```

## 🔍 How It Works

1. **Data Processing**: Raw anime data is cleaned and combined into searchable text chunks
2. **Vector Embedding**: Text is converted to high-dimensional vectors using HuggingFace embeddings
3. **Similarity Search**: User queries are matched against anime vectors using ChromaDB
4. **LLM Generation**: Retrieved context is processed by Groq's LLM to generate human-friendly recommendations

## 🧪 Technical Details

### Key Technologies

- **Vector Database**: ChromaDB for efficient similarity search
- **Embeddings**: HuggingFace `all-MiniLM-L6-v2` model
- **LLM**: Groq API with Mixtral-8x7B model
- **Framework**: LangChain for orchestrating the RAG pipeline
- **Frontend**: Streamlit for rapid web application development

### Performance Considerations

- Vector store is persisted locally for fast startup times
- Embeddings are cached to reduce API calls
- Chunking strategy optimized for anime synopsis length
- Temperature set to 0.1 for consistent recommendations

## 🐛 Troubleshooting

### Common Issues

1. **Missing API Key**: Ensure `GROQ_API_KEY` is set in your environment
2. **Data Files Not Found**: Verify anime CSV files are in the `data/` directory
3. **Vector Store Issues**: Delete `chroma_db/` and rebuild with `build_pipeline.py`
4. **Memory Issues**: Reduce batch size or use a smaller embedding model

### Logging

Application logs are stored in `logs/log_YYYY-MM-DD.log` with detailed error information.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **LangChain**: For the excellent RAG framework
- **Groq**: For providing fast LLM inference
- **HuggingFace**: For pre-trained embedding models
- **ChromaDB**: For efficient vector storage and retrieval



import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.chat_models import ChatAnthropic

# API keys are read from a local .env file (see .env.example). Nothing is hardcoded here.
load_dotenv()

SUPPORTED_MODELS = {
    "llama-3.1-8b-instant": lambda: ChatGroq(model="llama-3.1-8b-instant", temperature=0.2),
    "llama-3.3-70b-versatile": lambda: ChatGroq(model="llama-3.3-70b-versatile", temperature=0.2),
    "claude-2": lambda: ChatAnthropic(model="claude-2", temperature=0.2),
}


def load_model(model_name: str = "llama-3.1-8b-instant"):
    """Return a LangChain chat model shared by every agent in the pipeline."""
    try:
        return SUPPORTED_MODELS[model_name]()
    except KeyError:
        raise ValueError(
            f"Unsupported model: {model_name}. Choose one of: {', '.join(SUPPORTED_MODELS)}"
        ) from None


def check_env() -> None:
    """Fail early with a clear message if the required keys are missing."""
    missing = [k for k in ("GROQ_API_KEY", "TAVILY_API_KEY") if not os.getenv(k)]
    if missing:
        raise EnvironmentError(
            f"Missing environment variables: {', '.join(missing)}. "
            "Copy .env.example to .env and fill in your keys."
        )

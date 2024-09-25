import os
from langchain_groq import ChatGroq
from langchain.chat_models import ChatAnthropic
from langchain_community.chat_models import ChatPremAI

def load_model(model_name="llama3-8b-8192"):
    if model_name == "llama3-8b-8192":
        return ChatGroq(model=model_name, temperature=0.2)
    elif model_name == "claude-2":
        return ChatAnthropic(model=model_name, temperature=0.2)
    elif model_name == "llama-3.1-405b-instruct":
        return ChatPremAI(model=model_name, project_id=5881, temperature=0.2)
    else:
        raise ValueError(f"Unsupported model: {model_name}")

# Load environment variables
os.environ["PREMAI_API_KEY"] = "YOUR_PREMAI_API_KEY"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://eu.api.smith.langchain.com/"
os.environ["LANGCHAIN_API_KEY"] = "YOUR_LANGCHAIN_API_KEY"
os.environ["TAVILY_API_KEY"] = "YOUR_TAVILY_API_KEY"
os.environ["GROQ_API_KEY"] = "YOUR_GROQ_API_KEY"
os.environ["ANTHROPIC_API_KEY"] = "YOUR_ANTHROPIC_API_KEY"


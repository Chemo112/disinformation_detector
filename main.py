from agents.analyzer import run_agents
from utils.config import load_model

def main():
    model = load_model()
    
    # Example usage
    input_text = """
    A mysterious phenomenon has occurred in the small town of Pineview, Illinois, 
    where small, gelatinous orbs called "Gloopernuts" have begun falling from the sky.
    """
    
    result = run_agents(input_text, model)
    print(result)

if __name__ == "__main__":
    main()


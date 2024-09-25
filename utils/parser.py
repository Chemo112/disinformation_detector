import json
import re

def clean_json_string(s):
    s = s.strip()
    s = re.sub(r'^(`{1,3}json?\s*\n?)', '', s)
    s = re.sub(r'`{1,3}$', '', s)
    return s

def parse_text(input_text, model):
    template = """
    Parse the following text and return a JSON object with the following structure:
    {
        "SENTIMENT": {
            "CLASSIFICATION": "POSITIVE|NEGATIVE|NEUTRAL",
            "EXPLANATION": "Brief explanation of the sentiment"
        },
        "ENTITIES": {
            "PEOPLE": ["Person1", "Person2"],
            "ORGANIZATIONS": ["Org1", "Org2"],
            "OBJECTS": ["Object1", "Object2"],
            "ANIMALS": ["Animal1", "Animal2"],
            "LOCATIONS": ["Location1", "Location2"]
        },
        "MAIN_TOPICS": ["Topic1", "Topic2", "Topic3"]
    }
    """
    
    system_message = SystemMessage(content=template)
    user_message = HumanMessage(content=input_text)
    response = model([system_message, user_message])
    
    try:
        cleaned_content = clean_json_string(response.content)
        return json.loads(cleaned_content)
    except json.JSONDecodeError:
        return {
            "SENTIMENT": {"CLASSIFICATION": "UNKNOWN", "EXPLANATION": "Failed to parse"},
            "ENTITIES": {"PEOPLE": [], "ORGANIZATIONS": [], "OBJECTS": [], "ANIMALS": [], "LOCATIONS": []},
            "MAIN_TOPICS": ["Failed to parse"]
        }

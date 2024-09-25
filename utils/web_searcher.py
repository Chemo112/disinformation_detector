from langchain_community.tools import TavilySearchResults
from langchain_core.messages import HumanMessage, SystemMessage
import json

def extract_key_info(text, model):
    system_message = SystemMessage(content="""
    Extract key information from the given text that can be used to verify its authenticity.
    Focus on specific claims, events, people, organizations, and locations mentioned.
    Format the output as a list of key points, each on a new line starting with a dash (-).
    """)
    user_message = HumanMessage(content=text)
    response = model([system_message, user_message])
    return response.content.strip().split('\n')

def create_search_queries(key_points):
    return [f"fact check: {point.strip('- ')}" for point in key_points]

def analyze_search_results(original_text, search_results, model):
    analysis_prompt = f"""
    Compare the following original text with the search results provided.
    Determine if the original text appears to be accurate or if it might be a fake news article.

    Original text:
    {original_text}

    Search results:
    {search_results}

    Provide your analysis in the following JSON format:
    {{
        "CREDIBILITY_SCORE": A number between 0 (completely fake) and 10 (completely credible),
        "ANALYSIS": "A brief explanation of your credibility assessment",
        "MATCHING_FACTS": ["List of facts from the original text that were confirmed by the search results"],
        "CONTRADICTIONS": ["List of any contradictions or discrepancies found"],
        "UNVERIFIED_CLAIMS": ["List of claims from the original text that couldn't be verified"]
    }}
    """
    system_message = SystemMessage(content="You are an expert fact-checker. Analyze the provided information and respond in the requested JSON format.")
    user_message = HumanMessage(content=analysis_prompt)
    response = model([system_message, user_message])

    try:
        return json.loads(response.content)
    except json.JSONDecodeError:
        return {
            "CREDIBILITY_SCORE": 5,
            "ANALYSIS": "Unable to perform analysis due to parsing error.",
            "MATCHING_FACTS": [],
            "CONTRADICTIONS": [],
            "UNVERIFIED_CLAIMS": ["All claims (analysis failed)"]
        }

def web_search_agent(input_text, model):
    tool = TavilySearchResults(
        max_results=5,
        search_depth="advanced",
        include_answer=True,
        include_raw_content=True,
        include_images=False,
    )
    
    if isinstance(input_text, list):
        input_text = " ".join(input_text)

    key_points = extract_key_info(input_text, model)
    queries = create_search_queries(key_points)

    all_results = []
    for query in queries:
        try:
            search_result = tool.invoke({'query': query})
            all_results.extend(search_result)
        except Exception as e:
            print(f"Error during web search for query '{query}': {str(e)}")

    analysis = analyze_search_results(input_text, all_results, model)

    return {
        "KEY_POINTS": key_points,
        "SEARCH_RESULTS": all_results,
        "ANALYSIS": analysis
    }

import json
from utils.parser import parse_text
from utils.web_searcher import web_search_agent
from utils.templates import (
    template_sentiment, template_sensation, template_grammar,
    template_examinator, template_judge, template_scorer
)

def analyze_text(input_text, template, model):
    system_message = SystemMessage(content=template)
    user_message = HumanMessage(content=input_text)
    response = model([system_message, user_message])
    return response.content

def run_agents(input_text, model):
    output_sentiment = analyze_text(input_text, template_sentiment, model)
    sentiment_diz = parse_text(output_sentiment, model)

    output_searcher = web_search_agent(input_text, model)
    output_sensation = analyze_text(input_text, template_sensation, model)
    output_grammar = analyze_text(input_text, template_grammar, model)
    output_examinator = analyze_text(input_text, template_examinator, model)

    input_judge = (f"{output_sentiment}\n{output_sensation}\n{output_grammar}\n{output_examinator}\n{str(output_searcher)}")
    output_judge = analyze_text(input_judge, template_judge, model)

    output_scorer = analyze_text(output_judge, template_scorer, model)
    return output_scorer

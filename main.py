import argparse
import sys

from agents.analyzer import run_agents
from utils.config import check_env, load_model

SAMPLE_TEXT = """
A mysterious phenomenon has occurred in the small town of Pineview, Illinois,
where small, gelatinous orbs called "Gloopernuts" have begun falling from the sky.
"""


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Multi-agent disinformation analyzer: scores a text and explains why."
    )
    parser.add_argument("text", nargs="?", help="Text to analyze. Omit to use the built-in sample.")
    parser.add_argument("-f", "--file", help="Read the text to analyze from a file.")
    parser.add_argument("-m", "--model", default="llama-3.1-8b-instant", help="Model name (see utils/config.py).")
    args = parser.parse_args()

    if args.file:
        with open(args.file, encoding="utf-8") as fh:
            text = fh.read()
    elif args.text:
        text = args.text
    elif not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        text = SAMPLE_TEXT

    check_env()
    model = load_model(args.model)
    print(run_agents(text, model))


if __name__ == "__main__":
    main()

# Disinformation Detector

This project is designed to analyze text and detect potential disinformation using various NLP techniques and web searching capabilities.

## Project Structure

```
disinformation_detector/
├── main.py
├── agents/
│   └── analyzer.py
├── utils/
│   ├── config.py
│   ├── parser.py
│   ├── templates.py
│   └── web_searcher.py
├── data/
│   ├── Fake.csv
│   ├── True.csv
│   └── domain_list_clean.csv
├── requirements.txt
└── README.md
```

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/disinformation_detector.git
   cd disinformation_detector
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables in `utils/config.py` with your API keys.

## Usage

Run the main script:

```
python main.py
```

This will execute the disinformation detection process on a sample text. Modify `main.py` to analyze your own text or integrate it into your application.

## Components

- `main.py`: Entry point of the application
- `agents/analyzer.py`: Contains the main analysis functions
- `utils/config.py`: Configuration and environment variables
- `utils/parser.py`: Text parsing utilities
- `utils/templates.py`: Templates for various analysis tasks
- `utils/web_searcher.py`: Web search functionality for fact-checking

## Data

The `data/` directory contains CSV files with fake and true news examples, as well as a list of known disinformation domains.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the Apache 2.0 License.

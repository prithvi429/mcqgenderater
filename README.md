# MCQ Generator

## Overview
The MCQ Generator is a Python-based project designed to generate multiple-choice questions (MCQs) from given input data. It leverages advanced algorithms and utilities to create meaningful and accurate questions for educational purposes.

## Features
- **Automated MCQ Generation**: Generate MCQs from text data.
- **Customizable Options**: Configure the difficulty level, number of options, and more.
- **Streamlit Integration**: A user-friendly web interface for generating and viewing MCQs.
- **Logging**: Detailed logs for debugging and tracking.

## Project Structure
```
mcqgenderater/
├── README.md
├── requirements.txt
├── responce.json
├── setup.py
├── stremlitapp.py
├── test.py
├── build/
│   └── lib/
│       └── src/
│           ├── __init__.py
│           └── mcqgenerator/
│               ├── __init__.py
│               ├── logger.py
│               ├── MCQgenerator.py
│               └── utils.py
├── data.txt/
│   └── data.txt
├── env/
├── experiment/
│   ├── mcq.ipymb
│   └── mcq.ipynb
├── logs/
└── mcqgenderator.egg-info/
```

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd mcqgenderater
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Streamlit app:
   ```bash
   streamlit run stremlitapp.py
   ```
2. Follow the on-screen instructions to generate MCQs.

## Testing
Run the test suite to ensure everything is working correctly:
```bash
python test.py
```

## Logs
Logs are stored in the `logs/` directory with timestamps for easy debugging.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details .

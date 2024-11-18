# Flask Web Application

A simple Flask web application with automated testing using GitHub Actions.

## Project Structure
```
MyFlaskTest/
├── flaskapp/
│   ├── __init__.py
│   ├── app.py
│   └── templates/
│       └── index.html
├── tests/
│   ├── __init__.py
│   └── test_app.py
├── requirements.txt
└── setup.py
```

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/MyFlaskTest.git
cd MyFlaskTest
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the package in development mode:
```bash
pip install -e .
```

## Running Tests

To run the tests:
```bash
python -m pytest tests/
```

To run tests with coverage:
```bash
python -m pytest tests/ --cov=flaskapp
```

## Running the Application

To run the application:
```bash
python -m flask --app flaskapp.app run
```

The application will be available at `http://localhost:5000`.
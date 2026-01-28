# Sticky Ball Experiment One

A PySide6 autocomplete demo application with Docker containerization.

## Overview

This project demonstrates:
- Fetching random English words from an online dictionary API
- Building a PySide6 application with Qt autocomplete functionality
- Docker containerization for portable deployment

## Project Structure

```
sb_exp1/
├── docs/
│   ├── IMPLEMENTATION.md   # Detailed implementation plan
│   └── TASKS.md            # Task checklist
├── prd.txt                 # Product requirements
└── README.md
```

## Features

- **Word Generation**: Fetches 25 random English words (5-7 characters) and stores them in JSON
- **Autocomplete UI**: PySide6 text box with Qt autocomplete using the word corpus
- **Live Preview**: Second text box displays the first autocomplete match in real-time
- **Docker Support**: Containerized for consistent deployment

## Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Generate word list
python generate_words.py

# Run the application
python main.py
```

## Docker

```bash
# Build the container
docker build -t sb_exp1 .

# Run with Docker Compose
docker-compose up
```

## License

MIT

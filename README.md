# Langchain
Basic practice of gen ai 
# Event Management AI System

## Overview
This project is an **AI-driven Event Management System** that automates venue selection, logistics management, and event marketing using multiple agents. The system integrates **CrewAI** for agent orchestration, **ChromaDB** for persistent data storage, and **SerperDev** for web scraping.

## Features
- **Venue Selection**: Finds and stores venue details for future reference.
- **Logistics Management**: Handles catering and equipment arrangements.
- **Marketing & Communication**: Automates outreach and participant engagement.
- **Persistent Storage**: Uses ChromaDB to store and retrieve venue information efficiently.
- **Human Input Support**: Allows manual input where necessary.

## Installation
### Prerequisites
Ensure you have Python installed (recommended **Python 3.8+**).

### Install Dependencies
Run the following command to install required dependencies:
```sh
pip install -r requirements.txt
```

## Usage
### Running the Project
```sh
python main.py
```

### Workflow
1. **Venue Search**:
   - The system first checks if a venue exists in **ChromaDB**.
   - If found, it loads venue details from the database.
   - Otherwise, it scrapes the web for a new venue and stores it.
2. **Logistics and Marketing Tasks**:
   - The logistics manager arranges catering and equipment.
   - The marketing agent promotes the event and provides an engagement report.
3. **Persistent Storage**:
   - Venue details are stored in `chroma_db`.
   - Marketing reports are saved in `marketing_report.md`.

## Project Structure
```
├── chroma_db/             # Persistent database storage
├── venue_details.json     # JSON file storing venue data
├── marketing_report.md    # Marketing report output
├── main.py                # Main execution script
├── requirements.txt       # Required dependencies
└── README.md              # Project documentation
```

## API Keys
You need to set the following environment variables before running the project:
```sh
export OPENAI_API_KEY="your-api-key"
export SERPER_API_KEY="your-api-key"
```

## Contributors
- **Developer:** Your Name

## License
This project is licensed under the MIT License.


# 🛡️ SentinelPR - Autonomous DevSecOps Scanner

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688)
![DevSecOps](https://img.shields.io/badge/DevSecOps-Security-red)

A lightweight, continuous integration tool built with Python and FastAPI that intercepts GitHub webhooks to automatically scan pull requests for exposed secrets, API keys, and hardcoded credentials before they reach production.

## 🚀 The Problem it Solves
Data breaches often start with a simple developer mistake: accidentally committing an API key or database password to a repository. SentinelPR catches these vulnerabilities at the exact moment a developer opens a Pull Request, preventing bad code from ever merging.

## ✨ Features
- **Real-Time Scanning:** Instantly processes incoming GitHub webhook payloads.
- **Regex-Based Engine:** Detects high-risk patterns like AWS Access Keys, generic API secrets, and hardcoded passwords.
- **Automated Reporting:** Generates a structured JSON security report (`PASSED` or `FAILED` with remediation steps).
- **Interactive UI:** Built-in Swagger UI for easy testing and API documentation.

## 🛠️ Tech Stack
- **Language:** Python
- **Framework:** FastAPI
- **Server:** Uvicorn
- **Data Validation:** Pydantic

## 💻 How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/rohanpanwarr/SentinelPR.git](https://github.com/rohanpanwarr/SentinelPR.git)
cd SentinelPR 

2. Install Dependencies
pip install -r requirements.txt

3. Start the Server
Bash
python main.py
The server will start running at http://localhost:8000.

🧪 Testing the API
You can easily test the scanner without sending a real GitHub webhook by using the built-in interactive docs.

Open your browser and go to: http://localhost:8000/docs

Click on the POST /webhook endpoint.

Click "Try it out".

The request body will be pre-filled with a test payload containing a fake AWS key and password.

Click "Execute" to see the scanner catch the vulnerabilities and return a "status": "FAILED" report!

🛣️ Future Roadmap
[ ] Direct GitHub REST API integration to post security results as a comment directly on the PR.

[ ] Slack/Discord integration for high-severity vulnerability alerts.

[ ] Expanded regex rule engine for Stripe tokens, RSA keys, etc.
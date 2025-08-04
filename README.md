# 🏋️‍♂️ Workout Tracker with NLP & Google Sheets Integration

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![API](https://img.shields.io/badge/API-Nutritionix%20%7C%20ChatGPT%20%7C%20Google%20Sheets-orange.svg)
![Status](https://img.shields.io/badge/status-Active-brightgreen)

A simple yet powerful Python-based workout tracker that uses **natural language processing** (via ChatGPT API & Nutritionix) to interpret exercise input and automatically logs the data into a **Google Sheet** using the Sheety API.

---
## 🚀 Features

- 🧠 **Natural Language Input** — Just say things like *"I ran 2 miles and did 30 minutes of yoga"*.
- 🔍 **NLP-Powered Parsing** — Uses the **Nutritionix API** to extract detailed workout info (duration, calories, type).
- 🗓️ **Automatic Logging** — Records each session with date, time, and calories burned.
- 📊 **Google Sheets Integration** — Sends your workouts directly to a Google Sheet via **Sheety API**.
- 🔐 **Secure Key Management** — All API credentials are stored safely using `.env` environment variables.

---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/workout-tracker.git
cd workout-tracker

---

🛠️ Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/workout-tracker.git
cd workout-tracker
Install dependencies

bash
Copy
Edit
pip install python-dotenv requests
Set up environment variables
Create a .env file and add your API credentials:

ini
Copy
Edit
NUTRI_APP_ID=your_app_id
NUTRI_API_KEY=your_api_key
Run the program

bash
Copy
Edit
python main.py
🔒 Environment & Security
Uses python-dotenv to manage API keys securely.

API requests include bearer token authorization for Sheety.

🧩 Tech Stack
Python 3.9+

Nutritionix API – NLP for exercise parsing

Sheety API – Logging to Google Sheets

ChatGPT (via NLP provider) – Understanding natural language

dotenv – Secure configuration management

**🙋‍♀️ Future Ideas**
Add support for multiple exercises in one entry

Visualize progress with charts in Google Sheets or via a dashboard

Build a simple GUI or web interface



**🤝 Contributing**
Feel free to fork this repo, open issues, or submit pull requests to improve it!

**🌟 Give it a star if you like it!**

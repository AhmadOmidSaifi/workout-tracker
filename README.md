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
git clone https://github.com/your-username/workout-tracker.git
cd workout-tracker

### 📦 2. Install Dependencies

Make sure you have **Python 3.9+** installed.

You can install the required packages using **either of the following methods**:

#### ➤ Option 1: Install directly with pip

```bash
pip install python-dotenv requests

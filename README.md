# Secure Expense Tracker

A Django web application for tracking personal expenses, built for a cyber security course. It contains five deliberate security flaws from the OWASP Top 10, each documented with an exploit and a fix.

> **Warning:** This application is intentionally vulnerable. Do not deploy it to a public server or use real passwords or personal data in it.

## Overview

Users can register, log in, and manage their own expenses: add, view, edit, delete, and search. The app is a small but realistic backend system that stores user data. That makes it a good target for studying how common web vulnerabilities appear in real code and how to remediate them.

## Tech Stack

- Python 3.14
- Django 6.1.3
- SQLite (Django's default database)
- Plain HTML templates (no JavaScript framework)

## Features

- User registration, login, and logout
- Personal expense list with description, amount, category, and date
- Add, view, edit, and delete expenses
- Search expenses by category or description

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/YOUR-USERNAME/secure-expense-tracker.git
   cd secure-expense-tracker
   ```
2. (Optional) Create and activate a virtual environment:
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Create the database:
   ```
   python manage.py migrate
   ```
5. Start the development server:
   ```
   python manage.py runserver
   ```
6. Open http://127.0.0.1:8000/ in your browser.

If `django-admin` is not recognized on your system, use `python -m django` instead. `python manage.py` works either way.

## Security Flaws

Each flaw is in the backend and is real, not hypothetical. The vulnerable code is the active code, and the secure fix is written as a comment next to it, marked `# FIX:`.

| # | OWASP Category | Location | Status |
|---|----------------|----------|--------|
| 1 | Injection | Expense search | Planned |
| 2 | Broken Access Control | View/edit expense by ID | Planned |
| 3 | Identification and Authentication Failures | Login | Planned |
| 4 | Cryptographic Failures | Password storage | Planned |
| 5 | Security Logging and Monitoring Failures | Login and delete actions | Planned |

Detailed descriptions, line links to the flawed code and the fixes, and screenshots will be added as each flaw is implemented.

## Project Structure

```
secure-expense-tracker/
├── config/            # Project settings and root URL configuration
├── expenses/          # Main app: models, views, URLs, templates
├── screenshots/       # Before/after evidence for each flaw
├── manage.py
├── requirements.txt
└── README.md
```

## Screenshots

Screenshots demonstrating each exploit and its fix will be stored in the `screenshots/` folder, named `flaw-N-before` and `flaw-N-after`.

## References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [Django documentation](https://docs.djangoproject.com/en/6.1/)
- [Django security overview](https://docs.djangoproject.com/en/6.1/topics/security/)

## Disclaimer

This project is for educational purposes only. The vulnerabilities are intentional and exist to demonstrate common security mistakes.
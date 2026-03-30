from flask import Flask, request
import random
import requests
import os

app = Flask(__name__)

codes = {}

def generate_code():
    return str(random.randint(100000, 999999))

def send_email(email, code):
    url = "https://api.brevo.com/v3/smtp/email"

    headers = {
        "api-key": os.getenv("BREVO_API_KEY"),
        "Content-Type": "application/json"
    }

    data = {
        "sender": {"email": "support@vortex-ai.it.com"},
        "to": [{"email": email}],
        "subject": "رمز الدخول",
        "htmlContent": f"<h2>كودك هو: {code}</h2>"
    }

    requests.post(url, json=data, headers=headers)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.form

    email = data.get('email')
    paid = data.get('paid')

    if paid == 'true' and email:
        code = generate_code()
        codes[email] = code
        send_email(email, code)

    return "OK"

('/')app.route
:()def home
    "return "Server is running

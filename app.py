import json
import requests
from flask import render_template, Blueprint
from flask import Flask, redirect, url_for, request
from dotenv import load_dotenv
import os
import mysql.connector
from flaskext.mysql import MySQL
import smtplib
import random

# App
app = Flask(__name__)


@app.route('/',  methods=['POST', 'GET'])
def index():
    if request.method == 'POST':

        subject = request.form.get('subject')
        body = request.form.get('body')
        reciever = request.form.get('reciever')

        load_dotenv()

        EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
        EMAIL_PASSWORD = os.getenv('PASSWORD')

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            msg = f'Subject: {subject}\n\n{body}\n\n\nThis message was sent using the Online Email Sender application. Visit this application here: onlineemailsender.herokuapp.com'
            smtp.sendmail(EMAIL_ADDRESS, reciever, msg)

        return render_template('index.html', send_message=f'Email has been sucessfully sent to {reciever}.')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

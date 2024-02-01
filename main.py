import smtplib
import datetime as dt
import random
import pandas as pd


birthday = pd.read_csv('birthdays.csv')
my_email = "ipekkunluupy@gmail.com"
password = "your_email"


now = dt.datetime.now()
day = now.day
month = now.month

for index, row in birthday.iterrows():

    if row['month'] == month and row['day'] == day:

        with open(f"letter_templates/letter_{random.choice(range(1, 4))}.txt") as letter:
            content = letter.read()
            content = content.replace("[NAME]", row['name'])
            print(content)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)

            subject = "Happy Birthday"
            message = f"Subject: {subject}\n\n{content}".encode('utf-8')
            connection.sendmail(from_addr=my_email,
                                to_addrs=row['email'],
                                msg=message)
            connection.close()







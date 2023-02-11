# SEND AUTOMATIC BIRTHDAY EMAIL

import smtplib
import datetime as dt
import pandas as pd
from random import randint

# Required to send email

GMAIL = 'smtp.gmail.com'
EMAIL = 'EMAIL'
PASSWORD = 'PASSWORD'

# Persons birthday

bday_person_name = ''
bday_person_email = ''

# Email message

title = 'Happy Birthday!'
message = ''

# Read from birthday.csv

bday_data = pd.read_csv('./birthdays.csv').to_dict()
names = [value for (key, value) in bday_data['name'].items()]
emails = [value for (key, value) in bday_data['email'].items()]
birth_days = [value for (key, value) in bday_data['day'].items()]
birth_months = [value for (key, value) in bday_data['month'].items()]

# Check if today matches a birthday in the birthdays.csv

current_month = dt.datetime.now().month
current_day = dt.datetime.now().day

if current_day in birth_days and current_month in birth_months:
    index = birth_days.index(current_day)
    bday_person_name = names[index]
    bday_person_email = emails[index]

    # If true; pick random letter templates; replace the [NAME] with person's actual name from birthdays.csv

    letter_no = randint(1, 3)
    with open(f'./letter_templates/letter_{letter_no}.txt') as file:
        template = file.read()

    message = template.replace('[NAME]', f'{bday_person_name}')

    # Send birthday template to person's email address

    with smtplib.SMTP(GMAIL) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(to_addrs=bday_person_email,
                            from_addr=EMAIL,
                            msg=f'Subject: {title}\n\n{message}')





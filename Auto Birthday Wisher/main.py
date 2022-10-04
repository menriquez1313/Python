from datetime import datetime
import smtplib
import pandas
import random

#Add email and pw
MY_EMAIL = ""
MY_PASSWORD = ""

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    file_bath = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace("[NAME]", birthday_person["name"])
        
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.start()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["name"],
                            msg=f"Subject: Happy Birhday!\n\n{contents}"
                            )
        





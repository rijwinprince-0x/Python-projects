import smtplib
import datetime as dt
import random
MY_EMAIL = "<your email>"
MY_PASSWORD = "<your password>"

# 0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday,
# 4 = Friday, 5 = Saturday, 6 = Sunday
TARGET_DAY = 0

now=dt.datetime.now()
weekday=now.weekday()
if weekday==TARGET_DAY:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)


    print(quote)
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"subject:DAY Motivation\n\n{quote}".encode('utf-8')
        )





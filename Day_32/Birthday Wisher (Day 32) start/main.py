import smtplib
import datetime as dt
from random import choice
MY_EMAIL = "songponsosoxx@gmail.com"
MY_PASSWORD = "mhvrevylgezzeghd"
now = dt.datetime.now()
weak_day = now.weekday()
if weak_day == 0:
    with open("quotes.txt","r") as quotesfile:
        quotes = quotesfile.readlines()
        quote = choice(quotes)
        print(quote)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection: # Adjust port and timeout
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg=f"Subject:Monday Motivation\n\n{quote}")

        print("Email sent successfully!")



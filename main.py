import smtplib
import random
import datetime as dt


def quote_generator():
    with open("quotes.txt", 'r') as data:
        quote_list = data.readlines()
        stripped_quotes = [quote.strip("\n") for quote in quote_list]
        random_quote = random.choice(stripped_quotes)
        return random_quote


now = dt.datetime.now()
day = now.strftime("%A")

if day == "Monday":
    MY_EMAIL = 'your email'
    PASSWORD = "your password"
    quote = quote_generator()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # make connection secure
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="senders address",
                            msg=f"Subject:Quote for the day"
                                f"\n\n{quote}")

import smtplib
import random
import datetime as dt

my_email = "green.100days@gmail.com"
password = "tbofnhzlhzcsgruv"


# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="green.100days@yahoo.com", 
#         msg="Subject:Hello\n\nThis is the body of my email.")


# For Yahoo
# #connection = smtplib.SMTP("smtp.mail.yahoo.com")


# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()

# date_of_birth = dt.datetime(year=1995, month=12, day=15)

# print(now)



# A random quote generator
def random_line(file_name):
    lines = open(file_name).read().splitlines()
    return random.choice(lines)

## Frm Udemy course
# with open("quotes.txt") as quote_file:
#     all_quotes = quote_file.readlines()
#     quote = random.choice(all_quotes)


random_quote = random_line('quotes.txt')
print(random_quote)

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2: #set it to whatever day of the week it is for testing purposes
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr= my_email, 
            to_addrs= my_email, 
            msg= f"Subject:Monday Motivation\n\n{random_quote}")

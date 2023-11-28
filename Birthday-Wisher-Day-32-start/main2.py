##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv -> convert csv into pandas dataframe, check column value against date time

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import os, random
import pandas as pd
import datetime as dt

my_email = "green.100days@gmail.com"
password = "tbofnhzlhzcsgruv"
PLACEHOLDER = "[NAME]"

#Convert CSV file of birthdays to a Pandas df
df = pd.read_csv("birthdays.csv")

print(df)

now = dt.datetime.now()
month = now.month
day = now.day


# Check if today matches a birthday in the birthdays.csv
for ind in df.index:
    if df['month'][ind] == month and df['day'][ind] == day:
        letter_directory = "/home/andrew/100-days-of-code-python-bootcamp/Birthday-Wisher-Day-32-start/letter_templates"
        
        # Get only files in the directory
        letter_files = [f for f in os.listdir(letter_directory) if os.path.isfile(os.path.join(letter_directory, f))]
        
        # Check if there are any files in the directory
        if not letter_files:
            print("Error: No letter templates found.")
            break

        letter = random.choice(letter_files)
        letter_path = os.path.join(letter_directory, letter)
        with open(letter_path) as letter_file:
            letter_content = letter_file.read()
            new_letter = letter_content.replace(PLACEHOLDER, df['name'][ind])

        # Format the email body using triple-quoted string
        email_body = f"""Subject: Happy Birthday!\n\n{new_letter}"""

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=df['email'][ind],  # Send the email to the recipient's address
                msg=email_body
            )

#######--------Udemy Implementation-----------------###########

# from datetime import datetime

# today = datetime.now()
# today_tuple = (today.month, today.day)

# data = pd.read_csv("birthdays.csv")

# #dict comprehension
# birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows() }

# if today_tuple in birthdays_dict:
#     birthday_person = birthdays_dict[today_tuple]
#     file_path = "letter_templates/letter_{random.randint(1,3)}.txt"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#         contents = contents.replace("[NAME]", birthday_person["name"])
    
#     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#         connection.starttls()
#         connection.login(my_email, password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs=birthday_person["email"]
#             msg=f"Subject:Happy Birthday!\n\n{contents}"

#         )

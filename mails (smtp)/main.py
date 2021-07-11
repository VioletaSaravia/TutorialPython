import smtplib
import json
import datetime as dt
import pandas as pd
import random

smpt_info = {
	"hotmail.com" : "smtp.live.com",
	"yahoo.com" : "smtp.mail.yahoo.com",
	"gmail.com" : "smtp.gmail.com"
}

# with open('mails/smtps.json', 'w') as smptsfile:
    # smpt_info_dump = json.dumps(smpt_info) 
    # smptsfile.write(smpt_info_dump)

# # with open('mails.json', 'r+') as mailsfile:
    # # mailsdump = json.load('mails/mails.json')

# now = dt.datetime.now()
# year = now.year

# nacimiento = dt.datetime(year=1994, month=7, day=23, hour=7)
# dia = dt.datetime.now().weekday()

mi_mail = "saraviavioleta@gmail.com"

def get_smpt(mail):
	for server, address in smpt_info.items():
		if server in mail:
			return address

# with smtplib.SMTP(get_smpt(mi_mail)) as connection:
	# connection.starttls()
	# connection.login(user=mi_mail, password='rn2dFFnd8T^@r#')
	# mensaje = "Subject:Hola\n\nHola viole."
	# connection.sendmail(from_addr=mi_mail, to_addrs="bqkdvnvdzfrjgpsffm@upived.online", msg=mensaje)

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple] # si cumplen dos personas da error
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP(get_smpt(mi_mail)) as connection:
        connection.starttls()
        connection.login(mi_mail, MY_PASSWORD)
        connection.sendmail(
            from_addr=mi_mail,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
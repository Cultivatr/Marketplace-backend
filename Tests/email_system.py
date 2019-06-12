#####################################
##### NOT TRACKING MASTER ###########
#####################################


import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'cultivatr111@outlook.com'
PASSWORD = 'EvolveU1'


def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def send_email(farm_name, user_email):
    message_template = read_template('email_message.txt')
    # set up the SMTP server
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    msg = MIMEMultipart()       # create a message

    message = message_template.substitute(
        FARM_NAME=farm_name)

    msg['From'] = MY_ADDRESS
    msg['To'] = user_email
    msg['Subject'] = "Cultivatr Alert Email"

    msg.attach(MIMEText(message, 'plain'))

    s.send_message(msg)
    del msg

    s.quit()

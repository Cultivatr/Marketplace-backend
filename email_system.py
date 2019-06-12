import smtplib

MY_ADDRESS = 'noreply.cultivatr@gmail.com'
MY_PASSWORD = 'Cheese111'


def send_email(farm_name, user_email):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(MY_ADDRESS, MY_PASSWORD)
    SUBJECT = "Cultivatr Email Alert"
    TEXT = "{},\n\n Your order has been reviewed, please log in to your account to see the status. \n\n Cultivatr Team".format(
        farm_name)

    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    print("EMAIL", user_email)
    server.sendmail(
        MY_ADDRESS,
        user_email,
        message)
    server.quit()

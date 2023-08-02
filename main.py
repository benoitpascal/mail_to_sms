from get_mail import get_mails
from send_with_pushbullet import send_with_pushbullet
from config import *


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
    emails = get_mails(EMAIL_ADDRESS, PASSWORD)
    for email in emails:
        print("Sujet:", email["sujet"])
        print("De:", email["de"])
        print("Date:", email["date"])
        print("Corps:", email["corps"])
        print("")

    # send_with_pushbullet("titre_pb", "msg", TOKEN_PUSHBULLET)



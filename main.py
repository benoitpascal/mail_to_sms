from get_mail import get_mails
from analyse_mail import *
from send_with_pushbullet import send_with_pushbullet
from config import *


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
    print("")
    emails = get_mails(EMAIL_ADDRESS, PASSWORD, 10)
    for email in emails:
        print("")
        print("Sujet:", email["sujet"], ". De :", email["de"], ". Date :", email["date"])
        # print("Corps:", email["corps"])

        contains_date, parsed_date = loof_for_date(email["corps"])

        if contains_date:
            print("Une date a été trouvée dans le corps de l'e-mail:", parsed_date)
        else:
            print("Aucune date n'a été trouvée dans le corps de l'e-mail.")

    # send_with_pushbullet("titre_pb", "msg", TOKEN_PUSHBULLET)



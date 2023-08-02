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

    # On prépare le message à envoyer
    msg = ''
    print("")
    emails = get_mails(EMAIL_ADDRESS, PASSWORD, 15)
    for email in emails:
        # Par défaut, on indique que le mail n'est pas à notifier
        to_notify = False

        contains_date, parsed_date = loof_for_date(email["corps"])

        if contains_date:
            to_notify = True
            msg += "Une date a été trouvée dans le corps de l'e-mail"
            # msg += parsed_date

        text_to_control = [
            "rendez-vous",
            "rendez vous"
        ]

        for text in text_to_control:
            contains_text = loof_for_text(email["corps"], text)
            if contains_text:
                to_notify = True
                msg += f"Le texte {text} a été trouvée dans le corps de l'e-mail "

        if to_notify:
            msg += "Sujet"
            msg += email["sujet"]

    send_with_pushbullet("titre_pb", msg, TOKEN_PUSHBULLET)



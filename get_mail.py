import imaplib
import email
from email.header import decode_header


def get_mails(email_address, password, limite=1):

    # Connexion au serveur IMAP de Gmail
    mail = verifier_connexion(email_address, password)

    # Sélection de tous les emails
    mailbox_name = '"[Gmail]/Tous les messages"'
    mail.select(mailbox_name)

    # Recherche des e-mails non lus
    status, messages = mail.search(None, "ALL")

    print("Récupération des messages")
    # Liste des identifiants d'e-mails non lus
    email_ids = messages[0].split()
    print(len(email_ids), "messages récupérés")

    # Limiter au nombre spécifié d'e-mails
    if limite is not None and len(email_ids) > limite:
        email_ids = email_ids[-(limite):]

    emails = []

    print("Récupération du contenu des emails ...")
    print("id des emails", end=" :")
    for email_id in email_ids:
        print(email_id, end=", ")
        # Récupération du message
        status, msg_data = mail.fetch(email_id, "(RFC822)")
        raw_email = msg_data[0][1]

        # Parsing du message en tant qu'objet Email
        msg = email.message_from_bytes(raw_email)

        # Sujet de l'e-mail
        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else "utf-8")

        # De qui l'e-mail provient
        from_ = msg.get("From")

        # Date d'envoi de l'e-mail
        date_sent = msg.get("Date")

        # Corps de l'e-mail
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                if content_type == "text/plain":
                    body = part.get_payload(decode=True).decode('utf-8', errors='replace')
                    break
        else:
            body = msg.get_payload(decode=True).decode('utf-8', errors='replace')

        emails.append({
            "sujet": subject,
            "de": from_,
            "date": date_sent,
            "corps": body
        })

    # Déconnexion
    mail.logout()

    return emails


def verifier_connexion(adresse_email, mot_de_passe):
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        status, response = mail.login(adresse_email, mot_de_passe)
        if status == "OK":
            print("Connexion réussie.")
            return mail
        else:
            print("Échec de la connexion.")
            return None
    except Exception as e:
        print("Erreur lors de la connexion:", str(e))
        return None


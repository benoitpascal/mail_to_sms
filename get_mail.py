import imaplib
import email
from email.header import decode_header


def get_mails(email_address, password, limite=100):

    # Connexion au serveur IMAP de Gmail
    mail = verifier_connexion(email_address, password)
    # if mail is not None:
    #     mail.login(email_address, password)

    # Sélection de la boîte de réception (INBOX)
    mail.select("inbox")

    # Recherche des e-mails non lus
    status, messages = mail.search(None, "(ALL)")

    # Liste des identifiants d'e-mails non lus
    email_ids = messages[0].split()

    # Limiter à 100 premiers e-mails
    if len(email_ids) > 100:
        email_ids = email_ids[:100]

    # Limiter au nombre spécifié d'e-mails
    if limite is not None and len(email_ids) > limite:
        email_ids = email_ids[:limite]

    emails = []

    for email_id in email_ids:
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

        emails.append({
            "sujet": subject,
            "de": from_
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


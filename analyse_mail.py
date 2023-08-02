import email
from email.header import decode_header
import re
from dateutil.parser import parse as parse_date


def loof_for_date(email_body):
    # print(email_body)
    # Chercher des motifs de dates dans le corps de l'e-mail
    date_patterns = [
        r'\d{1,2}[/\-.]\d{1,2}[/\-.]\d{2,4}',  # Recherche des dates au format jour/mois/année
        r'\d{1,2}[/\-.]\w{3,}[/\-.]\d{2,4}',  # Recherche des dates au format jour/mois en lettres/année
        r'\d{4}[/\-.]\d{1,2}[/\-.]\d{1,2}',  # Recherche des dates au format année/mois/jour
        r'\b(?:Lundi|Mardi|Mercredi|Jeudi|Vendredi|Samedi|Dimanche)\s+\d{1,2}\s+\w+\b',  # Jour de la semaine + jour + mois en lettres
        r'\b\d{1,2}\s+\w+\s+\d{4}\b',  # Jour + mois en lettres + année
    ]

    for pattern in date_patterns:
        matches = re.findall(pattern, email_body)
        if matches:
            # Si au moins une date est trouvée, nous allons essayer de la parser
            for match in matches:
                try:
                    parsed_date = parse_date(match, fuzzy=True)
                    return True, parsed_date
                except:
                    continue

    return False, None

def loof_for_text(email_body, text):
    # Utilisez re.escape pour échapper les caractères spéciaux dans le motif
    escaped_text = re.escape(text)

    # Créez un motif en utilisant le texte échappé
    pattern = fr'\b{escaped_text}\b'

    # Recherche du motif de texte dans le corps de l'e-mail
    matches = re.findall(pattern, email_body, re.IGNORECASE)

    return len(matches) > 0

import requests

def send_with_pushbullet(titre, message, token):
    url = 'https://api.pushbullet.com/v2/pushes'
    headers = {
        'Access-Token': token,
        'Content-Type': 'application/json'
    }
    data = {
        'type': 'note',
        'title': titre,
        'body': message
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Message Pushbullet envoyé avec succès.")
    else:
        print("Échec de l'envoi du message Pushbullet.")
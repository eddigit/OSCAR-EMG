#!/usr/bin/env python3
"""
Script pour envoyer des emails via Gmail SMTP
Usage: python3 send_email.py "destinataire@email.com" "Sujet" "Corps du message"
"""

import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration Oscar
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "oscarcoachdigital@gmail.com"
SENDER_NAME = "Oscar - Coach Digital"
APP_PASSWORD = "dcgkrkghzrizhcnj"  # App password sans espaces

def send_email(to_email: str, subject: str, body: str, html: bool = False):
    """Envoie un email via Gmail SMTP"""
    try:
        # Créer le message
        msg = MIMEMultipart('alternative')
        msg['From'] = f"{SENDER_NAME} <{SENDER_EMAIL}>"
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Ajouter le corps du message
        if html:
            msg.attach(MIMEText(body, 'html', 'utf-8'))
        else:
            msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        # Connexion et envoi
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.send_message(msg)
        
        print(f"✅ Email envoyé à {to_email}")
        return True
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 send_email.py 'destinataire@email.com' 'Sujet' 'Corps du message'")
        sys.exit(1)
    
    to_email = sys.argv[1]
    subject = sys.argv[2]
    body = sys.argv[3]
    
    success = send_email(to_email, subject, body)
    sys.exit(0 if success else 1)

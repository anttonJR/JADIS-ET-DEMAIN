import os
import anthropic
import resend
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# --- KILL SWITCH ---
# Pour désactiver : mettre ENABLED=false dans le fichier .env
# Aucune requête ne sera faite si désactivé
ENABLED = os.getenv("ENABLED", "true").lower() == "true"

if not ENABLED:
    print("⏸️ Envoi désactivé (ENABLED=false dans .env). Aucune requête effectuée.")
    exit(0)

# --- CONFIG ---
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
RESEND_API_KEY = os.getenv("RESEND_API_KEY")
EMAIL_TO = os.getenv("EMAIL_TO")
EMAIL_FROM = os.getenv("EMAIL_FROM")  # ex: onboarding@resend.dev ou ton domaine vérifié
SHOP_NAME = os.getenv("SHOP_NAME", "notre magasin")

def generate_suggestions():
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    today = datetime.now().strftime("%A %d %B %Y")

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""Tu es un expert en marketing pour les magasins de vide grenier et brocantes.

Aujourd'hui c'est le {today}.

Génère exactement 5 suggestions de posts Instagram créatives et engageantes pour {SHOP_NAME}, un magasin de vide grenier permanent.

Pour chaque suggestion donne :
- 🎯 Le concept du post (en 1 ligne)
- 📝 La légende suggérée (2-3 phrases max, ton chaleureux et authentique)
- #️⃣ 5 hashtags pertinents

Pense à varier les types de contenu : story, produit du jour, ambiance magasin, anecdote, promotion, etc.
Adapte les suggestions à la saison et au jour de la semaine.
Formate clairement chaque suggestion avec un numéro."""
            }
        ]
    )

    return message.content[0].text

def send_email(suggestions):
    resend.api_key = RESEND_API_KEY

    today = datetime.now().strftime("%A %d %B")

    html_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; background-color: #FDF6EC;">

        <div style="background-color: #8B6F47; padding: 20px; border-radius: 10px 10px 0 0; text-align: center;">
            <h1 style="color: white; margin: 0;">✨ Vos 5 idées de posts du jour</h1>
            <p style="color: #FFD700; margin: 5px 0 0 0;">{today}</p>
        </div>

        <div style="background-color: white; padding: 25px; border-radius: 0 0 10px 10px; border: 1px solid #D4A574;">
            <p style="color: #666; font-style: italic;">Bonjour ! Voici vos suggestions du jour pour {SHOP_NAME} 🛍️</p>

            <div style="white-space: pre-wrap; line-height: 1.8; color: #333;">
{suggestions}
            </div>

            <hr style="border: 1px solid #D4A574; margin: 20px 0;">
            <p style="color: #999; font-size: 12px; text-align: center;">
                💡 Utilisez votre app pour générer vos stories Instagram !<br>
                Bonne journée et bonnes ventes ! 🎉
            </p>
        </div>

    </body>
    </html>
    """

    params = {
        "from": EMAIL_FROM,
        "to": [EMAIL_TO],
        "subject": f"✨ Vos 5 idées de posts Instagram - {today}",
        "html": html_content,
    }

    resend.Emails.send(params)
    print(f"✅ Email envoyé à {EMAIL_TO}")

if __name__ == "__main__":
    print("🤖 Génération des suggestions...")
    suggestions = generate_suggestions()
    print("📧 Envoi de l'email...")
    send_email(suggestions)
    print("🎉 Done !")

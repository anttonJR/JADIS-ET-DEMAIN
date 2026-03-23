import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import os

st.set_page_config(page_title="📸 Générateur Story Magasin", layout="wide", initial_sidebar_state="collapsed")

st.title("📸 Générateur de Stories Instagram")
st.subheader("Créez vos stories en 3 clics!")

# Charger la template
template_path = "template_story.png"
template = Image.open(template_path)

col1, col2 = st.columns(2)

with col1:
    st.write("**Étape 1: Choisir votre photo**")
    uploaded_file = st.file_uploader("Sélectionnez une photo", type=["jpg", "png", "jpeg"])
    
with col2:
    st.write("**Étape 2: Nom de l'article**")
    article_name = st.text_input("Écrivez le nom de l'article", placeholder="Ex: Vase vintage bleu")

if uploaded_file and article_name:
    st.divider()
    st.write("**Aperçu de votre story:**")
    
    # Charger la photo uploadée
    uploaded_image = Image.open(uploaded_file)
    
    # Créer une copie de la template
    result = template.copy()
    draw = ImageDraw.Draw(result)
    
    # Redimensionner et positionner la photo uploadée
    photo_width = 1020
    photo_height = 1400
    
    # Redimensionner la photo pour qu'elle s'adapte à l'espace
    uploaded_image.thumbnail((photo_width, photo_height), Image.Resampling.LANCZOS)
    
    # Centrer la photo dans la zone blanche
    photo_x = (1080 - uploaded_image.width) // 2
    photo_y = 200 + (photo_height - uploaded_image.height) // 2
    
    # Coller la photo
    result.paste(uploaded_image, (photo_x, photo_y))
    
    # Ajouter le texte du nom de l'article
    try:
        text_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 50)
    except:
        text_font = ImageFont.load_default()
    
    text_zone_y = 1920 - 250
    draw.text((540, text_zone_y + 80), article_name.upper(), 
             fill='white', font=text_font, anchor="mm")
    
    # Afficher l'aperçu
    st.image(result, use_container_width=True)
    
    # Bouton télécharger
    st.divider()
    img_io = io.BytesIO()
    result.save(img_io, format='PNG')
    img_io.seek(0)
    
    st.download_button(
        label="⬇️ Télécharger l'image",
        data=img_io,
        file_name=f"{article_name}.png",
        mime="image/png",
        use_container_width=True
    )
    
    st.success("✅ Prêt à poster sur Instagram!")

else:
    st.info("👆 Remplissez les deux étapes pour générer votre story")


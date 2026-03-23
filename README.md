# 📸 Générateur de Stories Instagram

Une petite app pour générer rapidement vos stories Instagram avec une template personnalisée!

## Installation & Utilisation

### Option 1 : Sur votre ordinateur (local)

**1. Installer Python** (si pas déjà fait)
- Télécharger depuis https://www.python.org/downloads/
- Cocher "Add Python to PATH" pendant l'installation

**2. Installer les dépendances**
```bash
pip install streamlit pillow
```

**3. Lancer l'app**
- Mettre le fichier `app.py` et `template_story.png` dans un dossier
- Ouvrir le terminal dans ce dossier
- Taper :
```bash
streamlit run app.py
```
- Une page s'ouvre automatiquement sur `http://localhost:8501`
- Accéder depuis votre téléphone en utilisant l'adresse IP de votre ordinateur

---

### Option 2 : En ligne (gratuit, partout)

**Déployer gratuitement sur Streamlit Cloud :**
1. Créer un compte sur https://streamlit.io/cloud
2. Uploader votre dossier sur GitHub
3. Connecter Streamlit à GitHub
4. L'app est accessible partout via un lien !

---

## Comment ça marche ?

1. **Choisir une photo** : Sélectionner une photo de votre téléphone ou ordinateur
2. **Taper le nom** : Écrire le nom de l'article (ex: "Vase vintage bleu")
3. **Générer** : L'image s'affiche avec votre photo + le texte
4. **Télécharger** : Cliquer le bouton et l'image est prête à poster en story !

---

## Customiser la template

Pour changer les couleurs ou le design de la template :
- Ouvrir `template_story.png` dans Photoshop, Canva, ou Paint
- Modifier et re-sauvegarder
- L'app utilisera la nouvelle version !

---

**Questions ?** Demandez ! 😊

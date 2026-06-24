# image_processing.py

"""
module responsable du traitement des images :
- ouverture de l'image principale
- ouverture du logo
- redimensionnement
- rotation
- collage
"""

from PIL import Image  # importe pillow pour manipuler les images


def process_images(image1_path: str, logo_path: str, output_path: str):
    # ouvre l'image principale
    img1 = Image.open(image1_path)  # charge l'image locale

    # redimensionne l'image principale
    img1 = img1.resize((800, 800))  # ajuste la taille de l'image

    # ouvre le logo
    logo = Image.open(logo_path)  # charge le logo

    # redimensionne le logo
    logo = logo.resize((200, 200))  # réduit la taille du logo

    # applique une rotation au logo
    logo = logo.rotate(15, expand=True)  # incline légèrement le logo

    # colle le logo en bas à droite
    img1.paste(logo, (img1.width - logo.width - 20, img1.height - logo.height - 20), logo)  # colle le logo avec transparence

    # sauvegarde l'image finale
    img1.save(output_path)  # enregistre l'image finale

    return output_path  # retourne le chemin de l'image finale


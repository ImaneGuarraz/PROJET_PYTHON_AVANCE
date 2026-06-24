# main.py

"""
script principal qui orchestre :
- la lecture du livre en local
- l'extraction du chapitre 1
- l'analyse des paragraphes
- la création du graphique
- le traitement des images
- la génération du document word
"""

from text_processing import download_book, extract_metadata_and_first_chapter, paragraph_stats  # importe les fonctions de traitement du texte
from charts_book import create_paragraph_length_chart  # importe la fonction de création du graphique
from image_processing import process_images  # importe la fonction de traitement d'image
from report_word import create_report_docx  # importe la fonction de génération du document word


# définit le chemin de l'image principale locale
IMAGE1_LOCAL = "assets/frankenstein_local.jpg"  # indique l'image locale utilisée comme image #1

# définit le chemin du logo (ton vrai logo)
LOGO_LOCAL = "assets/frankenstein_distribution.png"  # indique le logo utilisé pour le collage


def main():
    try:
        print("Lecture du livre local...")
        text = download_book()  # lit le fichier pg84.txt dans assets

        print("Extraction du chapitre 1...")
        meta = extract_metadata_and_first_chapter(text)  # extrait titre, auteur et chapitre 1
        chapter = meta["first_chapter"]  # récupère le texte du chapitre 1

        print("Analyse des paragraphes...")
        analysis = paragraph_stats(chapter)  # calcule les statistiques des paragraphes
        stats = analysis["stats"]  # récupère les statistiques globales

        print("Création du graphique...")
        chart_path = "frankenstein_distribution.png"  # définit le nom du fichier du graphique
        create_paragraph_length_chart(analysis["distribution"], chart_path)  # génère le graphique

        print("Traitement des images...")
        final_image_path = process_images(
            IMAGE1_LOCAL,  # image principale
            LOGO_LOCAL,  # logo réel
            "image_finale.jpg"  # nom de l'image finale
        )  # traite l'image et colle le logo

        print("Création du document Word...")
        output_docx = create_report_docx(
            meta,  # métadonnées du livre
            stats,  # statistiques des paragraphes
            chart_path,  # chemin du graphique
            final_image_path,  # chemin de l'image finale
            "Rapport_Frankenstein.docx"  # nom du document word généré
        )  # génère le document word

        print("\n=== Rapport généré ===")
        print(f"Document Word : {output_docx}")  # affiche le chemin du document généré
        print(f"Graphique : {chart_path}")  # affiche le chemin du graphique
        print(f"Image finale : {final_image_path}")  # affiche le chemin de l'image finale

    except Exception as e:
        print("\nUne erreur est survenue :")
        print(str(e))  # affiche l'erreur rencontrée


if __name__ == "__main__":
    main()  # exécute la fonction principale

import json

def process_stream_data(stream_data):
    # Initialiser une structure de données pour stocker les données uniques
    unique_links = set()

    # Fonction pour traiter un document JSON et éliminer les répétitions
    def process_json_document(json_document):
        data = json.loads(json_document)

        # Identifier les données uniques en utilisant la clé "link"
        link = data.get("link")

        # Vérifier si ce lien unique a déjà été traité
        if link not in unique_links:
            unique_links.add(link)

            # Faites ce que vous devez faire avec les données uniques, par exemple les enregistrer, les traiter, etc.
            print("Nouveau lien unique :", link)
        else:
            print("Lien en double détecté :", link)

    for json_document in stream_data:
        process_json_document(json.dumps(json_document))
         # Convertir l'objet en JSON pour le traitement\
    return unique_links







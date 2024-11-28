todos = []
# Fonction pour créer un todo
def creer_todo():
    titre = input("Entrez le titre du todo : ")
    todos.append({"titre": titre, "statut": "À faire"})
    print(f'Todo "{titre}" ajouté.')

# Fonction pour afficher tous les todos
def lister_todos():
    if len(todos) == 0:
        print("Aucun todo à afficher.")
    else:
        print("Voici la liste des todos :")
        for i, todo in enumerate(todos, start=1):
            print(f"{i}. {todo['titre']} - {todo['statut']}")

# Menu principal
def menu():
    while True:
        print("\n=== Menu ===")
        print("1. Ajouter un todo")
        print("2. Voir les todos")
        print("q. Quitter")
        choix = input("Votre choix : ")

        if choix == "1":
            creer_todo()
        elif choix == "2":
            lister_todos()
        elif choix == "q":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, essayez encore.")

# Démarrer le programme
menu()

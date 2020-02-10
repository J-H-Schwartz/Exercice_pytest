

class Display:

    def __init__(self, controller):
        self.controller = controller

    def start(self):
        self.display_all_articles()
        while True:
            choice = input(
                "Que souhaitez vous faire ? (L)ister  /  (C)réer article  /  (M)ise à jour article  /  (S)upprimer / "
                "(Q)uitter :").upper()
            if choice == "L":
                self.display_all_articles()
            elif choice == "C":
                self.create_article()
            elif choice == "M":
                self.update_article()
            elif choice == "S":
                self.delete_article()
            elif choice == "Q":
                break
            else:
                print("Commande non reconnue, recommencez.")

    def display_all_articles(self):
        all_articles = self.controller.get_all_articles()
        for article in all_articles:
            print(article)

    def update_article(self):
        title = input("Entrez le titre de l'article que vous souhaitez modifier: ")
        text = input("Entrez le nouveau texte de l'article: ")
        update = self.controller.update_article(title, text)
        if update:
            print("Article mis à jour avec succès.")
        else:
            print("L'article n'existe pas.")

    def create_article(self):
        title = input("Entrez le titre du nouvel article: ")
        text = input("Entre le texte du nouvel article: ")
        creation = self.controller.create_article(title, text)
        if creation:
            print("Article créé avec succès.")
        else:
            print("L'article existe déja.")

    def delete_article(self):
        title = input("Entrez le titre de l'article à supprimer: ")
        deletion = self.controller.delete_article(title)
        if deletion :
            print("Article supprimé avec succès.")
        else:
            print("L'article n'existe pas.")

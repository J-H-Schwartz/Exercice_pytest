
class Display:

    def __init__(self, controller):
        self.controller = controller

    def start(self, display):
        display.display_all_articles()
        while True:
            choice = input(
                "Que souhaitez vous faire ? (L)ister  /  (C)réer article  /  (M)ise à jour article  /  (S)upprimer / "
                "(Q)uitter :").upper()
            if choice == "L":
                display.display_all_articles()
            elif choice == "C":
                display.create_article()
            elif choice == "M":
                display.update_article()
            elif choice == "S":
                display.delete_article()
            elif choice == "Q":
                break
            else:
                print("Commande non reconnue, recommencez.")

    def display_all_articles(self):
        all_articles = self.controller.get_all_articles()
        for article in all_articles:
            print(article.title, article.text)

    def update_article(self):
        title = input("Entrez le titre de l'article que vous souhaitez modifier: ")
        text = input("Entrez le nouveau texte de l'article: ")
        self.controller.update_article(title, text)
        print("Article mis à jour avec succès.")

    def create_article(self):
        title = input("Entrez le titre du nouvel article: ")
        text = input("Entre le texte du nouvel article: ")
        self.controller.create_article(title, text)
        print("Article créé avec succès.")

    def delete_article(self):
        title = input("Entrez le titre de l'article à supprimer: ")
        self.controller.delete_article(title)
        print("Article supprimé avec succès.")

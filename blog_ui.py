
class Display:

    def __init__(self, controller):
        self.controller = controller

    def get_all_articles(self):
        all_articles = self.controller.get_all_articles()
        for article in all_articles:
            print(article.title, article.text)

    def update_article(self):
        title = input("Entrez le titre de l'artique que vous souhaitez modifier: ")
        text = input("Entrez le nouveau texte de l'article: ")
        self.controller.update_article(title, text)
        print("Article mis à jour avec succès.")

    def create_article(self):
        title = input("Entrez le titre du nouvel article: ")
        text = input("Entre le texte du nouvel article:")
        self.controller.create_article(title, text)
        print("Article créé avec succès.")

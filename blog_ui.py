from controller import Controller
from model_in_memory import Article
from model_in_memory import ModelInMemory



class Display:

    def __init__(self, controller):
        self.controller = controller

    def get_all_articles(self):
        all_articles = self.controller.get_all_articles()
        for article in all_articles:
            print(article.title, article.text)



display = Display(Controller(ModelInMemory([Article(title="title 1", text="text 1"), Article(title="title 2", text="text 2")])))
Display.get_all_articles(display)

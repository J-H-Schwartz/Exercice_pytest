from model_in_memory import Article
from model_in_memory import ModelInMemory
from model_in_memory import ModelInMemory1
from model_in_memory import ModelInMemory2

class Controller:

    def __init__(self, model):

        self.model = model
        self.articles = []

    def __str__(self):
        return "Controller ( model : {} )".format(self.model)

    def get_all_articles(self):
        return self.model.get_all_articles()

    def update_article(self, title, new_text):
        

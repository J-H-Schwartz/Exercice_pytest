from exceptions import *


class Controller:

    def __init__(self, model):

        self.model = model

    def __str__(self):
        return "Controller ( model : {} )".format(self.model)

    def get_all_articles(self):
        return self.model.get_all_articles()

    def update_article(self, title, new_text):
        try:
            self.model.update_article(title, new_text)
            update = True
        except NonExistantArticleException:
            update = False
        return update

    def create_article(self, title, text):
        try:
            self.model.create_article(title, text)
            creation = True
        except ArticleAlreadyExistException:
            creation = False
        return creation

    def delete_article(self, title):
        try:
            self.model.delete_article(title)
            deletion = True
        except NonExistantArticleException:
            deletion = False
        return deletion

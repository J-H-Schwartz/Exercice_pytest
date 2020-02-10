from peewee import *
from exceptions import *

mydb = SqliteDatabase("blog.db")


class Articles(Model):
    title = CharField()
    text = TextField()

    class Meta:
        database = mydb
        table_name = "articles"

    def get_title(self):
        return self.select(Articles.title)

    def get_text(self):
        return self.select(Articles.text)


class ModelInMemory:
    def __init__(self):
        self.articles = Articles

    def __str__(self):
        return "inmemory"

    def get_all_articles(self):
        articles = []
        for article in Articles.select():
            articles.append([article.title, article.text])
        return articles

    def update_article(self, title, new_text):
        for article in Articles.select():
            if title == article.title:
                self.articles.update(text=new_text).where(Articles.title == title).execute()
                return
        raise NonExistantArticleException("Article '{}' does not exist".format(title))

    def create_article(self, title, text):
        for article in Articles.select():
            if title == article.title:
                raise ArticleAlreadyExistException("Article '{}' already exists".format(article.get_title()))
        self.articles.insert(title=title, text=text).execute()

    def delete_article(self, title):
        for article in Articles.select():
            if title == article.title:
                self.articles.delete().where(title == Articles.title).execute()
                return
        raise NonExistantArticleException("Article '{}' does not exist".format(title))

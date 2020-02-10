
class ArticleAlreadyExistException(Exception):
    def __init__(self, message):
        self.message = message


class NonExistantArticleException(Exception):
    def __init__(self, message):
        self.message = message


class Article:
    def __init__(self, title, text):
        self.title = title
        self.text = text

    def get_title(self):
        return self.title

    def get_text(self):
        return self.text

    def update_article(self, title, new_text):
        if title in self.title:
            self.text = new_text


class ModelInMemory:
    def __init__(self, articles):
        self.articles = articles

    def __str__(self):
        return "inmemory"

    def get_all_articles(self):
        return self.articles

    def update_article(self, title, new_text):
        for article in self.articles:
            if title in article.get_title():
                article.update_article(title, new_text)
                return
        raise NonExistantArticleException("Article '{}' does not exist".format(title))

    def create_article(self, title, text):
        for article in self.articles:
            if title in article.get_title():
                raise ArticleAlreadyExistException("Article '{}' already exists".format(article.get_title()))
        self.articles.append(Article(title, text))


class ModelInMemory1:
    def __str__(self):
        return "inmemory1"


class ModelInMemory2:
    def __str__(self):
        return "inmemory2"
class Article:
    def __init__(self, title, text):
        self.title = title
        self.text = text

    def get_title(self):
        return self.title

    def get_text(self):
        return self.text

    def update_article_model(self, title, new_text):
        if self.title == title:
            self.text = new_text
        return self.text


class ModelInMemory:
    def __init__(self, articles):
        self.articles = articles

    def __str__(self):
        return "inmemory"

    def get_all_articles(self):
        return self.articles


class ModelInMemory1:
    def __str__(self):
        return "inmemory1"


class ModelInMemory2:
    def __str__(self):
        return "inmemory2"
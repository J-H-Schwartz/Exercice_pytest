from blog_ui import Display
from controller import Controller
from model_in_memory import Article
from model_in_memory import ModelInMemory


def main():
    display = Display(
        Controller(ModelInMemory([Article(title="title 1", text="text 1"), Article(title="title 2", text="text 2")])))
    display.start(display)


if __name__ == '__main__':
    main()

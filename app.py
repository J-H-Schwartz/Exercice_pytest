from blog_ui import Display
from controller import Controller
from model_in_memory import Article
from model_in_memory import ModelInMemory

model = Display(Controller(ModelInMemory([Article(title="title 1", text="text 1"), Article(title="title 2", text="text 2")])))


def main():
    Display.get_all_articles(model)
    while True:
        choice = input("Que souhaitez vous faire ? (L)ister  /  (C)réer article  /  (M)ise à jour article / (Q)uitter :"
                       " ").upper()
        if choice == "L":
            Display.get_all_articles(model)
        elif choice == "C":
            Display.create_article(model)
        elif choice == "M":
            Display.update_article(model)
        elif choice == "Q":
            break
        else:
            print("Commande non reconnue, recommencez.")


if __name__ == '__main__':
    main()

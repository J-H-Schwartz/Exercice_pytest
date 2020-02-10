from blog_ui import Display
from model_database import ModelInMemory
from controller import Controller

def main():
    display = Display(Controller(ModelInMemory()))
    display.start()


if __name__ == '__main__':
    main()

from blog_ui import Display
from model_database import ModelDatabase
from controller import Controller

def main():
    display = Display(Controller(ModelDatabase()))
    display.start()


if __name__ == '__main__':
    main()

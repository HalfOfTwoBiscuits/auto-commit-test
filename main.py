import pygame_menu
from gh_interface import Committer

class Project:

    @classmethod
    def __submit(cls):
        Committer.commit(cls.__text_widget.get_value())
    @classmethod
    def main(cls):
        menu = pygame_menu.Menu(width = 400, height = 300,
                                title='Commit a dummy file')
        cls.__text_widget = menu.add.text_input('Name: ')
        menu.add.button('Commit', cls.__submit)
        menu.add.button('Quit', pygame_menu.events.EXIT)

if __name__ == '__main__':
    main()
import pygame_menu
from pygame_menu.examples import create_example_window
from gh_interface import Committer
import asyncio

# Didn't work, I think because menu.mainloop() wasn't written async def
class Project:

    @classmethod
    def __submit(cls):
        Committer.commit(cls.__text_widget.get_value())
    @classmethod
    async def main(cls):
        TITLE = 'Commit a dummy file'
        surf = create_example_window(TITLE, (600, 400))
        menu = pygame_menu.Menu(width = 500, height = 300, title=TITLE,
                                theme=pygame_menu.themes.THEME_BLUE)
        cls.__text_widget = menu.add.text_input('Name: ')
        menu.add.button('Commit', cls.__submit)
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(surf)

if __name__ == '__main__':
    asyncio.run(Project.main())
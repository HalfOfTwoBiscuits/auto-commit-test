import pygame
import pygame_gui
import asyncio
from gh_interface import Committer

# Final attempt at an online version.
# Would work if pygbag supported PyGitHub, but it doesn't.
# The offline versions work - the test was partially successful
class Project:

    @classmethod
    async def main(cls):
        TITLE = 'Commit a dummy file'
        pygame.init()

        screen = pygame.display.set_mode((500, 200))
        pygame.display.set_caption(TITLE)
        clock = pygame.time.Clock()
        ui = pygame_gui.UIManager((500, 200))
        pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((50,50), (400, 100)),
            manager=ui, placeholder_text='Filename:')
        
        while True:
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    raise SystemExit
                if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                    Committer.commit(event.text)

                ui.process_events(event)

            time_delta = float(clock.tick(30) / 1000)
            screen.fill((225, 225, 225))
            ui.update(time_delta)
            ui.draw_ui(screen)
            pygame.display.update()
            await asyncio.sleep(0)

if __name__ == '__main__':
    asyncio.run(Project.main())
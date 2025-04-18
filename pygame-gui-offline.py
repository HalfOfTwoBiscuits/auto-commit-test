import pygame
import pygame_gui
from gh_interface import Committer

def main():
    TITLE = 'Commit a dummy file'
    pygame.init()

    screen = pygame.display.set_mode((500, 200))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    ui = pygame_gui.UIManager((500, 200))
    pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((50,50), (400, 100)),
        manager=ui, placeholder_text='Filename:')
    
    loop(screen, ui, clock)

def loop(screen,ui,clock):
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
        pygame.display.flip()

if __name__ == '__main__':
    main()
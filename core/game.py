import pygame as pyg


class Game:
    '''
    Main game class
    '''

    def __init__(self, window_size: tuple[int, int]) -> None:
        pyg.init()
        self.window = pyg.display.set_mode(window_size)
        self.clock = pyg.time.Clock()
        self.is_running = True
        self.should_quit = False

    def __del__(self):
        pyg.quit()

    def poll_events(self):
        events = pyg.event.get()
        for event in events:
            if event.type == pyg.QUIT:
                self.should_quit = True
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    self.should_quit = True
        return events

    def frame_begin(self):
        self.window.fill("black")

    def frame_end(self):
        pyg.display.flip()
        self.clock.tick(60)
        if self.should_quit:
            self.is_running = False

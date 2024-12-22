import pygame
from renderer import Renderer
from sorting import Sorter, SortingAlgorithms

class Application:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.running = True
        self.sorter = Sorter(50, SortingAlgorithms.GNOME)
        self.renderer = Renderer(pygame.display.set_mode((1280, 720)))

    def Run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.sorter.Sorted == False:
                    self.sorter.Step()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    self.sorter.ShuffleCollection()

            if self.sorter.Sorted == False:
                self.sorter.Step()

            self.renderer.DrawCollection(self.sorter.collection, self.sorter.GetCurrentIndex())

            self.clock.tick(60) 

        pygame.quit()
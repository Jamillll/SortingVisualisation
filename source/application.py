import pygame
from renderer import Renderer
from sorting import Sorter, SortingAlgorithms

class Application:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Sorting Visualiser")

        self.clock = pygame.time.Clock()
        self.running = True
        self.sorter = Sorter(100, SortingAlgorithms.BUBBLE)
        self.sorterPaused = True
        Renderer.init(pygame.display.set_mode((1280, 720)))

    def Run(self):
        while self.running:

            self.PollInputs()
            self.Update()
            self.Draw()

            self.clock.tick(60) 

        self.Exit()

    def PollInputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type != pygame.KEYDOWN:
                continue
            match event.key:
                case pygame.K_SPACE:
                    if self.sorter.Sorted == False:
                        self.sorter.Step()

                case pygame.K_s:
                    self.sorter.ShuffleCollection()
                case pygame.K_r:
                    self.sorterPaused = not self.sorterPaused
                
                case pygame.K_RIGHT:
                    self.sorter.SetSortingAlgorithm(self.sorter.sortingAlgorithm.value + 1)
                case pygame.K_LEFT:
                    self.sorter.SetSortingAlgorithm(self.sorter.sortingAlgorithm.value - 1)

                case pygame.K_UP:
                    self.sorter.SetCollectionSize(self.sorter.GetCollectionSize() + 10)
                case pygame.K_DOWN:
                    self.sorter.SetCollectionSize(self.sorter.GetCollectionSize() - 10)


    def Update(self):
        if self.sorterPaused == False and self.sorter.Sorted == False:
            self.sorter.Step()

    def Draw(self):
        Renderer.DrawCollection(self.sorter.collection, self.sorter.GetCurrentIndex())
        Renderer.DrawMenu()
        Renderer.DisplayText("Algorithm: " + str(self.sorter.sortingAlgorithm.name), (15, 10))
        Renderer.DisplayText("Collection Size: " + str(self.sorter.GetCollectionSize()), (15, 40))
        Renderer.DisplayText("Controls:", (15, 100))
        Renderer.DisplayText("Up- collection size + 10", (15, 140))
        Renderer.DisplayText("Down- collection size - 10", (15, 180))
        Renderer.DisplayText("Left/Right- change sorting", (15, 220))
        Renderer.DisplayText("Algorithm", (15, 245))
        Renderer.Render()

    def Exit(self):
        pygame.quit()
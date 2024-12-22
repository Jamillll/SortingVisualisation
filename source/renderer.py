import pygame

class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.indexColour = (255, 0, 0)

    def Draw(self):
        self.screen.fill("white")
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(0, 0, 60, 60))
        pygame.display.flip()

    def DrawCollection(self, collection, currentIndex):
        self.screen.fill((211,211,211))

        width = self.screen.get_width() - 200
        height = self.screen.get_height() - 20

        for i, item in enumerate(collection):
            rectLeft = (width / len(collection)) * (i + 1) + (1 * (i + 1))
            rectWidth = width / len(collection)
            rectHeight = height / (len(collection) / item)
            rectTop = height - rectHeight + 10

            colour = (0, 0, 0)
            if i == currentIndex:
                colour = (255, 0, 0)

            pygame.draw.rect(self.screen, colour, pygame.Rect(rectLeft, rectTop, rectWidth, rectHeight))
        pygame.display.flip()


import pygame

class Renderer:
    screen = None
    font = None
    indexColour = (255, 0, 0)

    def init (screen):
        Renderer.screen = screen
        Renderer.font = pygame.font.SysFont('Arial', 30)

    def Render():
        pygame.display.flip()

    def DisplayText(textToDisplay, location):
        textSurface = Renderer.font.render(textToDisplay, False, (0, 0, 0))
        Renderer.screen.blit(textSurface, location)

    def DrawMenu():
        menuBounds = pygame.Rect(10, 10, 300, 700)
        pygame.draw.rect(Renderer.screen, (211,211,211), menuBounds)

    def DrawCollection(collection, currentIndex):
        Renderer.screen.fill("white")
        collectionBounds = pygame.Rect(330, 10, 940, 700)

        pygame.draw.rect(Renderer.screen, (211,211,211), collectionBounds)
        for i, item in enumerate(collection):
            rectLeft = ((collectionBounds.width / len(collection)) * i) + collectionBounds.left
            rectWidth = collectionBounds.width / len(collection)
            rectHeight = collectionBounds.height / (len(collection) / item)
            rectTop = collectionBounds.height - rectHeight + collectionBounds.top

            colour = (0, 0, 0)
            if i == currentIndex:
                colour = (255, 0, 0)

            pygame.draw.rect(Renderer.screen, colour, pygame.Rect(rectLeft, rectTop, rectWidth, rectHeight))


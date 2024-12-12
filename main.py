import asyncio
import pygame, sys
import module
pygame.init()
screen = pygame.display.set_mode((512, 512))
pygame.display.set_caption('template')
clock = pygame.time.Clock()


class Class:

    def __init__(self):
        pass

    async def loop(self):
        while True:
            await asyncio.sleep(0)
            break


instance = Class()


async def loop():
    while True:
        await asyncio.sleep(0)
        break


async def main():
    color = 0
    while True:
        await asyncio.sleep(0)
        screen.fill((color, color, color))
        color = min(255, color + 1)
        await loop()
        await instance.loop()
        await module.loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    asyncio.run(main())

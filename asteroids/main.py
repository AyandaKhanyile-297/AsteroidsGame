import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    playerX = Player(x, y) 
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfieldZ = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers =  (shots, updatable, drawable)

    while True:
        log_state()
        #quits game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #checks collisions
        for asteroidX in asteroids:
          collison = playerX.collides_with(asteroidX)
          if collison:
            log_event("player_hit")
            print("Game over!")
            sys.exit()
          for shotX in shots:
              in_collision = asteroidX.collides_with(shotX)
              if in_collision:
                  log_event("asteroid_shot")
                  shotX.kill()
                  asteroidX.split()
        
        screen.fill("black")
        updatable.update(dt)
        for sprites in drawable:
          sprites.draw(screen)
        pygame.display.flip()
        
        dt = (clock.tick(60))/1000
    
if __name__ == "__main__":
    main()

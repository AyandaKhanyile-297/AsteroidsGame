import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid (CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    
  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
      self.kill()
      if self.radius <= ASTEROID_MIN_RADIUS:
          return
      else:
          log_event("asteroid_split")
          rand_ang = random.uniform(20, 50)
          first_asteroid = self.velocity.rotate(rand_ang)
          second_asteroid = self.velocity.rotate(-1 * rand_ang)
          new_radii = self.radius - ASTEROID_MIN_RADIUS
          asteroidX = Asteroid(self.position.x, self.position.y, new_radii)
          asteroidY = Asteroid(self.position.x, self.position.y, new_radii)
          asteroidX.velocity = first_asteroid * 1.2
          asteroidY.velocity = second_asteroid * 1.2

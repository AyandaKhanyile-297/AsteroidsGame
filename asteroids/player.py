import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH

class Player(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, PLAYER_RADIUS)
    self.rotation = 0
    
  # player is a circle but will be represented as a triangle
  def triangle(self):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]
    
  def draw(self, screen):
    pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
    
  def rotate(self, dt):
    self.__rotation += (PLAYER_TURN_SPEED * dt)

  def update(self, dt):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
      # rotate left
      move(-1*dt)
    if keys[pygame.K_d]:
      # rotate right
      move(dt)
    if keys[pygame.K_s]:
      # rotate backwards 
      rotate(-1*dt)
    if keys[pygame.K_w]:
      # rotate forwards
      rotate(dt)

	def move(self, dt):
    unit_vector = pygame.Vector2(0, 1)
		rotated_vector = unit_vector.rotate(self.rotation)
		rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
		self.position += rotated_with_speed_vector

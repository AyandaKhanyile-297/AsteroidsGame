import pygame
from shot import Shot
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_SPEED, PLAYER_TURN_SPEED, PLAYER_SHOOT_SPEED

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
    self.rotation += (PLAYER_TURN_SPEED * dt)

  def update(self, dt):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
      # rotate left
      self.move(-1*dt)
    if keys[pygame.K_d]:
      # rotate right
      self.move(dt)
    if keys[pygame.K_s]:
      # rotate backwards
      self.rotate(-1*dt)
    if keys[pygame.K_w]:
      # rotate forwards
      self.rotate(dt)
    if keys[pygame.K_SPACE]:
      # shoot 
      self.shoot()

  def move(self, dt):
      unit_vector = pygame.Vector2(0, 1)
      rotated_vector = unit_vector.rotate(self.rotation)
      rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
      self.position += rotated_with_speed_vector

  def shoot(self):
      shots = Shot(self.position.x, self.position.y)
      shot_unit_velocity = pygame.Vector2(0, 1)
      rotated_shot_dir = shot_unit_velocity.rotate(self.rotation)
      shot_dir_speed = rotated_shot_dir * PLAYER_SHOOT_SPEED
      shots.velocity += shot_dir_speed
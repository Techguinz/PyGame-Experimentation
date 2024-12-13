import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
screenWidth = screen.get_width()
screenHeight = screen.get_height()

screenCenter = pygame.Vector2(screenWidth / 2, screenHeight / 2)
playerSize = pygame.Vector2(20, 160)
accel = 10000

font = pygame.font.SysFont("Arial", 50)

def clampBallVelocity(velocity, minValue, maxValue):
    return max(min(velocity, maxValue), minValue)

def adjustBallVelocity(ballVelY, playerVel):
    velocityImpact = playerVel * 0.5
    ballVelY += velocityImpact

    return ballVelY

def simulatePlayer(position, velocity, acceleration, deltaTime):
        damping = 10
        acceleration -= velocity * damping
        position.y += velocity * deltaTime + acceleration * (deltaTime * deltaTime / 2)
        velocity += acceleration * deltaTime

        if position.y + playerSize.y > screenHeight:
            position.y = screenHeight - playerSize.y
            velocity = 0
        elif position.y < 0:
            position.y = 0
            velocity = 0

        return velocity 

def BallIsColliding(playerPosition, playerSize, ballRadius, ballPosition):
    collisionX = max(playerPosition.x, min(ballPosition.x, playerPosition.x + playerSize.x))
    collisionY = max(playerPosition.y, min(ballPosition.y, playerPosition.y + playerSize.y))

    distanceX = ballPosition.x - collisionX
    distanceY = ballPosition.y - collisionY

    return (distanceX ** 2 + distanceY ** 2) <= (ballRadius ** 2)

def displayWinscreen(winner):
    screen.fill("black")
    winText = font.render(f"Player {winner} Wins!", True, "white")
    instruction_text = font.render("Press R to Restart or Q to Quit", True, "white")
    screen.blit(winText, (screenWidth // 2 - winText.get_width() // 2, screenHeight // 2 - 100))
    screen.blit(instruction_text, (screenWidth // 2 - instruction_text.get_width() // 2, screenHeight // 2 + 50))
    pygame.display.update()

def displayMenu():
    screen.fill("black")
    titleText = font.render("Pong Game", True, "white")
    startText = font.render("Press SPACE to Start", True, "white")
    quitText = font.render("Press Q to Quit", True, "white")
    
    screen.blit(titleText, (screenWidth // 2 - titleText.get_width() // 2, screenHeight // 2 - 100))
    screen.blit(startText, (screenWidth // 2 - startText.get_width() // 2, screenHeight // 2))
    screen.blit(quitText, (screenWidth // 2 - quitText.get_width() // 2, screenHeight // 2 + 100))
    
    pygame.display.update()
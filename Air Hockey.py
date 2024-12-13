import pygame
from gameFunctions import *

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

ballPos = pygame.Vector2(screenWidth / 2, screenHeight / 2)
ballRadius = 10
ballVelX = 0
ballVelY = 0

player1Size = playerSize
player1Pos = pygame.Vector2(10, screenHeight / 2 - (playerSize.y / 2)) 
player1Vel = 0
player1Accel = 0

player2Size = playerSize
player2Pos = pygame.Vector2(screenWidth - playerSize.x - 10, screenHeight / 2 - (playerSize.y/2))
player2Vel = 0
player2Accel = 0

player1Score = 0
player2Score = 0
winner = None
gameStarted = False

font = pygame.font.SysFont("Arial", 50)

def resetGame():
    global ballPos, ballVelX, ballVelY, player1Pos, player2Pos, player1Score, player2Score, winner
    ballPos = pygame.Vector2(screenWidth / 2, screenHeight / 2)
    ballVelX = 0
    ballVelY = 0
    player1Pos = pygame.Vector2(10, screenHeight / 2 - (playerSize.y / 2)) 
    player2Pos = pygame.Vector2(screenWidth - playerSize.x - 10, screenHeight / 2 - (playerSize.y / 2))
    player1Score = 0
    player2Score = 0
    winner = None

def startGame():
    global ballVelX, ballVelY
    ballVelX = 400
    ballVelY = 400

while running:
    dt = clock.tick(144) * 0.001
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not gameStarted:
        displayMenu()
        pygame.display.update()
        if keys[pygame.K_SPACE]:
            gameStarted = True 
            resetGame()
            startGame()
        if keys[pygame.K_q]:
            running = False
        continue
    
    if winner is not None:
        displayWinscreen(winner)
        pygame.display.update()
        if keys[pygame.K_r]:
            resetGame()
            startGame()
        if keys[pygame.K_q]:
            running = False
        continue

    if gameStarted:
        ballPos.x += ballVelX * dt
        ballPos.y += ballVelY * dt

    if ballPos.y - ballRadius <= 0:
        ballPos.y = ballRadius
        ballVelY *= -1
    elif ballPos.y + ballRadius >= screenHeight:
        ballPos.y = screenHeight - ballRadius
        ballVelY *= -1

    if ballPos.x < 0:
        player2Score += 1
        ballPos = pygame.Vector2(screenWidth / 2, screenHeight / 2)
        ballVelX = -ballVelX
        ballVelY = 400

    if ballPos.x > screenWidth:
        player1Score += 1
        ballPos = pygame.Vector2(screenWidth / 2, screenHeight / 2)
        ballVelX = -ballVelX
        ballVelY = 400
    
    screen.fill("black")
    pygame.draw.circle(screen, "white", ballPos, ballRadius)
    pygame.draw.rect(screen, "white", pygame.Rect((player1Pos), (player1Size)))
    pygame.draw.rect(screen, "white", pygame.Rect((player2Pos), (player2Size)))

    pygame.draw.circle(screen, "white", screenCenter, 150, 1)
    pygame.draw.circle(screen, "black", screenCenter, 125, 1)
    pygame.draw.line(screen, "white", (screenWidth / 2, 0), (screenWidth / 2, screenHeight), 1)

    text = font.render(f"{player1Score} | {player2Score}", True, "white")
    screen.blit(text, (screenWidth // 2 - text.get_width() // 2, 20))

    player1Accel = 0
    if keys[pygame.K_w]:
        player1Accel -= accel
    if keys[pygame.K_s]:
        player1Accel += accel
    
    player2Accel = 0
    if keys[pygame.K_UP]:
        player2Accel -= accel
    if keys[pygame.K_DOWN]:
        player2Accel += accel
    
    player1Vel = simulatePlayer(player1Pos, player1Vel, player1Accel, dt)
    player2Vel = simulatePlayer(player2Pos, player2Vel, player2Accel, dt)

    if BallIsColliding(player1Pos, playerSize, ballRadius, ballPos):
        ballPos.x = player1Pos.x + playerSize.x + ballRadius
        ballVelX = -ballVelX
        ballVelY = adjustBallVelocity(ballVelY, player1Vel)
        ballVelY = clampBallVelocity(ballVelY, -900, 900)
        
        if keys[pygame.K_w]:
            ballVelY -= 100
        if keys[pygame.K_s]:
            ballVelY += 100

    if BallIsColliding(player2Pos, playerSize, ballRadius, ballPos):
        ballPos.x = player2Pos.x - ballRadius
        ballVelX = -ballVelX
        ballVelY = adjustBallVelocity(ballVelY, player2Vel)
        ballVelY = clampBallVelocity(ballVelY, -900, 900)

        if keys[pygame.K_UP]:
            ballVelY -= 100
        if keys[pygame.K_DOWN]:
            ballVelY += 100
    
    if player1Score == 3:
        winner = "1"
    if player2Score == 3:
        winner = "2"

    pygame.display.update()

pygame.quit()
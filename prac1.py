#Make a two-player Rock-Paper-Scissors game

print ("Let's play rock/paper/scissor!!!")

while True:
    player1 = str(input ("Enter your play (player1):\n"));
    player2 = str(input ("Enter your play (player2):\n"));
    r = "rock";
    s = "scissor";
    p = "paper";

    if (player1 == r and player2 == s):
        print("Player1 won");
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif (player1 == s and player2 == r):
        print("Player2 won");
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif (player1 == p and player2 == s):
        print("Player2 won");
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif (player1 == r and player2 == p):
        print("Player1 won");
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif (player1 == s and player2 == p):
        print("player1 won");
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif (player1 == p and player2 == p):
        print("Game draw");
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif (player1 == r and player2 == r):
        print ("Game draw");
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif (player1 == s and player2 == s):
        print ("Game draw");
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif (player1 == p and player2 == r):
        print ("Player2 won");
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break


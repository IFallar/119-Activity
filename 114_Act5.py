from random import Random

# SETTING THE BOARD: ASSIGNING SQUARES AS CHUTES OR LADDERS
CHUTES_LADDERS = {2: 28, 7: 19, 9: 31, 17: 4, 21: 42, 28: 84, 36: 44,
                  47: 26, 49: 11, 51: 67, 56: 53, 62: 19, 64: 60,
                  69: 81, 80: 100, 87: 24, 93: 73, 95: 75, 98: 78}

# SHOW ONLY GAME WINNERS


def simulate_game_winners_only(rseed=None, max_roll=6):

    rand = Random(rseed)
    p2position = 0
    p1position = 0
    turns = 0
    winner = 0

    while p1position < 100 and p2position < 100:
                
        turns += 1

        # PLAYER 1 ====================================================

        roll = rand.randint(1, max_roll)
        
        if p1position + roll > 100:
            continue
            
        p1position += roll
        
        p1position = CHUTES_LADDERS.get(p1position, p1position)
        
        # PLAYER 2 =====================================================

        if p1position < 100:
            roll = rand.randint(1, max_roll)
        
            if p2position + roll > 100:
                continue

            p2position += roll 

            p2position = CHUTES_LADDERS.get(p2position, p2position)

            if p2position == 100:
                winner = 2
                break    

        else:
            winner = 1
            break

    return turns, winner

# SHOW TURN BY TURN BREAKDOWN


def simulate_full_game(rseed=None, max_roll=6):

    rand = Random(rseed)
    p2position = 0
    p1position = 0
    winner = 0
    turns = 0
    while p1position < 100 and p2position < 100:
                
        turns += 1

        # PLAYER 1 =============================================================

        roll = rand.randint(1, max_roll)
        
        if p1position + roll > 100:
            continue
            
        p1position += roll
        p1landing = p1position

        print("Player 1 rolls " + str(roll) + " and lands at " + str(p1position))
        
        p1position = CHUTES_LADDERS.get(p1position, p1position)
        if p1landing < p1position:
            print("Player 1 is on a ladder tile and moves up to " + str(p1position))
        elif p1landing > p1position:
            print("Player 1 is on a chute tile and moves down to " + str(p1position))

        print("NEXT TURN =====================\n")
        
        # PLAYER 2 =============================================================

        if p1position < 100: 
            roll = rand.randint(1, max_roll)
        
            if p2position + roll > 100:
                continue
              
            p2position += roll  
            p2landing = p2position

            print("Player 2 rolls " + str(roll) + " and lands at " + str(p2position))

            p2position = CHUTES_LADDERS.get(p2position, p2position)
            if p2landing < p2position:
                print("Player 2 is on a ladder tile and moves up to " + str(p2position))
            elif p2landing > p2position:
                print("Player 2 is on a chute tile and moves down to " + str(p2position))
            
            print("NEXT TURN =====================\n")

            if p2position == 100:
                winner = 2
                break        

        else:
            winner = 1
            break

    print("\nGAME END ====================================================== WINNER is Player " + str(winner) + "\n")
    return turns, winner  

# VIEW SETTINGS ==============================


full_game = True  # Set to True if you want to see each game turn by turn.


see_game_winner = True  # Set this to True and 'full_game' to False if you only want to see the Winner for each game.


x = 0  # 100 - X = How many games you want to Simulate

# ============================================

p1wins = 0
p2wins = 0

while x < 100:

    if full_game is True:

        simulate_game_winners_only()

        if simulate_full_game()[1] == 1:
            p1wins += 1  
        else:
            p2wins += 1  

    else: 
        simulate_game_winners_only()
        if simulate_game_winners_only()[1] == 1:
            p1wins += 1  
            if see_game_winner is True:
                print("Player 1 wins at " + str(simulate_game_winners_only()[0]) + " turns")
        else:
            p2wins += 1  
            if see_game_winner is True:
                print("Player 2 wins at " + str(simulate_game_winners_only()[0]) + " turns")

    x += 1  

print("\nTotal Player 1 Wins: " + str(p1wins) + " - " + "Total Player 2 Wins: " + str(p2wins))

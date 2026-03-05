import random
import time
import json
import os

# ─────────────────────────────────────────
#   NUMBER GUESSING GAME
#   Guess the secret number between 1-100!
# ─────────────────────────────────────────

SCORES_FILE = "high_scores.json"


def load_high_scores():
    """Load high scores from file."""
    if os.path.exists(SCORES_FILE):
        try:
            with open(SCORES_FILE, "r") as f:
                return json.load(f)
        except:
            return {"easy": None, "medium": None, "hard": None}
    return {"easy": None, "medium": None, "hard": None}


def save_high_scores(scores):
    """Save high scores to file."""
    with open(SCORES_FILE, "w") as f:
        json.dump(scores, f, indent=2)


def play_game(difficulty):
    """One round of the game."""

    # Set max attempts based on difficulty
    max_attempts = {"easy": 10, "medium": 7, "hard": 5}[difficulty]

    # Computer picks a secret number
    secret = random.randint(1, 100)
    attempts = 0
    
    # Start the timer
    start_time = time.time()

    print(f"\n🎯 I've picked a number between 1 and 100.")
    print(f"   You have {max_attempts} attempts. Good luck!\n")

    while attempts < max_attempts:
        attempts_left = max_attempts - attempts

        # Show a hint when only 3 attempts left
        if attempts_left == 3:
            if secret % 2 == 0:
                print("💡 Hint: The number is EVEN")
            else:
                print("💡 Hint: The number is ODD")

        # Get the player's guess
        try:
            guess = int(input(f"   Attempt {attempts + 1}/{max_attempts} → Your guess: "))
        except ValueError:
            print("   ⚠️  Please enter a valid number!\n")
            continue

        # Check if out of range
        if guess < 1 or guess > 100:
            print("   ⚠️  Enter a number between 1 and 100!\n")
            continue

        attempts += 1
        difference = abs(secret - guess)

        # Check the guess
        if guess == secret:
            print(f"\n   🎉 CORRECT! The number was {secret}!")
            print(f"   ✅ You got it in {attempts} attempt(s)!\n")

            # Rate the performance
            if attempts == 1:
                print("   🏆 INCREDIBLE! First try!!")
            elif attempts <= 3:
                print("   ⭐ Amazing! Very few attempts!")
            elif attempts <= 5:
                print("   👍 Good job!")
            else:
                print("   😅 You made it, but try to do better!")
            
            # Calculate time and return
            elapsed_time = time.time() - start_time
            print(f"   ⏱️  Time: {elapsed_time:.1f} seconds\n")
            return (attempts, elapsed_time)

        elif guess < secret:
            # Give distance hints
            if difference > 30:
                print(f"   📈 Too LOW! (way too low)\n")
            elif difference > 10:
                print(f"   📈 Too LOW! (getting warmer...)\n")
            else:
                print(f"   📈 Too LOW! (very close!)\n")
        else:
            if difference > 30:
                print(f"   📉 Too HIGH! (way too high)\n")
            elif difference > 10:
                print(f"   📉 Too HIGH! (getting warmer...)\n")
            else:
                print(f"   📉 Too HIGH! (very close!)\n")

    # Out of attempts
    elapsed_time = time.time() - start_time
    print(f"\n   💀 GAME OVER! The secret number was {secret}.")
    print(f"   Better luck next time!")
    print(f"   ⏱️  Time: {elapsed_time:.1f} seconds\n")
    return (None, elapsed_time)


def play_game_two_player(difficulty):
    """Two player game mode - players take turns guessing."""
    
    # Set max attempts based on difficulty
    max_attempts = {"easy": 10, "medium": 7, "hard": 5}[difficulty]
    
    # Computer picks a secret number
    secret = random.randint(1, 100)
    
    # Track each player
    players = {
        "Player 1": {"attempts": 0, "guessed": False},
        "Player 2": {"attempts": 0, "guessed": False}
    }
    
    start_time = time.time()
    
    print(f"\n🎯 I've picked a number between 1 and 100.")
    print(f"   Each player has {max_attempts} attempts. Take turns!\n")
    
    current_player = "Player 1"
    
    while True:
        other_player = "Player 2" if current_player == "Player 1" else "Player 1"
        
        # Check if current player is out of attempts
        if players[current_player]["attempts"] >= max_attempts:
            if players[other_player]["attempts"] >= max_attempts:
                # Both out of attempts
                break
            else:
                # Switch to other player
                current_player = other_player
                continue
        
        attempts_left = max_attempts - players[current_player]["attempts"]
        
        # Show a hint when only 3 attempts left for a player
        if attempts_left == 3:
            if secret % 2 == 0:
                print(f"💡 Hint: The number is EVEN")
            else:
                print(f"💡 Hint: The number is ODD\n")
        
        # Get the player's guess
        try:
            guess = int(input(f"   {current_player} - Attempt {players[current_player]['attempts'] + 1}/{max_attempts} → Your guess: "))
        except ValueError:
            print("   ⚠️  Please enter a valid number!\n")
            continue
        
        # Check if out of range
        if guess < 1 or guess > 100:
            print("   ⚠️  Enter a number between 1 and 100!\n")
            continue
        
        players[current_player]["attempts"] += 1
        difference = abs(secret - guess)
        
        # Check the guess
        if guess == secret:
            elapsed_time = time.time() - start_time
            print(f"\n   🎉 {current_player} WINS!")
            print(f"   ✅ Guessed it in {players[current_player]['attempts']} attempt(s)!")
            print(f"   ⏱️  Total time: {elapsed_time:.1f} seconds\n")
            
            if players[other_player]["attempts"] > 0:
                print(f"   {other_player} made {players[other_player]['attempts']} attempt(s)\n")
            
            return (current_player, players[current_player]["attempts"], elapsed_time)
        
        elif guess < secret:
            if difference > 30:
                print(f"   📈 Too LOW! (way too low)\n")
            elif difference > 10:
                print(f"   📈 Too LOW! (getting warmer...)\n")
            else:
                print(f"   📈 Too LOW! (very close!)\n")
        else:
            if difference > 30:
                print(f"   📉 Too HIGH! (way too high)\n")
            elif difference > 10:
                print(f"   📉 Too HIGH! (getting warmer...)\n")
            else:
                print(f"   📉 Too HIGH! (very close!)\n")
        
        # Switch to other player
        current_player = other_player
    
    # Both players out of attempts
    elapsed_time = time.time() - start_time
    print(f"\n   💀 GAME OVER! The secret number was {secret}.")
    print(f"   Neither player guessed it!")
    print(f"   ⏱️  Total time: {elapsed_time:.1f} seconds\n")
    print(f"   Player 1: {players['Player 1']['attempts']} attempts")
    print(f"   Player 2: {players['Player 2']['attempts']} attempts\n")
    
    return (None, None, elapsed_time)


def show_scoreboard(scores, high_scores):
    """Show the session scores and all-time high scores."""
    
    print("\n   📊 YOUR SCORES THIS SESSION:")
    if scores:
        for i, s in enumerate(scores, 1):
            attempts, elapsed_time = s['result']
            print(f"      {i}. {s['difficulty'].upper()} → {attempts} attempts ({elapsed_time:.1f}s)")
        best = min([s for s in scores if s['result'][0] is not None], key=lambda x: x['result'][0])
        best_attempts, best_time = best['result']
        print(f"   🏅 Best: {best_attempts} attempt(s) on {best['difficulty'].upper()} ({best_time:.1f}s)\n")
    else:
        print("      No scores yet this session!\n")
    
    print("   🏆 ALL-TIME HIGH SCORES:")
    for difficulty in ["easy", "medium", "hard"]:
        score = high_scores[difficulty]
        if score:
            print(f"      {difficulty.upper()} → {score['attempts']} attempts ({score['time']:.1f}s)")
        else:
            print(f"      {difficulty.upper()} → No score yet")
    print()


def main():
    print("=" * 45)
    print("   🎮  NUMBER GUESSING GAME")
    print("=" * 45)

    scores = []  # store scores for this session
    high_scores = load_high_scores()  # load all-time high scores

    while True:
        # Choose difficulty
        print("\n   Choose game mode:")
        print("   1 → Easy   (10 attempts)")
        print("   2 → Medium  (7 attempts)")
        print("   3 → Hard    (5 attempts)")
        print("   4 → 2-Player Mode")
        print("   5 → Scores")
        print("   6 → Quit\n")

        choice = input("   Your choice (1/2/3/4/5/6): ").strip()

        if choice == "1":
            result = play_game("easy")
            if result[0] is not None:  # successful game
                scores.append({"difficulty": "easy", "result": result})
                # Update high score if better
                if high_scores["easy"] is None or result[0] < high_scores["easy"]["attempts"]:
                    high_scores["easy"] = {"attempts": result[0], "time": result[1]}
                    print("   🎉 NEW HIGH SCORE!\n")
                save_high_scores(high_scores)

        elif choice == "2":
            result = play_game("medium")
            if result[0] is not None:  # successful game
                scores.append({"difficulty": "medium", "result": result})
                # Update high score if better
                if high_scores["medium"] is None or result[0] < high_scores["medium"]["attempts"]:
                    high_scores["medium"] = {"attempts": result[0], "time": result[1]}
                    print("   🎉 NEW HIGH SCORE!\n")
                save_high_scores(high_scores)

        elif choice == "3":
            result = play_game("hard")
            if result[0] is not None:  # successful game
                scores.append({"difficulty": "hard", "result": result})
                # Update high score if better
                if high_scores["hard"] is None or result[0] < high_scores["hard"]["attempts"]:
                    high_scores["hard"] = {"attempts": result[0], "time": result[1]}
                    print("   🎉 NEW HIGH SCORE!\n")
                save_high_scores(high_scores)

        elif choice == "4":
            # 2-player mode
            print("\n   Choose difficulty for 2-Player Mode:")
            print("   1 → Easy   (10 attempts)")
            print("   2 → Medium  (7 attempts)")
            print("   3 → Hard    (5 attempts)\n")
            
            difficulty_choice = input("   Your choice (1/2/3): ").strip()
            difficulty_map = {"1": "easy", "2": "medium", "3": "hard"}
            
            if difficulty_choice in difficulty_map:
                result = play_game_two_player(difficulty_map[difficulty_choice])
                if result[0] is not None:  # successful game
                    scores.append({"difficulty": f"2P-{difficulty_map[difficulty_choice]}", "result": (result[1], result[2])})
            else:
                print("   ⚠️  Please enter 1, 2, or 3\n")

        elif choice == "5":
            show_scoreboard(scores, high_scores)

        elif choice == "6":
            show_scoreboard(scores, high_scores)
            print("   👋 Thanks for playing! Bye!\n")
            break

        else:
            print("   ⚠️  Please enter 1, 2, 3, 4, 5, or 6\n")



# Start the game
main()
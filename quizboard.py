 # Simple Quiz Score Board in Python

players = {}
num_players = int(input("Enter number of players: "))

# Add players
for i in range(num_players):
    name = input(f"Enter name of player {i+1}: ")
    players[name] = 0

# Quiz rounds
num_questions = int(input("Enter number of questions: "))

for q in range(1, num_questions + 1):
    print(f"\n--- Question {q} ---")
    
    for player in players:
        score = int(input(f"Enter score for {player}: "))
        players[player] += score

# Display final scoreboard
print("\n===== FINAL SCOREBOARD =====")

# Sort players by score (highest first)
sorted_players = sorted(players.items(), key=lambda x: x[1], reverse=True)

for rank, (player, score) in enumerate(sorted_players, start=1):
    print(f"{rank}. {player} - {score} points")

# Winner
winner = sorted_players[0]
print(f"\n🏆 Winner: {winner[0]} with {winner[1]} points!")

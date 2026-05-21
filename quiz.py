# Quiz Competition Program in Python

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Chennai", "B. Delhi", "C. Mumbai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    {
        "question": "Who invented Python?",
        "options": ["A. Dennis Ritchie", "B. James Gosling", "C. Guido van Rossum", "D. Elon Musk"],
        "answer": "C"
    }
]

# Dictionary to store player scores
scores = {}

# Number of participants
num_players = int(input("Enter number of participants: "))

# Get player names
players = []
for i in range(num_players):
    name = input(f"Enter name of participant {i+1}: ")
    players.append(name)
    scores[name] = 0

print("\n===== QUIZ COMPETITION STARTED =====")

# Ask questions to each player
for player in players:
    print(f"\n--- {player}'s Turn ---")
    
    for q in questions:
        print("\n" + q["question"])
        
        for option in q["options"]:
            print(option)
        
        answer = input("Enter your answer (A/B/C/D): ").upper()
        
        if answer == q["answer"]:
            print("✅ Correct Answer!")
            scores[player] += 1
        else:
            print(f"❌ Wrong Answer! Correct answer is {q['answer']}")

# Display scoreboard
print("\n===== FINAL SCOREBOARD =====")

sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

for rank, (player, score) in enumerate(sorted_scores, start=1):
    print(f"{rank}. {player} - {score} points")

# Winner announcement
winner = sorted_scores[0]

print(f"\n🏆 Winner of the Quiz Competition: {winner[0]}")
print(f"🎯 Final Score: {winner[1]} points")

print("\n===== THANK YOU FOR PARTICIPATING =====")

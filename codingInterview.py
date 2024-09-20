tasks = ["very easy", "very easy", "easy", "easy", "medium", "medium", "hard", "hard"]
interview1 = [5, 5, 10, 10, 15, 15, 20, 20]
interviwe1_time = 120
max_time = 120
max_very_easy = 5
max_easy = 10
max_medium = 15
max_hard = 20

def qualification(score, time):
    if time > max_time:
        return "Disquialified"
    for i in
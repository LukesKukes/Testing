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
    for i in score:
        if interview1.index(i) < 2:
            if i > max_very_easy:
                return "Disqualified"
        if interview1.index(i) < 4 and interview1.index(i) > 2:
            if i > max_easy:
                return "Disqualified"
        if interview1.index(i) < 6 and interview1.index(i) > 3:
            if i > max_medium:
                return "Disqualified"
        if interview1.index(i) < 9 and interview1.index(i) > 6:
            if i > max_hard:
                return "Disqualified"
    return "Qualified :)))"
print(qualification(interview1, interviwe1_time))
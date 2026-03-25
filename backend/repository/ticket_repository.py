def save_ticket(text, result):
    with open("backend/logs/system.log", "a") as f:
        f.write(f"{text} -> {result}\n")
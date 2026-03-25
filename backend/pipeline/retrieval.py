import json

def retrieve_similar(query):
    query = query.lower()

    try:
        with open("backend/data/tickets.json") as f:
            tickets = json.load(f)

        for t in tickets:
            issue = t["issue"].lower()

            # Check if key words match
            if "vpn" in query and "vpn" in issue:
                return t
            if "password" in query and "password" in issue:
                return t
            if "error" in query and "error" in issue:
                return t

    except Exception as e:
        print("Error:", e)

    return None
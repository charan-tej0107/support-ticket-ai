# backend/models/ticket_model.py

class Ticket:
    def __init__(self, text, category, priority, response):
        self.text = text
        self.category = category
        self.priority = priority
        self.response = response

    def to_dict(self):
        return {
            "text": self.text,
            "category": self.category,
            "priority": self.priority,
            "response": self.response
        }
def route_ticket(category):
    routes = {
        "Billing": "Finance Team",
        "Account": "Auth Team",
        "Technical": "Engineering Team",
        "Delivery": "Logistics Team",
        "Security": "Security Team"
    }
    return routes.get(category, "Support Team")
from flask import Flask, jsonify
import database

app = Flask(__name__)

database.initialize_database()

detail_data = {
    "expenses": {
        "title": "Expenses",
        "description": "Track your spending and monthly budget.",
        "items": ["Groceries - $84", "Gas - $42", "Internet - $65"]
    },
    "income": {
        "title": "Income",
        "description": "Monitor salary, dividends, and other income.",
        "items": ["Paycheck - $4000", "Side work - $600"]
    },
    "reports": {
        "title": "Reports",
        "description": "View spending trends and financial summaries.",
        "items": []
    }
}
# UI API
@app.get("/api/details/<box_id>")
def get_details(box_id):
    return jsonify(detail_data.get(box_id, {
        "title": "Not Found",
        "description": "No data available",
        "items": []
    }))

# DB API
@app.get("/api/expenses")
def api_get_expenses():
    expenses = database.get_all_expenses()
    return jsonify(expenses)

@app.post("/api/expenses")
def api_new_expense():
    None
# For example, imagine the request arrives. What should happen, step by step?

# Something like:

# Receive the HTTP request.
# Read the JSON body.
# Validate the required fields.
# Call add_expense(...).
# Return a success response.


if __name__ == "__main__":
    app.run(debug=True)
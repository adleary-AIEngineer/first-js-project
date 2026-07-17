from flask import Flask, request, jsonify
from flask_cors import CORS
import database
import sqlite3

app = Flask(__name__)
CORS(app)

database.initialize_database()

# detail_data = {
#     "expenses": {
#         "title": "Expenses",
#         "description": "Track your spending and monthly budget.",
#         "items": ["Groceries - $84", "Gas - $42", "Internet - $65"]
#     },
#     "income": {
#         "title": "Income",
#         "description": "Monitor salary, dividends, and other income.",
#         "items": ["Paycheck - $4000", "Side work - $600"]
#     },
#     "reports": {
#         "title": "Reports",
#         "description": "View spending trends and financial summaries.",
#         "items": []
#     }
# }
# # UI API
# @app.get("/api/details/<box_id>")
# def get_details(box_id):
#     return jsonify(detail_data.get(box_id, {
#         "title": "Not Found",
#         "description": "No data available",
#         "items": []
#     }))

# DB API
@app.get("/api/expenses")
def api_get_expenses():
    expenses = database.get_all_expenses()
    return jsonify(expenses)

@app.route("/api/expenses", methods=['POST'])
def api_new_expense():
    expense = request.get_json()
    date=expense.get("date")
    description=expense.get("description")
    amount=float(expense.get("amount"))
    payment_method=expense.get("payment_method")
    category=expense.get("category")
    notes=expense.get("notes")
    tags=expense.get("tags")

    if not date or not description or not amount or not payment_method:
        return jsonify({"error": "Missing fields"}), 400

    try:
        database.add_expense(date, description, amount, 
                         payment_method, category, 
                         notes, tags)
        return jsonify({"message": "Expense added"}), 201
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    app.run(debug=True)
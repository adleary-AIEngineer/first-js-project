from flask import Flask, jsonify

app = Flask(__name__)

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

@app.get("/api/details/<box_id>")
def get_details(box_id):
    return jsonify(detail_data.get(box_id, {
        "title": "Not Found",
        "description": "No data available",
        "items": []
    }))

if __name__ == "__main__":
    app.run(debug=True)
    
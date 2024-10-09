from flask import Flask, render_template, request, jsonify
import random
from datetime import datetime

app = Flask(__name__)

# Route for Home Page
@app.route('/') 
def home():
    return render_template('index.html')

# Route for Menu (Billing Page)
@app.route('/bill', methods=['POST'])
def bill():
    # Get the quantities from the form
    dosa_qty = int(request.form.get('Dosa', 0))
    pongal_qty = int(request.form.get('Pongal', 0))
    vada_qty = int(request.form.get('Vada', 0))
    puri_qty = int(request.form.get('Puri', 0))
    idli_qty = int(request.form.get('Idli', 0))
    tea_qty = int(request.form.get('Tea', 0))
    coffee_qty = int(request.form.get('Coffee', 0))

    # Calculate costs
    total_cost = (dosa_qty * 45) + (pongal_qty * 55) + (vada_qty * 20) + (puri_qty * 50) + (idli_qty * 30) + (tea_qty * 15) + (coffee_qty * 20)
    service_charge = total_cost * 0.10  # 10% service charge
    tax = total_cost * 0.18  # 18% tax
    total_amount = total_cost + service_charge + tax

    bill_no = random.randint(1, 500)
    bill_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Return the bill information as JSON
    return jsonify({
        'bill_no': bill_no,
        'date': bill_date,
        'total_cost': total_cost,
        'service_charge': service_charge,
        'tax': tax,
        'total_amount': total_amount
    })

if __name__ == '__main__':
    app.run(debug=True)
 
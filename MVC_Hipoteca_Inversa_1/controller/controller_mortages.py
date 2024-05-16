from datetime import datetime
from flask import render_template, request
from logic.Calculations import MortgageLifetimeInverse
from app import app


@app.route('/')
@app.route('/hi_lifetime_cal', methods=['GET', 'POST'])
def hi_lifetime_cal():
    if request.method == 'POST':
        
        total_amount = float(request.form['total_amount'])
        interest = float(request.form['interest'])
        interest_housing = float(request.form['interest_housing'])
        age = "Desde la base de datos"
        gender = "Desde la base de datos"

        monthly_payment = MortgageLifetimeInverse(total_amount, interest, interest_housing, age, gender)

        # Renderizar la plantilla con el resultado del cálculo
        return render_template('login_user.html', monthly_payment=monthly_payment)
    
    return render_template('lifetime.html', title='HI VITALICA', message='Por favor, ingrese los datos solicitados.', year=datetime.now().year)

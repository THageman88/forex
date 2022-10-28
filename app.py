from flask import Flask, render_template,request, session , redirect, flash
from forex_python.converter import CurrencyRates, CurrencyCodes, RatesNotAvailableError
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SeceretsMakeFriends'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app) 


c_r = CurrencyRates()


@app.route('/')
def home_page():
    """This displays the home page for our converter"""

    return render_template('index.html')


@app.route('/conversion', methods=['POST'])
def perform_conversion():
    """Grabs Form Data and Redirects to Display Page"""
    try:
        #Grabs the currencies from the currency from and currency to inputs as well as the amount
        currency_from = request.form['currency_from'].upper()
        currency_to = request.form['currency_to'].upper()

        amount = float(request.form['amount'])
        
        #perform calculation and assign current amount to the calculated amount
        amount = c_r.convert(currency_from, currency_to, amount)
        # add the amount to the session
        session['amount'] = amount
        
        return redirect('/display')
        
    except RatesNotAvailableError:
        flash('Be sure currency abbreviation are 3 letters and the amount is a number')
        return redirect('/')

    
    


@app.route('/display')
def display_conversion():
    """Displays the Converted Amount and Button to go Back to Homepage"""
    # get the amount out of the session 
    amount_result = session.get('amount')

    return render_template('display.html', amount_result=amount_result )

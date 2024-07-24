# from flask import Flask, render_template, request, jsonify
# import requests
#
# app = Flask(__name__)
#
# # API endpoint and key
# API_URL = "https://financialmodelingprep.com/api/v3/search"
# API_KEY = "mqmzPFtqOryDzvu8r1raeg7avQFfTa3R"
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/search', methods=['POST'])
# def search():
#     query = request.form['query']
#     response = requests.get(f"{API_URL}?query={query}&apikey={API_KEY}")
#     data = response.json()
#     return jsonify(data)
#
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# API endpoint and key
API_URL = "https://financialmodelingprep.com/api/v3/search"
API_KEY = "mqmzPFtqOryDzvu8r1raeg7avQFfTa3R"
DETAILS_URL = "https://financialmodelingprep.com/api/v3/profile"  # Endpoint for detailed stock data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    response = requests.get(f"{API_URL}?query={query}&apikey={API_KEY}")
    data = response.json()
    return jsonify(data)

@app.route('/predict', methods=['POST'])
def predict():
    symbol = request.form['symbol']
    # Fetch detailed data
    response = requests.get(f"{DETAILS_URL}/{symbol}?apikey={API_KEY}")
    data = response.json()

    # Simple prediction logic (placeholder)
    # Here you can add more sophisticated prediction logic
    if data:
        stock = data[0]
        prediction = {
            'symbol': stock['symbol'],
            'companyName': stock['companyName'],
            'price': stock['price'],
            'prediction': "Likely to rise"  # Placeholder prediction
        }
        return jsonify(prediction)
    return jsonify({'error': 'Stock not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

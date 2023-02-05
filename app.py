from flask import Flask,request,jsonify
import requests

app = Flask(__name__ )

@app.route('/', methods=['POST'])
def welcome():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']
    # print(str(source_currency) + " " + str(amount) + " " + str(target_currency))

    cf = fetch_conversion_factor(target_currency , source_currency , amount)

    response = {
        'fulfillmentText':"{} {} is {} {}".format(amount , source_currency , cf , target_currency)
    }

    print(response)
    return jsonify(response)
 
def fetch_conversion_factor( target , source,  amount):
    

    url = "https://api.apilayer.com/fixer/convert?to={}&from={}&amount={}".format(target , source , amount)

    payload = {}
    headers= {
    "apikey": "8FmSysZF63nvXKgSkGt4iai3gOIYfFLR"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    # status_code = response.status_code
    response = response.json()
    # print(response['result'])
    return response['result']

if __name__ == "__main__":
    app.run(debug=True)
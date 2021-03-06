#! /usr/bin/env python3.6

"""
server.py
Stripe Recipe.
Python 3.6 or newer required.
"""

import logging
import stripe
import json
import os

from flask import Flask, render_template, jsonify, request, send_from_directory
from dotenv import load_dotenv, find_dotenv

app = Flask(__name__, static_url_path="")

# Setup Stripe python client library
load_dotenv(find_dotenv())
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
stripe.api_version = os.getenv('STRIPE_API_VERSION')

def product_details():
  return {
    'currency': 'USD',
    'amount': 3000
  }

@app.route('/', methods=['GET'])
def home():
    return "Hello from the API!"

@app.route('/public-key', methods=['GET'])
def PUBLISHABLE_KEY():
    return jsonify({
        'publicKey': os.getenv('STRIPE_PUBLISHABLE_KEY')
    })

@app.route('/product-details', methods=['GET'])
def get_product_details():
    product = product_details()
    return jsonify(product)

@app.route('/create-payment-intent', methods=['POST'])
def post_payment_intent():
    # Reads application/json and returns a response
    data = json.loads(request.data or '{}')
    product = product_details()

    options = dict()
    options.update(data)
    options.update(product)
    
    # Create a PaymentIntent with the order amount and currency
    payment_intent = stripe.PaymentIntent.create(**options,
     # Add Metadata
    metadata={'integration_check':'accept_a_payment'})

    try:
        return jsonify(payment_intent)
    except Exception as e:
        return jsonify(error=str(e)), 403

@app.route('/webhook', methods=['POST'])
def webhook_received():
    webhook_secret = os.getenv('STRIPE_WEBHOOK_SECRET')
    request_data = json.loads(request.data)

    if webhook_secret:
        # Retrieve the event by verifying the signature using the raw body and secret if webhook signing is configured.
        signature = request.headers.get('stripe-signature')
        try:
            event = stripe.Webhook.construct_event(
                payload=request.data, sig_header=signature, secret=webhook_secret)
            data = event['data']
        except Exception as e:
            return e
        # Get the type of webhook event sent - used to check the status of PaymentIntents.
        event_type = event['type']
    else:
        data = request_data['data']
        event_type = request_data['type']
    data_object = data['object']
    
    print('event ' + event_type)

    if event_type == 'payment_intent.succeeded':
        # Handle the payment intent succeeded event and fulfill the order
        logging.info("💰 Payment received! Fulfill the order.")

    if event_type == 'payment_intent.payment_failed':
        #Notify the customer that their order was not fulfilled
        logging.info("❌ Payment failed.")

    return jsonify({'status': 'success'})

    #Logging

if __name__== '__main__':
    logging.basicConfig(filename='fulfillment.log', level=logging.INFO, filemode='w')
    logging.getLogger('stripe').setLevel(logging.CRITICAL)
    logging.getLogger('werkzeug').setLevel(logging.CRITICAL)
    logging.info("starting server...")
    app.run(host='0.0.0.0', port=4242)

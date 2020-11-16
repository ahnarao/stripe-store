# Features

This site is built using React and uses the [Payment Intents API](https://stripe.com/docs/payments/payment-intents) to collect credit card information. The fullfillment.log file captures all attempts as well as orders to fulfill.

# How to run locally

Clone and configure this project.

To run this locally you need to start both a local dev server for the client and a back end server. Instructions are below.

Additionally you will need a Stripe account in order to run the demo. Once you set up your account, go to the Stripe [developer dashboard](https://stripe.com/docs/development/quickstart#api-keys) to find your API keys. You will need to add those API keys to the .env file. Don't worry about adding the webhook yet, that value will be returned when you set up listening.

```
STRIPE_PUBLISHABLE_KEY=<replace-with-your-publishable-key>
STRIPE_SECRET_KEY=<replace-with-your-secret-key>
```

### Running the API server

1. Create and activate a new virtual environment:`python3 -m venv /path/to/new/virtual/environment`
2. Activate a new virtual environment: `source /path/to/new/virtual/environment/venv/bin/activate`
2. Go to `server/`
3. Run `pip install -r requirements.txt` to install dependencies
4. Run `python3 server.py`

### Running the React client

1. Go to `client/`
1. Run `yarn`
1. Run `yarn start` and your default browser should now open with the front-end being served from `http://localhost:3000/`.

## How to run Stripe CLI for integration testing & webhook testing

Follow the [installation steps](https://github.com/stripe/stripe-cli#installation) to install the Stripe CLI. The CLI is what you will need to locally test the webhooks and Stripe integration.

1. Run `Stripe Status` to check that the Stripe CLI is set up properly
2. Run `Stripe login` (you will be prompted to connect your account)
3. Run `stripe listen --forward-to localhost:4242/webhook` and a webhook url will be returned
4. Add the webhook url to the .env file

### Buying crystals

When running both servers, you are now ready to use the app running in [http://localhost:3000](http://localhost:3000).

1. Enter your name and card details (test cards are here: https://stripe.com/docs/payments/accept-a-payment?integration=elements#web-test-integration )
1. Hit "Pay"
1. 🎉

### Run integration tests
1. Navigate to this page: https://stripe.com/docs/payments/accept-a-payment?integration=elements#web-test-integration
2. Ensure you are logged in to your Stripe account
3. Note the 3 test credit cards, follow the steps above to enter your name and each of the card details and click submit
4. Click "check payments" on the stripe test page

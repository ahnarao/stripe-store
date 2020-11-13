import React from "react";
import { loadStripe } from "@stripe/stripe-js";
import { Elements } from "@stripe/react-stripe-js";
import DemoText from "./components/DemoText";
import CheckoutForm from "./components/CheckoutForm";

import api from "./api";

import "./App.css";

const stripePromise = api.getPublicStripeKey().then(key => loadStripe(key));

export default function App() {
  return (
    <div className="App">
      <div className="sr-root">
        <div className="sr-main">
          <header className="sr-header">
            <div className="sr-header__logo" />
          </header>
          <Elements stripe={stripePromise}>
            <CheckoutForm />
          </Elements>
        </div>

        <div className="sr-content">
          <div className="crystal-image-stack">
            <img
              alt=""
              src="https://lh3.googleusercontent.com/1mQmuBdwob9Wns4K9QVirxhRklvEDpDVKsADlO1mDbitEFf99ShKMwKtySqx0CESs36Nm7bVE9g73YEfUS903UK_J2pWmPvNgIm-Y0EzIP0lUGbhsoAV4RsskdEaIG-97ygLb3piHw=w2400"
              width="160"
              height="180"
            />
            <img
              alt=""
              src="https://lh3.googleusercontent.com/jvw66Tm2xnBIWizAuX5iEREqFErFZD8TmcFuXKmSiv3EH7KtDkqYj2xSqtnBT8x19WhS1rwbnUgnNvT5NCD6_mLfyXke2EIkQYIxt-ohZBeMoUn1hzaYRYSxdsNp8mp2AkrBX6JI9A=w2400"
              width="160"
              height="180"
            />
            <img
              alt=""
              src="https://lh3.googleusercontent.com/TO5oDcvvX5_qTTKDULHa2NmA7Qn7qGS34y8H41L1QWQ6flXgqdQHYGO0EIi2yU0LUridASpO5qIozVJGZl8KGT-JgbhwsVu7ISiaQYVGroGlKiR7_OQz8DbY2VP7yjsElFjUqtQ9tA=w2400"
              width="160"
              height="180"
            />
          </div>
        </div>
      </div>
      <DemoText />
    </div>
  );
}

import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_price(amount):
    "Создание цены в страйпе."

    return stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        product_data={"name: Course price"},
    )


def create_stripe_session(price):
    "Создание сессии на оплату в страйпе."

    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="Payment",
    )
    return session.get("id"), session.get("url")

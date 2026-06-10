from flask import Flask, render_template
import os

app = Flask(__name__)


# HOME PAGE
@app.route('/')
def home():
    return render_template('index.html')


# ABOUT PAGE
@app.route('/about')
def about():
    return render_template('about.html')


# SERVICES PAGE
@app.route('/services')
def services():
    return render_template('services.html')


# CONTACT PAGE
@app.route('/contact')
def contact():
    return render_template('contact.html')


# FAQ PAGE
@app.route('/faq')
def faq():
    return render_template('faq.html')


# PRODUCT PAGE
@app.route("/product/<dress_id>")
def product(dress_id):

    # Product details
    products = {

        "dress1": {
            "name": "LT-341",
            "fabric": "Interlock,Net",
            "size": "S,M,L,XL"
        },

        "dress2": {
            "name": "LT-343",
            "fabric": "corduroy(woven fabric)",
            "size": "S,M,L,XL"
        },

        "dress3": {
            "name": "LT-342",
            "fabric": "interlock",
            "size": "S,M,L,XL"
        },

        "dress4": {
            "name": "LT-344",
            "fabric": "interlock/waffle(print)",
            "size": "S,M,L,XL"
        },

        "dress5": {
            "name": "LT-332",
            "fabric": "corduroy/denim/waffle",
            "size": "S,M,L,XL"
        },

        "dress6": {
            "name": "LT-331",
            "fabric": "Pure Cotton",
            "size": "S,M,L,XL"
        },

        "dress7": {
            "name": "LT-333",
            "fabric": "interlock/double fabric",
            "size": "S,M,L,XL"
        },

        "dress8": {
            "name": "LT-202",
            "fabric": "knitted fabric",
            "size": "S,M,L"
        }
    }


    # Get product data
    product_data = products.get(dress_id)

    if not product_data:
        return "Product not found"


    # Automatically find images
    images = []
    i = 1

    while True:

        image_name = f"{dress_id}-{i}.png"

        image_path = os.path.join(
            "static/images",
            image_name
        )

        if os.path.exists(image_path):
            images.append(image_name)
            i += 1
        else:
            break


    return render_template(
        "product.html",
        dress_id=product_data["name"],
        fabric=product_data["fabric"],
        size=product_data["size"],
        images=images
    )


if __name__ == "__main__":
    app.run(debug=True)
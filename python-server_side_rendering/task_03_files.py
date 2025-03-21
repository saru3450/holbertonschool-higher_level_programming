import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def read_csv(file_path):
    products = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    # Load data based on source
    if source == "json":
        try:
            products = read_json('products.json')
        except FileNotFoundError:
            return render_template('product_display.html', error="JSON file not found.")
    elif source == "csv":
        try:
            products = read_csv('products.csv')
        except FileNotFoundError:
            return render_template('product_display.html', error="CSV file not found.")
    else:
        return render_template('product_display.html', error="Wrong source. Please use 'json' or 'csv'.")

    # Filter by ID if provided
    if product_id:
        products = [product for product in products if product['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found.")

    # Pass data to the template
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)


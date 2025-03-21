import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# Functions to read data from different sources
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

def read_sqlite():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        conn.close()
        return [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in rows]
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return None

# Flask route
@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

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
    elif source == "sql":
        products = read_sqlite()
        if products is None:
            return render_template('product_display.html', error="Database error.")
    else:
        return render_template('product_display.html', error="Wrong source. Please use 'json', 'csv', or 'sql'.")

    # Filter by ID if provided
    if product_id:
        products = [product for product in products if product['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found.")

    # Pass data to the template
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

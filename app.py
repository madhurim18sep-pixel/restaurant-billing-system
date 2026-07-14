from flask import Flask, render_template, request, jsonify
from datetime import datetime, date
import random
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'receipts'

# Create receipts folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Menu items with prices
MENU = {
    "Chickenbiryani": 210,
    "Kadaipaneer": 120,
    "Butterchicken": 250,
    "Rumaliroti": 40,
    "Naan": 60,
    "Momos": 100,
    "Frenchfries": 90,
    "Noodles": 150,
    "Vegburger": 60,
    "Burrito": 100
}

DISCOUNT_PERCENTAGE = 10
GST_PERCENTAGE = 18

# Dish display names and images
DISH_INFO = {
    "Chickenbiryani": {"name": "Chicken Biryani", "image": "chickenbiryani.jpg"},
    "Kadaipaneer": {"name": "Kadai Paneer", "image": "kadaipaneer.jpg"},
    "Butterchicken": {"name": "Butter Chicken", "image": "butterchicken.jpg"},
    "Rumaliroti": {"name": "Rumali Roti", "image": "rumaliroti.jpg"},
    "Naan": {"name": "Naan", "image": "naan.jpg"},
    "Momos": {"name": "Momos", "image": "momos.jpg"},
    "Frenchfries": {"name": "French Fries", "image": "frenchfries.jpg"},
    "Noodles": {"name": "Noodles", "image": "noodles.jpg"},
    "Vegburger": {"name": "Veg Burger", "image": "vegburger.jpg"},
    "Burrito": {"name": "Burrito", "image": "burrito.jpg"}
}

def generate_order_id():
    """Generate a unique order ID"""
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    random_letters = ''.join(random.choice(letters) for _ in range(3))
    random_digits = ''.join(random.choice(digits) for _ in range(3))
    return f"MYS_{random_letters}{random_digits}"

@app.route('/')
def index():
    """Home page - main ordering interface"""
    return render_template('index.html', menu=MENU, dish_info=DISH_INFO)

@app.route('/api/menu')
def get_menu():
    """API endpoint to get menu items"""
    return jsonify(MENU)

@app.route('/api/calculate', methods=['POST'])
def calculate_total():
    """API endpoint to calculate totals with discount and GST"""
    data = request.json
    subtotal = float(data.get('subtotal', 0))
    
    discount = (DISCOUNT_PERCENTAGE / 100) * subtotal
    discounted_total = subtotal - discount
    gst = (GST_PERCENTAGE / 100) * discounted_total
    final_total = discounted_total + gst
    
    return jsonify({
        'subtotal': round(subtotal, 2),
        'discount': round(discount, 2),
        'discounted_total': round(discounted_total, 2),
        'gst': round(gst, 2),
        'final_total': round(final_total, 2)
    })

@app.route('/api/generate-receipt', methods=['POST'])
def generate_receipt():
    """Generate and save receipt as text file"""
    data = request.json
    order_id = data.get('order_id')
    items = data.get('items', [])
    subtotal = float(data.get('subtotal', 0))
    discount = float(data.get('discount', 0))
    gst = float(data.get('gst', 0))
    final_total = float(data.get('final_total', 0))
    
    order_day = date.today()
    order_time = datetime.now()
    
    receipt_content = f"""The Mystic

{order_day.strftime("%x")}
{order_time.strftime("%X")}

-----------------------------------------------------------
ITEMS       PRICES

"""
    
    for item in items:
        receipt_content += f"{item}\n"
    
    receipt_content += f"""-----------------------------------------------------------

Subtotal: ${subtotal: .2f}
Discount ({DISCOUNT_PERCENTAGE}%): -${discount: .2f}
GST ({GST_PERCENTAGE}%): +${gst: .2f}
Final Total: ${final_total: .2f}

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                      THANK YOU                                    
                     Visit Again !                                    
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""
    
    # Save receipt
    receipt_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{order_id}.txt")
    with open(receipt_path, 'w') as f:
        f.write(receipt_content)
    
    return jsonify({
        'success': True,
        'message': 'Receipt generated successfully',
        'order_id': order_id,
        'receipt_content': receipt_content
    })

if __name__ == '__main__':
    app.run(debug=True)
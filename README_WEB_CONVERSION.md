# Mystic Restaurant - Web Billing System

This is a web-based version of the Mystic Restaurant desktop billing system, converted from a Tkinter GUI to a Flask web application.

## Conversion Overview

### Original (Desktop)
- **Framework**: Tkinter (Python GUI)
- **Features**: Desktop application with local image handling
- **Limitations**: Single-user, local file storage only

### New (Web)
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Advantages**: Multi-user accessible, remote access, database-ready

## Installation & Setup

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation Steps

1. **Install required packages:**
```bash
pip install -r requirements.txt
```

2. **Project Structure:**
```
restaurant-billing-system/
├── app.py                  # Flask backend
├── templates/
│   └── index.html          # HTML template
├── static/
│   ├── style.css           # Styling
│   ├── script.js           # Frontend logic
│   └── images/             # Dish and banner images
│       ├── logo.jpg
│       ├── topbanner.jpg
│       ├── displaydefault.jpg
│       ├── chickenbiryani.jpg
│       ├── kadaipaneer.jpg
│       ├── butterchicken.jpg
│       ├── rumaliroti.jpg
│       ├── naan.jpg
│       ├── momos.jpg
│       ├── frenchfries.jpg
│       ├── noodles.jpg
│       ├── vegburger.jpg
│       └── burrito.jpg
└── receipts/               # Generated receipts folder
```

3. **Place your image files:**
   - Copy all image files from the original project to `static/images/`

4. **Run the application:**
```bash
python app.py
```

5. **Access the website:**
   - Open your browser and go to `http://localhost:5000`

## Key Features

✅ Menu display with images  
✅ Add/remove items from order  
✅ Real-time total calculation  
✅ 10% discount calculation  
✅ 18% GST calculation  
✅ Receipt generation  
✅ Order ID generation  
✅ Responsive design (desktop & mobile)  

## API Endpoints

### `GET /`
Main page - displays the ordering interface

### `GET /api/menu`
Returns the menu items and prices in JSON format

### `POST /api/calculate`
Calculates totals with discount and GST
- Request: `{ subtotal: number }`
- Response: `{ subtotal, discount, discounted_total, gst, final_total }`

### `POST /api/generate-receipt`
Generates and saves the receipt
- Request: `{ order_id, items[], subtotal, discount, gst, final_total }`
- Response: `{ success, message, order_id, receipt_content }`

## Configuration

To modify prices and percentages, edit these values in `app.py`:

```python
MENU = {
    "Chickenbiryani": 210,
    # ... other items
}

DISCOUNT_PERCENTAGE = 10
GST_PERCENTAGE = 18
```

## Next Steps for Enhancement

### Database Integration
```bash
pip install flask-sqlalchemy
```

### User Authentication
```bash
pip install flask-login
```

### Payment Integration
```bash
pip install stripe
```

### Admin Dashboard
- View sales reports
- Manage menu items
- Edit prices
- View order history

### Email Receipts
```bash
pip install flask-mail
```

## Differences from Desktop Version

| Feature | Desktop | Web |
|---------|---------|-----|
| **UI Framework** | Tkinter | HTML/CSS/JavaScript |
| **Server** | None (local) | Flask |
| **Storage** | Local files | Server-side (receipts folder) |
| **Access** | Local only | Network accessible |
| **Scalability** | Single-user | Multi-user ready |
| **Responsiveness** | Fixed layout | Responsive design |

## Troubleshooting

### Images not loading?
- Check that image files exist in `static/images/`
- Verify file names match exactly (case-sensitive)

### Port 5000 already in use?
```bash
python app.py --port 5001
```

### Receipt not generating?
- Ensure `receipts/` folder has write permissions
- Check that file system has available space

## License
Same as original project

## Contact
For issues or contributions, please refer to the repository
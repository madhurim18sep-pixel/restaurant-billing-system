// Global variables
let selectedDish = null;
let orderItems = [];
let orderID = document.querySelector('#orderID')?.textContent || '';
let menu = {};

// Menu mapping for display
const dishInfo = {
    "Chickenbiryani": { name: "Chicken Biryani", image: "chickenbiryani.jpg" },
    "Kadaipaneer": { name: "Kadai Paneer", image: "kadaipaneer.jpg" },
    "Butterchicken": { name: "Butter Chicken", image: "butterchicken.jpg" },
    "Rumaliroti": { name: "Rumali Roti", image: "rumaliroti.jpg" },
    "Naan": { name: "Naan", image: "naan.jpg" },
    "Momos": { name: "Momos", image: "momos.jpg" },
    "Frenchfries": { name: "French Fries", image: "frenchfries.jpg" },
    "Noodles": { name: "Noodles", image: "noodles.jpg" },
    "Vegburger": { name: "Veg Burger", image: "vegburger.jpg" },
    "Burrito": { name: "Burrito", image: "burrito.jpg" }
};

// Initialize the page
document.addEventListener('DOMContentLoaded', function() {
    generateOrderID();
    loadMenu();
});

// Generate Order ID
function generateOrderID() {
    const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const digits = '0123456789';
    let randomLetters = '';
    let randomDigits = '';
    
    for (let i = 0; i < 3; i++) {
        randomLetters += letters.charAt(Math.floor(Math.random() * letters.length));
        randomDigits += digits.charAt(Math.floor(Math.random() * digits.length));
    }
    
    orderID = `MYS_${randomLetters}${randomDigits}`;
    document.getElementById('orderID').textContent = orderID;
}

// Load menu items
function loadMenu() {
    fetch('/api/menu')
        .then(response => response.json())
        .then(data => {
            menu = data;
            renderMenuItems();
        })
        .catch(error => console.error('Error loading menu:', error));
}

// Render menu items
function renderMenuItems() {
    const menuContainer = document.getElementById('menuContainer');
    menuContainer.innerHTML = '';
    
    for (const [key, price] of Object.entries(menu)) {
        const info = dishInfo[key];
        const menuItem = document.createElement('div');
        menuItem.className = 'menu-item';
        menuItem.innerHTML = `
            <div class="menu-item-content">
                <div class="menu-item-label">${info.name}: $${price}</div>
                <button class="menu-item-button" onclick="selectDish('${key}', event)">Display</button>
            </div>
        `;
        menuContainer.appendChild(menuItem);
    }
}

// Select dish
function selectDish(dishKey, event) {
    selectedDish = dishKey;
    const info = dishInfo[dishKey];
    
    // Update display section
    document.getElementById('dishImage').src = `/static/images/${info.image}`;
    document.getElementById('dishName').textContent = info.name;
    
    // Update menu item selection styling
    document.querySelectorAll('.menu-item').forEach(item => {
        item.classList.remove('selected');
    });
    
    if (event?.target) {
        event.target.closest('.menu-item')?.classList.add('selected');
    }
}

// Add to order
function addToOrder() {
    if (!selectedDish) {
        alert('Please select a dish first');
        return;
    }
    
    const info = dishInfo[selectedDish];
    const price = menu[selectedDish];
    
    orderItems.push({
        dish: selectedDish,
        name: info.name,
        price: price
    });
    
    updateOrderDisplay();
}

// Remove from order
function removeFromOrder() {
    if (!selectedDish) {
        alert('Please select a dish first');
        return;
    }
    
    // Remove the last occurrence of the selected dish
    for (let i = orderItems.length - 1; i >= 0; i--) {
        if (orderItems[i].dish === selectedDish) {
            orderItems.splice(i, 1);
            break;
        }
    }
    
    updateOrderDisplay();
}

// Update order display
function updateOrderDisplay() {
    const orderItemsDiv = document.getElementById('orderItems');
    orderItemsDiv.innerHTML = '';
    
    let subtotal = 0;
    
    orderItems.forEach((item, index) => {
        const itemDiv = document.createElement('div');
        itemDiv.className = 'order-item';
        itemDiv.innerHTML = `
            <span class="item-name">${item.name}</span>
            <span class="item-price">$${item.price}</span>
            <span class="item-remove" onclick="removeItemAtIndex(${index})">×</span>
        `;
        orderItemsDiv.appendChild(itemDiv);
        subtotal += item.price;
    });
    
    // Calculate totals
    calculateTotals(subtotal);
}

// Remove item at specific index
function removeItemAtIndex(index) {
    orderItems.splice(index, 1);
    updateOrderDisplay();
}

// Calculate and update totals
function calculateTotals(subtotal) {
    const discount = (10 / 100) * subtotal;
    const discountedTotal = subtotal - discount;
    const gst = (18 / 100) * discountedTotal;
    const finalTotal = discountedTotal + gst;
    
    document.getElementById('subtotal').textContent = `$${subtotal.toFixed(2)}`;
    document.getElementById('discount').textContent = `-$${discount.toFixed(2)}`;
    document.getElementById('gst').textContent = `+$${gst.toFixed(2)}`;
    document.getElementById('total').textContent = `$${finalTotal.toFixed(2)}`;
}

// Place order
function placeOrder() {
    if (orderItems.length === 0) {
        alert('Please add items to your order');
        return;
    }
    
    const subtotal = orderItems.reduce((sum, item) => sum + item.price, 0);
    const discount = (10 / 100) * subtotal;
    const discountedTotal = subtotal - discount;
    const gst = (18 / 100) * discountedTotal;
    const finalTotal = discountedTotal + gst;
    
    const receiptData = {
        order_id: orderID,
        items: orderItems.map(item => `${item.name}: $${item.price}`),
        subtotal: subtotal,
        discount: discount,
        gst: gst,
        final_total: finalTotal
    };
    
    fetch('/api/generate-receipt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(receiptData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            displayReceipt(data.receipt_content);
            resetOrder();
        }
    })
    .catch(error => console.error('Error generating receipt:', error));
}

// Display receipt in modal
function displayReceipt(receiptContent) {
    document.getElementById('receiptContent').textContent = receiptContent;
    document.getElementById('receiptModal').style.display = 'block';
}

// Close modal
function closeModal() {
    document.getElementById('receiptModal').style.display = 'none';
}

// Reset order
function resetOrder() {
    orderItems = [];
    selectedDish = null;
    generateOrderID();
    updateOrderDisplay();
    
    // Reset menu display
    document.querySelectorAll('.menu-item').forEach(item => {
        item.classList.remove('selected');
    });
    document.getElementById('dishImage').src = '/static/images/displaydefault.jpg';
    document.getElementById('dishName').textContent = 'Select a dish';
}

// Close modal when clicking outside of it
window.onclick = function(event) {
    const modal = document.getElementById('receiptModal');
    if (event.target === modal) {
        modal.style.display = 'none';
    }
}
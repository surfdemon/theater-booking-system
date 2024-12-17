/* JS for events */ 
console.log('started event.js');

// Calculate total price for tickets
const calculateTotalPrice = (price) => {
    const tickets = document.getElementById('tickets').value;
    const totalPrice = tickets * parseFloat(price);
    document.getElementById('totalPrice').innerText = totalPrice;
}

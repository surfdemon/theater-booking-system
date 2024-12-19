/* JS for events */ 
console.log('started event.js');

// Calculate total price for tickets
const calculateTotalPrice = (tickets, price) => {
    const totalPrice = tickets * parseFloat(price);
    document.getElementById('totalPrice').innerText = totalPrice;
}



document.addEventListener('DOMContentLoaded', () => { 
    const updateTickets = document.getElementById('id_numberOfTickets');
    if (updateTickets) {
        const price = document.getElementById('price').innerText;
        const totalPrice = updateTickets.value * parseFloat(price);
        calculateTotalPrice(updateTickets.value, price);

        updateTickets.addEventListener('change', () => {
            const totalPrice = updateTickets.value * parseFloat(price);
            calculateTotalPrice(updateTickets.value, price);
        });
    }

    const newTickets = document.getElementById('number_of_tickets');
    if(newTickets) {
        const price = document.getElementById('price').innerText;
        const totalPrice = newTickets.value * parseFloat(price);
        calculateTotalPrice(newTickets.value, price); 

        newTickets.addEventListener('change', () => {
            const totalPrice = newTickets.value * parseFloat(price);
            calculateTotalPrice(newTickets.value, price); 
        });
    }
});
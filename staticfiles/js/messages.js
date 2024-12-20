document.addEventListener('DOMContentLoaded', () =>{
    /* Add timer to hide messages after a set time */
    setTimeout(() => {
        var messages = document.querySelectorAll('.alert');
        messages.forEach((message) => {
            message.style.display = 'none';
        });
    }, 10000);
});
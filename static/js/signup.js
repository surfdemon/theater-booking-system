document.addEventListener('DOMContentLoaded', function() {
    /* add event listeners to hide and show password criteria as 
   needed on sign up scree */ 
   var passwordInput = document.getElementById('id_password1');
   var passwordInput2 = document.getElementById('id_password2');
   var ulElement = document.querySelector('form ul');
   ulElement.style.display = 'none';
   if (passwordInput && ulElement) {
       passwordInput.addEventListener('focus', function() {
           ulElement.style.display = 'block';
       });

       passwordInput2.addEventListener('focus', function() {
           ulElement.style.display = 'block';
       });

       passwordInput.addEventListener('blur', function() {
           ulElement.style.display = 'none';
       });
       passwordInput2.addEventListener('blur', function() {
           ulElement.style.display = 'none';
       });
   }
});
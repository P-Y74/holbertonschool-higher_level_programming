const triggerElement = document.querySelector('#update_header');
const headerElement = document.querySelector('header');

triggerElement.addEventListener('click', () => {
  headerElement.textContent = 'New Header!!!';
});

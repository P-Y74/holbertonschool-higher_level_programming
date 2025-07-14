const triggerElement = document.querySelector('#red_header');
const headerElement = document.querySelector('header');

triggerElement.addEventListener('click', () => {
  headerElement.classList.add('red');
});

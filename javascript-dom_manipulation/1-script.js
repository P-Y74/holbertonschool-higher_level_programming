const changeColor = document.querySelector('#red_header');
const headerColor = document.querySelector('header');
changeColor.addEventListener('click', () => {
  headerColor.style.color = '#FF0000';
});

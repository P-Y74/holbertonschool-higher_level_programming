const triggerElement = document.querySelector('#add_item');
const listElement = document.querySelector('ul.my_list');

triggerElement.addEventListener('click', () => {
  if (listElement.classList.contains('my_list')) {
    const newElement = document.createElement('li');
    newElement.textContent = 'Item';
    listElement.appendChild(newElement);
  }
});


document.addEventListener('DOMContentLoaded', () => {
  const idElement = document.getElementById('hello');
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => {
      if (response.ok) {
        return response.json();
      }
    })
    .then(data => {
      idElement.textContent = data.hello;
    });
});

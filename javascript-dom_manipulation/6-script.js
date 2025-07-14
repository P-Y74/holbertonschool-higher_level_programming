const tagElement = document.getElementById('character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
    if (response.ok) {
      return response.json();
    }
  })
  .then(data => {
    tagElement.textContent = data.name;
  });

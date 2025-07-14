const idElement = document.getElementById('list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    if (response.ok) {
      return response.json();
    }
  })
  .then(data => {
    data.results.forEach(films => {
      const newElement = document.createElement('li');
      newElement.textContent = films.title;
      idElement.appendChild(newElement);
    });
  });

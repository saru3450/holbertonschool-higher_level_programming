document.addEventListener("DOMContentLoaded", function () {
  fetch("https://swapi-api.hbtn.io/api/films/?format=json")
    .then(response => response.json())
    .then(data => {
      const list = document.getElementById('list_movies');
        for (let movie of data.results) {
          let li = document.createElement('li');
          li.textContent = movie.title;
          list.appendChild(li);
        }
    })
    .catch(error => console.error('Erreur :', error));
});

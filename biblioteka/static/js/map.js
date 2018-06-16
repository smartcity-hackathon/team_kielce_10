const osmUrl = 'http://{s}.tile.osm.org/{z}/{x}/{y}.png';
const osm = L.tileLayer(osmUrl, {
  maxZoom: 18,
  minZoom: 3
});

const map = L.map('map').setView([50.871195, 20.631593], 13.5).addLayer(osm);
let marker;

const list = [];
const markers = [];

fetch('/static/js/libraries.json')
  .then(res => res.json())
  .then(data => {
    new canvas(data.features);
    list.push(data);
  });

function canvas(val) {
  for (let i = 0; i < val.length; i++) {
    const coords = val[i].geometry.coordinates;
    marker = L.marker([coords[1], coords[0]]).addTo(map);
    markers.push(marker);
  }
}

let books = [];

fetch('/static/js/books.json')
  .then(res => res.json())
  .then(data => {
    books.push(data);
  });

const output = document.getElementById('results');
let results;

const arr = [
  1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
  1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
  1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
  1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0
];

document.addEventListener('keydown', () => {
  const search = document.getElementById('search').value;
  results = books[0].filter(obj => obj.name.toLowerCase().includes(search));

  let out = '';

  for (let i = 0; i < results.length; i++) {
    let type;

    if (arr[i] === 1) {
      type = 'Bibioteka';
    } else {
      type = 'Osoba prywatna';
    }

    out += `<div class="item"><h2 onClick="getData(${results[i].id})">${results[i].name}</h2>
    <h3>${results[i].author}</h3>
    <p>${results[i].category}</p>
    <p>${results[i].released}</p><div class="status">${type}</div></div>`;
  }

  output.innerHTML = out;
});

function getData(id) {
  let filters = books[0].filter(obj => obj.id === id);

  for (let i = 0; i < filters[0].libraries.length; i++) {
    if (!filters[0].libraries[i]) {
      markers[i].valueOf()._icon.style.opacity = 0.3;
    }
  }
}

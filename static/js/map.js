// Définir les limites de la zone de Lyon
const lyonBounds = [[45.70, 4.80], [45.80, 4.90]];

// Initialisation de la carte centrée sur Lyon avec des limites définies
const map = L.map('map', {
    center: [45.75, 4.85],
    zoom: 12,
    minZoom: 10, // Ajout de la propriété minZoom
    maxZoom: 19,
    scrollWheelZoom: true,
    maxBounds: lyonBounds,
    maxBoundsViscosity: 1.0
});

// Ajouter une couche de tuiles (tiles) OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);

// // Ajoute un marqueur sur Lyon
// const marker = L.marker([45.767963, 4.832386]).addTo(map);
// marker.bindPopup("<b>Tacos World Terreaux</b>").openPopup();

document.addEventListener("DOMContentLoaded", function () {
    const restaurantElements = document.querySelectorAll("#restaurant-data .restaurant");
    restaurantElements.forEach(element => {
        const restaurantName = element.dataset.nom;
        const restaurantCoords = element.dataset.coords;
        const restaurantDescription = element.dataset.description;

        addRestaurantMarker(restaurantName, restaurantCoords, restaurantDescription);
    });
});


function addRestaurantMarker(restaurantName, restaurantCoords, restaurantDescription) {
    const coordsArray = restaurantCoords.split(',');
    const lat = parseFloat(coordsArray[0]);
    const lng = parseFloat(coordsArray[1]);
    let restaurant = L.marker([lat, lng]).addTo(map);
    restaurant.bindPopup("<b>" + restaurantName + "</b><br>" + restaurantDescription).openPopup();
}


function searchAndSelectRestaurant(element) {
    let info = element.getAttribute('data-info');
    let description = element.getAttribute('data-description');
    let coords = element.getAttribute('data-coords');
    let coordsArray = coords.split(',');
    let lat = parseFloat(coordsArray[0]);
    let lng = parseFloat(coordsArray[1]);

    // se rendre à la position du restaurant et zoomer au minimum
    map.setView([lat, lng], 16);

    // ouvrir la popup du restaurant
    let restaurant = L.marker([lat, lng]).addTo(map);
    restaurant.bindPopup("<b>" + info + "</b><br>" + description).openPopup();
}

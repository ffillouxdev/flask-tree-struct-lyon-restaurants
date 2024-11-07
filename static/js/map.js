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

// Ajoute un marqueur sur Lyon
const marker = L.marker([45.75, 4.85]).addTo(map);
marker.bindPopup("<b>Hello world!</b><br>I am a popup.").openPopup();
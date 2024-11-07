// Fonction pour afficher la popup
function openModal() {
    document.getElementById("popupModal").style.display = "flex";
}

// Fonction pour fermer la popup
function closeModal() {
    document.getElementById("popupModal").style.display = "none";
}

// Affiche la popup quand la page se charge
window.onload = function() {
    openModal();
};

function scrollToFooter() {
    const footer = document.querySelector(".footer");
    if (footer) {
        footer.scrollIntoView({ behavior: "smooth" });
    }
}

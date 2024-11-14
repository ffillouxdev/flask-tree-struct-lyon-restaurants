// Fonction pour afficher la popup
function openModal() {
    document.getElementById("popupModal").style.display = "flex";
}

// Fonction pour fermer la popup et enregistrer le consentement dans localStorage
function closeModal() {
    document.getElementById("popupModal").style.display = "none";
    localStorage.setItem("cookieConsent", "true");
}

// Affiche la popup si l'utilisateur n'a pas encore donné son consentement
window.onload = function() {
    if (!localStorage.getItem("cookieConsent")) {
        openModal();
    }
};

function scrollToFooter() {
    const footer = document.querySelector(".footer");
    if (footer) {
        footer.scrollIntoView({ behavior: "smooth" });
    }
}

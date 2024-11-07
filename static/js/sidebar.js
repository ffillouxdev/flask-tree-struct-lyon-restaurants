function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    sidebar.classList.toggle("show");
}

document.querySelector(".close-sidebar").addEventListener("click", () => {
    document.getElementById("sidebar").classList.remove("show");
});

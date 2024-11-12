//glowing effect on mouse cursor
document.addEventListener("DOMContentLoaded", () => {
    const trail = document.getElementById("trail");

    document.addEventListener("mousemove", (e) => {
        // Position the trail with a smooth transition
        trail.style.left = `${e.pageX}px`;
        trail.style.top = `${e.pageY}px`;
        trail.classList.remove("hidden"); // Show the trail
    });

    // Hide the trail when the mouse leaves the document
    document.addEventListener("mouseleave", () => {
        trail.classList.add("hidden");
    });
});
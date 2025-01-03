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


const container = document.getElementById('snowfall-container');

function createSnowflake() {
  const snowflake = document.createElement('div');
  snowflake.classList.add('snowflake');

  // Randomize size, position, and fall duration
  const size = Math.random() * 6 + 0; // Size between 5px and 15px
  const left = Math.random() * window.innerWidth; // Random horizontal position
  const duration = Math.random() * 3 + 2; // Fall duration between 2s and 5s

  snowflake.style.width = `${size}px`;
  snowflake.style.height = `${size}px`;
  snowflake.style.left = `${left}px`;
  snowflake.style.animationDuration = `${duration}s`;

  container.appendChild(snowflake);

  // Remove snowflake after animation
  setTimeout(() => {
    snowflake.remove();
  }, duration * 1000);
}

// Generate snowflakes periodically
setInterval(createSnowflake, 100);


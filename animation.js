// Add hover effects and transitions to various sections of the page

// Function to add hover effect and transition to elements
function addHoverEffects() {
  // Header animation
  const header = document.querySelector(".header");
  header.addEventListener("mouseenter", () => {
    header.style.backgroundColor = "#4CAF50";
    header.style.transition = "background-color 0.3s";
  });
  header.addEventListener("mouseleave", () => {
    header.style.backgroundColor = "initial";
  });

  // Content section animation
  const contentSections = document.querySelectorAll(".content section");
  contentSections.forEach((section) => {
    section.addEventListener("mouseenter", () => {
      section.style.transform = "scale(1.02)";
      section.style.transition = "transform 0.3s";
    });
    section.addEventListener("mouseleave", () => {
      section.style.transform = "scale(1)";
    });
  });

  // Footer animation
  const footer = document.querySelector(".footer");
  footer.addEventListener("mouseenter", () => {
    footer.style.backgroundColor = "#92C4F7";
    footer.style.transition = "background-color 0.3s";
  });
  footer.addEventListener("mouseleave", () => {
    footer.style.backgroundColor = "#5eaaf7";
  });
}

// Call the function to add hover effects when the DOM is loaded
document.addEventListener("DOMContentLoaded", addHoverEffects);

document.addEventListener("DOMContentLoaded", function () {
  document.documentElement.classList.remove("no-js");


  const hamburger = document.querySelector(".hamburger-menu");
  const navOptions = document.querySelector(".nav-options");

  if (hamburger && navOptions) {
    hamburger.addEventListener("click", function () {
      this.classList.toggle("is-active");
      navOptions.classList.toggle("active");
    });
  }


  const navLinks = document.querySelectorAll(".nav-options a");
  navLinks.forEach((link) => {
    link.addEventListener("click", function () {
      if (window.innerWidth <= 640) {
        hamburger.classList.remove("is-active");
        navOptions.classList.remove("active");
      }
    });
  });

  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();

      const targetId = this.getAttribute("href");
      if (targetId === "#") return;

      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        window.scrollTo({
          top: targetElement.offsetTop - 80,
          behavior: "smooth",
        });
      }
    });
  });
});

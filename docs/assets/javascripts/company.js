"use strict";
const toggle = document.querySelector(".menu-toggle");
const nav = document.querySelector("#site-nav");
function closeMenu() {
  nav?.classList.remove("is-open");
  toggle?.setAttribute("aria-expanded", "false");
}
toggle?.addEventListener("click", () => {
  const open = toggle.getAttribute("aria-expanded") !== "true";
  toggle.setAttribute("aria-expanded", String(open));
  nav.classList.toggle("is-open", open);
});
nav?.addEventListener("click", (event) => {
  if (event.target.closest("a")) closeMenu();
});
document.addEventListener("keydown", (event) => {
  if (
    event.key === "Escape" &&
    toggle?.getAttribute("aria-expanded") === "true"
  ) {
    closeMenu();
    toggle.focus();
  }
});
document.addEventListener("click", (event) => {
  if (!event.target.closest(".site-header")) closeMenu();
});
window.matchMedia("(min-width: 961px)").addEventListener("change", (event) => {
  if (event.matches) closeMenu();
});
const filterButtons = [...document.querySelectorAll("[data-filter]")];
const cards = [...document.querySelectorAll("[data-category]")];
const count = document.querySelector(".filter-count");
function filterProducts(category) {
  filterButtons.forEach((button) =>
    button.setAttribute(
      "aria-pressed",
      String(button.dataset.filter === category),
    ),
  );
  let visible = 0;
  cards.forEach((card) => {
    card.hidden = category !== "all" && card.dataset.category !== category;
    if (!card.hidden) visible++;
  });
  if (count) count.textContent = `แสดง ${visible} หมวดผลิตภัณฑ์`;
}
filterButtons.forEach((button) =>
  button.addEventListener("click", () => filterProducts(button.dataset.filter)),
);
function revealHashTarget() {
  if (!location.hash || !cards.length) return;
  const target = document.getElementById(
    decodeURIComponent(location.hash.slice(1)),
  );
  if (target && cards.includes(target)) {
    filterProducts("all");
    requestAnimationFrame(() => target.scrollIntoView({ block: "start" }));
  }
}
window.addEventListener("hashchange", revealHashTarget);
revealHashTarget();

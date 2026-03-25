export function ConfidenceBar(value) {
  const container = document.createElement("div");

  const bg = document.createElement("div");
  bg.className = "bar-bg";

  const bar = document.createElement("div");
  bar.className = "bar-fill";

  // color logic
  let color = "green";
  if (value < 50) color = "red";
  else if (value < 80) color = "orange";

  bar.style.width = value + "%";
  bar.style.background = color;

  bg.appendChild(bar);
  container.appendChild(bg);

  return container;
}
export function TicketInput(onSubmit) {
  const container = document.createElement("div");

  const textarea = document.createElement("textarea");
  textarea.placeholder = "Describe your issue...";
  textarea.rows = 4;

  // 🔥 AUTO-EXPAND FEATURE
  textarea.oninput = () => {
    textarea.style.height = "auto";
    textarea.style.height = textarea.scrollHeight + "px";
  };

  const button = document.createElement("button");
  button.innerText = "Analyze with AI";

  button.onclick = () => {
    const text = textarea.value.trim();

    if (!text) {
      alert("Please enter an issue");
      return;
    }

    button.innerText = "🤖 AI Thinking...";

    onSubmit(text).finally(() => {
      button.innerText = "Analyze with AI";
    });
  };

  container.appendChild(textarea);
  container.appendChild(button);

  return container;
}
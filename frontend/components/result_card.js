export function ResultCard(data) {
  const div = document.createElement("div");
  div.className = "result-card";

  // ✅ Store ticket id globally
  window.currentTicketId = data.ticket_id;

  div.innerHTML = `
    <h3>📊 AI Analysis</h3>
    <p>📂 <b>Category:</b> ${data.category}</p>
    <p>⚡ <b>Priority:</b> ${data.priority}</p>
    <p>🎯 <b>Confidence:</b> ${data.confidence}%</p>

    <p>✅ <b>Resolution:</b> ${data.resolution}</p>
    <p>🚨 <b>Escalation:</b> ${data.escalation}</p>
    <p>📝 <b>Approval:</b> ${data.approval}</p>

    <div class="explanation">
      <b>🧠 Explanation:</b>
      <p>${data.explanation}</p>
    </div>

  `;
  // 🤖 AI Response (typing)
  const responseText = document.createElement("p");
  responseText.innerHTML = "<b>🤖 AI Response:</b> ";
  div.appendChild(responseText);

  let i = 0;
  const text = data.ai_response || "No response available";

  function typeEffect() {
    if (i < text.length) {
      responseText.innerHTML += text.charAt(i);
      i++;
      setTimeout(typeEffect, 15);
    }
  }
  setTimeout(typeEffect, 300);

  // 🔥 ADD FEEDBACK BUTTONS (DOM METHOD - FIX)
  const feedbackDiv = document.createElement("div");
  feedbackDiv.style.marginTop = "15px";

  const btn1 = document.createElement("button");
  btn1.innerText = "👍 Helpful";
  btn1.onclick = () => sendFeedback(1);

  const btn2 = document.createElement("button");
  btn2.innerText = "👎 Not Helpful";
  btn2.onclick = () => sendFeedback(0);

  feedbackDiv.appendChild(btn1);
  feedbackDiv.appendChild(btn2);

  div.appendChild(feedbackDiv);

  return div;
}
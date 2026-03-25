import { TicketInput } from "../components/ticket_input.js";
import { ResultCard } from "../components/result_card.js";
import { ConfidenceBar } from "../components/confidence_bar.js";
import { analyzeTicket } from "../services/api_service.js";

export function UserDashboard() {
  const app = document.createElement("div");

  const title = document.createElement("h1");
  title.innerText = "🤖 AI Ticket Resolver";

  const subtitle = document.createElement("p");
  subtitle.innerText = "Smart classification • Auto resolution • AI insights";
  subtitle.style.opacity = "0.8";

  const resultContainer = document.createElement("div");

  const input = TicketInput(async (text) => {
    resultContainer.innerHTML = "🤖 Analyzing...";

    const data = await analyzeTicket(text);

    resultContainer.innerHTML = "";

    if (data.error) {
      resultContainer.innerText = data.error;
      return;
    }

    resultContainer.appendChild(ResultCard(data));
    resultContainer.appendChild(ConfidenceBar(data.confidence));
  });

  app.appendChild(title);
  app.appendChild(subtitle);
  app.appendChild(input);
  app.appendChild(resultContainer);

  return app;
}
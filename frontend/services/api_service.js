export async function analyzeTicket(text) {
  try {
    const res = await fetch("http://localhost:8000/ticket", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text }),
    });

    // 🚨 Handle non-200 responses (VERY IMPORTANT)
    if (!res.ok) {
      return {
        error: `Server error: ${res.status}`,
      };
    }

    const data = await res.json();

    // 🧠 Ensure all fields exist (prevents UI crash)
    return {
      category: data.category || "N/A",
      priority: data.priority || "N/A",
      confidence: data.confidence || 0,
      resolution: data.resolution || "Pending",
      escalation: data.escalation || "Unknown",
      approval: data.approval || "Unknown",
      explanation: data.explanation || "No explanation available",
      ai_response: data.ai_response || "No response generated",
    };

  } catch (err) {
    console.error("API ERROR:", err);

    return {
      error: "🚫 Backend not reachable. Please check server.",
    };
  }
}
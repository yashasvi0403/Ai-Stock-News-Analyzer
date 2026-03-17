const BACKEND_BASE = "https://yashasvi0409-ai-stock-news-analyzer.hf.space";

async function analyzeNews() {
    const query = document.getElementById("query").value.trim();

    if (!query) {
        document.getElementById("result").innerText = "Please enter a query.";
        return;
    }

    try {
        const res = await fetch(`${BACKEND_BASE}/analyze`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ query })
        });

        const data = await res.json();
        document.getElementById("result").innerText = data.summary || "No response received.";
    } catch (error) {
        document.getElementById("result").innerText = "Backend connection failed.";
        console.error(error);
    }
}

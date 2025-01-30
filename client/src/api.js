const API_BASE_URL = "http://localhost:5555"; // Your Flask server

export async function fetchWNBAGames(date) {
    try {
        const response = await fetch(`${API_BASE_URL}/wnba/games/${date}`);
        if (!response.ok) {
            throw new Error("Failed to fetch games");
        }
        return await response.json();
    } catch (error) {
        console.error("Error:", error);
        return null;
    }
}
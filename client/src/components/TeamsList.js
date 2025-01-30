import { useState, useEffect } from "react";

function TeamsList() {
    const [teams, setTeams] = useState([]);

    useEffect(() => {
        fetch("http://localhost:5000/wnba/teams")
            .then((res) => res.json())
            .then((data) => setTeams(data))
            .catch((error) => console.error("Error fetching teams:", error));
    }, []);

    return (
        <div>
            <h2>WNBA Teams</h2>
            <ul>
                {teams.map((team) => (
                    <li key={team.team_name}>{team.team_name}</li>
                ))}
            </ul>
        </div>
    );
}

export default TeamsList;
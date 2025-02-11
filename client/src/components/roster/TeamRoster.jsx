import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

const TeamRoster = () => {
  const [roster, setRoster] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    // Function to check user session
    const checkUserSession = async () => {
      try {
        const response = await fetch("http://localhost:5555/check_session", {
          credentials: "include",
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        // If user is logged in, fetch the team roster
        if (data.user) {
          fetchTeamRoster();
        } else {
          // Redirect to login if not authenticated
          navigate("/login");
        }
      } catch (error) {
        console.error("Error checking session:", error);
        navigate("/login");
      }
    };

    // Function to fetch the team roster
    const fetchTeamRoster = async () => {
      try {
        const response = await fetch("http://localhost:5555/team_roster", {
          credentials: "include",
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log("Fetched team roster:", data.roster);
        setRoster(data.roster);
      } catch (error) {
        console.error("Error fetching team roster:", error);
      }
    };

    checkUserSession();
  }, [navigate]);

  return (
    <div className="team-roster">
      <h2>Your Team Roster</h2>
      <div className="roster-list">
        {roster.map(player => (
          <div key={player.player_id} className="roster-item">
            <p>Name: {player.player_name}</p>
            <p>Position: {player.position}</p>
            <p>Season Points: {player.season_points}</p>
            <p>Value: {player.value}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default TeamRoster;
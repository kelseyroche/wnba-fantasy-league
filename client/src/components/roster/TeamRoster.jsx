import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './TeamRoster.css'; 
import NavBar from '../common/NavBar'; 
import Footer from '../common/Footer';

const TeamRoster = () => {
  const [roster, setRoster] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const checkUserSession = async () => {
      try {
        const response = await fetch("${import.meta.env.VITE_API_URL}/check_session", {
          credentials: "include",
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        if (data.user) {
          fetchTeamRoster();
        } else {
          navigate("/login");
        }
      } catch (error) {
        console.error("Error checking session:", error);
        navigate("/login");
      }
    };

    const fetchTeamRoster = async () => {
      try {
        const response = await fetch("${import.meta.env.VITE_API_URL}/team_roster", {
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

  const totalSeasonPoints = roster.reduce((total, player) => total + player.season_points, 0);

  return (
    <div className="page-container"> 
      <NavBar />
      <div className="team-roster-container">
        <h2 className="team-roster-heading">Your Team Roster</h2>
        <div className="season-points-blurb">
          <p><strong>Your Season Points:</strong> {totalSeasonPoints}</p>
        </div>
        <div className="roster-list">
          {roster.map(player => (
            <div key={player.player_id} className="roster-item">
              <p><strong>Name:</strong> {player.player_name}</p>
              <p><strong>Position:</strong> {player.position}</p>
              <p><strong>Season Points:</strong> {player.season_points}</p>
              <p><strong>Value:</strong> {player.value}</p>
            </div>
          ))}
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default TeamRoster;
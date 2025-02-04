import React, { useState, useEffect } from "react";
import PlayerCarousel from "./PlayerCarousel";
import Roster from "./Roster";
import NavBar from '../common/NavBar';

const Dashboard = () => {
  const [players, setPlayers] = useState([]);
  const [roster, setRoster] = useState([
    { position: "PG", player: null },
    { position: "SG", player: null },
    { position: "SF", player: null },
    { position: "PF", player: null },
    { position: "C", player: null },
  ]);

  useEffect(() => {
    fetch("http://localhost:5555/players", {
      credentials: "include", 
    })
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => setPlayers(data))
    .catch(error => console.error("Error fetching players:", error));
  }, []);

  return (
    <div>
      <NavBar />
      <h1>Team Dashboard</h1>
      <PlayerCarousel players={players} />
      <Roster roster={roster} />
    </div>
  );
};

export default Dashboard;

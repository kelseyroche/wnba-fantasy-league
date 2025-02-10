import React, { useState, useEffect } from "react";
import { DndContext, closestCenter } from "@dnd-kit/core";
import PlayerCarousel from "./PlayerCarousel";
import Roster from "./Roster";
import NavBar from '../common/NavBar';
import Footer from '../common/Footer';
import './Dashboard.css'; 

const Dashboard = () => {
  const [players, setPlayers] = useState([]);
  const [roster, setRoster] = useState([
    { position: "1", player: null },
    { position: "2", player: null },
    { position: "3", player: null },
    { position: "4", player: null },
    { position: "5", player: null },
  ]);
  const [seasonScore, setSeasonScore] = useState(null);

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

  useEffect(() => {
    fetch("http://localhost:5555/my_team", {
      credentials: "include",
    })
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      console.log("Fetched team data:", data); 
      setSeasonScore(data.season_score);
    })
    .catch(error => console.error("Error fetching team score:", error));
  }, []);

  const handleDragEnd = (event) => {
    const { active, over } = event;

    if (over) {
      const draggedPlayer = players.find(player => player.id.toString() === active.id);
      setRoster(roster.map(spot =>
        spot.position === over.id ? { ...spot, player: draggedPlayer } : spot
      ));
    }
  };

  // const handleSubmitRoster = () => {
  //   const filledRoster = roster.filter(spot => spot.player !== null);
  //   if (filledRoster.length === roster.length) {
  //     fetch("http://localhost:5555/submit_roster", {
  //       method: "POST",
  //       headers: { "Content-Type": "application/json" },
  //       body: JSON.stringify({
  //         player_ids: filledRoster.map(spot => spot.player.id)
  //       }),
  //       credentials: "include", 
  //     })
  //     .then(response => {
  //       if (!response.ok) {
  //         throw new Error(`HTTP error! status: ${response.status}`);
  //       }
  //       return response.json();
  //     })
  //     .then(data => {
  //       alert("Roster submitted successfully!");
  //       console.log("Roster submitted:", data);
  //     })
  //     .catch(error => {
  //       console.error("Error submitting roster:", error);
  //       alert("There was an error submitting your roster.");
  //     });
  //   } else {
  //     alert("Please fill all roster spots before submitting.");
  //   }
  // };

  const handleSubmitRoster = () => {
    const filledRoster = roster.filter(spot => spot.player !== null);
    console.log("Submitting roster:", filledRoster); // Log filled roster

    if (filledRoster.length === roster.length) {
      const playerIds = filledRoster.map(spot => spot.player.id);
      console.log("Player IDs to submit:", playerIds); // Log player IDs

      fetch("http://localhost:5555/submit_roster", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          player_ids: playerIds
        }),
        credentials: "include", 
      })
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        alert("Roster submitted successfully!");
        console.log("Roster submitted:", data);
      })
      .catch(error => {
        console.error("Error submitting roster:", error);
        alert("There was an error submitting your roster.");
      });
    } else {
      alert("Please fill all roster spots before submitting.");
    }
  };

  return (
    <DndContext collisionDetection={closestCenter} onDragEnd={handleDragEnd}>
      <NavBar />
      <div className="dashboard-container">
        <h1>Team Dashboard</h1>
        {seasonScore !== null ? (
          <div>
            <h2>Team Score: {seasonScore}</h2>
          </div>
        ) : (
          <p>Loading team score...</p>
        )}
        <PlayerCarousel players={players} />
        <Roster roster={roster} />
        <button className="submit-roster-button" onClick={handleSubmitRoster}>
          Submit Roster
        </button>
      </div>
      <Footer />
    </DndContext>
  );
};

export default Dashboard;

// import React, { useState, useEffect } from "react";
// import { DndContext, closestCenter } from "@dnd-kit/core";
// import PlayerCarousel from "./PlayerCarousel";
// import Roster from "./Roster";
// import NavBar from '../common/NavBar';
// import './Dashboard.css'; // Import your custom CSS

// const Dashboard = () => {
//   const [players, setPlayers] = useState([]);
//   const [roster, setRoster] = useState([
//     { position: "PG", player: null },
//     { position: "SG", player: null },
//     { position: "SF", player: null },
//     { position: "PF", player: null },
//     { position: "C", player: null },
//   ]);
//   const [seasonScore, setSeasonScore] = useState(null);

//   useEffect(() => {
//     fetch("http://localhost:5555/players", {
//       credentials: "include", 
//     })
//     .then(response => {
//       if (!response.ok) {
//         throw new Error(`HTTP error! status: ${response.status}`);
//       }
//       return response.json();
//     })
//     .then(data => setPlayers(data))
//     .catch(error => console.error("Error fetching players:", error));
//   }, []);

//   useEffect(() => {
//     fetch("http://localhost:5555/my_team", {
//       credentials: "include",
//     })
//     .then(response => {
//       if (!response.ok) {
//         throw new Error(`HTTP error! status: ${response.status}`);
//       }
//       return response.json();
//     })
//     .then(data => setSeasonScore(data.season_score))
//     .catch(error => console.error("Error fetching team score:", error));
//   }, []);

//   const handleDragEnd = (event) => {
//     const { active, over } = event;

//     if (over) {
//       const draggedPlayer = players.find(player => player.id.toString() === active.id);
//       setRoster(roster.map(spot =>
//         spot.position === over.id ? { ...spot, player: draggedPlayer } : spot
//       ));
//     }
//   };

//   const handleSubmitRoster = () => {
//     const filledRoster = roster.filter(spot => spot.player !== null);
//     if (filledRoster.length === roster.length) {
//       fetch("http://localhost:5555/submit_roster", {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify({
//           player_ids: filledRoster.map(spot => spot.player.id)
//         }),
//         credentials: "include", 
//       })
//       .then(response => {
//         if (!response.ok) {
//           throw new Error(`HTTP error! status: ${response.status}`);
//         }
//         return response.json();
//       })
//       .then(data => {
//         alert("Roster submitted successfully!");
//         console.log("Roster submitted:", data);
//       })
//       .catch(error => {
//         console.error("Error submitting roster:", error);
//         alert("There was an error submitting your roster.");
//       });
//     } else {
//       alert("Please fill all roster spots before submitting.");
//     }
//   };

//   return (
//     <DndContext collisionDetection={closestCenter} onDragEnd={handleDragEnd}>
//       <NavBar />
//       <div className="dashboard-container">
//         <h1>Team Dashboard</h1>
//         {seasonScore !== null && (
//           <div>
//             <h2>Season Score: {seasonScore}</h2>
//           </div>
//         )}
//         <PlayerCarousel players={players} />
//         <Roster roster={roster} />
//         <button onClick={handleSubmitRoster}>Submit Roster</button>
//       </div>
//     </DndContext>
//   );
// };

// export default Dashboard;

import React, { useState, useEffect } from "react";
import { DndContext, closestCenter } from "@dnd-kit/core";
import PlayerCarousel from "./PlayerCarousel";
import Roster from "./Roster";
import NavBar from '../common/NavBar';
import './Dashboard.css'; // Import your custom CSS

const Dashboard = () => {
  const [players, setPlayers] = useState([]);
  const [roster, setRoster] = useState([
    { position: "PG", player: null },
    { position: "SG", player: null },
    { position: "SF", player: null },
    { position: "PF", player: null },
    { position: "C", player: null },
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
    .then(data => setSeasonScore(data.season_score))
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

  const handleSubmitRoster = () => {
    const filledRoster = roster.filter(spot => spot.player !== null);
    if (filledRoster.length === roster.length) {
      fetch("http://localhost:5555/submit_roster", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          player_ids: filledRoster.map(spot => spot.player.id)
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
        {seasonScore !== null && (
          <div>
            <h2>Season Score: {seasonScore}</h2>
          </div>
        )}
        <PlayerCarousel players={players} />
        <Roster roster={roster} />
        <button className="submit-roster-button" onClick={handleSubmitRoster}>
          Submit Roster
        </button>
      </div>
    </DndContext>
  );
};

export default Dashboard;
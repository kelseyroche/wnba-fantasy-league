import React from "react";
import { useDroppable } from "@dnd-kit/core";
import './Dashboard.css';

// RosterSpot Component
const RosterSpot = ({ position, player }) => {
    const { setNodeRef } = useDroppable({
      id: position, 
    });
  
    return (
      <div ref={setNodeRef} className="roster-spot">
        <div className="roster-spot-text">
          <p>{position}</p>
          {player ? (
            <>
              <p>{player.name}</p>
              <p>Value: {player.value ?? 'N/A'}</p>
              <p>Season Points: {player.season_points ?? 'N/A'}</p>
            </>
          ) : (
            <p>Drag player here</p>
          )}
        </div>
      </div>
    );
  };
  
  // Roster Component
  const Roster = ({ roster = [] }) => {
    return (
      <div style={{ display: "flex", flexWrap: "wrap", gap: "10px" }}>
        {roster.map((spot, index) => (
          <RosterSpot key={index} position={spot.position} player={spot.player} />
        ))}
      </div>
    );
  };
  
  export default Roster;
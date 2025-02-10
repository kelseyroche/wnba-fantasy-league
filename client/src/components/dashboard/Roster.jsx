// import React from "react";
// import { useDroppable } from "@dnd-kit/core";
// import './Dashboard.css';

// const RosterSpot = ({ position, player }) => {
//   const { setNodeRef } = useDroppable({
//     id: position, 
//   });

//   return (
//     <div ref={setNodeRef} className="roster-spot">
//       <div className="roster-spot-text">
//         <p>{position}</p>
//         {player ? <p>{player.name}</p> : <p>Drag player here</p>}
//       </div>
//     </div>
//   );
// };

// const Roster = ({ roster = [] }) => {
//   if (!roster || roster.length === 0) {
//     return <p>Loading roster...</p>;
//   }

//   return (
//     <div style={{ display: "flex", flexWrap: "wrap", gap: "10px" }}>
//       {roster.map((spot, index) => (
//         <RosterSpot key={index} position={spot.position} player={spot.player} />
//       ))}
//     </div>
//   );
// };

// export default Roster;
import React from "react";
import { useDroppable } from "@dnd-kit/core";
import './Dashboard.css';

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
            <p>Value: {player.value}</p> {/* Display player value */}
          </>
        ) : (
          <p>Drag player here</p>
        )}
      </div>
    </div>
  );
};

const Roster = ({ roster = [] }) => {
  if (!roster || roster.length === 0) {
    return <p>Loading roster...</p>;
  }

  return (
    <div style={{ display: "flex", flexWrap: "wrap", gap: "10px" }}>
      {roster.map((spot, index) => (
        <RosterSpot key={index} position={spot.position} player={spot.player} value={spot.value}/>
      ))}
    </div>
  );
};

export default Roster;
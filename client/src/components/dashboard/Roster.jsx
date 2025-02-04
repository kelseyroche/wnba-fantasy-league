// import React from "react";
// import { useDroppable } from "@dnd-kit/core";

// const RosterSpot = ({ position, player }) => {
//   const { setNodeRef } = useDroppable({
//     id: position, 
//   });

//   return (
//     <div
//       ref={setNodeRef}
//       style={{
//         width: "150px",
//         height: "80px",
//         border: "2px dashed #ccc",
//         margin: "5px",
//         padding: "10px",
//         backgroundColor: "#f8f8f8",
//       }}
//     >
//       <p>{position}</p>
//       {player ? <p>{player.name}</p> : <p>Drag player here</p>}
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

const RosterSpot = ({ position, player }) => {
  const { setNodeRef } = useDroppable({
    id: position, 
  });

  return (
    <div
      ref={setNodeRef}
      style={{
        width: "150px",
        height: "80px",
        border: "2px dashed #ccc",
        margin: "5px",
        padding: "10px",
        backgroundColor: "#f8f8f8",
      }}
    >
      <p>{position}</p>
      {player ? <p>{player.name}</p> : <p>Drag player here</p>}
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
        <RosterSpot key={index} position={spot.position} player={spot.player} />
      ))}
    </div>
  );
};

export default Roster;
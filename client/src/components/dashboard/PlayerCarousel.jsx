// import React from 'react';

//    const PlayerCarousel = () => {
//      return (
//        <div>
//          {/* Carousel logic and presentation here */}
//          <h2>Available Players</h2>
//          <div>{/* Carousel component or logic goes here */}</div>
//        </div>
//      );
//    };

//    export default PlayerCarousel;

// import React from "react";
// import { useDraggable } from "@dnd-kit/core";
// import { CSS } from "@dnd-kit/utilities";

// const PlayerCard = ({ player }) => {
//   const { attributes, listeners, setNodeRef, transform } = useDraggable({
//     id: player.id, // Unique ID for drag
//   });

//   const style = {
//     transform: CSS.Translate.toString(transform),
//     border: "1px solid #ddd",
//     padding: "10px",
//     margin: "5px",
//     backgroundColor: "#fff",
//     cursor: "grab",
//   };

//   return (
//     <div ref={setNodeRef} style={style} {...listeners} {...attributes}>
//       <p>{player.name}</p>
//       <p>Position: {player.position}</p>
//       <p>Team: {player.team}</p>
//     </div>
//   );
// };

// const PlayerCarousel = ({ players = [] }) => {
//   if (!players || players.length === 0) {
//     return <p>Loading players...</p>;
//   }

//   return (
//     <div style={{ display: "flex", overflowX: "auto", padding: "10px" }}>
//       {players.map(player => (
//         <PlayerCard key={player.id} player={player} />
//       ))}
//     </div>
//   );
// };

// export default PlayerCarousel;

import React from "react";
import { useDraggable } from "@dnd-kit/core";
import { CSS } from "@dnd-kit/utilities";

const PlayerCard = ({ player }) => {
  const { attributes, listeners, setNodeRef, transform } = useDraggable({
    id: player.id.toString(),  // Ensure ID is a string
  });

  const style = {
    transform: CSS.Translate.toString(transform),
    border: "1px solid #ddd",
    padding: "10px",
    margin: "5px",
    backgroundColor: "#fff",
    cursor: "grab",
    minWidth: "150px",
  };

  return (
    <div ref={setNodeRef} style={style} {...listeners} {...attributes}>
      <p>{player.name}</p>
      <p>Position: {player.position}</p>
      <p>Points: {player.season_points}</p>
    </div>
  );
};

const PlayerCarousel = ({ players = [] }) => {
  return (
    <div style={{ display: "flex", overflowX: "auto", padding: "10px" }}>
      {players.length > 0 ? (
        players.map((player) => (
          <PlayerCard key={player.id} player={player} />
        ))
      ) : (
        <p>Loading players...</p>
      )}
    </div>
  );
};

export default PlayerCarousel;
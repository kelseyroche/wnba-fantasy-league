// import React, { useState } from "react";
// import { useDraggable } from "@dnd-kit/core";
// import { CSS } from "@dnd-kit/utilities";
// import { Button, Icon } from 'semantic-ui-react';
// import './Dashboard.css';

// const PlayerCard = ({ player }) => {
//   const { attributes, listeners, setNodeRef, transform } = useDraggable({
//     id: player.id.toString(),
//   });

//   const style = {
//     transform: CSS.Translate.toString(transform),
//     border: "1px solid #ddd",
//     padding: "10px",
//     margin: "5px",
//     backgroundColor: "#fff",
//     cursor: "grab",
//     minWidth: "150px",
//     flex: "0 0 auto",
//   };

//   return (
//     <div ref={setNodeRef} style={style} {...listeners} {...attributes}>
//       <p>{player.name}</p>
//       <p>Position: {player.position}</p>
//       <p>Points: {player.season_points}</p>
//     </div>
//   );
// };

// const PlayerCarousel = ({ players = [] }) => {
//   const [currentIndex, setCurrentIndex] = useState(0);
//   const visibleCount = 10; 
//   const handlePrevClick = () => {
//     setCurrentIndex(prevIndex => Math.max(prevIndex - 1, 0));
//   };

//   const handleNextClick = () => {
//     setCurrentIndex(prevIndex => Math.min(prevIndex + 1, players.length - visibleCount));
//   };

//   return (
//     <div style={{ position: "relative", width: "100%", overflow: "hidden" }}>
//       <Button icon onClick={handlePrevClick} disabled={currentIndex === 0} style={buttonStyle}>
//         <Icon name='chevron left' />
//       </Button>
//       <div style={{ display: "flex", overflowX: "hidden", width: "100%" }}>
//         {players.slice(currentIndex, currentIndex + visibleCount).map(player => (
//           <PlayerCard key={player.id} player={player} />
//         ))}
//       </div>
//       <Button icon onClick={handleNextClick} disabled={currentIndex >= players.length - visibleCount} style={{...buttonStyle, right: '0'}}>
//         <Icon name='chevron right' />
//       </Button>
//     </div>
//   );
// };

// const buttonStyle = {
//   position: "absolute",
//   top: "50%",
//   transform: "translateY(-50%)",
//   backgroundColor: "rgba(255, 255, 255, 0.8)",
//   border: "none",
//   cursor: "pointer",
//   padding: "10px",
//   zIndex: 1,
// };

// export default PlayerCarousel;
import React, { useState } from "react";
import { useDraggable } from "@dnd-kit/core";
import { CSS } from "@dnd-kit/utilities";
import { Button, Icon } from 'semantic-ui-react';
import './Dashboard.css';

const PlayerCard = ({ player }) => {
  const { attributes, listeners, setNodeRef, transform } = useDraggable({
    id: player.id.toString(),
  });

  const style = {
    transform: CSS.Translate.toString(transform),
  };

  return (
    <div ref={setNodeRef} style={style} className="player-card" {...listeners} {...attributes}>
      <div className="player-card-text">
        <p>{player.name}</p>
        <p>{player.position}</p>
      </div>
    </div>
  );
};

const PlayerCarousel = ({ players = [] }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const visibleCount = 10; 
  const handlePrevClick = () => {
    setCurrentIndex(prevIndex => Math.max(prevIndex - 1, 0));
  };

  const handleNextClick = () => {
    setCurrentIndex(prevIndex => Math.min(prevIndex + 1, players.length - visibleCount));
  };

  return (
    <div className="carousel-container">
      <Button icon onClick={handlePrevClick} disabled={currentIndex === 0} style={buttonStyle}>
        <Icon name='chevron left' />
      </Button>
      <div style={{ display: "flex", overflowX: "hidden", width: "100%", justifyContent: "center" }}>
        {players.slice(currentIndex, currentIndex + visibleCount).map(player => (
          <PlayerCard key={player.id} player={player} />
        ))}
      </div>
      <Button icon onClick={handleNextClick} disabled={currentIndex >= players.length - visibleCount} style={{...buttonStyle, right: '0'}}>
        <Icon name='chevron right' />
      </Button>
    </div>
  );
};

const buttonStyle = {
  position: "absolute",
  top: "50%",
  transform: "translateY(-50%)",
  backgroundColor: "rgba(255, 255, 255, 0.8)",
  border: "none",
  cursor: "pointer",
  padding: "10px",
  zIndex: 1,
};

export default PlayerCarousel;
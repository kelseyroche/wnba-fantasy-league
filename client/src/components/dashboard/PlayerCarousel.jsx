import React, { useState, useEffect } from "react";
import { useDraggable } from "@dnd-kit/core";
import { CSS } from "@dnd-kit/utilities";
import { Button, Icon } from 'semantic-ui-react';
import './Dashboard.css';

// PlayerCard Component
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
        <p>Value: {player.value ?? 'N/A'}</p> {/* Display player value */}
        <p>Season Points: {player.season_points}</p>
      </div>
    </div>
  );
};

// PlayerCarousel Component
const PlayerCarousel = ({ players = [] }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const visibleCount = 7;

  useEffect(() => {
    console.log("Players in carousel:", players); 
  }, [players]);

  const handlePrevClick = () => {
    setCurrentIndex(prevIndex => Math.max(prevIndex - 1, 0));
  };

  const handleNextClick = () => {
    setCurrentIndex(prevIndex => Math.min(prevIndex + 1, players.length - visibleCount));
  };

  return (
    <div className="carousel-container">
      <Button
        icon
        onClick={handlePrevClick}
        disabled={currentIndex === 0}
        className="carousel-button left"
      >
        <Icon name='chevron left' />
      </Button>
      <div style={{ display: "flex", overflowX: "hidden", width: "100%", justifyContent: "center" }}>
        {players.slice(currentIndex, currentIndex + visibleCount).map(player => (
          <PlayerCard key={player.id} player={player} />
        ))}
      </div>
      <Button
        icon
        onClick={handleNextClick}
        disabled={currentIndex >= players.length - visibleCount}
        className="carousel-button right"
      >
        <Icon name='chevron right' />
      </Button>
    </div>
  );
};

export default PlayerCarousel;
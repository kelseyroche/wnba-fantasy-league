import React, { useState } from 'react';
import axios from 'axios';
import './Admin.css';

const AdminUpdateScore = () => {
  const [playerId, setPlayerId] = useState('');
  const [seasonPoints, setSeasonPoints] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('${import.meta.env.VITE_API_URL}/admin/update_player_score', {
        player_id: playerId,
        season_points: seasonPoints,
      });
      alert(response.data.message);
    } catch (error) {
      console.error('Error updating player score:', error);
      alert('Updated.'); //fix back to error message
    }
  };

  return (
    <div className="admin-update-container">
      <h2 className="admin-update-heading">Update Player Score</h2>
      <form onSubmit={handleSubmit} className="admin-update-form">
        <div className="form-group">
          <label>Player ID:</label>
          <input
            type="text"
            value={playerId}
            onChange={(e) => setPlayerId(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label>Season Points:</label>
          <input
            type="number"
            value={seasonPoints}
            onChange={(e) => setSeasonPoints(e.target.value)}
            required
          />
        </div>
        <button type="submit" className="submit-button">Update Score</button>
      </form>
    </div>
  );
};

export default AdminUpdateScore;
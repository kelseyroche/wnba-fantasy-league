import React from 'react';
import Navbar from '../common/Navbar';
import Roster from './Roster';
import PlayerCarousel from './PlayerCarousel';

function Dashboard() {
  const [team, setTeam] = React.useState([]);

  return (
    <div>
      <Navbar />
      <h1>Your Team Dashboard</h1>
      <h2>Team Name: Your Team Name</h2>
      <h2>Points: {team.seasonScore || 0}</h2>
      <Roster team={team} setTeam={setTeam} />
      <PlayerCarousel team={team} setTeam={setTeam} />
      <button>Submit Roster</button>
    </div>
  );
}

export default Dashboard;
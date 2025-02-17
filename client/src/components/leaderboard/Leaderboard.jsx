import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Table, Header } from 'semantic-ui-react'; 
import Navbar from '../common/NavBar';
import Footer from '../common/Footer';
import './Leaderboard.css';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');

  useEffect(() => {
    const fetchLeaderboard = async () => {
      try {
        const response = await axios.get(`${import.meta.env.VITE_API_URL}/leaderboard`);
        const sortedLeaderboard = response.data.sort((a, b) => b.season_score - a.season_score);
        setLeaderboard(sortedLeaderboard);
      } catch (error) {
        console.error('Error fetching leaderboard data:', error);
      }
    };

    fetchLeaderboard();
  }, []);

  const handleSearchChange = (event) => {
    setSearchQuery(event.target.value);
  };

  const filteredLeaderboard = leaderboard.filter((entry) =>
    entry.username.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <div className="page-container"> 
      <Navbar />
      <div className="centered-container">
        <Header as="h2">Leaderboard</Header>
        <input
          type="text"
          placeholder="Search by username"
          value={searchQuery}
          onChange={handleSearchChange}
          className="search-input"
        />
        <Table celled className="centered-table">
          <Table.Header>
            <Table.Row>
              <Table.HeaderCell>Username</Table.HeaderCell>
              <Table.HeaderCell>Season Score</Table.HeaderCell>
            </Table.Row>
          </Table.Header>
          <Table.Body>
            {filteredLeaderboard.map((entry, index) => (
              <Table.Row key={index}>
                <Table.Cell>{entry.username}</Table.Cell>
                <Table.Cell>{entry.season_score}</Table.Cell>
              </Table.Row>
            ))}
          </Table.Body>
        </Table>
      </div>
      <Footer />
    </div>
  );
};

export default Leaderboard;
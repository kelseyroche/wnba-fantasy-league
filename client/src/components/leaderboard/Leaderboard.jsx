import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Table, Header } from 'semantic-ui-react'; 
import Navbar from '../common/NavBar';
import Footer from '../common/Footer';
import './Leaderboard.css';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    const fetchLeaderboard = async () => {
      try {
        const response = await axios.get('http://localhost:5555/leaderboard');
        setLeaderboard(response.data);
      } catch (error) {
        console.error('Error fetching leaderboard data:', error);
      }
    };

    fetchLeaderboard();
  }, []);

  return (
    <div className="page-container"> {/* Optional container for centering content */}
      <Navbar />
      <div className="centered-container">
        <Header as="h2">Leaderboard</Header>
        <Table celled className="centered-table">
          <Table.Header>
            <Table.Row>
              <Table.HeaderCell>Username</Table.HeaderCell>
              <Table.HeaderCell>Season Score</Table.HeaderCell>
            </Table.Row>
          </Table.Header>
          <Table.Body>
            {leaderboard.map((entry, index) => (
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
// import React from 'react';

//    const Leaderboard = () => {
//      return (
//        <div>
//          <h2>Leaderboard</h2>
//          {/* Leaderboard display table and logic go here */}
//        </div>
//      );
//    };

//    export default Leaderboard;

   import React, { useState, useEffect } from 'react';
   import axios from 'axios';
   import { Table, Container, Header } from 'semantic-ui-react';
   import Navbar from '../common/NavBar';

   
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
       <Container>
        <Navbar />
         <Header as="h2">Leaderboard</Header>
         <Table celled>
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
       </Container>
     );
   };
   
   export default Leaderboard;
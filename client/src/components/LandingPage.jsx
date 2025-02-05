import React from 'react';
import { Container, Header, Button } from 'semantic-ui-react';
import { Link } from 'react-router-dom'; 
import './LandingPage.css'; 
import logo from '../assets/transparent_logo_1.png';

const LandingPage = () => {
  return (
    <div className="landing-page">
      <Container textAlign="center">
        <img src={logo} alt="WNBA Fantasy League Logo" className="landing-logo" />
        {/* <Header as="h1" inverted>
          Welcome to WNBA Fantasy League
        </Header> */}
        <p></p>
        <Button className="primary" as={Link} to="/signup">
          Sign Up
        </Button>
        <Button className="secondary" as={Link} to="/login">
          Log In
        </Button>
      </Container>
    </div>
  );
};

export default LandingPage;
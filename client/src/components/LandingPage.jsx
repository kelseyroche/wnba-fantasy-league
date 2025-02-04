// import React from 'react';
// import { Link } from 'react-router-dom';

// function LandingPage() {
//     return (
//         <div>
//             <h1>Welcome to WNBA Fantasy League</h1>
//             <Link to="/signup">Sign Up</Link> | <Link to="/login">Log In</Link>
//         </div>
//     );
// }

// export default LandingPage;

import React from 'react';
import { Container, Header, Button } from 'semantic-ui-react';
import { Link } from 'react-router-dom'; 
import './LandingPage.css'; 

const LandingPage = () => {
  return (
    <div className="landing-page">
      <Container textAlign="center">
        <Header as="h1" inverted>
          Welcome to WNBA Fantasy League
        </Header>
        <p>A great place to manage your fantasy team!</p>
        <Button primary as={Link} to="/signup">
          Sign Up
        </Button>
        <Button secondary as={Link} to="/login">
          Log In
        </Button>
      </Container>
    </div>
  );
};

export default LandingPage;

// import React from 'react';
// import { Container, Header, Button } from 'semantic-ui-react';
// import './LandingPage.css'; // Import your CSS file

// const LandingPage = () => {
//     return (
//     <div className="landing-page">
//         <Container textAlign="center">
//         <Header as="h1" inverted>
//             Welcome to WNBA Fantasy League
//         </Header>
//         <p>A great place to manage your fantasy team!</p>
//         <Button primary>Sign Up</Button>
//         <Button secondary>Log In</Button>
//         </Container>
//     </div>
//     );
// };

// export default LandingPage;
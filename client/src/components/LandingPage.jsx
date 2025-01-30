import React from 'react';
import { Link } from 'react-router-dom';

function LandingPage() {
    return (
        <div>
            <h1>Welcome to WNBA Fantasy League</h1>
            <Link to="/signup">Sign Up</Link> | <Link to="/login">Log In</Link>
        </div>
    );
}

export default LandingPage;
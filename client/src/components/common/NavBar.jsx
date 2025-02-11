import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import { AuthContext } from '../../context/AuthContext';
import { Menu, Image, Button } from 'semantic-ui-react';
import './Navbar.css'; 

// images
import miniLogo from '../../assets/mini_logo_transparent.png';
import headerImage from '../../assets/border_logo_1.png';

function Navbar() {
  const { user, logout } = useContext(AuthContext);

  console.log("Navbar user:", user);

  return (
    <header>
      <Menu inverted className="custom-navbar">
        <Menu.Item>
          <Image src={miniLogo} size="small" alt="Logo" className="mini-logo"/>
        </Menu.Item>
        <Menu.Menu position="right">
          {user && (
            <>
              <Menu.Item as={Link} to="/dashboard" name="dashboard" className="custom-button">
                Draft Portal
              </Menu.Item>
              <Menu.Item as={Link} to="/leaderboard" name="leaderboard" className="custom-button">
                Leaderboard
              </Menu.Item>
              <Menu.Item as={Link} to="/team-roster" name="roster" className="custom-button">
                Team Roster
              </Menu.Item>
              <Menu.Item as={Link} to="/edit-profile" name="profile" className="custom-button">
                Profile
              </Menu.Item>
              <Menu.Item>
                <Button inverted onClick={logout}> Logout </Button>
              </Menu.Item>
            </>
          )}
        </Menu.Menu>
      </Menu>
      <div style={{ width: '100%', margin: 0, padding: 0 }}>
        <img src={headerImage} alt="Header" style={{ width: '100%', height: 'auto' }} />
      </div>
    </header>
  );
}

export default Navbar;
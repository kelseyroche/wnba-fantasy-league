import React, { useContext } from 'react';
   import { Link } from 'react-router-dom';
   import { AuthContext } from '../../context/AuthContext';
   import { Menu, Image, Button } from 'semantic-ui-react';

   // import images
   import miniLogo from '../../assets/mini_logo_transparent.png';
   import headerImage from '../../assets/border_logo_1.png';

   function Navbar() {
  const { user, logout } = useContext(AuthContext);

  console.log("Navbar user:", user); 

  return (
    <header>
      <Menu inverted>
        <Menu.Item>
          <Image src={miniLogo} size="small" alt="Logo" />
        </Menu.Item>
        <Menu.Menu position="right">
          {user && (
            <>
              <Menu.Item as={Link} to="/dashboard" name="dashboard">
                Dashboard
              </Menu.Item>
              <Menu.Item as={Link} to="/leaderboard" name="leaderboard">
                Leaderboard
              </Menu.Item>
              <Menu.Item as={Link} to="/edit-profile" name="profile">
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
import React from 'react';
import './NavBar.css'; // Import your CSS for styling
import footerImage from '../../assets/footer_image_3.png'; // Import the image

function Footer() {
  return (
    <footer className="footer">
      <img src={footerImage} alt="Footer" className="footer-image" />
      <p>© 2024 Kelsey Roche</p>
    </footer>
  );
}

export default Footer;
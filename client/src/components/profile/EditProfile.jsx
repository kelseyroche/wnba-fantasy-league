import React, { useState, useContext } from 'react';
import { AuthContext } from '../../context/AuthContext';
import { Form, Button } from 'semantic-ui-react';
import axios from 'axios';
import Navbar from '../common/NavBar';
import Footer from '../common/Footer';
import './EditProfile.css'; // Import your updated CSS

const EditProfile = () => {
  const { user, setUser } = useContext(AuthContext);
  const [username, setUsername] = useState(user?.username || '');
  const [email, setEmail] = useState(user?.email || '');
  const [currentPassword, setCurrentPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5555/edit_profile', {
        username,
        email,
        current_password: currentPassword,
        new_password: newPassword,
      });
      setUser(response.data.user);
      alert('Profile updated successfully!');
    } catch (error) {
      console.error('Error updating profile:', error);
      alert('Failed to update profile.');
    }
  };

  return (
    <div>
      <Navbar />
      <div className="centered-container">
        <h2>Edit Profile</h2>
        <Form onSubmit={handleSubmit} className="centered-form">
          <Form.Input
            label="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <Form.Input
            label="Email"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <Form.Input
            label="Current Password"
            type="password"
            value={currentPassword}
            onChange={(e) => setCurrentPassword(e.target.value)}
          />
          <Form.Input
            label="New Password"
            type="password"
            value={newPassword}
            onChange={(e) => setNewPassword(e.target.value)}
          />
          <Button type="submit" primary>
            Update Profile
          </Button>
        </Form>
      </div>
      <Footer />
    </div>
  );
};

export default EditProfile;
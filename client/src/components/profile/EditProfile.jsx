import React, { useState, useContext } from 'react';
import { AuthContext } from '../../context/AuthContext';
import { Container, Form, Button } from 'semantic-ui-react';
import axios from 'axios';

const EditProfile = () => {
  const { user, setUser } = useContext(AuthContext);
  const [username, setUsername] = useState(user?.username || '');
  const [email, setEmail] = useState(user?.email || '');
  const [currentPassword, setCurrentPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/edit_profile', {
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
    <Container>
      <h2>Edit Profile</h2>
      <Form onSubmit={handleSubmit}>
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
    </Container>
  );
};

export default EditProfile;
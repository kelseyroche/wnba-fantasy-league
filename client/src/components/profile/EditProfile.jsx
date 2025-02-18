import React, { useState, useContext } from 'react';
import { AuthContext } from '../../context/AuthContext';
import { Form, Button } from 'semantic-ui-react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import Navbar from '../common/NavBar';
import Footer from '../common/Footer';
import './EditProfile.css';

const EditProfile = () => {
  const { user, setUser } = useContext(AuthContext);
  const [username, setUsername] = useState(user?.username || '');
  const [email, setEmail] = useState(user?.email || '');
  const [currentPassword, setCurrentPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(`${import.meta.env.VITE_API_URL}/edit_profile`, {
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


const handleDeleteAccount = async () => {
    if (window.confirm('Are you sure you want to delete your account? This action cannot be undone.')) {
      try {
        const response = await axios.delete(`${import.meta.env.VITE_API_URL}/delete_account`, {
          withCredentials: true,
        });
        alert(response.data.message);
        setUser(null); 
  
        navigate('/');
      } catch (error) {
        console.error('Error deleting account:', error);
        alert('There was an error deleting your account.');
      }
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
          <Button type="submit" className="update-profile-button" style={{ backgroundColor: '#FF8640', color: 'white' }}>
            Update Profile
          </Button>
          <Button type="button" className="delete-account-button" onClick={handleDeleteAccount} style={{ backgroundColor: '#471B94', color: 'white', marginLeft: '10px' }}>
            Delete Account
          </Button>
        </Form>
      </div>
      <Footer />
    </div>
  );
};

export default EditProfile;
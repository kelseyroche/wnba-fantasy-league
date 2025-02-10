import React, { useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { AuthContext } from '../../context/AuthContext';
import { Form, Button, Container, Header, Message } from 'semantic-ui-react';
import './LoginRegister.css'; // Import the CSS file
import backgroundImage from '../../assets/background_1.jpg'; // Ensure path is correct

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const { login } = useContext(AuthContext);
  const navigate = useNavigate();
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);

    try {
      await login(email, password);
      navigate('/dashboard');
    } catch (error) {
      setError("Login failed. Please check your email and password.");
    }
  };

  return (
    <div
      className="auth-container"
      style={{
        backgroundImage: `url(${backgroundImage})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat',
        height: '100vh',
        width: '100vw'
      }}
    >
      <Container className="auth-container">
        <Header as="h2" className="auth-header">Login</Header>
        <Form className="auth-form" onSubmit={handleSubmit}>
          <Form.Input
            label="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <Form.Input
            label="Password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <Button type="submit" className="auth-button">Login</Button>
        </Form>

        {error && <Message negative className="auth-message">{error}</Message>}
      </Container>
    </div>
  );
}

export default Login;
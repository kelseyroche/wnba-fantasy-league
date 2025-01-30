import React, { useState, useContext } from 'react';
import { useHistory } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';
import { Form, Button, Message, Container, Header } from 'semantic-ui-react';

function Login() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const { login } = useContext(AuthContext); // Access login function from context
    const history = useHistory();

    const handleSubmit = async (event) => {
        event.preventDefault();
        setError('');

        try {
            const response = await fetch('http://localhost:5555/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email, password }),
            });

            if (response.ok) {
                const data = await response.json();
                login(); // Update the authentication state
                history.push('/team-dashboard'); // Redirect to team dashboard
            } else {
                const errorData = await response.json();
                setError(errorData.error || 'Failed to log in');
            }
        } catch (err) {
            setError('An error occurred. Please try again.');
        }
    };

    return (
        <Container text>
            <Header as='h2' textAlign='center'>Login</Header>
            {error && <Message negative>{error}</Message>}
            <Form onSubmit={handleSubmit}>
                <Form.Field>
                    <label htmlFor="email">Email:</label>
                    <input
                        type="email"
                        id="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </Form.Field>
                <Form.Field>
                    <label htmlFor="password">Password:</label>
                    <input
                        type="password"
                        id="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </Form.Field>
                <Button type="submit" primary fluid>
                    Login
                </Button>
            </Form>
        </Container>
    );
}

export default Login;
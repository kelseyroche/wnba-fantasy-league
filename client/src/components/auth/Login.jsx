// import React, { useState, useContext } from 'react';
//    import { useNavigate } from 'react-router-dom'; // Updated import
//    import { AuthContext } from '../../context/AuthContext';
//    import { Form, Button, Message, Container, Header } from 'semantic-ui-react';

//    function Login() {
//      const [email, setEmail] = useState('');
//      const [password, setPassword] = useState('');
//      const { login } = useContext(AuthContext);
//      const navigate = useNavigate(); // Updated hook

//      const handleSubmit = async (e) => {
//        e.preventDefault();
//        try {
//          await login(email, password);
//          navigate('/dashboard'); // Use navigate instead of history.push
//        } catch (error) {
//          console.error("Login failed", error);
//        }
//      };

//      return (
//        <Container>
//          <Header as="h2">Login</Header>
//          <Form onSubmit={handleSubmit}>
//            <Form.Input
//              label="Email"
//              value={email}
//              onChange={(e) => setEmail(e.target.value)}
//            />
//            <Form.Input
//              label="Password"
//              type="password"
//              value={password}
//              onChange={(e) => setPassword(e.target.value)}
//            />
//            <Button type="submit">Login</Button>
//          </Form>
//        </Container>
//      );
//    }

//    export default Login;

import React, { useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { AuthContext } from '../../context/AuthContext';  // Check this path

import { Form, Button, Container, Header } from 'semantic-ui-react';

function Login() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const auth = useContext(AuthContext);

    if (!auth) {
        console.error("AuthContext is undefined. Make sure AuthProvider wraps the app.");
        return <p>Error: AuthContext is not available.</p>;
    }

    const { login } = auth;
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await login(email, password);
            navigate('/dashboard');
        } catch (error) {
            console.error("Login failed", error);
        }
    };

    return (
        <Container>
            <Header as="h2">Login</Header>
            <Form onSubmit={handleSubmit}>
                <Form.Input
                    label="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <Form.Input
                    label="Password"
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <Button type="submit">Login</Button>
            </Form>
        </Container>
    );
}

export default Login;
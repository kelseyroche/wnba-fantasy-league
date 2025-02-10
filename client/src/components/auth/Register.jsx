// import React, { useState } from 'react';
// import { useNavigate } from 'react-router-dom';
// import { Form, Button, Container, Header, Message } from 'semantic-ui-react';

// function Register() {
//   const [username, setUsername] = useState('');
//   const [email, setEmail] = useState('');
//   const [password, setPassword] = useState('');
//   const [error, setError] = useState(null);
//   const [success, setSuccess] = useState(false);
//   const navigate = useNavigate();

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     setError(null);
//     setSuccess(false);

//     try {
//       const response = await fetch('http://127.0.0.1:5555/register', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//           'Accept': 'application/json'
//         },
//         credentials: 'include', 
//       });

//       const data = await response.json();

//       if (!response.ok) {
//         throw new Error(data.error || 'Registration failed');
//       }

//       setSuccess(true);
//       setTimeout(() => navigate('/dashboard'), 1000);
//     } catch (error) {
//       setError(error.message);
//     }
//   };

//   return (
//     <Container>
//       <Header as="h2">Register</Header>
//       <Form onSubmit={handleSubmit}>
//         <Form.Input
//           label="Username"
//           value={username}
//           onChange={(e) => setUsername(e.target.value)}
//           required
//         />
//         <Form.Input
//           label="Email"
//           value={email}
//           onChange={(e) => setEmail(e.target.value)}
//           type="email"
//           required
//         />
//         <Form.Input
//           label="Password"
//           type="password"
//           value={password}
//           onChange={(e) => setPassword(e.target.value)}
//           required
//         />
//         <Button type="submit" primary>
//           Register
//         </Button>
//       </Form>

//       {error && <Message negative>{error}</Message>}
//       {success && <Message positive>Registration successful! Redirecting...</Message>}
//     </Container>
//   );
// }

// export default Register;

import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Form, Button, Container, Header, Message } from 'semantic-ui-react';

function Register() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setSuccess(false);

    console.log("Registering user:", { username, email, password }); // Log the data being sent

    try {
      const response = await fetch('http://127.0.0.1:5555/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        credentials: 'include',
        body: JSON.stringify({ username, email, password }) // Ensure body is included
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || 'Registration failed');
      }

      setSuccess(true);
      console.log("Registration successful:", data); // Log success response
      setTimeout(() => navigate('/dashboard'), 1000);
    } catch (error) {
      console.error("Error during registration:", error); // Log any errors
      setError(error.message);
    }
  };

  return (
    <Container>
      <Header as="h2">Register</Header>
      <Form onSubmit={handleSubmit}>
        <Form.Input
          label="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <Form.Input
          label="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          type="email"
          required
        />
        <Form.Input
          label="Password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <Button type="submit" primary>
          Register
        </Button>
      </Form>

      {error && <Message negative>{error}</Message>}
      {success && <Message positive>Registration successful! Redirecting...</Message>}
    </Container>
  );
}

export default Register;
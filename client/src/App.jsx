import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
// import 'fomantic-ui-css/semantic.min.css';


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        {/* <TeamsList />  */}
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App

// import React, { useState } from 'react';
//    import { BrowserRouter as Router, Route, Switch, Redirect } from 'react-router-dom';
//    import LandingPage from './components/LandingPage';
//    import SignUp from './components/SignUp';
//    import Login from './components/Login';
//    import TeamDashboard from './components/TeamDashboard';
//    import TransferPortal from './components/TransferPortal';
//    import Leaderboard from './components/Leaderboard';
//    import Profile from './components/Profile';
//    import 'fomantic-ui-css/semantic.min.css';


//    function App() {
//        const [isAuthenticated, setIsAuthenticated] = useState(false);

//        const PrivateRoute = ({ component: Component, ...rest }) => (
//            <Route {...rest} render={(props) => (
//                isAuthenticated
//                    ? <Component {...props} />
//                    : <Redirect to='/login' />
//            )} />
//        );

//        return (
//            <Router>
//                <Switch>
//                    <Route path="/" exact component={LandingPage} />
//                    <Route path="/signup" component={SignUp} />
//                    <Route path="/login" component={Login} />
//                    <PrivateRoute path="/team-dashboard" component={TeamDashboard} />
//                    <PrivateRoute path="/transfer-portal" component={TransferPortal} />
//                    <PrivateRoute path="/leaderboard" component={Leaderboard} />
//                    <PrivateRoute path="/profile" component={Profile} />
//                    <Redirect to="/" />
//                </Switch>
//            </Router>
//        );
//    }

//    export default App;

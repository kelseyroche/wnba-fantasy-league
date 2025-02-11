
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import ProtectedRoute from './components/common/ProtectedRoute';
import LandingPage from './components/LandingPage';
import Login from './components/auth/Login';
import Register from './components/auth/Register';
import Dashboard from './components/dashboard/Dashboard';
import Leaderboard from './components/leaderboard/Leaderboard';
import EditProfile from './components/profile/EditProfile';
import TeamRoster from './components/roster/TeamRoster';
import AdminUpdateScore from './components/admin/AdminUpdateScore'; // Adjust path as necessary




function App() {
  return (
  <Router>
      <AuthProvider>
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Register />} />
          <Route path="/dashboard" element={<ProtectedRoute component={Dashboard} />} />
          <Route path="/leaderboard" element={<ProtectedRoute component={Leaderboard} />} />
          <Route path="/team-roster" element={<ProtectedRoute component={TeamRoster} />} />
          <Route path="/edit-profile" element={<ProtectedRoute component={EditProfile} />} />
          {/* <Route path="/admin" component={AdminUpdateScore} /> */}
          <Route path="/admin" element={<AdminUpdateScore />} />
        </Routes>
      </AuthProvider>
    </Router>
  );
}

export default App;
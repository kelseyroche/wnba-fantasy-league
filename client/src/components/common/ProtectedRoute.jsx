import React, { useContext } from 'react';
import { Navigate } from 'react-router-dom';
import { AuthContext } from '../../context/AuthContext';

function ProtectedRoute({ component: Component }) {
    const { user, loading } = useContext(AuthContext);

    if (loading) {
        return <div>Loading...</div>;
    }

    return user ? <Component /> : <Navigate to="/" />;
}

export default ProtectedRoute;
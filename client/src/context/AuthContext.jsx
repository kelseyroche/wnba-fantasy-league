import React, { createContext, useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { api } from '../utils/api';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const navigate = useNavigate();

    useEffect(() => {
        // Example: Check if user is already logged in
        api.get('/check_session')
            .then(response => {
                setUser(response.data.user);
                setLoading(false);
            })
            .catch(() => {
                setLoading(false);
                setUser(null);
            });
    }, []);

    const login = async (email, password) => {
        try {
            const response = await api.post('/login', { email, password });
            setUser(response.data.user);
            navigate('/dashboard');
        } catch (error) {
            console.error("Login failed", error);
        }
    };

    const logout = () => {
        api.post('/logout').then(() => {
            setUser(null);
            navigate('/');
        });
    };

    return (
        <AuthContext.Provider value={{ user, login, logout, loading }}>
            {children}
        </AuthContext.Provider>
    );
};
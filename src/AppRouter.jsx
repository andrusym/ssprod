import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Journal from './pages/Journal';
import StrategyConfig from './pages/StrategyConfig';
import WealthConfig from './pages/WealthConfig';
import AdminPanel from './pages/AdminPanel';
import LoginPage from './LoginPage';
import ProtectedRoute from './ProtectedRoute';
import { useAuth } from './AuthContext';
import Layout from './components/Layout';

const AppRouter = () => {
  const { user } = useAuth();

  return (
    <Router>
      <Routes>
        {/* Public Route */}
        <Route path="/login" element={<LoginPage />} />

        {/* Protected Routes with Layout */}
        <Route
          path="/"
          element={
            <ProtectedRoute isAuthenticated={!!user}>
              <Layout />
            </ProtectedRoute>
          }
        >
          <Route path="dashboard" element={<Dashboard />} />
          <Route path="journal" element={<Journal />} />
          <Route path="config/strategies" element={<StrategyConfig />} />
          <Route path="config/wealth" element={<WealthConfig />} />
          <Route path="admin" element={<AdminPanel />} />
          <Route index element={<Navigate to="/dashboard" replace />} />
        </Route>
      </Routes>
    </Router>
  );
};

export default AppRouter;
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Dashboard from './Dashboard';
import Journal from './Journal';
import LoginPage from './LoginPage';
import PerformanceSummary from './PerformanceSummary';
import Layout from './components/Layout';
import TradeJournalEditor from './components/TradeJournalEditor';
import ProtectedRoute from './ProtectedRoute';
import { AuthProvider, useAuth } from './AuthContext';

const AppRoutes = () => {
  const { user } = useAuth();

  return (
    <Routes>
      <Route path="/login" element={<LoginPage />} />
      <Route
        path="/dashboard"
        element={
          <ProtectedRoute isAuthenticated={!!user}>
            <Layout>
              <Dashboard />
            </Layout>
          </ProtectedRoute>
        }
      />
      
      <Route path="/summary" element={
        <ProtectedRoute isAuthenticated={!!user}>
          <Layout>
            <PerformanceSummary />
          </Layout>
        </ProtectedRoute>
      } />
      <Route path="/editor" element={
        <ProtectedRoute isAuthenticated={!!user}>
          <Layout>
            <TradeJournalEditor />
          </Layout>
        </ProtectedRoute>
      } />
    <Route path="*" element={<Navigate to="/dashboard" />} />
    </Routes>
  );
};

const AppRouter = () => (
  <AuthProvider>
    <Router>
      <AppRoutes />
    </Router>
  </AuthProvider>
);

export default AppRouter;

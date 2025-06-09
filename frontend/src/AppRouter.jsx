import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Dashboard from './Dashboard';
import Journal from './Journal';
import LoginPage from './LoginPage';
import PerformanceSummary from './PerformanceSummary';
import Layout from './components/Layout';
import SetupPage from './pages/SetupPage.jsx';
import ConfigPage from './pages/ConfigPage.jsx';
import AdminPanel from './pages/AdminPanel.jsx';
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
        <Route path="/setup" element={
          <ProtectedRoute isAuthenticated={true}>
            <Layout><SetupPage /></Layout>
          </ProtectedRoute>
        } />
        <Route path="/config" element={
          <ProtectedRoute isAuthenticated={true}>
            <Layout><ConfigPage /></Layout>
          </ProtectedRoute>
        } />
        <Route path="/admin" element={
          <ProtectedRoute isAuthenticated={true}>
            <Layout><AdminPanel /></Layout>
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

import { Link } from 'react-router-dom';

const Sidebar = () => {
  return (
    <div
      style={{
        height: '100vh',
        width: '220px',
        background: '#111',
        color: '#fff',
        padding: '20px',
        position: 'fixed',
        top: 0,
        left: 0,
      }}
    >
      <h3 style={{ color: '#00bfff', marginBottom: '24px' }}>SkyStrike</h3>
      <nav>
        <ul style={{ listStyle: 'none', padding: 0 }}>
          <li style={{ marginBottom: '12px' }}>
            <Link to="/dashboard" style={{ color: '#fff', textDecoration: 'none' }}>Dashboard</Link>
          </li>
          <li style={{ marginBottom: '12px' }}>
            <Link to="/journal" style={{ color: '#fff', textDecoration: 'none' }}>Journal</Link>
          </li>
          <li style={{ marginBottom: '12px' }}>
            <Link to="/performance" style={{ color: '#fff', textDecoration: 'none' }}>Performance</Link>
          </li>
          <li style={{ marginBottom: '12px' }}>
            <Link to="/strategies" style={{ color: '#fff', textDecoration: 'none' }}>Strategies</Link>
          </li>
          <li style={{ marginTop: '32px' }}>
            <Link to="/login" style={{ color: '#aaa', textDecoration: 'none' }}>Logout</Link>
          </li>
        </ul>
      </nav>
    </div>
  );
};

export default Sidebar;

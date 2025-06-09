import React from 'react';
import { Link } from 'react-router-dom';
import './Sidebar.css';

const Sidebar = () => {
  return (
    <div className="sidebar">
      <h2>SkyStrike</h2>
      <ul>
        <li><Link to="/dashboard">Dashboard</Link></li>
        <li><Link to="/journal">Journal</Link></li>
        <li><Link to="/config/strategies">Strategy Config</Link></li>
        <li><Link to="/config/wealth">Wealth Engine</Link></li>
        <li><Link to="/admin">Admin Panel</Link></li>
      </ul>
    </div>
  );
};

export default Sidebar;
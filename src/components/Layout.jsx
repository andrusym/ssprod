import React from 'react';
import { Outlet } from 'react-router-dom';
import Sidebar from './Sidebar';
import ThemeToggle from './ThemeToggle';

const Layout = () => {
  return (
    <div className="app-layout">
      <Sidebar />
      <div className="main-content">
        <ThemeToggle />
        <Outlet />
      </div>
    </div>
  );
};

export default Layout;
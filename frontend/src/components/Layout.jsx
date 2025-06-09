import Sidebar from "./Sidebar";
import ThemeToggle from "./ThemeToggle";

const Layout = ({ children }) => {
  return (
    <div className="layout">
      <Sidebar />
      <div className="main-content">
        <div className="top-bar">
          <ThemeToggle />
        </div>
        <div className="page-content">
          {children}
        </div>
      </div>
    </div>
  );
};

export default Layout;

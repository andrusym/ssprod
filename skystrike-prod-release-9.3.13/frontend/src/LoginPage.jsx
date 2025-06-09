import React, { useContext } from "react";
import { ThemeContext } from "./components/ThemeToggle";
import ThemeToggle from "./components/ThemeToggle";
import lightLogo from "./assets/skystrike-logo-light.png";
import darkLogo from "./assets/skystrike-logo-dark.png";

const LoginPage = () => {
  const { theme } = useContext(ThemeContext);
  const logo = theme === "dark" ? darkLogo : lightLogo;

  return (
    <div className={`login-page ${theme}`}>
      <div className="login-container">
        <div className="top-bar">
          <ThemeToggle />
        </div>
        <img src={logo} alt="SkyStrike Logo" className="logo" />
        <h2>Welcome to SkyStrike</h2>
        <div className="login-form">
          <input type="text" placeholder="Enter username" />
          <input type="password" placeholder="Enter password" />
        </div>
        <button className="login-button">Login</button>
      </div>
    </div>
  );
};

export default LoginPage;

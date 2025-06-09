import Sidebar from "./components/Sidebar";
;

const Dashboard = () => {
  return (
    <div style={{ display: 'flex' }}>
      <Sidebar />
      <div style={{ marginLeft: '220px', padding: '20px', width: '100%' }}>
        <h2>Dashboard</h2>
        <p>Welcome to the SkyStrike dashboard.</p>
      </div>
    </div>
  );
};

export default Dashboard;

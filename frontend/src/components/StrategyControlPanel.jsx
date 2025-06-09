
const StrategyControlPanel = ({ onPause, onResume }) => {
  return (
    <div className="strategy-controls">
      <button onClick={onPause}>Pause</button>
      <button onClick={onResume}>Resume</button>
    </div>
  );
};

export default StrategyControlPanel;
import React from 'react';

const BacktestOverlay = ({ data }) => {
  return (
    <div className="backtest-overlay">
      <h4>Backtest Results</h4>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
};

export default BacktestOverlay;
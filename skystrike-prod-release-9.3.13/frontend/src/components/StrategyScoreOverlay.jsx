import React from 'react';

const StrategyScoreOverlay = ({ score }) => {
  return (
    <div className="strategy-score-overlay">
      <h5>ML Score: {score}</h5>
    </div>
  );
};

export default StrategyScoreOverlay;
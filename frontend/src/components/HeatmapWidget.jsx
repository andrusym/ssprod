
const HeatmapWidget = ({ heatmap }) => {
  return (
    <div className="heatmap-widget">
      <h4>Strategy Heatmap</h4>
      <pre>{JSON.stringify(heatmap, null, 2)}</pre>
    </div>
  );
};

export default HeatmapWidget;
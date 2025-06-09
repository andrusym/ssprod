
const ConfigPage = () => {
  const [settings, setSettings] = useState([
    { key: 'autoRetry', label: 'Auto Retry Failed Trades', enabled: true },
    { key: 'mlScoring', label: 'Enable ML Scoring', enabled: false },
    { key: 'drawdownProtect', label: 'Drawdown Protection', enabled: true },
  ]);

  const handleToggle = (key) => {
    const updated = settings.map(item =>
      item.key === key ? { ...item, enabled: !item.enabled } : item
    );
    setSettings(updated);
  };

  return (
    <div className="config-panel">
      <h2>Platform Configuration</h2>
      {settings.map((item) => (
        <div key={item.key}>
          <label>{item.label}</label>
          <input
            type="checkbox"
            checked={item.enabled}
            onChange={() => handleToggle(item.key)}
          />
        </div>
      ))}
    </div>
  );
};

export default ConfigPage;

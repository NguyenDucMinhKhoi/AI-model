import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState({ temperature: null, heartRate: null });
  const [loading, setLoading] = useState(false);

  const handleMeasure = async () => {
    setLoading(true);
    try {
      const result = await axios.get('http://your-esp8266-ip/measure');
      setData(result.data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
    setLoading(false);
  };

  return (
    <div>
      <h1>Dog Health Monitor</h1>
      <button onClick={handleMeasure} disabled={loading}>
        {loading ? 'Measuring...' : 'Measure'}
      </button>
      {data.temperature !== null && data.heartRate !== null && (
        <div>
          <p>Temperature: {data.temperature} °C</p>
          <p>Heart Rate: {data.heartRate} bpm</p>
        </div>
      )}
    </div>
  );
}

export default App;

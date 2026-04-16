import React, { useState } from 'react';

function PhishScanner() {
  const [url, setUrl] = useState('');
  const [result, setResult] = useState(null);

  const checkUrl = async () => {
    const response = await fetch('http://localhost:5000/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ url: url })
    });
    const data = await response.json();
    setResult(data.status);
  };

  return (
    <div style={{ padding: '20px', textAlign: 'center' }}>
      <h2>AI Phishing Detector</h2>
      <input 
        type="text" 
        placeholder="Enter URL to scan..." 
        onChange={(e) => setUrl(e.target.value)} 
      />
      <button onClick={checkUrl}>Scan Now</button>
      {result && <h3 style={{color: result === 'Safe' ? 'green' : 'red'}}>Result: {result}</h3>}
    </div>
  );
}
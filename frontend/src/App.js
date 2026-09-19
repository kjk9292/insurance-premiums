import './App.css';
import React, { useState } from 'react';
import { Bar } from 'react-chartjs-2';
import { fetchInsuranceData } from './api.js'; 
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend
} from 'chart.js';

ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend
);

function formatChartData(rawData) {
    const state = rawData[0].state;

    return {
        labels: ['Collision', 'Comprehensive', 'Liability'],
        datasets: [
            {
                label: '2021',
                data: rawData.filter(d => d.year === 2021).map(d => d.premium),
                backgroundColor: 'rgba(66, 133, 244, 0.8)'
            },
            {
                label: '2022',
                data: rawData.filter(d => d.year === 2022).map(d => d.premium),
                backgroundColor: 'rgba(234, 67, 53, 0.8)'
            },
            {
                label: '2023',
                data: rawData.filter(d => d.year === 2023).map(d => d.premium),
                backgroundColor: 'rgba(251, 188, 4, 0.8)' 
            }
        ],
        title: state
    }
}

function App() {
  const [zip, setZip] = useState('');
  const [data, setData] = useState(null);

  async function handleSubmit() {
    if (!/^\d{5}$/.test(zip)) {
        setData('invalid');
        return;
    }
    const result = await fetchInsuranceData(zip);
    if (result.length === 0) {
        setData('invalid');
        return;
    }
    const formatted = formatChartData(result);
    setData(formatted);
  }
  
  return (
    <div className="app-container">
        <h1 className="app-title">Insurance Premium Lookup</h1>
        <div className="search-section">
            <input 
              className="zip-input" 
              value={zip} 
              onChange={e => setZip(e.target.value)}
              onKeyDown={e => e.key === 'Enter' && handleSubmit()}
            />
            <button className="search-button" onClick={handleSubmit}>Search</button>
        </div>
        {data === 'invalid' && <p>Invalid zip code. Please try again.</p>}
        <div className={data && data !== 'invalid' ? "chart-section" : ""}>
            {data && data !== 'invalid' && <Bar 
                data={data} 
                  options={{
                    plugins: {
                        title: {
                            display: true,
                            text: 'Insurance Premiums for ' + data.title,
                            font: {
                                size: 25
                            }
                        },
                        legend: {
                            labels: {
                                font: {
                                    size: 15
                                }
                            }
                        }
                    },
                    scales: {
                        x: {
                            ticks: {
                                font: {
                                    size: 20
                                }
                            }
                        },
                        y: {
                            ticks: {
                                font: {
                                    size: 20
                                }
                            }
                        }
                    }
                    }}
            />}
        </div>
    </div>
  );
}

export default App;

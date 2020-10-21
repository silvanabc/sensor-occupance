import React, { useState } from 'react';
import './App.css';

function App() {
  const [selectedSensor, setSelectedSensor] = useState(1);
  const [occupanceSensor, setOccupanceSensor] = useState({});


  const showError = () => {
    alert('Error in retrieving information of Sensor ' + selectedSensor);
  }

  const showOccupance = () => {
    //request and set occupance
    fetch('/api/occupance/' + selectedSensor)
    .then(res => {
      if (!res.ok){
        throw new Error()
      }
      return res.json()
    })
    .then(
      result => {
        if(result.inside != null){
          setOccupanceSensor({
            id: selectedSensor,
            peopleInside: result.inside
          })
        }else{
          showError();
        }      
      },
      error => {
        showError();
      }
    )
      
  };

  let handleChange = (e) => {
    setSelectedSensor(e.target.value)
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>Meeting Room Occupance</h1>
      </header>
      
      <section className="Main-Section">
        <div>
          <span>Select a Sensor: </span>
          <select value={selectedSensor} onChange={handleChange}>
            <option value="1">Sensor 1</option>
            <option value="2">Sensor 2</option>
            <option value="3">Sensor 3</option>
            <option value="4">Sensor 4</option>
          </select>
        </div>

        
        <button onClick={showOccupance}>Show Occupance</button>


        <div className={occupanceSensor.id == null ? 'hidden': ''}>
          <div className="Sensor-Occupance">
            Sensor {occupanceSensor.id} reports room occupance of {occupanceSensor.peopleInside} people.
          </div>
        </div>
        
      </section>

    </div>
  );
}

export default App;

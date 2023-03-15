import React, { useState } from 'react';
import { Input } from 'antd';

const { TextArea } = Input;

function App() {
  const [inputValue, setInputValue] = useState('');
  const [outputValue, setOutputValue] = useState('');

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  }

  const handleButtonClick = () => {
    // const processedValue = inputValue.toUpperCase();

    // Update output value
    setOutputValue(inputValue);
  }

  return (
    <div style={{ padding: '20px' }}>
      <Input placeholder="Input your text here" onChange={handleInputChange} />
      <br /><br />
      <button onClick={handleButtonClick}>Process</button>
      <br /><br />
      <TextArea value={outputValue} rows={6} />
    </div>
  );
}

export default App;

import React, { useState } from 'react';

function DynamicButtonList() {
  const [buttons, setButtons] = useState([]);

  // Function to add a new button
  const addNewButton = () => {
    const newButton = {
      label: `Button ${buttons.length + 1}`,
      onClick: () => {
        alert(`Button ${buttons.length + 1} clicked`);
      },
    };
    setButtons([...buttons, newButton]);
  };

  // Function to remove the last button
  const removeLastButton = () => {
    if (buttons.length > 0) {
      const newButtons = [...buttons];
      newButtons.pop();
      setButtons(newButtons);
    }
  };

  return (
    <div>
      <button onClick={addNewButton}>Add Button</button>
      <button onClick={removeLastButton}>Remove Last Button</button>
      <div>
        {buttons.map((button, index) => (
          <button key={index} onClick={button.onClick}>
            {button.label}
          </button>
        ))}
      </div>
    </div>
  );
}

export default DynamicButtonList;

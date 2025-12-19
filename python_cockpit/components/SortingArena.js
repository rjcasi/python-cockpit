import React, { useState, useEffect } from "react";

const SortingArena = () => {
  const [array, setArray] = useState([5, 3, 8, 4, 2, 7, 1, 6]);
  const [steps, setSteps] = useState([]);
  const [currentStep, setCurrentStep] = useState(0);

  // Bubble sort animation
  useEffect(() => {
    let arr = [...array];
    let tempSteps = [];
    for (let i = 0; i < arr.length; i++) {
      for (let j = 0; j < arr.length - i - 1; j++) {
        if (arr[j] > arr[j + 1]) {
          [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
          tempSteps.push([...arr]);
        }
      }
    }
    setSteps(tempSteps);
  }, []);

  useEffect(() => {
    if (steps.length > 0 && currentStep < steps.length) {
      const timer = setTimeout(() => {
        setArray(steps[currentStep]);
        setCurrentStep(currentStep + 1);
      }, 500);
      return () => clearTimeout(timer);
    }
  }, [steps, currentStep]);

  return (
    <div>
      <h2>Sorting Arena (Bubble Sort)</h2>
      <div style={{ display: "flex", gap: "5px" }}>
        {array.map((val, idx) => (
          <div
            key={idx}
            style={{
              height: `${val * 20}px`,
              width: "20px",
              backgroundColor: "teal",
            }}
          ></div>
        ))}
      </div>
    </div>
  );
};

export default SortingArena;
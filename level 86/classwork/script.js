function calculate() {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const operation = document.getElementById('operation').value;
    let result;
  
    if (isNaN(num1) || isNaN(num2)) {
      result = 'Please enter valid numbers';
    } else {
      if (operation === 'add') {
        result = num1 + num2;
      } else if (operation === 'subtract') {
        result = num1 - num2;
      } else if (operation === 'multiply') {
        result = num1 * num2;
      } else if (operation === 'divide') {
        result = num2 !== 0 ? num1 / num2 : 'Error: Division by zero is not allowed';
      } else {
        result = 'Invalid operation';
      }
    }
  
    document.getElementById('result').textContent = `Result: ${result}`;
  }
  
  function checkEvenOdd() {
    const num = parseInt(document.getElementById('checkNumber').value);
    if (isNaN(num)) {
      document.getElementById('evenOddResult').textContent = 'Please enter a valid number';
      return;
    }
  
    const result = num % 2 === 0 ? 'This number is even' : 'This number is odd';
    document.getElementById('evenOddResult').textContent = result;
  }
  
  function squareNumber() {
    const num = parseFloat(document.getElementById('checkNumber').value);
    if (isNaN(num)) {
      document.getElementById('squareResult').textContent = 'Please enter a valid number';
      return;
    }
  
    const result = num * num;
    document.getElementById('squareResult').textContent = `Square: ${result}`;
  }
  
  function checkNumberSign() {
    const num = parseFloat(document.getElementById('checkNumber').value);
    if (isNaN(num)) {
      document.getElementById('signResult').textContent = 'Please enter a valid number';
      return;
    }
  
    let result;
    if (num > 0) {
      result = 'The number is positive';
    } else if (num < 0) {
      result = 'The number is negative';
    } else {
      result = 'The number is zero';
    }
  
    document.getElementById('signResult').textContent = result;
  }
  
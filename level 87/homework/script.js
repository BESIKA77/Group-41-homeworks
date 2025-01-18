// 1. Sum of numbers from 1 to 10
let sum = 0;
for (let i = 1; i <= 10; i++) {
  sum += i;
}
console.log(`საბოლო რიცხვების ჯამი არის ${sum}`);

// 2. Square of numbers from 1 to 10
for (let i = 1; i <= 10; i++) {
  console.log(`${i} - ის კვადრატი არის ${i * i}`);
}

// 3. Print each character of a string
const str = "გამარჯობა";
for (let i = 0; i < str.length; i++) {
  console.log(str[i]);
}

// 4. FizzBuzz program
for (let i = 1; i <= 100; i++) {
  if (i % 3 === 0 && i % 5 === 0) {
    console.log("FizzBuzz");
  } else if (i % 3 === 0) {
    console.log("Fizz");
  } else if (i % 5 === 0) {
    console.log("Buzz");
  } else {
    console.log(i);
  }
}

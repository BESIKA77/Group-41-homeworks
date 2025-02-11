let car = {
    brand: "Toyota",
    model: "Corolla",
    year: 2020,
    color: "Black",
    weight: "1300kg",
    
    getInfo: function() {
        return `ამ მანქანის ბრენდია ${this.brand}, კონკრეტული მოდელია ${this.model}, გამოშვების წელი არის ${this.year}, ფერი არის ${this.color}, ხოლო წონა - ${this.weight}.`;
    }
};

console.log(car.getInfo());
console.log(car.brand);
console.log(car.model);
console.log(car.year);
console.log(car.color);
console.log(car.weight);

car.brand = "BMW";
car.model = "X5";
car.year = 2022;
car.color = "White";
car.weight = "2000kg";

console.log(car.getInfo());

car.mode = "Automatic";
console.log(car);


delete car.mode;
console.log(car);

let myCarBrand = "BMW";
if (car.brand === myCarBrand) {
    console.log("იგივე მანქანის ბრენდი გვყოლია ძმობილო");
} else {
    console.log("სხვადასხვა მანქანის ბრენდია, ჩემი მოუგებს");
}

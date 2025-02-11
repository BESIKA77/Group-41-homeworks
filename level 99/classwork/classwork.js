const person = {
    firstName: "ბესო",
    lastName: "გელხაური",
    age: 15,
    height: 160,
    city: "თბილისი",
    mother: {
        firstName: "ნინო",
        lastName: "ალანია",
        age: 33,
        height: 170,
        city: "თბილისი"
    },
    father: {
        firstName: "ბექა",
        lastName: "გელხაური",
        age: 35,
        height: 165,
        city: "თბილისი"
    },
    sibling: {
        firstName: "დანიელი",
        lastName: "იასაღაშვილი",
        age: 4,
        height: 110,
        city: "თბილისი"
    }
};

// ობიექტის მონაცემების გამოტანა
console.log(person);
console.log(`დედა: ${person.mother.firstName}, ასაკი: ${person.mother.age}`);
console.log(`მამა: ${person.father.firstName}, ასაკი: ${person.father.age}`);
console.log(`და-ძმა: ${person.sibling.firstName}, ასაკი: ${person.sibling.age}`);

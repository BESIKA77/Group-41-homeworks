const academy = {
    name: "Goal-Oriented-Academy(GOA)",
    courses: ["JavaScript", "Python", "Web Development"],
    socialLink: "https://GOA academy.com",
    reviews: {
        user1: { name: "besika", status: "chilf", review: "მომავალი მენტორია ეს ბიჭი! დდ" },
        user2: { name: "დავითი", status: "mentor", review: "G.O.A.T" },
        user3: { name: "nino", status: "parent", review: "good parent" }
    }
};


console.log(Object.keys(academy));

console.log(Object.values(academy));

console.log(academy.hasOwnProperty("courses"));
console.log(academy.hasOwnProperty("members"));

const additionalInfo = {
    members: 1500
};

const mergedAcademy = Object.assign({}, academy, additionalInfo);
console.log(mergedAcademy);

Object.freeze(mergedAcademy);

console.log(Object.isFrozen(mergedAcademy));


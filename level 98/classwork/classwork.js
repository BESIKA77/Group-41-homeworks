function User(name, lastName, phoneNumber, email, password, confirmPassword) {
    this.name = name;
    this.lastName = lastName;
    this.phoneNumber = phoneNumber;
    this.email = email;
    this.password = password;
    this.confirmPassword = confirmPassword;

    this.introduce = function() {
        return `ჩემი სახელია ${this.name}, ჩემი გვარია ${this.lastName}, ჩემი ტელეფონის ნომერია ${this.phoneNumber}, ჩემი ელფოსტაა ${this.email}.`;
    };
}

const user1 = new User("ბესიკა", "გელხაური", "571 05 10 61", "besogelxauri77", "პასვორდი7", "პასვორდი7");
const user2 = new User("ნინო", "ალანია", "568 61 01 05", "alanianino77", "მელიაკუდიგრძელია8383", "მელიაკუდიგრძელია8383");
const user3 = new User("ლევანა", "აბაშიძე", "555 83 91 33", "kaikaci_levana99", "ჭიანჭველა888", "ჭიანჭველა888");

console.log(user1.introduce());
console.log(user2.introduce());
console.log(user3.introduce());

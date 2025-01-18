const password = 'Group 41 is best';

function guessPassword() {
    let attempts = 3;

    while (attempts > 0) {
        const userInput = prompt('შეიყვანეთ პაროლი:');
        
        if (userInput === password) {
            alert('თქვენი შეყვანილი პაროლი სწორია');
            return;
        } else {
            attempts--; 
            alert(`არასწორი პაროლი. დარჩენილია ${attempts} ცდა.`);
        }
    }

    alert('თქვენ ამოგეწურათ ცდების რაოდენობა');
}


guessPassword();

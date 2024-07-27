function getStrength(password){
    var strength=0;
    if (password.match(/[a-z]+/)){      strength+=1; }
    if (password.match(/[A-Z]+/)){      strength+=1; }
    if (password.match(/[0-9]+/)){      strength+=1; }
    if (password.match(/[!|@·#$~€%&¬/()=?¿¡{},.;:_*+]+/)){    strength+=1; }
    if(password.length >= 8){ strength+=1; }
    return strength;
}

function swapPasswordElements(password){
    dict = {NUMBER:"number",LETTER:"letter",CAPITAL:"capital",SPECIAL:"special",LENGTH:"length"};
    document.getElementById(dict.NUMBER).style.color = password.match(/[0-9]+/) ? "green" : "red";
    document.getElementById(dict.LETTER).style.color = password.match(/[a-z]+/) ? "green" : "red";
    document.getElementById(dict.CAPITAL).style.color = password.match(/[A-Z]+/) ? "green" : "red";
    document.getElementById(dict.SPECIAL).style.color = password.match(/[!|@·#$~€%&¬/()=?¿¡{},.;:_*+]+/) ? "green" : "red";
    document.getElementById(dict.LENGTH).style.color = password.length >= 8 ? "green" : "red";
}

function verifyPassword(password,confirmPassword,submit) {
    let match = true;
    if (password.value != confirmPassword.value || getStrength(password.value) != 5) {
        isValidInput(confirmPassword, false);
        isValidInput(password, false);
        submit.disabled = true;
        match = false;
    }
    else {
        isValidInput(confirmPassword, true);
        isValidInput(password, true);
        submit.disabled = false;
    }
    return match;
}

function isValidInput(input, valid){
    if (valid)
        input.classList.remove("is-invalid");
    else
        input.classList.add("is-invalid");
}
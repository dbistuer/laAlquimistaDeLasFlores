// Used to swap the radio button values in the Django form with a dictionary of values key = radioButtonId, value = radioButtonValue
function swapRadioButtons(element_id) {
    elements = getElementsByType('radio');
    setAllRadioButtons(elements,element_id);
}

function getElementsByType( type ) {
            return document.querySelectorAll('input[type='+type+']');
        }

function setAllRadioButtons( elements,element_id ) {
    elements.forEach( element => {
        element_id == element.id ? element.checked = true : element.checked = false;
    });
}

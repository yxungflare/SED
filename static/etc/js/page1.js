document.getElementById('main-form').addEventListener("submit", checkForm);

function checkForm(event){
    event.preventDefault();
    var el = document.getElementById('main-form');

    var name = el.contact_name.value;
    var surname = el.contact_surname.value;
    var farthername = el.contact_fathername.value;

    var fail = "";

    if(name == "" || surname == "" || fathername == "")
        fail = "Заполните все поля";
    else if (name.length <= 1 || surname.length <= 1 || fathername.length <= 1)
        fail = "Введите корректные данные";

    if(fail != "")
        document.getElementById('error').innerHTML = fail;
    else {
        window.location = 'page2.html';
    }
}
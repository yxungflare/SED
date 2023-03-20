function dop_processing(){
    // обработка диапозона цены
    let min_value = Number(document.getElementById('input-0').value);
    let max_value = Number(document.getElementById('input-1').value);
    let sred = (max_value + min_value) / 2 // <-------------- !!!
    console.log(sred);

    // обработка приоритета в вычислениях
    let choose = document.querySelector('input[name="choose"]:checked').value // <-------------- !!!
    console.log(choose)
}

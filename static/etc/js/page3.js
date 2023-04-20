var element = document.getElementById('block-1');
var button  = document.getElementById('clear');
button.addEventListener('click', clearFunction);

var submit = document.getElementById('countChecked');
submit.addEventListener('click', isCountCheck);

function test(){
    
    var div = document.createElement('div');
    var label = document.createElement('label');
    var input = document.createElement('input');
    var span1 = document.createElement('span');
    var span2 = document.createElement ('span');
    var span3 = document.createElement('span');
    var img = document.createElement('img');


// родитель.appendChild(элемент)

    element.appendChild(div);
    div.appendChild(label);
    label.appendChild(input);
    label.appendChild(span1);
    span1.appendChild(span3);
    span1.appendChild(span2);
    span3.appendChild(img);


    document.forms.publish.onsubmit = function(){
        var message = this.message.value;
        span2.innerHTML = message;
        return false;
    };
    
    input.type = "checkbox";
    
    img.src = "https://cdn4.iconfinder.com/data/icons/data-management-2-3/50/94-512.png";


    div.className = "checkbox";
    label.className = "checkbox-wrapper";
    input.className = "checkbox-input";
    span1.className = "checkbox-tile";
    span2.className = "checkbox-label";
    span3.className = "checkbox-icon";
}


function clearFunction(){
        element.removeChild(element.lastChild);
}

// checkbox = document.getElementById('checkbox-input');
// if (checkbox.checked){
//   icon_on();
// }

// checkbox.addEventListener("change", function() {
//   if (this.checked) {
//     icon_on();
//   }
// });

// icon_on();

function icon_on(){
  if(document.getElementById('checkbox-input').checked == true){
    document.getElementById('icon_info').style.display='block';
  }
  else{
    document.getElementById('icon_info').style.display='none';
  }


  if(document.getElementById('checkbox-input-1').checked == true){
    document.getElementById('icon_info-1').style.display='block';
  }
  else{
    document.getElementById('icon_info-1').style.display='none';
  }


  if(document.getElementById('checkbox-input-2').checked == true){
    document.getElementById('icon_info-2').style.display='block';
  }
  else{
    document.getElementById('icon_info-2').style.display='none';
  }


  if(document.getElementById('checkbox-input-3').checked == true){
    document.getElementById('icon_info-3').style.display='block';
  }
  else{
    document.getElementById('icon_info-3').style.display='none';
  }


  if(document.getElementById('checkbox-input-4').checked == true){
    document.getElementById('icon_info-4').style.display='block';
  }
  else{
    document.getElementById('icon_info-4').style.display='none';
  }


  if(document.getElementById('checkbox-input-5').checked == true){
    document.getElementById('icon_info-5').style.display='block';
  }
  else{
    document.getElementById('icon_info-5').style.display='none';
  }


  if(document.getElementById('checkbox-input-6').checked == true){
    document.getElementById('icon_info-6').style.display='block';
  }
  else{
    document.getElementById('icon_info-6').style.display='none';
  }


  if(document.getElementById('checkbox-input-7').checked == true){
    document.getElementById('icon_info-7').style.display='block';
  }
  else{
    document.getElementById('icon_info-7').style.display='none';
  }


  if(document.getElementById('checkbox-input-8').checked == true){
    document.getElementById('icon_info-8').style.display='block';
  }
  else{
    document.getElementById('icon_info-8').style.display='none';
  }


  if(document.getElementById('checkbox-input-9').checked == true){
    document.getElementById('icon_info-9').style.display='block';
  }
  else{
    document.getElementById('icon_info-9').style.display='none';
  }


  if(document.getElementById('checkbox-input-10').checked == true){
    document.getElementById('icon_info-10').style.display='block';
  }
  else{
    document.getElementById('icon_info-10').style.display='none';
  }
   // Для выбора конкретной модели СЗИ1
  if(document.getElementById('checkbox-input1_1').checked == true){
    document.getElementById('icon_info-1_1').style.display='block';
  }
  else{
    document.getElementById('icon_info-1_1').style.display='none';
  }
  if(document.getElementById('checkbox-input1_2').checked == true){
    document.getElementById('icon_info-1_2').style.display='block';
  }
  else{
    document.getElementById('icon_info-1_2').style.display='none';
  }
  if(document.getElementById('checkbox-input1_3').checked == true){
    document.getElementById('icon_info-1_3').style.display='block';
  }
  else{
    document.getElementById('icon_info-1_3').style.display='none';
  }
  if(document.getElementById('checkbox-input1_4').checked == true){
    document.getElementById('icon_info-1_4').style.display='block';
  }
  else{
    document.getElementById('icon_info-1_4').style.display='none';
  }
  if(document.getElementById('checkbox-input1_5').checked == true){
    document.getElementById('icon_info-1_5').style.display='block';
  }
  else{
    document.getElementById('icon_info-1_5').style.display='none';
  }

  // Для выбора конкретной модели СЗИ2
  if(document.getElementById('checkbox-input2_1').checked == true){
    document.getElementById('icon_info-2_1').style.display='block';
  }
  else{
    document.getElementById('icon_info-2_1').style.display='none';
  }
  if(document.getElementById('checkbox-input2_2').checked == true){
    document.getElementById('icon_info-2_2').style.display='block';
  }
  else{
    document.getElementById('icon_info-2_2').style.display='none';
  }
  if(document.getElementById('checkbox-input2_3').checked == true){
    document.getElementById('icon_info-2_3').style.display='block';
  }
  else{
    document.getElementById('icon_info-2_3').style.display='none';
  }
  if(document.getElementById('checkbox-input2_4').checked == true){
    document.getElementById('icon_info-2_4').style.display='block';
  }
  else{
    document.getElementById('icon_info-2_4').style.display='none';
  }
  if(document.getElementById('checkbox-input2_5').checked == true){
    document.getElementById('icon_info-2_5').style.display='block';
  }
  else{
    document.getElementById('icon_info-2_5').style.display='none';
  }
  // Для выбора конкретной модели СЗИ3
  if(document.getElementById('checkbox-input3_1').checked == true){
    document.getElementById('icon_info-3_1').style.display='block';
  }
  else{
    document.getElementById('icon_info-3_1').style.display='none';
  }
  if(document.getElementById('checkbox-input3_2').checked == true){
    document.getElementById('icon_info-3_2').style.display='block';
  }
  else{
    document.getElementById('icon_info-3_2').style.display='none';
  }
  if(document.getElementById('checkbox-input3_3').checked == true){
    document.getElementById('icon_info-3_3').style.display='block';
  }
  else{
    document.getElementById('icon_info-3_3').style.display='none';
  }
  if(document.getElementById('checkbox-input3_4').checked == true){
    document.getElementById('icon_info-3_4').style.display='block';
  }
  else{
    document.getElementById('icon_info-3_4').style.display='none';
  }
  if(document.getElementById('checkbox-input3_5').checked == true){
    document.getElementById('icon_info-3_5').style.display='block';
  }
  else{
    document.getElementById('icon_info-3_5').style.display='none';
  }
  // Для выбора конкретной модели СЗИ4
  if(document.getElementById('checkbox-input4_1').checked == true){
    document.getElementById('icon_info-4_1').style.display='block';
  }
  else{
    document.getElementById('icon_info-4_1').style.display='none';
  }
  if(document.getElementById('checkbox-input4_2').checked == true){
    document.getElementById('icon_info-4_2').style.display='block';
  }
  else{
    document.getElementById('icon_info-4_2').style.display='none';
  }
  if(document.getElementById('checkbox-input4_3').checked == true){
    document.getElementById('icon_info-4_3').style.display='block';
  }
  else{
    document.getElementById('icon_info-4_3').style.display='none';
  }
  if(document.getElementById('checkbox-input4_4').checked == true){
    document.getElementById('icon_info-4_4').style.display='block';
  }
  else{
    document.getElementById('icon_info-4_4').style.display='none';
  }
  if(document.getElementById('checkbox-input4_5').checked == true){
    document.getElementById('icon_info-4_5').style.display='block';
  }
  else{
    document.getElementById('icon_info-4_5').style.display='none';
  }
  // Для выбора конкретной модели СЗИ5
  if(document.getElementById('checkbox-input5_1').checked == true){
    document.getElementById('icon_info-5_1').style.display='block';
  }
  else{
    document.getElementById('icon_info-5_1').style.display='none';
  }
  if(document.getElementById('checkbox-input5_2').checked == true){
    document.getElementById('icon_info-5_2').style.display='block';
  }
  else{
    document.getElementById('icon_info-5_2').style.display='none';
  }
  if(document.getElementById('checkbox-input5_3').checked == true){
    document.getElementById('icon_info-5_3').style.display='block';
  }
  else{
    document.getElementById('icon_info-5_3').style.display='none';
  }
  if(document.getElementById('checkbox-input5_4').checked == true){
    document.getElementById('icon_info-5_4').style.display='block';
  }
  else{
    document.getElementById('icon_info-5_4').style.display='none';
  }
  if(document.getElementById('checkbox-input5_5').checked == true){
    document.getElementById('icon_info-5_5').style.display='block';
  }
  else{
    document.getElementById('icon_info-5_5').style.display='none';
  }
  // Для выбора конкретной модели СЗИ6
  if(document.getElementById('checkbox-input6_1').checked == true){
    document.getElementById('icon_info-6_1').style.display='block';
  }
  else{
    document.getElementById('icon_info-6_1').style.display='none';
  }
  if(document.getElementById('checkbox-input6_2').checked == true){
    document.getElementById('icon_info-6_2').style.display='block';
  }
  else{
    document.getElementById('icon_info-6_2').style.display='none';
  }
  if(document.getElementById('checkbox-input6_3').checked == true){
    document.getElementById('icon_info-6_3').style.display='block';
  }
  else{
    document.getElementById('icon_info-6_3').style.display='none';
  }
  if(document.getElementById('checkbox-input6_4').checked == true){
    document.getElementById('icon_info-6_4').style.display='block';
  }
  else{
    document.getElementById('icon_info-6_4').style.display='none';
  }
  if(document.getElementById('checkbox-input6_5').checked == true){
    document.getElementById('icon_info-6_5').style.display='block';
  }
  else{
    document.getElementById('icon_info-6_5').style.display='none';
  }
  // Для выбора конкретной модели СЗИ7
  if(document.getElementById('checkbox-input7_1').checked == true){
    document.getElementById('icon_info-7_1').style.display='block';
  }
  else{
    document.getElementById('icon_info-7_1').style.display='none';
  }
  if(document.getElementById('checkbox-input7_2').checked == true){
    document.getElementById('icon_info-7_2').style.display='block';
  }
  else{
    document.getElementById('icon_info-7_2').style.display='none';
  }
  if(document.getElementById('checkbox-input7_3').checked == true){
    document.getElementById('icon_info-7_3').style.display='block';
  }
  else{
    document.getElementById('icon_info-7_3').style.display='none';
  }
  if(document.getElementById('checkbox-input7_4').checked == true){
    document.getElementById('icon_info-7_4').style.display='block';
  }
  else{
    document.getElementById('icon_info-7_4').style.display='none';
  }
  if(document.getElementById('checkbox-input7_5').checked == true){
    document.getElementById('icon_info-7_5').style.display='block';
  }
  else{
    document.getElementById('icon_info-7_5').style.display='none';
  }
  // Для выбора конкретной модели СЗИ8
  if(document.getElementById('checkbox-input8_1').checked == true){
    document.getElementById('icon_info-8_1').style.display='block';
  }
  else{
    document.getElementById('icon_info-8_1').style.display='none';
  }
  if(document.getElementById('checkbox-input8_2').checked == true){
    document.getElementById('icon_info-8_2').style.display='block';
  }
  else{
    document.getElementById('icon_info-8_2').style.display='none';
  }
  if(document.getElementById('checkbox-input8_3').checked == true){
    document.getElementById('icon_info-8_3').style.display='block';
  }
  else{
    document.getElementById('icon_info-8_3').style.display='none';
  }
  if(document.getElementById('checkbox-input8_4').checked == true){
    document.getElementById('icon_info-8_4').style.display='block';
  }
  else{
    document.getElementById('icon_info-8_4').style.display='none';
  }
  if(document.getElementById('checkbox-input8_5').checked == true){
    document.getElementById('icon_info-8_5').style.display='block';
  }
  else{
    document.getElementById('icon_info-8_5').style.display='none';
  }
  // Для выбора конкретной модели СЗИ9
  if(document.getElementById('checkbox-input9_1').checked == true){
    document.getElementById('icon_info-9_1').style.display='block';
  }
  else{
    document.getElementById('icon_info-9_1').style.display='none';
  }
  if(document.getElementById('checkbox-input9_2').checked == true){
    document.getElementById('icon_info-9_2').style.display='block';
  }
  else{
    document.getElementById('icon_info-9_2').style.display='none';
  }
  if(document.getElementById('checkbox-input9_3').checked == true){
    document.getElementById('icon_info-9_3').style.display='block';
  }
  else{
    document.getElementById('icon_info-9_3').style.display='none';
  }
  if(document.getElementById('checkbox-input9_4').checked == true){
    document.getElementById('icon_info-9_4').style.display='block';
  }
  else{
    document.getElementById('icon_info-9_4').style.display='none';
  }
  if(document.getElementById('checkbox-input9_5').checked == true){
    document.getElementById('icon_info-9_5').style.display='block';
  }
  else{
    document.getElementById('icon_info-9_5').style.display='none';
  }
  // Для выбора конкретной модели СЗИ10
  if(document.getElementById('checkbox-input10_1').checked == true){
    document.getElementById('icon_info-10_1').style.display='block';
  }
  else{
    document.getElementById('icon_info-10_1').style.display='none';
  }
  if(document.getElementById('checkbox-input10_2').checked == true){
    document.getElementById('icon_info-10_2').style.display='block';
  }
  else{
    document.getElementById('icon_info-10_2').style.display='none';
  }
  if(document.getElementById('checkbox-input10_3').checked == true){
    document.getElementById('icon_info-10_3').style.display='block';
  }
  else{
    document.getElementById('icon_info-10_3').style.display='none';
  }
  if(document.getElementById('checkbox-input10_4').checked == true){
    document.getElementById('icon_info-10_4').style.display='block';
  }
  else{
    document.getElementById('icon_info-10_4').style.display='none';
  }
  if(document.getElementById('checkbox-input10_5').checked == true){
    document.getElementById('icon_info-10_5').style.display='block';
  }
  else{
    document.getElementById('icon_info-10_5').style.display='none';
  }
  // Для выбора конкретной модели СЗИ11
  if(document.getElementById('checkbox-input11_1').checked == true){
    document.getElementById('icon_info-11_1').style.display='block';
  }
  else{
    document.getElementById('icon_info-11_1').style.display='none';
  }
  if(document.getElementById('checkbox-input11_2').checked == true){
    document.getElementById('icon_info-11_2').style.display='block';
  }
  else{
    document.getElementById('icon_info-11_2').style.display='none';
  }
  if(document.getElementById('checkbox-input11_3').checked == true){
    document.getElementById('icon_info-11_3').style.display='block';
  }
  else{
    document.getElementById('icon_info-11_3').style.display='none';
  }
  if(document.getElementById('checkbox-input11_4').checked == true){
    document.getElementById('icon_info-11_4').style.display='block';
  }
  else{
    document.getElementById('icon_info-11_4').style.display='none';
  }
  if(document.getElementById('checkbox-input11_5').checked == true){
    document.getElementById('icon_info-11_5').style.display='block';
  }
  else{
    document.getElementById('icon_info-11_5').style.display='none';
  }
}







function goback(){
  window.location = "page2.html";
}


function visible_off(){
  document.querySelectorAll("icon_info").addClass("hidden");
}


$("input").keydown(function(event){
  if (event.keyCode === 13) {
     return false;
 }
})


// на page4 отображаем загрузку
// Открываем новое окно с заданными размерами
function showSpinner(){
  var width = 800;
  var height = 600;
  var left = (screen.width - width) / 2;
  var top = (screen.height - height) / 2;
  var options = "width=" + width + ",height=" + height + ",left=" + left + ",top=" + top + ",location=no,toolbar=no";
  var newWindow = window.open("page4.html", "Example", options);
}


function checkAnySelected() {
  var checkboxes = document.querySelectorAll('input[type="checkbox"]');
  var anySelected = Array.prototype.slice.call(checkboxes).some(function(checkbox) {
    return checkbox.checked;
  });
  return anySelected;
}
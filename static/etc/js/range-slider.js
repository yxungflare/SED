const rangeSlider = document.getElementById('range-slider');

if(rangeSlider){
    noUiSlider.create(rangeSlider, {
        start: [500, 999999],
        connect: true,
        step: 1,
        range: {
            'min': [500],
            'max': [999999]
        }
    });

    const input0 = document.getElementById('input-0');
    const input1 = document.getElementById('input-1');
    const inputs = [input0, input1];

    rangeSlider.noUiSlider.on('update', function(values, handle){
        inputs[handle].value = Math.round(values[handle]);
    });



    const setRangeSlider = (i, value) => {
        let arr = [null, null];
        arr[i] = value;
        
        // console.log(arr); - наш диапозон
        rangeSlider.noUiSlider.set(arr);
    };

    inputs.forEach((el, index) => {
        el.addEventListener('change', (e) => {
            // console.log(index); - какая часть ползунка задействована 0 - левая, 1 - правая
            setRangeSlider(index, e.currentTarget.value);
        });
    });

    console.log(value)
}

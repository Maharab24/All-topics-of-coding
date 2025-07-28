const number = 45;

function name_of_a_function(){

    console.log('this is a function');

}

name_of_a_function();


function square(number){

    number*=number;
    console.log(number)
}

square(4);


//return

function TenTimes(number)
{
    const result= number*10;
    return result;
}

const return_value = TenTimes(10); 
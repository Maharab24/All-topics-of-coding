//Print 5
//  console.log(5)


/**

5 things to declare a variable

var weight =38;
var price =70;
var year = 2000;
year=2003;

var age;

string type variable:

var name = "Maharab Hossain OPi ";
console.log(name);

Boolean type variable:

var isRich = true; kolon hobe na

check type of a variable:
console.log(typeof isRich); j kono variable er type check kora jay



How to create name of a variable:

1. no keyword in variable name --> var false =45; false is a keyword
2. no space or gap in variable name
3. no quote
4. can not start with a number but other than the first letter is allowed
5. name is case sensitive-->
        address
        Address
        ADDRESS
        addRess

        ekhane 4 ta variable count hobe

6. how to write a long varibale
    var my_current_home_address = " djfa kdfj dlkf"; //snake case
    var myCurrentHomeAddress = " jdfldjfa";  // camel case
     var MyCurrentHomeAddress = " jdfldjfa";  // Pascal case

7. var (correct)
    Var,vAr etc (wrong)




How to convert string to number -->

var first= 20;
var second = '20';

var third =parseInt('20');

var third =parseInt(second);

var third =perseFloat('20');


Fixed number after decimal point -->

var first = 0.1;
var second = 0.2;

var total = first + second;
console.log(total) --> 0.30000000000000000004

now fixed the numbers after decimal point.

console.log(total.toFixed(2)) --> 0.30

toFixed use korle number ta string hoye jabe




Ternary --> three parts

    ?    :

condition ? do something when true : do something when false

const age=19 ;

age>=18 ? console.log("vote dio") : console.log("ghumao");



let price =500;    // const use korle kokhono ar change korbe na, let use korle change kora jabe
const isLeader = true;

price = isLeader === true ? 0 : price+100;





Array -->

const numbers = [12,22,54,65];
console.log(numbers); --> [12,22,54,65]

console.log(numbers.length); --> 4

numbers.push(44);

console.log(numbers); --> [12,22,54,65,44]


numbers.push(55,56,77);
console.log(numbers); --> [12,22,54,65,44,55,56,77]


numbers.pop();
console.log(numbers); --> [12,22,54,65,44,55,56]

numbers.shift(); --> remove from first index
console.log(numbers); --> [22,54,65,44,55,56]


numbers.unshift(13); --> add in 1st index
console.log(numbers); --> [13,22,54,65,44,55,56]




check a element is includes or not

console.log(numbers.includes(65)); true


find index number of an element

console.log(numbers.indexOf(54)); --> 2

console.log(numbers.indexOf(100)); --> -1



check it is array or not

console.log(Array.isArray(numbers)); --> true


numbers.join('+'); --> [13+22+54+65+44+55+56]



concat -->

firstArray.concat(secondArray);


array_name.slice(2,4); --> start from 2 index to 4 index;



for(const num of numbers)
console.log(num);

for(let i=0 ; i <=5 ; i++ )
console.log(i);



String -->

const school = "hasan ali";
console.log(school.toLowerCase());



const drink = '  water ';
const liqud = 'water';

drink.trim();      eita korle age pore space soraiya fele



Slice -->
const address = 'andorkilla';
const part = address.slice(2,5);  dor



split -->

const sentence

const sentence ="I am a good person";
console.log(sentence.split(' ')); [ 'I', 'am', 'a', 'good', 'person' ]
ekhane space er vittite sob alada krse.
Space er bodole jeita dibo oitar vitti te sob alada korbe.


Join-->

inverse of split


Concate -->

const first ='Abid';
const last = 'Nabid';





Reverse a string-->

const sentence = 'I am learning web dev.';

let reverse = ''

for(const letter of sentence)
{
    reverse = letter + reverse ; 
}



 */




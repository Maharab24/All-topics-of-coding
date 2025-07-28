
/**

ek line error hole er porer kono line ar kaj kore na.

jei line error dey ba dite pare, oi line try er moddhe rakhle
porer baki code kaj korbe. ei jonno try and catch use kora hoy.


 */



function checkAge(){
    const ageField = document.getElementById('age');
    const ageText =ageField;

    try {
            console.log(dlkfjdsf); // emon kono variable nai,tai eita error khabe.

            throw "Please enter a number"; // eitar kaj holo catch er error er moddhe ei msg ta throw kora. eita generally if diye use hoy 

    } catch (error) {

        console.log('Error : ', error); // ei line er kaj holo ki error khaise oita dekhano


    }


    finally{
        console.log('All done'); // age diye  error khak ba na khak finally er vitore ja ja ase sob kaj korbe.
    }

}
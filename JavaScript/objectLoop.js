const mobie={
    brand: 'samsung',
    price: 250000,
    color: 'black',
    cameera: '12mp'
}



// for of : array
// for in : object


for(const prop in mobile)
{
    console.log(prop);//sob property name asbe
    console.log(mobie[prop]);
    // prop er moddhe jokhon jei property asbe tokhon oitar value print korbe

}

const keys = Object.keys(mobile);

for(const key of keys){
    console.log(key,':',mobile[key]);
}
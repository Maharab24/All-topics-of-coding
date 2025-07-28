const bottle = {
    brand: 'apple',
    price: 45,
    color: 'white',
    isClean: false,
    "another brand": 'samsung'
}


const subject = {
    name: 'Biology',
    teacher: 'rasheda mam',
    examDate: '30 feb',
    chapters: ['fist','second','third'],

    exams:{
        name: 'final exam',
        marks: 100
    }
}

console.log(bottle); //jemne ase omnei print hobe
console.log(bottle.brand); // apple

const bottle_color = bottle.color;
console.log(bottle_color); //white;

console.log(bottle['brand']); //apple

bottle.price=50;
// price change hoiya 50 hoiya jabe
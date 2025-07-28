const computer={
    brand: 'lenovo',
    price: 35000,
    processor: 'intel',
    hdd: '512gb',
    monitor: 'hp'
}


const keys = Object.keys(computer);
console.log(keys); //[ 'brand', 'price', 'processor', 'hdd', 'monitor' ]

const values=Object.values(computer);
console.log(values); //[ 'lenovo', 35000, 'intel', '512gb', 'hp' ]
const user = {id: 1, name: 'Maharab hossain' , job: 'actor'};

//JavaScript Object Notation (JSON)

const stringified = JSON.stringify(user);
console.log(user); //{ id: 1, name: 'Maharab hossain', job: 'actor' }
console.log(stringified); //{"id":1,"name":"Maharab hossain","job":"actor"}

const shop = {
    owner: 'opi',
    address : {
        street : 'kochukhet voot er goli',
        city: 'dhaka',
        country: 'BD'
    },
    product : ['laptop','mic','keyboard','monitor'],
    revenue: 3999,
    isOpen: true,
    isNew: false
};

const shopJSON = JSON.stringify(shop);
console.log(shopJSON);

const shopObj = JSON.parse;
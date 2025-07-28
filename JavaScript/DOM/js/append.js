//Add a line step to step

// 1. Where to add
const placesList = document.getElementById('places-list');

//2. what to be added
const li = document.createElement('li');
li.innerText = 'uttor badda';

//3. add the child
placesList.appendChild(li);


//Add a section step by step

//1. select the parent. here parent is <main>

// set an id in the <main> tag

const mainContainer = document.getElementById('main-container');

const section = document.createElement('section');
const h1 = document.createElement('h1');
h1.innerText='My food list';
section.appendChild(h1);

const ul = document.createElement('ul');
const li1 = document.createElement('li');
li1.innerText = 'biriyani';

ul.appendChild(li1);

const li2 = document.createElement('li');
li2.innerText = 'borhani';

ul.appendChild(li2);

const li3 = document.createElement('li');
li3.innerText = 'salad';

ul.appendChild(li3);


section.appendChild(ul);


mainContainer.appendChild(section);


//set innerHTML directly

const sectionDress = document.createElement('section');
sectionDress.innerHTML=
`

<h1> My dress section </h2>
<ul>
    <li>T-shir</li>
    <li>Lungi</li>
    <li>genji</li>

</ul>

`

mainContainer.appendChild(sectionDress)

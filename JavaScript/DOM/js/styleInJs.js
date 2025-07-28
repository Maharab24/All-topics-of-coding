//set background color in every section

const sections = document.querySelectorAll('section');

// getElementByClassName dile for each deya jaito na

for(const section of sections)
{
    section.style.border='2px solid steelblue';

    section.style.marginBottom='5px';
    section.style.borderRadius = '15px';
    section.style.paddingRight='7px';
    section.style.backgroundColor = 'lightgray';
}



// const placesContainer = document.getElementById('places-container');

// placesContainer.style.backgroundColor = 'yellow';


//now add the class name by js

const placesContainer =document.getElementById('places-container');
placesContainer.classList.add('yellow-bg');
//eita normally hobe na,, krn age style add kore asci jeita oitar priority besi ,
// ekhn ei class er moddhe !important dile hobe
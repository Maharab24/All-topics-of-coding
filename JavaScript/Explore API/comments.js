//arrow function

const loadComments = () =>{
    fetch('https://jsonplaceholder.typicode.com/comments')
    .then(res=>res.json())
    .then(data => console.log(data))
    .catch(error => console.error('error happened',error));
}


//other rule to wirte the same function

// eita use korle data jotokhon na asbe totokhhon wait korbe. r ager ta use korle data ashuk ba na ashuk oita samne chole jabe

// const loadComments2= async() =>{
//     const res = await fetch('https://jsonplaceholder.typicode.com/comments');
//     const data = await res.json();
//     console.log(data);
// }


//if any error found ,,, to catch the error the function should wirte with try

const loadComments2= async() =>{
    try{
        const res = await fetch('https://jsonplaceholder.typicode.com/comments');
    const data = await res.json();
    console.log(data);
    }
    catch(error){
        co
    }
}




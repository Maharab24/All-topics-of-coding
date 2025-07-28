function loadPost() {
    fetch('https://jsonplaceholder.typicode.com/posts')
        .then(res => res.json())
        .then(data => displayPost(data))
}

/*

1. get the container element where you want to add the new elements
2. create  child element
3. set innertext  or innerHtml
4. appendChild

*/



function displayPost(posts) {

    const postsContainer = document.getElementById('posts-container');

    for (const post of posts) {
        const div = document.createElement('div');
        div.classList.add('post')
        div.innerHTML = `
            <h4> User-${post.id}</h4>
            <h5>Post: ${post.title} </h5>
            <p>Post Description : ${post.body}</p>
        `;

        postsContainer.appendChild(div);
    }
}

loadPost();


//delete post

function deletePost() {
    fetch('https://jsonplaceholder.typicode.com/posts/1', {
        method: 'DELETE',
    });
}


//patch a post

function patchPost() {
    fetch('https://jsonplaceholder.typicode.com/posts/1', {
        method: 'PATCH',
        body: JSON.stringify({
            title: 'foo',
        }),
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
        },
    })
        .then((response) => response.json())
        .then((json) => console.log(json));
}



function createPost(){



    fetch('https://jsonplaceholder.typicode.com/posts', {
  method: 'POST',
  body: JSON.stringify({
    title: 'foo',
    body: 'bar',
    userId: 1,
  }),
  headers: {
    'Content-type': 'application/json; charset=UTF-8',
  },
})
  .then((response) => response.json())
  .then((json) => console.log(json));
}
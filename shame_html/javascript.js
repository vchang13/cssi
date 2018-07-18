console.log('Hello World!');

const name = 'Charlie';
// console.log('Hello ' + name = '!');
console.log(`Hello ${name}!`);

const age = 16;
// console.log('You are ' + age = ' years old!');
console.log(`You are ${age} years old!`);

if (/** boolean expression*/ age>=18) {
  // execute if expression is true
  console.log('You can get your driver\'s license and vote.');
} else if (age<15){
  // execute if expression is false
  console.log('You will have to wait to get your permit and cannot vote.');
} else {
  console.log('You can get your permit but you cannot vote');
}

function makeGreetingMessage(name1, name2=null) {
  // enter code here
  if (name2 == null /*|| name2 === undefined*/) {
    return (`Hello ${name1}.`);
    // anything after return won't print
  } else {
    return (`Hello ${name1} and ${name2}`);
  }
}

// function greet(name1, name2=null) {
//   // enter code here
//   if (name2 == null /*|| name2 === undefined*/) {
//     console.log(`Hello ${name1}`);
//   } else {
//   console.log(`Hello ${name1} and ${name2}`);
//   }
// }

function greet(name1, name2=null) {
  if (name1[0] !== 'A') {
    return;
  }
  console.log(makeGreetingMessage(name1, name2));
}

greet('Alice', 'Bob');

document.addEventListener('DOMContentLoaded', () => {
  const likeButton = document.querySelector('.likeButton');
  likeButton.addEventListener('click', () => {
    const greetingMessage = makeGreetingMessage('Alice');
    likeButton.innerText = greetingMessage;
    // likeButton.innerText = 'Liked!';
    likeButton.style.backgroundColor = 'blue';
  })
  });


  const names = ['Alice', 'Bob', 'Charlie', 'Deborah', 'Evan'];
  // print out names
  // console.log(names[0]);
  // console.log(names[1]);
  // console.log(names[2]);
  // console.log(names[3]);

  // or can use a loop
  for (let i = 0; i < names.length; i++) {
    console.log(names[i]);
  }

let count = 0;
while (count < 5) {
  count++;
  console.log(count);
}

// same as earlier for loop
names.forEach((name) => {
  console.log(`forEach: ${name}`);
})


const article = {
  name: 'Dog family gives birth to litter of 10 puppies',
  views: 1234,
  datePublished: '03/25/2018',
  author: [{
    name: 'Joe Corgi',
    title: 'Senior Canine Editor',
  }],
  editors: [{
    name: '...',
    title: '...',
  }, {
    name: '....',
    title: '....',
  },],

};

document.addEventListener('DOMContentLoaded', () => {
  const floatingBox = document.querySelector('.floatingBox');
  let boxTop = 100;
  let boxLeft = 100;
  document.addEventListener('keydown', (event) => {
    const key = event.key;
    if (key === 'ArrowDown') {
      boxTop +=5
    } else if (key === 'ArrowUp') {
      boxTop -=5
    } else if (key === 'ArrowLeft') {
      boxLeft -=5
    } else if (key === 'ArrowRight') {
      boxLeft +=5
    } else {
      return;
    }

    floatingBox.style.top = boxTop + 'px';
    floatingBox.style.left = boxLeft + 'px';
    console.log(event);
  });
});

// const multiplyBy3 = (x) => x * 3;
// console.log(multiplyBy3(3));
//
// let n = 0;
// setInterval(() => {
//   n += 1;
//   console.log(n);
// }, 1000);
//
// const multiplyBy4 = function (x) {
//   return x * 3;
// };

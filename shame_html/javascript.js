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

const multiplyBy3 = (x) => x * 3;
console.log(multiplyBy3(3));

let n = 0;
setInterval(() => {
  n += 1;
  console.log(n);
}, 1000);

const multiplyBy4 = function (x) {
  return x * 3;
};

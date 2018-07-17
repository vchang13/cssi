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

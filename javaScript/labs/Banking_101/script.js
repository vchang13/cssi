// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

let customer_name;
let balance;

function openAccount(name, stbal){
  if (stbal == null) {
    balance = 0;
    // Set the value for customer_name equal to name below
    let customer_name = `${name}`;
    // THIS WAY WORKS TOO
    // customer_name = name; 
    return (`${customer_name} has opened a new account with a balance of $0.`);
     //write the statment you need to return here
  } else {
    let customer_name = `${name}`;
    return (`${customer_name} has opened a new account with a balance of $${stbal}.`);
  }
}

function deposit(value){
  // update the value of balance

  //return the correct statement
}

function withdraw(/*argument here*/){
  //update the value of balance
  //return the correct statement
}

// Write your script below

// to test the js
// function testMe(a){
//   return a + 4;
// }
//
// let result = testMe(5);
// console.log(result);
//
// console.log(testMe(5));

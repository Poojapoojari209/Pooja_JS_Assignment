//foreach method
let numbers = [1, 2, 3, 4, 5];
numbers.forEach(function(num){
    console.log(num * 2);
});

//map method
let numbers1 = [1, 2, 3, 4, 5];
let res = numbers1.map(function(num){
    return num * 2;

});
console.log(res);

//reduce method
let numbers3 = [1, 2, 3, 4, 5];
let sum = numbers3.reduce(function(total, num){
 return total + num;
});

console.log(sum);
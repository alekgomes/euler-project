// Encontrar a soma de todos os numeros pares da 
// sequencia de fibonacci até o limite de 4000000


// - Encontrar e somar todos os pares
// - Retornar Sequência de Fibo

function fibo(limite){
  let a = 1;
  let b = 1;
  let c = 0;
  let arr = [];

  while(c < limite){
    c = a + b; // c = 2 // c = 3 // c = 5 //
    a = b;  // a = 1 // a = 2 // a = 3 //
    b = c; // b = 2 // b = 3 // b = 5 // 
    arr.push(c);
  }

  return (arr);
}

function verificaPar(){
  const arr = fibo(4000000);

  let soma = 0;
  for (num of arr){
    if (num % 2 === 0){
      soma += num;
    }    
  }
  console.log(soma);

}

verificaPar()

	
# curso-programacao-concorrente
Exercícios resolvidos do curso de Programação Concorrente do livro "The Little Book of Semaphores" - by Allen B. Downey.

O livro apresenta linguagem de programação genérica nos exemplos, então para a resolução dos exercícios propostos optei por Python.

3-3 Desafio Rendezvous

Puzzle: Generalize the signal pattern so that it works both ways. Thread A has to wait for Thread B and vice versa. In other words, given this code
 
Thread A                Thread B
1 statement a1          1 statement b1
2 statement a2          2 statement b2

we want to guarantee that a1 happens before b2 and b1 happens before a2. In writing your solution, be sure to specify the names and initial values of your semaphores.


<h1 align="center"> Atividade avaliativa para a P2</h1>
<img src="https://universidadedevassouras.edu.br/wp-content/uploads/2021/12/logo_horizontal_univasso.svg">

<h5>Curso: Engenharia de Software<br>
Disciplica: Arquitetura e Projeto de Software<br>
Professor: Sidney Loyola de Sá<br>
Período: 6° Período<br>
Aluno: Gabriel Victor Martins Carvalho</h5>

##

<b><h1>Testes Automatizados com Python</h1> </b>
<br>
<b>Introdução:</b><br> 
Este relatório apresenta as etapas realizadas para corrigir bugs em três classes implementadas em Python: FibonacciGenerator, StringUtils e UserManager. Além disso, foi implementada uma bateria de testes automatizados utilizando a biblioteca pytest. O objetivo é validar as funcionalidades, garantindo o funcionamento esperado de cada método e identificando possíveis regressões em cenários futuros. 

O generate_sequence da classe FibonacciGenerator, o cálculo do próximo número da sequência de Fibonacci estava incorreto. Em vez de somar os dois últimos números da lista, o método somava o último número consigo mesmo, o que resultava em valores errados. 

Já o reverse_string da classe StringUtils, a função retornava a string original, sem realizar qualquer inversão. Esse erro aconteceu porque o retorno simplesmente repetia a entrada sem nenhuma modificação. 

E por fim o remove_user da classe UserManager, uma tentativa de remover um usuário que não estava presente na lista gerava uma exceção do tipo ValueError. Isso ocorre porque o método list.remove em Python não verifica se o elemento existe antes de tentar removê-lo. 

 

<b>Correção</b><br>
Corrigindo os bugs do generate_sequence o cálculo do próximo número foi corrigido para somar os dois últimos números da sequência, utilizando a expressão sequence[-1] + sequence[-2]. Isso garante que o método siga corretamente a lógica da sequência de Fibonacci, onde cada número é a soma dos dois anteriores. Já get_nth_number o loop usado para calcular o enésimo número na sequência de Fibonacci estava iterando um número insuficiente de vezes, devido ao uso do intervalo range(n - 2). Esse intervalo foi ajustado para range(n - 1), permitindo que o cálculo percorra todas as iterações necessárias para alcançar o número correto.  

Em reverse_string substituímos a lógica incorreta de retorno pela utilização de (s[::-1]), que inverte a string diretamente. Essa abordagem é eficiente e simplifica o código, garantindo que o método retorne a string invertida corretamente. 

E em remove_user adicionando uma verificação condicional para verificar se o usuário está presente na lista antes de tentar removê-lo. Caso o usuário não seja encontrado, o método agora retorna uma mensagem informando o problema, em vez de lançar uma exceção inesperada. 

 

<b>Testes Automatizados:</b>

A correção dos bugs e a implementação de testes unitários foram fundamentais para garantir que as classes funcionem conforme o esperado em diversos cenários. A utilização da biblioteca pytest permitiu criar uma base confiável para futuras atualizações no código, minimizando a probabilidade de erros e regressões. 

<b>Conclusão: </b>

A aplicação de testes automatizados utilizando a biblioteca pytest foi essencial para garantir que as correções realizadas nas classes FibonacciGenerator, StringUtils e UserManager resolveram os problemas identificados, e que os métodos funcionam corretamente em todos os cenários testados. A experiência demonstrou a importância de integrar testes desde o início do ciclo de desenvolvimento. Isso não apenas melhora a qualidade do código, mas também reduz significativamente o tempo necessário para identificar e corrigir problemas. 

* Esse é um progama que foi desenvolvido junto com um amigo de faculdade para o trabalho de " Atividades Prática Supervisionadas ".


-----------------------------------------------------------------------------------------------------------------------------------


## FUNÇÕES DO PROGAMA:


-- Esse progama tem 2 funções, uma de " criptografar uma mensagem " e a outra para " descriptografar uma mensagem ".


## COMO FUNCIONA O PROGAMA:


-- Ao executar o progama será perguntado se deseja " criptografar ou descriptografar uma mensagem ", sendo " 1 " para " criptografar " e " 2 " para descriptografar.


-- O próximo passo pedirá para digitar a mensagem e em seguida a senha (apenas números inteiros).


-- Após fazer os passos acima será retornada a mesagem criptografada/descriptografada.


## COMO FUNCIONA O CÓDIGO DO PROGAMA:


-- No caso da opção de " criptografar ", o progama irá pedir para criar uma mensagem e em seguida uma senha.


-- A senha fornecida pelo usuário será usado como uma " seed " para gerar 2 números de 1 até 99 (sempre que for fornecido a mesma seed, os números gerados serão os mesmos)


-- Em seguida o código irá chamar a função de " criptografar " e nessa função a mensagem vai passar por um looping, que tem como função iterar em todos os caracteres da mensagem, um por um.


-- A cada looping irá alterar um caracter da mensagem. Primeiro o caracter é substituído pelo seu representante numérico da " Tabela ASCII " usando a função " ord ".


-- Logo então o representante numérico do caracter é somado com o produto dos 2 números gerados pela seed (senha que foi fornecida pelo usuário).


-- E por último, com o resultado da conta feita, é usado a função " chr( função oposta da função ord ) " que substitui o representante numérico da " Tabela ASCII " para um caracter.


-- Então o looping irá se repetir até ter criptografado a mensagem inteira.


-- Já no caso da opção de " descriptografar ", o progama irá pedir para inserir a mensagem que foi criptografada junto com a senha criada da mesma.


-- O código irá rodar da mesma forma que foi explicado acima com a opção de " criptografar ", com a diferença que em vez de fazer " a soma do produto dos 2 números gerados pela seed com o representante numérico da Tabela ASCII " será feita a " subtração da divisão dos 2 números gerados pela seed com o representante numérico da Tabela ASCII ". Que é o equivalente ao processo inverso da criptografia.

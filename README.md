# Gerador de Senhas Aleatórias

Este projeto é um simples gerador de senhas aleatórias em Python. Ele utiliza a biblioteca random para criar senhas seguras e as salva em um arquivo de texto, associando cada senha ao serviço para o qual será usada.

### Funcionalidades
- Geração de Senhas Aleatórias: Utiliza uma string de caracteres (incluindo letras maiúsculas, minúsculas, números e símbolos especiais) para gerar senhas seguras.
- Salvamento de Senhas: As senhas geradas são salvas em um arquivo de texto (passwords.txt), juntamente com o nome do serviço fornecido pelo usuário.

### Estrutura do Código
- generate_password(lenghtPassword=15): Função que gera uma senha aleatória com o comprimento especificado (padrão é 15 caracteres).
- write_file(service="Senha sem serviço especificado"): Função que gera uma senha e a escreve no arquivo de texto, associando-a ao serviço especificado.
- main(): Função principal que solicita ao usuário o nome do serviço e chama write_file para salvar a senha.

## Como Usar
1. Clone este repositório.
2. Execute o script Python.
3. Insira o nome do serviço quando solicitado.
4. A senha gerada será salva em passwords.txt no diretório especificado.
#### Notas
- Este projeto foi criado para fins educacionais e pessoais. 
- Para uso em produção, considere implementar medidas de segurança adicionais.

## Melhorias Futuras
- Melhorar a interface do usuário para uma experiência mais amigável.
- Implementar criptografia para proteger as senhas salvas.
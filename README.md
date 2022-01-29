# Python Balanceamento Server

## Sumário

- [Executando a Aplicação](#executando-a-aplicação)
- [Testes](#testes)



Na pasta src, tem os arquivos server.py e user.py que possuem as abstrações para servidores e usuários, respectivamente. Além destes arquivos, contém o main.py que possui todo o fluxo da aplicação (simulação do balanceamento de carga nos servidores).

---

## Executando a Aplicação

É esperado que o usuário esteja na pasta src do repositório e que a pasta resources contenha um arquivo input.txt. Então, a partir de um terminal execute o comando:

```sh
$ python main.py # Archlinux-based
$ python3 main.py # Debian-based
```

Isso irá fazer o programa executar e gravar um arquivo (output.txt) na pasta resources.

---

## Testes

Os testes estão no diretório de testes e foram feitos utilizando o módulo pytest do python. Para verificar todos os testes implementados, é necessários estar no diretório src da aplicação, em seguida rode o comando:

```sh
$ python -m pytest ../test/ # Archlinux-based
$ python3 -m pytest ../test/ # Debian-based
```


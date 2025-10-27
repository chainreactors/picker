---
title: Explorando SQL Injection no INSERT - BHack CTF 2022 - Jogo da Velha - [PT-BR]
url: https://fireshellsecurity.team/bhack2022-jogo-da-velha/
source: FireShell Security Team
date: 2022-12-11
fetch_date: 2025-10-04T01:12:31.991043
---

# Explorando SQL Injection no INSERT - BHack CTF 2022 - Jogo da Velha - [PT-BR]

[![](/assets/images/title.gif)](/)

* [Home](/)
* [Team](/team/)
* [Articles](/articles/)
* [Portfolio](/portfolio/)
* [Sponsors](/sponsors/)
* [About](/about/)
* Toggle theme
  + Light
  + Dark
  + Auto

Saturday, December 10, 2022

# Explorando SQL Injection no INSERT - BHack CTF 2022 - Jogo da Velha - [PT-BR]

by [Neptunian](/neptunian/)

Explorando SQL Injection no INSERT - BHack CTF 2022 - Jogo da Velha - [PT-BR]

Tive o grande prazer de participar do evento de segurança **BHack 2022** e ajudar na organização do CTF, incluindo a elaboração de dois desafios.

Neste write-up, explico o desafio web `Jogo da Velha` e o método proposto de solu.. hacking :)

Pra facilitar a vida de quem estiver começando, serei bastante detalhista em alguns pontos, focando na linha de raciocínio para a solução do desafio.

## O Desafio

![](https://i.imgur.com/uDd0xLr.png)

```
Junte-se a centenas de atletas ao redor do mundo para competir pelo título de melhor jogador do ano na Copa do Mundo de Jogo da Velha!!

A flag é a senha do usuário "admin"
```

Neste desafio, você tem um Jogo da Velha, onde você compete com a “inteligência artificial” do servidor - que é apenas um random, claro :)

![](https://i.imgur.com/Qbjw6aC.png)

Após se registrar e logar, você pode criar novos jogos e jogar contra a máquina, além de listar os jogos já criados e retomar.

## Análise de Código

O código-fonte da aplicação está disponível, permitindo uma análise mais aprofundada do seu comportamento.

### Setup Local (Linux)

Para quem não teve acesso e quiser experimentar, disponibilizei o [código do desafio no github](https://github.com/Neptunians/bhack-ctf-jogo-da-velha).

O código vem com o arquivo [docker-compose.yml](https://github.com/Neptunians/bhack-ctf-jogo-da-velha/blob/main/docker-compose.yml), pra facilitar o setup, principalmente porque temos uma composição de aplicação e banco de dados MySQL.

Por isso, para iniciar o desafio, você precisa ter instaladas as ferramentas abaixo:

* https://docs.docker.com/engine/install/
* https://docs.docker.com/compose/install/compose-plugin/

Com as ferramentas instaladas, você pode entrar na pasta e digitar:

`$ docker compose up`

Obs: o container do banco de dados demora BASTANTE a ser criado na primeira vez (pelo menos uns 5 minutos) e o container da aplicação fica dando erro e reiniciando até que o banco esteja disponível.
Obs: já sei como melhorar esse item, mas não tive tempo de trabalhar nisso antes do CTF.

Exemplo de saída:

```
neptunian:~/safe/bhack-ctf-jogo-da-velha$ docker compose up
[+] Running 2/2
 ⠿ Container bhack-ctf-jogo-da-velha-jogo-da-velha-db-1  Created                                                                         0.5s
 ⠿ Container bhack-ctf-jogo-da-velha-tic-tac-toe-1       Created                                                                         0.3s
Attaching to bhack-ctf-jogo-da-velha-jogo-da-velha-db-1, bhack-ctf-jogo-da-velha-tic-tac-toe-1
bhack-ctf-jogo-da-velha-jogo-da-velha-db-1  | 2022-11-28 23:22:30+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.29-1.el8 started.
bhack-ctf-jogo-da-velha-jogo-da-velha-db-1  | 2022-11-28 23:22:30+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
bhack-ctf-jogo-da-velha-jogo-da-velha-db-1  | 2022-11-28 23:22:30+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.29-1.el8 started.
bhack-ctf-jogo-da-velha-jogo-da-velha-db-1  | 2022-11-28 23:22:30+00:00 [Note] [Entrypoint]: Initializing database files
bhack-ctf-jogo-da-velha-jogo-da-velha-db-1  | 2022-11-28T23:22:30.951563Z 0 [System] [MY-013169] [Server] /usr/sbin/mysqld (mysqld 8.0.29) initializing of server in progress as process 42
bhack-ctf-jogo-da-velha-jogo-da-velha-db-1  | 2022-11-28T23:22:30.983855Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
bhack-ctf-jogo-da-velha-tic-tac-toe-1       |  * Serving Flask app 'app' (lazy loading)
bhack-ctf-jogo-da-velha-tic-tac-toe-1       |  * Environment: production
bhack-ctf-jogo-da-velha-tic-tac-toe-1       |    WARNING: This is a development server. Do not use it in a production deployment.
bhack-ctf-jogo-da-velha-tic-tac-toe-1       |    Use a production WSGI server instead.
bhack-ctf-jogo-da-velha-tic-tac-toe-1       |  * Debug mode: off

## erro nas primeiras conexões (mostrando somente as linhas iniciais)

bhack-ctf-jogo-da-velha-tic-tac-toe-1       | Traceback (most recent call last):
bhack-ctf-jogo-da-velha-tic-tac-toe-1       |   File "/home/ttt/.local/lib/python3.10/site-packages/mysql/connector/connection_cext.py", line 263, in _open_connection
bhack-ctf-jogo-da-velha-tic-tac-toe-1       |     self._cmysql.connect(**cnx_kwargs)
bhack-ctf-jogo-da-velha-tic-tac-toe-1       | _mysql_connector.MySQLInterfaceError: Can't connect to MySQL server on 'jogo-da-velha-db:3306' (111)
bhack-ctf-jogo-da-velha-tic-tac-toe-1       |
bhack-ctf-jogo-da-velha-tic-tac-toe-1       | The above exception was the direct cause of the following exception:
...

## sucesso depois de alguns minutos

bhack-ctf-jogo-da-velha-jogo-da-velha-db-1  | 2022-11-28T23:24:01.432841Z 0 [Warning] [MY-010068] [Server] CA certificate ca.pem is self signed.
bhack-ctf-jogo-da-velha-jogo-da-velha-db-1  | 2022-11-28T23:24:01.432906Z 0 [System] [MY-013602] [Server] Channel mysql_main configured to support TLS. Encrypted connections are now supported for this channel.
bhack-ctf-jogo-da-velha-jogo-da-velha-db-1  | 2022-11-28T23:24:01.619661Z 0 [System] [MY-011323] [Server] X Plugin ready for connections. Bind-address: '::' port: 33060, socket: /var/run/mysqld/mysqlx.sock
bhack-ctf-jogo-da-velha-jogo-da-velha-db-1  | 2022-11-28T23:24:01.619713Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.0.29'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server - GPL.
bhack-ctf-jogo-da-velha-tic-tac-toe-1 exited with code 1
bhack-ctf-jogo-da-velha-tic-tac-toe-1       |  * Serving Flask app 'app' (lazy loading)
bhack-ctf-jogo-da-velha-tic-tac-toe-1       |  * Environment: production
bhack-ctf-jogo-da-velha-tic-tac-toe-1       |    WARNING: This is a development server. Do not use it in a production deployment.
bhack-ctf-jogo-da-velha-tic-tac-toe-1       |    Use a production WSGI server instead.
bhack-ctf-jogo-da-velha-tic-tac-toe-1       |  * Debug mode: off
bhack-ctf-jogo-da-velha-tic-tac-toe-1       |  * Running on all addresses (0.0.0.0)
bhack-ctf-jogo-da-velha-tic-tac-toe-1       |    WARNING: This is a development server. Do not use it in a production deployment.
bhack-ctf-jogo-da-velha-tic-tac-toe-1       |  * Running on http://127.0.0.1:5000
bhack-ctf-jogo-da-velha-tic-tac-toe-1       |  * Running on http://172.27.0.3:5000 (Press CTRL+C to quit)
```

Para testar a app funcionando, é só testar no navegador:
`http://localhost:5000/`

Antes de ler o resto do artigo com a solução, sugiro uma tentativa de hackear a aplicação e obter a senha do `admin`.

### Entendendo o Setup

Em uma App com o `docker-compose.yml` disponível, vale dar uma olhada no arquivo pra entender alguns pontos importantes.

```
version: '3.7'
services:
  jogo-da-velha-db:
    image: mysql:8
    restart: always
    volumes:
      - ./db/schema.sql:/docker-entrypoint-initdb.d/schema.sql:ro
    environment:
      - MYSQL_RANDOM_ROOT_PASSWORD=yes
      - MYSQL_DATABASE=ttt
      - MYSQL_USER=ttt
      - MYSQL_PASSWORD=NAO_DISPONIVEL

  tic-tac-toe:
    build: .
    restart: always
    ports:
      - 5000:5000
    environment:
      - MYSQL_DATABASE=ttt
      - MYSQL_USER=ttt_app
      - MYSQL_PASSWORD=simples
      - MYSQL_HOST=jogo-da-velha-db
    depends_on:
      - jogo-da-velha-db
```

**Resumo**

* A aplicação é composta por dois containers:
  + tic-tac-toe (web app)
  + jogo-da-velha-db (banco de dados mysql)
* O entrypoint do mysql é o script chamado na inicialização do banco, normalmente pra criar uma estrutura inicial ([schema.sql](https://github.com/Neptunians/bhack-ctf-jogo-da-velha/blob/main/db/schema.sql)).

#...
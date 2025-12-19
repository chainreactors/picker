---
title: login-bonus (Daily AlpacaHack 2025/12/17) 公式Writeup
url: https://ptr-yudai.hatenablog.com/entry/2025/12/18/151253
source: CTFするぞ
date: 2025-12-18
fetch_date: 2025-12-19T03:22:13.732183
---

# login-bonus (Daily AlpacaHack 2025/12/17) 公式Writeup

[![CTFするぞ](https://cdn.image.st-hatena.com/image/square/994ee0e012cf90178bff014bfd99123c02a89b36/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F153103571%2F1535456424487441)](https://ptr-yudai.hatenablog.com/)

[CTFするぞ](https://ptr-yudai.hatenablog.com/)

[読者になる](https://blog.hatena.ne.jp/ptr-yudai/ptr-yudai.hatenablog.com/subscribe?utm_campaign=subscribe_blog&utm_source=blogs_topright_button&utm_medium=button)

# [CTFするぞ](https://ptr-yudai.hatenablog.com/)

## CTF以外のことも書くよ

[2025-12-18](https://ptr-yudai.hatenablog.com/archive/2025/12/18)

# [login-bonus (Daily AlpacaHack 2025/12/17) 公式Writeup](https://ptr-yudai.hatenablog.com/entry/2025/12/18/151253)

[CTF](https://ptr-yudai.hatenablog.com/archive/category/CTF)
[Writeup](https://ptr-yudai.hatenablog.com/archive/category/Writeup)

# はじめに

この記事では、私が2025年12月17日の [Daily AlpacaHack](https://alpacahack.com/daily) で出題した login-bonus の解説をします。プログラミングは少しできるあるいは[Linux](https://d.hatena.ne.jp/keyword/Linux)は少し触れるけどCTFには参加したことがない、くらいの層を想定して書いています。

問題を先に解きたい方は [こちら](https://alpacahack.com/daily/challenges/login-bonus) からどうぞ。

# 問題概要

以下の5つのファイルが渡されます。

```
$ ls
compose.yaml  Dockerfile  flag.txt  login  login.c
```

基本的にpwnの問題では、サーバ側で動作しているプログラムに[脆弱性](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C8%BC%EF%BF%BD%EF%BF%BD%EF%BF%BD)があり、それを悪用することで不正な動作を起こしたり、サーバ側で任意コード実行したりすることを目的とします。そのため、配布ファイルにはほぼ必ずサーバ側で動作しているプログラム本体があり、場合によっては[ソースコード](https://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)も与えられます。

fileコマンド等で確認すると、今回は `login` という名前のファイルが実行可能ファイルであることがわかります。（ELFとは、[Linux](https://d.hatena.ne.jp/keyword/Linux)で使われる実行可能ファイルの形式名です。）そして、 `login.c` はその[ソースコード](https://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)にあたります。

```
$ file login
login: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, not stripped
```

CTFにおいては多くの場合、サーバ側で[dockerコンテナ](https://www.docker.com/ja-jp/)上でプログラムが動作しています。これはpwnに限らず、webやcryptoでもdockerが使われることが多いです。理由は環境のデプロイが簡単なのと、[脆弱性](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C8%BC%EF%BF%BD%EF%BF%BD%EF%BF%BD)を使って危険な操作をできてしまうという性質上、ホストマシンと分離する必要があるからです。

今回の問題でも配布されている `Dockerfile` や `compose.yaml` は、このdockerコンテナを起動するためのファイルになります。問題を解く際に必ずしも使う必要はありませんが、サーバ側で実際に動作している状況を正確に再現し、手元のマシンで攻撃コードを試すために利用できます。

簡単な問題の場合、環境に依存せず解けることが多いです。その場合は、次のように単純に手元でプログラムを起動して動作を確認しても問題ありません。

```
$ ./login
```

Dockerコンテナを立ち上げて試したい場合は、次のようなコマンドを使います。Dockerのインストールは[こちら](https://docs.docker.com/engine/install/)を参照ください。

```
$ docker compose up --build
あるいは
$ sudo docker compose up --build
```

コンテナのビルドと起動が完了すると、dockerコンテナが立ち上がります。

```
$ docker ps
CONTAINER ID   IMAGE                     COMMAND              CREATED          STATUS          PORTS                                         NAMES
0953281143fe   login-bonus-login-bonus   "xinetd -dontfork"   20 seconds ago   Up 19 seconds   0.0.0.0:9999->9999/tcp, [::]:9999->9999/tcp   login-bonus-login-bonus-1
```

この例ではコンテナ内部の9999番ポート（ `9999/tcp` ）が、ホストマシンの9999番ポート（ `0.0.0.0:9999` ）にバインドされて見える状態になっています。

開放されたポートには通常socketを利用して接続する必要がありますが、毎回プログラムを書いていると面倒です。そこで、接続テストには[netcat (nc)](https://ja.wikipedia.org/wiki/Netcat)と呼ばれるプログラムを利用するのが一般的です。[Ubuntu](https://d.hatena.ne.jp/keyword/Ubuntu)の場合は `apt install netcat` などでインストールできます。

接続すると、以下のようにサーバ（dockerコンテナ内で動作しているプログラム）からの応答があり、こちらからも入力を送信できます。

```
$ nc 0.0.0.0 9999
[DEBUG] Generating secure password...
Password: test # こちらからの入力
[DEBUG] Authenticating...
[-] Wrong password
[DEBUG] 'test' != 'FUHPXMUOBWLBLDVK'
```

本番のサーバに攻撃する場合は、問題文で提示された[IPアドレス](https://d.hatena.ne.jp/keyword/IP%EF%BF%BD%EF%BF%BD%EF%BF%BD%C9%A5%EC%A5%B9)に対してncで接続します。

接続した結果を見ると、どうやらパスワードを聞かれているようですが、適当に入力してもログインできません。
最後に正しいパスワードと思われる文字列が表示されますが、この部分は毎回ランダムに作られるため、現状ではパスワードがわかりません。

# 解説

問題を解くまでの流れを解説します。

## [ソースコード](https://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)の読解

さて、今回は[C言語](https://d.hatena.ne.jp/keyword/C%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)の[ソースコード](https://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)が配布されているので、これを読んでみましょう。

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/random.h>

#define debug_report(fmt, ...) printf("[DEBUG] " fmt "\n", ##__VA_ARGS__)

char password[32];
char secret[32];

int main() {
  /* Input password */
  printf("Password: ");
  scanf("%[^\n]", password);

  /* Check password */
  debug_report("Authenticating...");
  if (strcmp(password, secret)) {
    puts("[-] Wrong password");
    debug_report("'%s' != '%s'", password, secret);

  } else {
    puts("[+] Success!");
    system("/bin/sh");
  }

  return 0;
}

__attribute__((constructor))
void setup() {
  int seed;
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);

  /* Generate random password */
  debug_report("Generating secure password...");
  getrandom(&seed, sizeof(seed), 0);
  srand(seed);
  for (size_t i = 0; i < 16; i++)
    secret[i] = 'A' + (rand() % 26);
}
```

このプログラムでは `main` と `setup` という関数、 `password` と `secret` という[グローバル変数](https://d.hatena.ne.jp/keyword/%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD%D0%A5%EF%BF%BD%EF%BF%BD%D1%BF%EF%BF%BD)、さらに `debug_report` というマクロが定義されており、なにやらゴチャゴチャしています。ひとつずつ読んでいきましょう。

[C言語](https://d.hatena.ne.jp/keyword/C%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)は `main` 関数から始まるので、 `main` 関数の中身を読んでみましょう。まず、最初に `printf` で「Password: 」と出力して、変数 `password` に `scanf` で入力を受け付けます。

```
/* Input password */
printf("Password: ");
scanf("%[^\n]", password);
```

`scanf` は書式文字列という文字列を第一引数に受け取り、入力されたデータをそれに従って変数に格納します。今回の書式文字列は「%[^\n]」で、少し馴染みのないものになっていますが、「改行（\n）以外（^）で構成される文字列を受け取る」という意味になります。
したがって、我々が入力した文字列（パスワード）が変数 `password` に格納されることになります。

続いて、パスワードの比較があります。`debug_report` マクロは、内部的には `printf` を呼び出しているだけで、[デバッグ](https://d.hatena.ne.jp/keyword/%EF%BF%BD%C7%A5%D0%A5%C3%A5%EF%BF%BD)メッセージを表示するために使われています。

```
/* Check password */
debug_report("Authenticating...");
if (strcmp(password, secret)) {
  puts("[-] Wrong password");
  debug_report("'%s' != '%s'", password, secret);

} else {
  puts("[+] Success!");
  system("/bin/sh");
}
```

`strcmp` 関数を使って `password` と `secret` （後述しますが、ここに正しいパスワードがある。）の文字列を比較しています。 `strcmp` 関数を検索すると、2つの文字列が一致した場合に0を返すことがわかります。したがって、 `if` 文のtrueのブロックはパスワードが間違っているとき、falseのブロックはパスワードが正しいときの処理を表します。
間違っているときは「Wrong password」と表示し、さらに入力したパスワードと正しいパスワードを `debug_report` で出力します。
正しいときは「Success!」と表示し、 `system("/bin/sh")` を呼び出します。

ここで、 `system` 関数は第一引数のコマンドを実行する関数です。また、 `/bin/sh` はシェルと呼ばれる、どのようなコマンドでも実行できるインタフェースにあたります。
したがって、この問題ではパスワードが一致して、 `/bin/sh` を起動することができれば、サーバ側で自由な操作をできるようになります。

このように、CTFのpwn問題では多くの場合、何かしらの方法で `/bin/sh` を起動させることが最終的な目標になります。

さて、パスワード文字列を比較している `secret` という変数ですが、これは `setup` 関数で初期化されています。
`setup` 関数はどこからも呼び出されていませんが、 `__attribute__((constructor))` という属性が付けられています。これはプログラムが起動して `main` 関数が始まるよりも前に呼び出したい関数に付けられる属性です。したがって、 `setup` 関数は `main` 関数よりも先に実行されます。

```
int seed;
setbuf(stdin, NULL);
setbuf(stdout, NULL);

/* Generate random password */
debug_report("Generating secure password...");
getrandom(&seed, sizeof(seed), 0);
srand(seed);
for (size_t i = 0; i < 16; i++)
  secret[i] = 'A' + (rand() % 26);
```

この関数では、まず `setbuf` 関数を2回呼び出しています。これは標準入出力のバッファリングを無効化するためのコードで、これがないと例えば `printf` の出力結果がバッファリングされ、ネットワーク越しだと出力されない、といった問題が起こる場合があります。バッファリングの問題を防ぐために、CTFのプログラムでは最初に`setbuf`が呼び出されることがしばしばあります。CTFを始めたうちは、おまじないだと思って問題ありません。

次に、 `getrandom` 関数で十分に安全なシード値を作ったあと、 `srand` と `rand` 関数（乱数生成）を使って `secret` 文字列を構築します。
[C言語](https://d.hatena.ne.jp/keyword/C%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD)において、文字の表現は[ASCIIコード](https://ja.wikipedia.org/wiki/ASCII)に従って決められています。例えば'A'という文字は0x41（10進数で65）が割り当てられています。

'A'〜'Z'までのアルファベットは連番です。したがって、 `'A' + (rand() % 26)` のコードは'A'から'Z'までのランダムなアルファベット1文字を...
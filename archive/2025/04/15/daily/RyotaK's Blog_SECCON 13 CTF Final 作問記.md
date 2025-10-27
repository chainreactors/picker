---
title: SECCON 13 CTF Final 作問記
url: https://blog.ryotak.net/post/seccon-13-ctf-final-author-writeup/
source: RyotaK's Blog
date: 2025-04-15
fetch_date: 2025-10-06T22:05:19.745842
---

# SECCON 13 CTF Final 作問記

[RyotaK's Blog](https://blog.ryotak.net/)
技術的な話とか

## [SECCON 13 CTF Final 作問記](https://blog.ryotak.net/post/seccon-13-ctf-final-author-writeup/)

2025-04-15
 10376 字
 [CTF](/tags/ctf) [Writeup](/tags/writeup) [SECCON](/tags/seccon) [Web](/tags/web)

## 要約

SECCON 13 CTF決勝戦の作問に誘われたので、「super-fastcgi」という名前の問題と、「not-that-short」という問題の2問を作ってきました。
「super-fastcgi」の方の難易度は「Easy-Medium」、「not-that-short」の方の難易度は「Hard」を想定しており、決勝中の解答率から見ても想定難易度と合致していたかな、という感触でした。

本記事では、それぞれの作問者Writeupと作問記を兼ねて、どういった経緯や意図を持って作問したのかを解説していきます。

## はじまり

時は遡ること2025年2月3日、SECCON 13 CTF決勝戦の一ヶ月前、Twitterにてこんなメッセージを受け取りました。

![TwitterのDMにて「これは公式の依頼なのですが、近々開催されるSECCON CTFの決勝の作問って興味あったりしますか？」、「Web要員がいなくて作問神を探しています。」](/img/seccon-13-ctf-final-author-writeup/twitter-dm.png)

CTFの作問は過去に数回しかしたことがなかったため、決勝戦に出せるクオリティの問題が作れるのか自信がなく、一旦は断ろうとしていました。
しかしながら、他の作問者の方にレビューいただけるとのことであったため、せっかくなら挑戦してみるかということで作問をすることにしました。

## super-fastcgi

この問題のコンセプトは、「バイナリプロトコル、やばいなり！」です。
2024年のDEF CON 32で発表された、[SQL Injection Isn’t Dead - Smuggling Queries at the Protocol Level](https://media.defcon.org/DEF%20CON%2032/DEF%20CON%2032%20presentations/DEF%20CON%2032%20-%20Paul%20Gerste%20-%20SQL%20Injection%20Isn%27t%20Dead%20Smuggling%20Queries%20at%20the%20Protocol%20Level.pdf)という発表に着想を得て、様々なバイナリベースのプロトコルを調査していた際に得た知見をベースとして作成した問題となります。

この問題は、不適切なFastCGI実装によるRequest Smugglingを行うという趣旨のもので、FastCGIのヘッダの「contentLength」が16ビットであることを利用して、Integer Overflowを発生させてコンポーネント間の解釈を混乱させ、本来フィルタリングされているヘッダ値を設定するのがゴールとなります。

実際に問題のソースコードを読んでいきましょう。

ディレクトリ構造としては、以下のようになっています。

```
.
├── child
│   ├── child.go
│   └── Dockerfile
├── compose.yaml
├── nginx.conf
└── server
    ├── Dockerfile
    ├── fcgi.go
    ├── go.mod
    └── main.go
```

まず着目するべきは「nginx.conf」です。nginxの設定ファイルを確認すると、以下のように「$http\_givemeflag」が設定されている場合にリクエストが拒否されることがわかります。

つまり、この問題のゴールはどうにかして「Givemeflag」ヘッダをバックエンド側に送信することであると推測できます。

`nginx.conf`

```
events {
    worker_connections 1024;
}

http {
    server {
        listen 80;
        server_name localhost;

        # Block requests containing GiveMeFlag in headers
        if ($http_givemeflag) {
            return 403;
        }

        # Forward all other requests to port 9090
        location / {
            proxy_pass http://server:9090;
        }
    }
}
```

実際、「child」側のコードを確認すると、以下のように「HTTP\_GIVEMEFLAG」が「true」の場合にフラグを送信するようになっていることがわかります。

`child/child.go` 126行目～139行目

```
func handleRequest(params map[string]string, body []byte) string {

	if params["HTTP_GIVEMEFLAG"] == "true" {
		return "Content-type: text/plain\r\n\r\nOh, you want the flag? Here you go: " + os.Getenv("FLAG")
	}

	response := fmt.Sprintf("Content-type: text/plain\r\n\r\nReceived FastCGI Request\n\nParams:\n")
	for key, value := range params {
		response += fmt.Sprintf("%s: %s\n", key, value)
	}
	response += fmt.Sprintf("\nBody length: %d\n", len(body))

	return response
}
```

そして、「server」側のコンポーネントを確認すると、以下のようにFastCGIのサーバーが動作していることがわかります。

`server/main.go` 156行目～171行目

```
func main() {

        server := NewFastCGIServer(
                "child:9000", // FastCGI application address
        )

        // Create HTTP server
        http.Handle("/", server)

        slog.Info("Starting server on :9090")
        if err := http.ListenAndServe(":9090", nil); err != nil {
                slog.Error("Failed to start server", "error", err)
        }
}
```

後続の処理を確認すると、以下のように「child」に対してFastCGIプロトコルによるリクエストを送信しているように見受けられます。

`server/main.go` 24行目～127行目

```
func (s *FastCGIServer) ServeHTTP(w http.ResponseWriter, r *http.Request) {

        if r.Header.Get("Givemeflag") != "" {
                w.Header().Set("Content-Type", "text/plain")
                w.WriteHeader(http.StatusForbidden)
                w.Write([]byte("You are not allowed to access this resource"))
                return
        }

        // Create FastCGI client
        client, err := NewClient("tcp", s.FcgiAddr)
        if err != nil {
                http.Error(w, "Failed to connect to FastCGI application", http.StatusBadGateway)
                slog.Error("FastCGI connection error", "error", err)
                return
        }

        [...]

        // Send request to FastCGI application
        response, err := client.Do(fcgiReq)
        if err != nil {
                http.Error(w, "Failed to process request", http.StatusBadGateway)
                slog.Error("FastCGI request error", "error", err)
                return
        }
        [...]
}
```

「ServeHTTP」の最初の方に「r.Header.Get(“Givemeflag”)」が空でなければエラーを返すという処理が存在するため、「nginx -> server」間ではRequest Smugglingによるヘッダの挿入をしても特に意味がないことがわかります。

ということで、次は「server -> child」間でどういった処理が行われているのかを確認していきます。

「server」内の「fcgi.go」というファイルを見ると、FastCGIを自前で実装している様子が確認できます。

`server/fcgi.go` 12行目～37行目

```
const (
	FCGI_BEGIN_REQUEST = 1
	FCGI_ABORT_REQUEST = 2
	FCGI_END_REQUEST   = 3
	FCGI_PARAMS        = 4
	FCGI_STDIN         = 5
	FCGI_STDOUT        = 6
	FCGI_STDERR        = 7
	FCGI_DATA          = 8

	FCGI_RESPONDER = 1
	FCGI_VERSION_1 = 1
)

type header struct {
	Version       uint8
	Type          uint8
	RequestID     uint16
	ContentLength uint16
	PaddingLength uint8
	Reserved      uint8
}

type Client struct {
	conn net.Conn
}
```

この実装を読んでいくと、一箇所おかしなところが見つかります。

`server/fcgi.go` 130行目～158行目

```
func (c *Client) writeStdin(requestID uint16, content []byte) error {
	contentSize := len(content)

	h := header{
		Version:       FCGI_VERSION_1,
		Type:          FCGI_STDIN,
		RequestID:     requestID,
		ContentLength: uint16(contentSize),
		PaddingLength: 0,
	}
	[...]
}
```

本来、「contentLength」の上限に引っかからないように分割で送信されるべき「FCGI\_STDIN」レコードが、一切分割されずに送信されているではありませんか。
「content」は、送信するべきリクエストボディそのものであるため、「uint16」の上限を超えてしまうとオーバーフローが発生して本来のレコード長とは異なる値が送信されてしまうことになります。

後続の処理を確認すると、特に「content」を切り捨てたりせずにそのまま送信していることが確認できます。

`server/fcgi.go` 145行目～147行目

```
	if _, err := c.conn.Write(content); err != nil {
		return err
	}
```

つまり、例えば65537バイトのリクエストボディを「server」に向けて送信すると、「FCGI\_STDIN」レコードの「contentLength」が1になった状態で、65537バイトのリクエストボディが「child」へ送信されることになります。

「child」側のコードを確認すると、「contentLength」の値を元にレコード内容を読み取っています。

`child/child.go` 52行目～57行目

```
		if err := binary.Read(reader, binary.BigEndian, h); err != nil {
			if err != io.EOF {
				slog.Error("Error reading header", "error", err)
			}
			return
		}
```

前述のようにInteger Overflowが発生すると、本来読まれるべきボディの長さよりも短いバイト数が読まれ、後続のレコードとしてパースするようになってしまいます。

これにより、細工したリクエストボディを送信することで、任意の種別のFastCGIレコードを任意の内容で送ることが可能となります。

例えば、以下のようなリクエストボディを送信すると、先頭の「a」のみがリクエストボディとして扱われ、その後の「\x01」以降が別のレコードとして扱われます。

```
a\x01\x04\x00\x01\x00\x15\x00\x00\x0f\x04HTTP_GIVEMEFLAGtrue\x01\x05\x00\x01\x00\x00\x00\x00[65499バイトのa]
```

ここでは、「\x04」 (FCGI\_PARAMS)として解釈され、「HTTP\_GIVEMEFLAG」が「true」に設定されます。
「true」の後の「\x01\x05…」は0バイトの「FCGI\_STDIN」レコードであり、「FCGI\_STDIN」の終端として解釈されます。

nginxやserverの時点ではリクエストボディとして解釈されているため、前述のフィルタリングには引っかかりません。
これにより、「child」に対して「HTTP\_GIVEMEFLAG」を送信し、「child」からフラグを返させることが可能となります。

## not-that-short

この問題のコンセプトは、「NELで問題を練る！」です。
問題を作問する数ヶ月前に、バグバウンティで報告した脆弱性を元に作問したもので、[Network Error Logging](https://web.dev/articles/network-error-logging) を用いることによって、同一ドメイン上に送信されたリクエストのクエリパラメーターをリークするという趣旨の問題です。

決勝戦で出題した問題は、リファクタリング時にミスをしてしまったために部分的な非想定解が存在しました。ここでは、後日[修正して公開したバージョン](https://not-that-short.pages.dev/)を元に解説を行います。

この問題は大きく分けて4段階に分かれているため、一つ一つ見ていきます。
ファイル構造は以下のとおりです。

```
.
├── admin
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── server.py
│   └── utils
│       ├── auth.py
│       └── utils.py
├── app
│   ├── config
│   │   └── database.py
│   ├── Dockerfile
│   ├── handlers
│   │   └── http_handler.py
│   ├── models
│   │   └── url.py
│   ├── requirements.txt
│   ├── server.py
│   ├── services
│   │   └── shortener.py
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   ├── index.html
│   │   └── js
│   │       └── main.js
│   └── utils
│       ├── auth.py
│       ├── token.py
│       └── utils.py
├── auth
│   ├── Dockerfile
│   ├── package.json
│   ├── package-lock.json
│   ├── server.js
│   └── views
│       ├── home.ejs
│       ├── login.ejs
│       └── register.ejs
├── bot
│   ├── bot.js
│   ├── Dockerfile
│   ├── index.j...
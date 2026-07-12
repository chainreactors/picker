---
title: 第31篇 全栈AI Web流量分析、冰蝎解密、Java内存马排查与Fastjson漏洞利用全流程
url: https://mp.weixin.qq.com/s/CS9Cb1NtgKcYAWEyFKex8w
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:08:42.479152
---

# 第31篇 全栈AI Web流量分析、冰蝎解密、Java内存马排查与Fastjson漏洞利用全流程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MaPMjrvzf7dia1icVqKBbw9tI4PzzWLFB792nqXg8gScMW8Db80kHVwPTTSH70jGD8baLNdBkURU0NmRY4sVPsO3lBbU8NlE05RfN9oJGicKvI/0?wx_fmt=jpeg)

# 第31篇 全栈AI Web流量分析、冰蝎解密、Java内存马排查与Fastjson漏洞利用全流程

原创

陈看山
陈看山

安全诸子

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

内容总结

本次教学围绕三道网络安全CTF题目展开，依次讲解Web流量包分析提取冰蝎WebShell、本地导出Java类文件排查隐藏内存马、Fastjson漏洞关联哥斯拉流量解密获取Flag的完整实操步骤，同时补充了自定义加密WebShell流量无法解密的核心限制条件。

![网络安全CTF实操教学](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MaPMjrvzf7cQd97HuEAYXmSY57QtQxMnl19R23jyM7tr5aiaIrWiakxUSjB9gpaN3n5hicjz7t3XDbVcwwSVGWXy0tcDIozB9UHg55ZHPcyEXo/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaX5oD1Bgk6NMQDadCzSN1MZk6pyCMWFoSv48dulWC0Ah02JAyZicV4jv0U5u30WqbGWyd1mVOYicsiaw/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaXqWLwTRoib4mcGgQXe0uyNThsTjomPqsr7lykET2zWiaFzsWHjpAsgwudB4rFxf4155TF9jETjPHpQ/640?from=appmsg)

Web流量包基础过滤与框架识别

* HTTP流量过滤技巧：Web攻防场景中90%的流量包都属于HTTP协议流量，拿到流量包后优先过滤HTTP协议，可以快速缩小分析范围，跳过无关冗余数据。
* Tomcat框架识别方法：在流量包的info字段中发现manager.html路径，结合Tomcat默认的manager后台管理特征，可直接判定目标服务为Tomcat架构。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaX5oD1Bgk6NMQDadCzSN1MZk6pyCMWFoSv48dulWC0Ah02JAyZicV4jv0U5u30WqbGWyd1mVOYicsiaw/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaXqWLwTRoib4mcGgQXe0uyNThsTjomPqsr7lykET2zWiaFzsWHjpAsgwudB4rFxf4155TF9jETjPHpQ/640?from=appmsg)

Tomcat认证信息提取

* Authorization字段解密规则：Tomcat的manager后台登录认证，要求在authorization字段中传入经过base64encode编码的「账号:密码」格式字符串，直接对该字段内容解码即可获取明文凭证。
* 实战提取结果：本次流量包中解码得到的登录账号为Admin，对应密码为admin23，可直接用于Tomcat后台登录操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaX5oD1Bgk6NMQDadCzSN1MZk6pyCMWFoSv48dulWC0Ah02JAyZicV4jv0U5u30WqbGWyd1mVOYicsiaw/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaXqWLwTRoib4mcGgQXe0uyNThsTjomPqsr7lykET2zWiaFzsWHjpAsgwudB4rFxf4155TF9jETjPHpQ/640?from=appmsg)

WebShell路径定位

* 访问特征判定方法：攻击者会高频持续访问上传的WebShell路径，统计流量包中重复请求次数最多的JSP文件，即可精准定位WebShell位置。
* 实战定位结果：本次流量中攻击者反复访问testtest.jsp路径，该文件就是攻击者上传的核心WebShell。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaX5oD1Bgk6NMQDadCzSN1MZk6pyCMWFoSv48dulWC0Ah02JAyZicV4jv0U5u30WqbGWyd1mVOYicsiaw/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaXqWLwTRoib4mcGgQXe0uyNThsTjomPqsr7lykET2zWiaFzsWHjpAsgwudB4rFxf4155TF9jETjPHpQ/640?from=appmsg)

WebShell文件导出操作

* 上传包定位逻辑：通过manager POST upload路径筛选Tomcat的文件上传请求，在所有上传包中选择体积最大的那个，即可找到完整的WebShell上传数据。
* 二进制导出步骤：在流量包的form data字段中找到3025字节的二进制上传内容，右键导出分组字节点到本地，将导出的二进制文件后缀名修改为.zip即可正常解压。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaX5oD1Bgk6NMQDadCzSN1MZk6pyCMWFoSv48dulWC0Ah02JAyZicV4jv0U5u30WqbGWyd1mVOYicsiaw/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaXqWLwTRoib4mcGgQXe0uyNThsTjomPqsr7lykET2zWiaFzsWHjpAsgwudB4rFxf4155TF9jETjPHpQ/640?from=appmsg)

WebShell MD5值计算

* 文件解压验证：解压修改后缀后的压缩包，可得到testtest.jsp和shellTest.jsp两个JSP文件，结合攻击者高频访问的路径，确定目标文件为testtest.jsp。
* 哈希值计算方式：使用MD5工具或server uto工具，直接对导出的testtest.jsp文件进行哈希运算，即可得到题目要求的WebShell MD5值。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaX5oD1Bgk6NMQDadCzSN1MZk6pyCMWFoSv48dulWC0Ah02JAyZicV4jv0U5u30WqbGWyd1mVOYicsiaw/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaXqWLwTRoib4mcGgQXe0uyNThsTjomPqsr7lykET2zWiaFzsWHjpAsgwudB4rFxf4155TF9jETjPHpQ/640?from=appmsg)

冰蝎WebShell加密参数解密

* 加密参数获取：打开导出的冰蝎WebShell源码，可直接读取到加密密钥为`CC031DC30317`，通过在线MD5解密工具可破解得到明文密码为test123。
* 反向流量分析技巧：将HTTP流量包按照number序号倒序排序，使用ABC蓝队分析工具导入冰蝎3的解密规则，填入密钥和明文密码，定位到分组1093的有效对话。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaX5oD1Bgk6NMQDadCzSN1MZk6pyCMWFoSv48dulWC0Ah02JAyZicV4jv0U5u30WqbGWyd1mVOYicsiaw/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaXqWLwTRoib4mcGgQXe0uyNThsTjomPqsr7lykET2zWiaFzsWHjpAsgwudB4rFxf4155TF9jETjPHpQ/640?from=appmsg)

冰蝎流量解密获取Flag

* 解密结果验证：对分组1093的冰蝎流量执行解密操作，可直接得到明文命令`echo flagHex go go go go2026`，该字符串即为第一道题目的最终答案。

![Java内存马排查实操](https://mmbiz.qpic.cn/mmbiz_jpg/MaPMjrvzf7cezKQlnfcFkE2ogFwn6s8yzS7tpelAOic9vbz9bHG6CuSCIUAbhw0zUtNx8Uy6pVkZezZy0xJibyC47FicLkh6yAI08u4v32ZQ3g/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaX5oD1Bgk6NMQDadCzSN1MZk6pyCMWFoSv48dulWC0Ah02JAyZicV4jv0U5u30WqbGWyd1mVOYicsiaw/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaXqWLwTRoib4mcGgQXe0uyNThsTjomPqsr7lykET2zWiaFzsWHjpAsgwudB4rFxf4155TF9jETjPHpQ/640?from=appmsg)

Java内存马两种排查思路

* 在线内存排查方式：通过SC新点filter、SC新点CIVILI命令直接进入Tomcat内存空间，遍历所有加载的Java类进行人工排查，该方式操作难度相对较高。
* 本地导出分析方式：通过已获取的WebShell环境，将服务器上所有已加载的Java类文件批量导出到本地，使用编辑器全局搜索敏感关键字，排查效率远高于在线命令行操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaX5oD1Bgk6NMQDadCzSN1MZk6pyCMWFoSv48dulWC0Ah02JAyZicV4jv0U5u30WqbGWyd1mVOYicsiaw/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaXqWLwTRoib4mcGgQXe0uyNThsTjomPqsr7lykET2zWiaFzsWHjpAsgwudB4rFxf4155TF9jETjPHpQ/640?from=appmsg)

本地Java类批量排查实操

* 编辑器筛选方法：使用Sublime或IDEA编辑器打开导出的Java类文件夹，按下`Ctrl+Shift+F`快捷键执行全局搜索，可快速定位包含敏感关键字的类文件。
* 查杀工具辅助验证：使用D盾WebShell查杀工具对所有导出类文件进行扫描，仅发现being serializer modifier存在异常，但该文件并非题目要找的目标内存马本体。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaX5oD1Bgk6NMQDadCzSN1MZk6pyCMWFoSv48dulWC0Ah02JAyZicV4jv0U5u30WqbGWyd1mVOYicsiaw/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaXqWLwTRoib4mcGgQXe0uyNThsTjomPqsr7lykET2zWiaFzsWHjpAsgwudB4rFxf4155TF9jETjPHpQ/640?from=appmsg)

敏感关键字定位隐藏内存马

* 核心搜索关键词：依次全局搜索Secret、AES、decode、CRYPTO、DECREPT等加解密相关关键字，可快速命中目标异常类文件。
* 特征匹配验证：命中的类文件中包含request、response、session等Web请求处理相关字段，完全符合内存马处理会话的典型代码特征。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaX5oD1Bgk6NMQDadCzSN1MZk6pyCMWFoSv48dulWC0Ah02JAyZicV4jv0U5u30WqbGWyd1mVOYicsiaw/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaXqWLwTRoib4mcGgQXe0uyNThsTjomPqsr7lykET2zWiaFzsWHjpAsgwudB4rFxf4155TF9jETjPHpQ/640?from=appmsg)

Base64加密类文件还原

* 解密代码编写：类文件中存在一串超长的Base64加密字符串，不推荐使用在线工具解密，自行编写Python解密脚本执行后，可得到名为reload.class的二进制类文件。
* 反编译查看源码：将reload.class文件导入JAD反编译工具，即可得到完整可读的Java源代码，源码中直接暴露了题目要求的secret key参数。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaX5oD1Bgk6NMQDadCzSN1MZk6pyCMWFoSv48dulWC0Ah02JAyZicV4jv0U5u30WqbGWyd1mVOYicsiaw/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaXqWLwTRoib4mcGgQXe0uyNThsTjomPqsr7lykET2zWiaFzsWHjpAsgwudB4rFxf4155TF9jETjPHpQ/640?from=appmsg)

Fastjson漏洞流量分析

* 攻击特征识别：流量包中大量出现`POST /json`请求，结合Fastjson漏洞的典型利用特征，可判定攻击者使用Fastjson漏洞发起攻击，payload中包含哥斯拉内存马和ABC标准利用链。
* 攻击流程梳理：攻击者先发送大量GET请求进行目录爆破探测，后续通过Fastjson漏洞成功拿下服务器权限，最终使用bteam.ico路径作为哥斯拉内存马的维持路径。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaX5oD1Bgk6NMQDadCzSN1MZk6pyCMWFoSv48dulWC0Ah02JAyZicV4jv0U5u30WqbGWyd1mVOYicsiaw/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaXqWLwTRoib4mcGgQXe0uyNThsTjomPqsr7lykET2zWiaFzsWHjpAsgwudB4rFxf4155TF9jETjPHpQ/640?from=appmsg)

哥斯拉流量解密规则

* 握手阶段流量特征：哥斯拉建立连接的三次握手包体积依次变化，第一个包体积最大，包含完整的服务器环境和Java信息；第二个包用于服务端返回session完成验证；第三个包返回服务器环境变量信息。
* 解密参数配置：使用ABC蓝队分析工具导入哥斯拉Java解密规则，将pass参数修改为1024，使用默认密钥即可对加密流量进行解密。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaX5oD1Bgk6NMQDadCzSN1MZk6pyCMWFoSv48dulWC0Ah02JAyZicV4jv0U5u30WqbGWyd1mVOYicsiaw/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaXqWLwTRoib4mcGgQXe0uyNThsTjomPqsr7lykET2zWiaFzsWHjpAsgwudB4rFxf4155TF9jETjPHpQ/640?from=appmsg)

哥斯拉命令执行流量解密

* 有效包筛选方法：跳过握手阶段的大体积流量包，选择后续体积较小的命令执行包进行解密，可直接得到明文命令内容。
* 实战解密结果：解密后的命令为`echo flag fast json rce by never show`，该字符串即为Fastjson分析题目的最终Flag答案。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaX5oD1Bgk6NMQDadCzSN1MZk6pyCMWFoSv48dulWC0Ah02JAyZicV4jv0U5u30WqbGWyd1mVOYicsiaw/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/I1fyHmvzZiaXqWLwTRoib4mcGgQXe0uyNThsTjomPqsr7lykET2zWiaFzsWHjpAsgwudB4rFxf4155TF9jETjPHpQ/640?from=appmsg)

WebShell流量解密通用规则总结

* 开源框架解密前提：冰蝎、哥斯拉这类公开开源的WebShell，可通过反编译其Java源码获取完整加解密逻辑，填入正确的password和secret参数后即可完成流量解密。
* 自定义加密流量限制：如果攻击者使用自行修改加

![Fastjson漏洞利用分析](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MaPMjrvzf7emvBaCK21WicdCCYsrUj7uaK2oNsHnTMHvLMcqyrLfVKQDpVNe9AajdkuQJLibqVicNwBHBE9RjzAyycyWK7EVTicw5evcGiclFEbw/640?from=appmsg)

![](https://mmbiz.qpic...
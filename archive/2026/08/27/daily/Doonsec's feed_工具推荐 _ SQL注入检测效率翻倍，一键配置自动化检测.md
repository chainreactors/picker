---
title: 工具推荐 | SQL注入检测效率翻倍，一键配置自动化检测
url: https://mp.weixin.qq.com/s/ccbJdlj-25HhGylyMxoiUg
source: Doonsec's feed
date: 2026-08-27
fetch_date: 2026-08-28T13:36:10.004762
---

# 工具推荐 | SQL注入检测效率翻倍，一键配置自动化检测

# 工具推荐 | SQL注入检测效率翻倍，一键配置自动化检测

JaveleyQAQ
JaveleyQAQ

星落安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/spc4mP9cfo75FXwfFhKxbGU93Z4H0tgt4O9libYH9mKfZdHgvke0CeibvXDtNcdaqamRk3dEEcRQiaWbGiacZ2waVw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

点击上方蓝字关注我们

![](https://mmbiz.qpic.cn/mmbiz_png/WN0ZdfFXY80dA2Z4y8cq7zy2dicHmWOIib5sIn8xAxRIzJibo2fwVZ3aicVBM8RnAqRPH5Libr4f02Zs5YnMLBcREnA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)

现在只对常读和星标的公众号才展示大图推送，建议大家能把**星落安全团队**“**设为星标**”，否则可能就看不到了啦！

【声明】本文所涉及的技术、思路和工具仅用于安全测试和防御研究，切勿将其用于非法入侵或攻击他人系统以及盈利等目的，一切后果由操作者自行承担！！！

![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllln8Wic8bXXhG32kroVKo4gU6tzImuia8ibpGL8tdsriaNsFLZJtUicibJa271C0Pd1Jwcjnsia0sIiaMjXS2w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&watermark=1&tp=webp#imgIndex=2)

***工具介绍***

SQL Injection Scout 是一个用于 Burp Suite 的扩展，专为帮助安全研究人员和开发人员检测和分析 SQL 注入漏洞而设计。该扩展提供了丰富的配置选项和直观的用户界面，便于用户自定义扫描和分析过程。

![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0flllldvS8Gbw7IEPNj4GYlcAl8E6PiafzfsZL8J7QY4j6Olzusicaia44qMVj4VJ3fn0fRMynxopTNaLzXQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=3)

功能特性

* **被动检测SQL**

  ：支持对除`OPTIONS`外的所有请求的参数进行 `FUZZ` 测试，支持 `XML`、`JSON`、`FORM`等表单数据格式。
* **最小化探测**

  ：通过最小化的 `payload` 探测，减少对目标的影响。
* **响应差异分析**

  ：对响应进行 `diff` 分析，自动标记无趣（灰色）和有趣（绿色）的响应。

+ ....
+ **判断原理**

  ：假设页面参数为反射类型，通过比较 `payload` 和 `diff` 的长度，相同则认为无趣。
+ **重复内容过滤**

  ：对绿色标记的分组进行进一步分析，出现`6`次以上重复的 `diff` 被标记为无趣。
+ **结果排序**

  ：根据颜色对最终结果进行排序展示。

+ **✅：标记为值得进一步分析的响应。**
+ **🔥：标记为存在Sql注入**
+ **`Error`：标记为检测到`SQL Error`信息存在`Response`中**
+ **`Max Params`：标记为请求参数大于配置数**
+ **`Skip URL`：匹配配置中需绕过的URL**

* **自动匹配**

  ：在扫描页面的响应中自动匹配 `diff` 结果，默认取第一处的差异。
* **正则匹配**

  ：正则匹配无需扫描的`URL`
* **内置范围**

  ：支持内置的 `scope` 范围设置。
* **延时扫描**

  ：支持固定抖动+随机抖动发包检测，更精准规避 `WAF`。
* **自定义扫描参数数量**

  ：防止参数过多导致的性能问题或误报，默认`50`
* **🔥 Fuzz隐藏参数SQL注入**

  : 支持用户在原始请求中追加隐藏参数列表，进行`FUZZ`测试
* 在`Site map`/`HTTP history`/`Logger`面板添加右键菜单，支持检测站点**单个**与**所有**请求

+ （搭配CaA使用本插件的`Fuzz Params List`功能）

使用指南

1. 启动 Burp Suite 并确保 SQL Injection Scout 扩展已加载。
2. 在 `Extender` 选项卡中，找到 SQL Injection Scout 并打开其配置面板。
3. 根据需要调整参数和模式设置。
4. 使用 Burp Suite 的代理、扫描器等功能进行测试，SQL Injection Scout 将自动应用配置并提供结果。

![](https://mmbiz.qpic.cn/mmbiz_png/rlSBJ0flllldvS8Gbw7IEPNj4GYlcAl8Cylx0uv4YJWUiaVHRiaw3vpmhUaYH3cuaw4FCs9D1h8dzuSLwajhNiaoA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=4)

***相关地址***

****关注微信公众号后台回复“****入群****”，即可进入星落安全交流群！****

关注微信公众号后台回复“20260827**”，即可获取项目下载地址！**

***圈子介绍***

博主介绍：

目前工作在某安全公司攻防实验室，一线攻击队选手。自2022-2024年总计参加过30+次省/市级攻防演练，擅长工具开发、免杀、代码审计、信息收集、内网渗透等安全技术。

目前已经更新的免杀内容：

* 部分免杀项目源代码
* 星落安全内部免杀工具箱1.4.1
* GoCobaltStrike星落专版2.6.1

* 一键击溃windows defender
* 一键击溃火绒进程
* CobaltStrike免杀加载器
* 数据库直连工具免杀版
* aspx文件自动上线cobaltbrike
* jsp文件自动上线cobaltbrike
* 哥斯拉免杀工具 XlByPassGodzilla
* 冰蝎免杀工具 XlByPassBehinder
* 冰蝎星落专版 xlbehinder
* 正向代理工具 xleoreg
* 反向代理工具xlfrc
* 内网扫描工具 xlscan

* Todesk/向日葵密码读取工具
* 导出lsass内存工具 xlrls
* 绕过WAF免杀工具 ByPassWAF
* 等等...

![图片](https://mmbiz.qpic.cn/mmbiz_png/DWntM1sE7icZvkNdicBYEs6uicWp0yXACpt25KZIiciaY7ceKVwuzibYLSoup8ib3Aghm4KviaLyknWsYwTHv3euItxyCQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=9)

目前星球已满1100人，价格由208元调整为218元(交个朋友啦)，1200名以后涨价至268元。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaHtVP5bJUquz5ian4B4GRzI1sdB85DTOfLUUlzFh5ueQGkrYtELaxnhJmHadKXaxzmTGZFG8ETu4v5GsyIB3yXoU5ic0icc8tibKSg/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=17)

![图片](https://mmbiz.qpic.cn/mmbiz_png/MuoJjD4x9x3siaaGcOb598S56dSGAkNBwpF7IKjfj1vFmfagbF6iaiceKY4RGibdwBzJyeLS59NlowRF39EPwSCbeQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=11)

往期推荐

1.[加量不加价 | 星落免杀第二期，助你打造专属免杀武器库](https://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247495969&idx=1&sn=d3379e8f69c2cefb6d0564299e13d579&scene=21#wechat_redirect)

2.[【干货】你不得不学习的内网渗透手法](https://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247489483&idx=1&sn=0cbeb449e56db1ae48abfb924ffd0b43&scene=21#wechat_redirect)

3.[新增全新Web UI版本，操作与管理全面升级 | GoCobalt Strike 2.0正式发布！](https://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247497899&idx=1&sn=018f02ef4064930cbcb40d6b0495e136&scene=21#wechat_redirect)

4.[【免杀】原来SQL注入也可以绕过杀软执行shellcode上线CoblatStrike](http://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247489950&idx=1&sn=a54e05e31a2970950ad47800606c80ff&chksm=c0e2b221f7953b37b5d7b1a8e259a440c1ee7127d535b2c24a5c6c2f2e773ac2a4df43a55696&scene=21&token=458856676&lang=zh_CN#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/DWntM1sE7icZvkNdicBYEs6uicWp0yXACpt25KZIiciaY7ceKVwuzibYLSoup8ib3Aghm4KviaLyknWsYwTHv3euItxyCQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=12)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllT7yxybzslhp8mC8ibaTia9STZtOXaUjfJbHfLJzPAAs44YKKbWvBj9YPicLA34xgAFpXMfB3SaUnUQ/0?wx_fmt=png)

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
---
title: SRC漏洞挖掘新手入门指南：怎么挖、去哪挖？一篇文章带你零基础入门到精通！
url: https://mp.weixin.qq.com/s/zX6Ie2KIzY3O4BTGjoKK5Q
source: Doonsec's feed
date: 2026-08-18
fetch_date: 2026-08-19T02:53:43.614280
---

# SRC漏洞挖掘新手入门指南：怎么挖、去哪挖？一篇文章带你零基础入门到精通！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbWEHMerrBaW2qhekCVlaE8HYViavsfzYQaFJCk5msAKHjG62wGEYmMGzSmhvQ2X82zzO7c4mCEGqUn5QzdQpOSk6lNLhbKGicvhRJYXnGGmI/0?wx_fmt=jpeg)

# SRC漏洞挖掘新手入门指南：怎么挖、去哪挖？一篇文章带你零基础入门到精通！

编程技术栈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

前言

经常会有粉丝朋友私信我，想探究一下国内的SRC（安全响应中心）平台究竟支持了多少白帽黑客的生活？又有多少白帽黑客能够不依赖于传统工作，全职从事漏洞挖掘并以此维生？以下信息或许可以为那些有意踏上这条道路的朋友们提供一些宝贵的参考。

SRC，即安全响应中心（Security Response Center），是一个组织或者公司用来接收和处理安全漏洞报告的平台。对于网络安全新手来说，快速挖掘SRC漏洞并报告是一个挑战，但也是一个提升技能和知识的良好机会。以下是一些个人挖掘SRC的一些经验之谈，希望可以帮助新手快速上手SRC漏洞挖掘。

* 如果觉得光看文章过于晦涩难懂
* 可以点击这里【[技术教程](https://mp.weixin.qq.com/s?__biz=MzkxNDU0MTUyNw==&mid=2247494403&idx=1&sn=1d4ce60c23b90e678185809c683996d7&scene=21#wechat_redirect)】查收网络安全&漏洞挖掘全套视频教程以及配套电子书哦！

![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6YnBvoBcYkTTI0Y33jWrhI1SBEMKCr5ibNzYibPVcMZ5MKdITVyW8CTxUkNyYiaPMEeOUxBvIj9Hc1CnVZNXSMZMA/640?wx_fmt=jpeg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

一、个人经验

个人最初挖掘前期感受

我挖掘SRC没有怎么挖过公益，也没有怎么挖掘过edu，就直接跳到企业SRC了。一开始也是不知道从何入手，在网上看了很多文章感觉自己学会了，自己挖的时候一挖就废，况且在2026年的安全行业如此“卷”的情况下，各个企业、公益、edu等SRC都被好多大佬刷了一遍又一遍，觉得自己肯定没戏，挖不倒漏洞，赚不到赏金，想着就直接放弃，前期感受估计都是和大多数师傅一样，看了成百上千个资产挖不到一个漏洞、要不就是提交的漏洞是重复、危害不足、内部已知。以上现象重复多了越挖越没信心。慢慢地就放弃对挖洞的热爱，开始摆烂人生。

就我个人而言，前期也是大多是挖一些低危漏洞，甚至前几个月经常挖的都是低危，中危都没有。其实对于低危漏洞来说前期对于新手是很重的，通过一个低危漏洞不仅收获了赏金（虽然钱不多），最重要的事给了你信心。可以在SRC挖掘道路上继续前行。我个人挖掘逻辑漏洞比较多，我前期挖的比较多的漏洞比如swagger未授权，spring未授权等其他各类未授权，并发漏洞，反射XSS、信息泄露、验证码问题、用户名枚举、爆破、短信轰炸等这类漏洞挖掘较多。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbWEHMerrBbvxuaWZDJ1jMHiaAdtkaW53hc6NY6AZYOehZGEc3PItozQ908BhFXXLIOHGkbS0rB3IxlibRg5bLNiaibickCiczQQd1tkIlaEib7ib1c/640?wx_fmt=jpeg&from=appmsg)

挖一段时间后对该企业SRC的资产也比较熟悉了，就要学会利用前期收集到的信息进行挖掘、比如用户名、邮箱、接口、系统框架CMS等信息

当然挖掘SRC要想有高产出，一定要仔细、慢慢地去分析、一个个数据包慢慢去看、要有耐心。每个参数要分析是干嘛用的，不要着急，越急估计越事与愿违。

这里个人觉得比较重要的一点就是，一定要熟悉你挖掘的企业SRC的资产。了解资产构成、他们的系统都喜欢用什么框架、什么CMS、是否统一认证、他们的账号密码是否大部分系统通用情况等等。很多信息这里不一一介绍了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbWEHMerrBaH9eFHiaragR5OxA7V5GkrfF1JSUCUFcR51LhFIxV6cp5jSfiasficRweljuFtz9QaLhib4xExpFqDHvxMm87RHiawJ8zEaQEc75Ac/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sbWEHMerrBa5aIPzHib9DmojEibFxA86y6ib7B7VcqUeI8wEEDdlDfvFBadXjPKFzf8SSOCF3ljMichlnTuKLf83cAM1KHTO26LicEsltiawY600A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sbWEHMerrBaAJSIHyM2pUEMtK0rCbCYpRQjdkVq27dqIJGG52ROLKn15Yo5JlZ3iaNJZL9N3UqNRiblVv3jlOicjtrtEMyDbsqbuztpRSDmUfY/640?wx_fmt=png&from=appmsg)

二、SRC挖掘路线规划

学习基础 时间：1周 ~ 2周：

① 了解基本概念：（SQL注入、XSS、上传、CSRF、一句话木马、等：可以通过Google搜索获取资料）为之后的WEB渗透测试打下基础。 ② 查看一些论坛的一些Web渗透资料，学一学案例的思路，每一个站点都不一样，所以思路是主要的。 ③ 学会提问的艺术，如果遇到不懂得要善于提问。

配置渗透环境 时间：3周 ~ 4周：

① 了解渗透测试常用的工具，例如（AWVS、SQLMAP、NMAP、BURP、中国菜刀等）。 ② 下载这些工具无后门版本并且安装到计算机上。 ③ 了解这些工具的使用场景，懂得基本的使用，推荐在Google上查找资料。

渗透实战操作 时间：约6周：

① 在网上搜索渗透实战案例，深入了解SQL注入、文件上传、解析漏洞等在实战中的使用。 ② 自己搭建漏洞环境测试，推荐DWVA，SQLi-labs，Upload-labs，bWAPP。 ③ 懂得渗透测试的阶段，每一个阶段需要做那些动作：例如PTES渗透测试执行标准。 ④ 深入研究手工SQL注入，寻找绕过waf的方法，制作自己的脚本。 ⑤ 研究文件上传的原理，如何进行截断、双重后缀欺骗(IIS、PHP)、解析漏洞利用（IIS、Nignix、Apache）等，参照：上传攻击框架。 ⑥ 了解XSS形成原理和种类，在DWVA中进行实践，使用一个含有XSS漏洞的cms，安装安全狗等进行测试。 ⑦ 了解一句话木马，并尝试编写过狗一句话。 ⑧ 研究在Windows和Linux下的提升权限，Google关键词：提权

经常逛网络安全有关的网站 时间：∞

① 例如：Freebuf、i春秋、安全客、安全类的微信公众号、google搜索。 ② 遇到有意义的文章可以转载到自己博客 熟悉Windows & Kali Linux系统 时间：2周 ~ 4周 ①了解Windows系统下的常用命令，如：ipconfig,nslookup,tracert,net,tasklist,taskkill等。 ② 熟悉Linux系统的常用命令，如：wget、mv、cd、rm、mkdir等。 ③ 熟悉Kali Linux系统下的常用工具。

学习服务器的安全配置 时间：4周左右

① 了解03、08、12系统下iis的基本配置，了解Win下的目录权限（例如iis写权限），建立一个简单的站点。 ② 了解Linux的运行权限、跨目录、文件夹权限，学会配置Linux Web服务器，并建立一个简单的站点。 ③ 使用自动化工具扫描已经建立好的站点，并利用Google学会修补漏洞。 ④ 学会打补丁、iptables限制端口、添加规则等。 ⑤ 下载一款waf软件，熟悉它的使用。

学习一些编程知识 时间：约8周

① 在w3cschool上学习html、php、数据库的基础，建议每一种学到第8节就可以了。 ② 学习Python（也可以是其他语言，但是强烈建议使用python）。要求学习：爬虫（基础）、多线程、文件操作、正则表达式（基础）还有一些常用的第三方库，可能需要安装pip。 ③ 利用python写一个简单的poc或者exp。 ④ 开发一些渗透时会用到的程序，例如：端口扫描等。 ⑤ 选择一个php框架进行学习，不要太深入。

学习代码审计 时间：4周 ~ 6周

① 了解代码审计的静态和动态方法，懂得分析程序。 ② 在乌云镜像里找到开源的漏洞程序，跟着学习分析方法，尝试自己分析3~5次代码。 ③ 了解web漏洞形成的原因，熟悉常见漏洞函数。

安全体系开发 时间：∞

① 开发一些安全工具，并将其开源，可以托管到码云或者github上，展示个人实力。 ② 建立自己的一套安全体系，拥有独立的思路方法。

三、挖漏洞前期准本工作

一些在线的搜索引擎网站：

（一）资产测绘引擎

> fofa资产测绘引擎：https://fofa.info/
>
> 鹰图资产测绘引擎：https://hunter.qianxin.com/shodan
>
> 资产测绘引擎：https://www.shodan.io/
>
> 360资产测绘引擎：https://quake.360.net/
>
> 零零信安资产测绘引擎：https://0.zone/
>
> 谷歌hacker语法：https://codeleading.com/article/8526777820/

以上的搜索引擎网站都是用来收集目标网站信息的一些网络空间资产测绘，可以帮助我们快速的定位到目标的资产，批量获取url进行漏洞挖掘！

（二）企业信息查询

> 爱企查：https://aiqicha.baidu.com
>
> 天眼查：https://www.tianyancha.com
>
> 企查查：https://www.qcc.com
>
> 小蓝本：https://www.xiaolanben.com

以上的网站是为了查询网站所属的企业的一些信息，为了方便在提交漏洞的时候填写详细联系方式和公司的地址。

（三）域名信息查询

> 爱站：https://www.aizhan.com
>
> 站长工具：https://tool.chinaz.com
>
> oneforall：https://github.com/shmilylty/OneForAll
>
> JSFinder：https://github.com/Threezh1/JSFinder
>
> subDomainsBrute：https://github.com/lijiejie/subDomainsBrute
>
> DNSdumpster：https://dnsdumpster.com/
>
> 在线域名爆破：http://z.zcjun.com
>
> 谷歌/必应：site:url.com

#网络安全#web安全#漏洞挖掘#渗透测试#安全SRC#网络安全技术#计算机#信息安全

四、网络安全学习干货

如果你也是零基础想转行网络安全，却苦于没系统学习路径、不懂核心攻防技能？光靠盲目摸索不仅浪费时间，还消磨自己信心。这份 360 智榜样学习中心独家出版《网络攻防知识库》专为转行党量身打造！

#### 01 **内容涵盖**

这份资料专门为零基础转行设计，19 大核心模块从 Linux 系统、Python 基础、HTTP协议等地基知识到 Web 渗透、代码审计、CTF 实战层层递进，攻防结合的讲解方式让新手轻松上手，真实实战案例 + 落地脚本直接对标企业岗位需求，帮你快速搭建转行核心技能体系！

![img](https://mmbiz.qpic.cn/mmbiz_png/sbWEHMerrBaoJqO9tkIHgGbiaEn0eLB0nC1CVfIEAFicMHfTEDDQjRY4oqt0CJNTibMSXCCbhoJgX3lCRZCHqIqgnvHwm0IsaXdSBu5VOPXgMA/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=17)

![img](https://mmbiz.qpic.cn/sz_mmbiz_gif/sbWEHMerrBZMDDrSNpicXnMXZiaE80AnFOojVbKdwKT8rqvFHFrhHiaH4KytZrZjkQhBO26dPlgarzW6pkGWHXEQyEApxGvMZPDv82AhDHTicibs/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=18)

`《网络安全/黑客技术入门学习大礼包》，可以扫描下方二维码免费领取！`

![图片](https://mmbiz.qpic.cn/mmbiz_png/sbWEHMerrBa1hoM9xlD96zZ8HZQib7TkHfBJicvrnjS7OIuEF36LgGSlCo0DbXFsUAibkvUrypfHWDIxicN7vbStB6acxJiaibkG5ickcw6qfzWG3M/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=19)

#### **02 知识库价值**

* **深度**

  ： 本知识库超越常规工具手册，深入剖析攻击技术的底层原理与高级防御策略，并对业内挑战巨大的APT攻击链分析、隐蔽信道建立等，提供了**独到的技术视角和实战验证过的对抗方案**。

* **广度**

  ： 面向企业安全建设的核心场景（渗透测试、红蓝对抗、威胁狩猎、应急响应、安全运营），本知识库覆盖了从攻击发起、路径突破、权限维持、横向移动到防御检测、响应处置、溯源反制的全生命周期关键节点，是**应对复杂攻防挑战的实用指南**。

* **实战性**

  ： 知识库内容源于**真实攻防对抗和大型演练实践**，通过详尽的攻击复现案例、防御配置实例、自动化脚本代码来传递核心思路与落地方法。

#### **03 谁需要掌握本知识库**

* 负责企业整体安全策略与建设的 **CISO/安全总监**

* 从事渗透测试、红队行动的 **安全研究员/渗透测试工程师**

* 负责安全监控、威胁分析、应急响应的 **蓝队工程师/SOC分析师**

* 设计开发安全产品、自动化工具的 **安全开发工程师**

* 对网络攻防技术有浓厚兴趣的 **高校信息安全专业师生**

#### **04** **部分核心内容展示**

#### **![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/sbWEHMerrBbm521YmH24M4NViaAjpf3d2R36bVszktBujguJ3W7Mu59uJqibu1khY8J1vUvUdsueNyehRBN0Fk6wShYx7sRC7WQEFIaacLCQc/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=20)**

360智榜样学习中心独家《网络攻防知识库》采用**由浅入深、攻防结合**的讲述方式，既夯实基础技能，更深入高阶对抗技术。

内容组织紧密结合攻防场景，辅以大量**真实环境复现案例、自动化工具脚本及配置解析**。通过**策略讲解、原理剖析、实战演示**相结合，是你学习过程中好帮手。

**1、网络安全意识**

**![图片](https://mmbiz.qpic.cn/mmbiz_png/sbWEHMerrBawd1g5syXxgy19pgtu2gW51LSao89FwWG6xBFmsupHeicDNuAJA3oDCp9C7KHGhEgw0lMIY6oyibScOj4QLRM5mia4kVU8gJ9aeo/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=21)**

**2、Linux操作系统**

**![图片](https://mmbiz.qpic.cn/mmbiz_png/sbWEHMerrBZElPaU3dTuibQpAcQQPjtyyo0UxahFAhic5TIFTlLFYNHxyK4hwzaAJ86XLSVrcBRWHyqI6YDibjW7y8Eiao3a3j3MbWCsHAC9mgk/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=22)**

**3、WEB架构基础与HTTP协议**

**![图片](https://mmbiz.qpic.cn/mmbiz_png/sbWEHMerrBZCic0BfbJ3r74hULJibQMCR0niaYicLKOLF62drfAicw76B8JlFvjmiaicY9tm10Bt583nZL2Av3e0mTCBSpyq2kFmCr41B9Kv9oJIDw/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=23)**

**4、Web渗透测试**

**![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/sbWEHMerrBYCe5AFPANKq1d176gxYpIDKNI9212MwibOJiaKsSg5BJlXMFrrfyODqshKrLVT19Q44IxN8RcMpQfm4ZBFF2Db8cEYQwsTNY3zc/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=24)**

**5、渗透测试案例分享**

**![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/sbWEHMerrBY6MyVAhmN3Wicfv1LZd4rqU7n9Bm5OqUG79iaHR7dQY0pd0Qkx35TJq0n8S1gtK7cV6BNxx7csYOZLxcyPM3swvRPcYrDJ2ZmpY/640?wx_fmt=png&from=a...
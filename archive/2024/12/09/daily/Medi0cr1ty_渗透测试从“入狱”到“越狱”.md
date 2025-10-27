---
title: 渗透测试从“入狱”到“越狱”
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODE3NTU1OQ==&mid=2247484452&idx=1&sn=16d3185d5a662c0695f5ebc2ec75081b&chksm=c067c30cf7104a1aa6aff2eba21164bde58f42974be41dc1ffb76b2fd8b8111c2028d04e085d&scene=58&subscene=0#rd
source: Medi0cr1ty
date: 2024-12-09
fetch_date: 2025-10-06T19:38:08.682683
---

# 渗透测试从“入狱”到“越狱”

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZiaGB6iaicqkWhYc7xzPDT3amNFI5lHNOOhOXGvLHvtQtIGHqo6IciaCySHausvqnBDICHiba2kHZicGebzZ3IdVqCVw/0?wx_fmt=jpeg)

# 渗透测试从“入狱”到“越狱”

原创

medi0cr1ty

Medi0cr1ty

记一次黑盒测试打坏目标系统“入狱”到docker逃逸并修复实现“越狱”的日站过程。提醒大家日站需谨慎，不然亲人两行泪～

**Part.01**

**起**

在测试时某公网系统发现弱口令，登陆上去后发现是一个设备管理类系统。第一时间锁定到一个上传接口，测试发现可以实现任意目录任意文件写。

![](https://mmbiz.qpic.cn/mmbiz_png/ZiaGB6iaicqkWhYc7xzPDT3amNFI5lHNOOhDN81l5OHvGKNng1yqVNoqkI5PCoNHMBZofw4IQt3pDAukoJicmwbqDg/640?wx_fmt=png&from=appmsg)

尝试向其 ssh 目录写 ssh key，写计划任务发现均未成功。

springboot项目，参考前人思路尝试利用懒加载向 JDK 目录写入 charsets.jar ，但并未触发成功，起初无法确定是权限低还是 jdk 目录没写对，后续通过别的功能列目录确认 charsets.jar 写入成功，仍未执行猜测是已经加载过了。

![](https://mmbiz.qpic.cn/mmbiz_png/ZiaGB6iaicqkWhYc7xzPDT3amNFI5lHNOOh61mZDYWUPicacj9EjS3rYlC9greNPgfKcWeDLaNCCxGoJhNrAjbdWlQ/640?wx_fmt=png&from=appmsg)

**Part.02**

**承**

写文件的点无思路后转向其他功能，发现了任意文件读，列目录等，可惜测试随手试了下lic文件上传的点，传完整个系统所有页面就直接提示lic无效，也就是说手贱一下把别人系统打坏掉了......成功入狱- ^ -。

发现读文件和列目录以及测lic的过程是同步的，并未先把代码读到本地，事情陷入僵局。此刻漏洞也已经不是最重要的了，想办法恢复lic，让该系统正常运转才是重点。

扫描目标服务器的其他端口，发现除了22以及目标端口外，并未开放其他服务，爆破ssh未果，重新回到目标服务的测试上，从以往白盒的经验上来看，lic检查和登陆态检查一样，不应该所有路径都限制死，肯定有加白的路径，或者验证方式有问题，那就还有戏。

经过一顿黑盒 fuzz 方式发现和猜想一致，使用/static/..;/ 可绕过部分接口的lic检查 ，此前读写文件，列目录的接口也在范围内！

利用之前的点火速下载目标代码 ，验证该代码lic上传处的逻辑也很粗鲁，正常逻辑应该是先校验通过再覆盖原本的lic文件，而这个项目是先覆盖后校验，这也是直接导致系统被打坏的原因。同时也看到校验逻辑处确实通过 startWith 方式判断可导致绕过。

进一步在代码中看到 License 验证的逻辑：

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZiaGB6iaicqkWhYc7xzPDT3amNFI5lHNOOhH4j7FKplgJ1rn7ndUM3ggaleWPJm6PRCjdoeuRdGFWUeWsL13v1yXQ/640?wx_fmt=jpeg&from=appmsg)

在 Filter 中验证 license ，从 license 文件中取得机器码、  mac 地址与本地获取的验证判断。

license 文件中机器码、mac地址可通过某接口构造出 json 写入，这两个字段的值通过代码里逻辑发现可读固定目录文件获取到。

那我们已经有目标系统的任意文件读写的接口，有代码，按照校验逻辑反向编写lic生成代码即可，感觉恢复lic在望？

但... 实际测试时发现，读机器码：/sys/class/dmi/id/product\_serial 文件时

apache commons io组件报错：Unexpected read size. current: 37, expected: 4096 。预设的 buffer 缓冲值是 4096，而实际文件长度只读到 37 ，导致读取失败.... 奇怪的bug。

随后琢磨了这个文件的内容生成的逻辑，有无可能通过别的信息组合算出来等思路，尝试均无果。

**Part.03**

**转**

进一步代码分析并未发现其他可以恢复lic的点，将目标重新放回到机器本身，通过列文件的点仔细分析整个系统，期望找到某个会定时运行的脚本之类的功能实现rce。

重新列项目数据目录时注意到有docker-compose yml 文件，按理构建容器的文件不该出现在容器里面，读取后发现其将物理机的计划任务目录映射到了数据目录的 cron目录下：

![](https://mmbiz.qpic.cn/mmbiz_png/ZiaGB6iaicqkWhYc7xzPDT3amNFI5lHNOOhR8x61lPs2TWice8FS4TAjohmFRT0JhlxibpibPHKib24XMIAaEuszjwtMQ/640?wx_fmt=png&from=appmsg)

天赐逃逸！

![](https://mmbiz.qpic.cn/mmbiz_png/ZiaGB6iaicqkWhYc7xzPDT3amNFI5lHNOOhcj6O90HNfxNwobmsHlhKicn71Fd5YbiaRLia89S7eDqbbHvsfKFWbjRUw/640?wx_fmt=png&from=appmsg)

Part.**04**

**合**

写计划任务逃逸到物理机，然后重新进入容器，读取到机器码，按照检验算法构造出 Lic 并恢复了系统正常使用，越狱成功！

同样的漏洞还打了另外几台机器，也在其中一台机器的其历史命令中翻到 aksk，发现可控多个 ECS、OSS ，测试过程发生在非工作时间，也未有系统 lic 过期的投诉 ，到此整个过程告一段落。

后续分析了下common io读取product\_serial文件失败原因，此类文件是系统自动生成的虚拟文件，在linux系统中默认文件的块大小为4096，但由于没有自动填充与实际大小差异部分的字符串，导致common io获取预期和实际读取的字节数量不一致，进而导致报错。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZiaGB6iaicqkWgZe1vrPKR3r2nK86bn8RL2HDnIDFEaKzCPlQK7xaCdRWMhf1zcP8uuDpfEPJEVomeD43vvLljORQ/0?wx_fmt=png)

Medi0cr1ty

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZiaGB6iaicqkWgZe1vrPKR3r2nK86bn8RL2HDnIDFEaKzCPlQK7xaCdRWMhf1zcP8uuDpfEPJEVomeD43vvLljORQ/0?wx_fmt=png)

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
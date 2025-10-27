---
title: 【EFS的加密与解密】
url: https://mp.weixin.qq.com/s?__biz=MzAwNDcwMDgzMA==&mid=2651045186&idx=1&sn=6867465cecb00fab9193fea7ed9262b1&chksm=80d0f2b3b7a77ba5f3a1c1da05c1e51568eb52bd3c83541ff1f51a214b641fb8addab2f8e383&scene=58&subscene=0#rd
source: 电子物证
date: 2023-03-28
fetch_date: 2025-10-04T10:53:24.301427
---

# 【EFS的加密与解密】

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dDhDhftpRFsOibwEd74uXHVMBibic2N99aticWawHyQbRzaExZ1sYUb8zDSvliaiceCrDjEeC3YsWhMQm9kCiaa1G4nJg/0?wx_fmt=jpeg)

# 【EFS的加密与解密】

电子物证

![](https://mmbiz.qpic.cn/mmbiz_png/PqtlRibQeeRxTePY3fZIKskELbzG3Kgt7BzyG8Okus7Q6ibQSliaOib0kkJibVqPR1plgPb1fUApSSGm6wReRl1dSlA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**一**｜EFS简介

EFS（Encrypting File System，加密文件系统）是Windows操作系统中基于NTFS（New Technology
File
System，新技术文件系统）实现对文件进行加密与解密服务的一项技术。EFS采用核心文件加密技术，当文件或文件夹被加密之后，对于合法Windows用户来说不会改变其使用习惯。当操作经EFS加密后的文件时与操作普通文件没有任何区别，所有的用户身份认证和解密操作由系统在后台自动完成。而对于非法Windows用户来说，则无法打开经EFS加密的文件或文件夹。在多用户Windows操作系统中，不同的用户，可通过EFS加密自己的文件或文件夹，实现对重要数据的安全保护。

![](https://mmbiz.qpic.cn/mmbiz_png/PqtlRibQeeRxTePY3fZIKskELbzG3Kgt7mibhLYe4nyRgAHExDVaaENGlYJmJMMqaFia2KlxMNKbQr46Gn2dSsTwg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/PqtlRibQeeRxTePY3fZIKskELbzG3Kgt7BzyG8Okus7Q6ibQSliaOib0kkJibVqPR1plgPb1fUApSSGm6wReRl1dSlA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**二**｜EFS加密操作

Windows操作系统中，EFS加密操作十分简单，选中文件或文件夹右击选择“属性”-点击“高级”，在弹出的对话框中将“加密内容以便保护数据”复选框中勾选，点击“确定”。中间会提示子文件加的处理方法，选择默认即可，再点击“确定”即可完成加密。加密对象就会显示锁头标志，说明加密成功。

![](https://mmbiz.qpic.cn/mmbiz_png/PqtlRibQeeRxTePY3fZIKskELbzG3Kgt77DGtPVEOZspYwmR1DzZIcGjof0kC2zTpeR4ibRBPWac0v50HFPrico0Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/PqtlRibQeeRxTePY3fZIKskELbzG3Kgt77yOp0OSySpOhlJR4IXkvTIXcZRd3weJSO9k1vo9UtcLDoxIAJgy01A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

若为首次EFS加密，右下角通知栏会弹出“备份文件加密证书和密钥”提示。

![](https://mmbiz.qpic.cn/mmbiz_png/PqtlRibQeeRxTePY3fZIKskELbzG3Kgt7AYDicI8MkMvU7uYSRQ81mWpa11hwjBPXLhXP1ltiaz7T8OZOGcEsrqrA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**拓展**｜EFS加密原理

在使用EFS加密一个文件或文件夹时，系统首先会生成一个由伪随机数组成的FEK(File
Encryption
Key，文件加密钥匙)，然后将利用FEK和数据扩展标准X算法创建加密后的文件，并把它存储到硬盘上，同时删除未加密的原始文件。接下来系统利用你的公钥加密FEK，并把加密后的FEK存储在同一个加密文件中。而在访问被加密的文件时，系统首先利用当前用户的私钥解密FEK，然后利用FEK解密出文件。在首次使用EFS时，如果用户还没有公钥/私钥对(统称为密钥)，则会首先生成密钥，然后加密数据。如果你登录到了域环境中，密钥的生成依赖于域控制器，否则它就依赖于本地机器。

若未有提示备份通知，则可以自行在证书管理器中导出证书，具体如下：

![](https://mmbiz.qpic.cn/mmbiz_png/PqtlRibQeeRxTePY3fZIKskELbzG3Kgt7vT1lliahl2ccVuMHegania1qUPonaiafhmEfWk196Xzwv6t5t2ACB1ojg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

1、按“Windows徽标键+R键”，在弹出窗口输入“certmgr.msc”回车，调出证书管理器；

![](https://mmbiz.qpic.cn/mmbiz_png/PqtlRibQeeRxTePY3fZIKskELbzG3Kgt7JOlg1GENgwAvu6jkric61JSqASBURI7AOJMeTQxm8d5mt7JW4JlwibZg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/PqtlRibQeeRxTePY3fZIKskELbzG3Kgt7vT1lliahl2ccVuMHegania1qUPonaiafhmEfWk196Xzwv6t5t2ACB1ojg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

2、点击“个人”-“证书”，在右边的窗口中找到“加密文件系统”的证书。选中后右击鼠标，选择“所有任务”-“导出”。

![](https://mmbiz.qpic.cn/mmbiz_png/PqtlRibQeeRxTePY3fZIKskELbzG3Kgt7yTwpILzTo7S4ovarGaTQdRqt8Um96ibuReicSdA9RoJicNq31oOmHgazA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/PqtlRibQeeRxTePY3fZIKskELbzG3Kgt7vT1lliahl2ccVuMHegania1qUPonaiafhmEfWk196Xzwv6t5t2ACB1ojg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

3、打开“导出向导”，点击“下一步”。

![](https://mmbiz.qpic.cn/mmbiz_png/PqtlRibQeeRxTePY3fZIKskELbzG3Kgt77519lMwnfyewfibrDDZg76HDEgKJ4D1aG5mmicOGXCicEwRtbZaXK5c5w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/PqtlRibQeeRxTePY3fZIKskELbzG3Kgt7vT1lliahl2ccVuMHegania1qUPonaiafhmEfWk196Xzwv6t5t2ACB1ojg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

4、选择“是，导出私钥”，点击“下一步”；

![](https://mmbiz.qpic.cn/mmbiz_png/PqtlRibQeeRxTePY3fZIKskELbzG3Kgt7aBk4T1iaaiarnVLmjHmBRgnIa7AgVoyz220myH0IiaLlbBu6I03gcTfSA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/PqtlRibQeeRxTePY3fZIKskELbzG3Kgt7vT1lliahl2ccVuMHegania1qUPonaiafhmEfWk196Xzwv6t5t2ACB1ojg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

5、选择“密码”，输入两次相同的密码（这个密码将在恢复导入的时候使用），点击“下一步”；

![](https://mmbiz.qpic.cn/mmbiz_png/PqtlRibQeeRxTePY3fZIKskELbzG3Kgt7icGKcCNicDATnb3ozQcDYokbpG8V0eulwDIJNOiaylzoL22VSleTQqykg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/PqtlRibQeeRxTePY3fZIKskELbzG3Kgt7vT1lliahl2ccVuMHegania1qUPonaiafhmEfWk196Xzwv6t5t2ACB1ojg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

6、点击“浏览”选择保存的路径和名称；

![](https://mmbiz.qpic.cn/mmbiz_png/PqtlRibQeeRxTePY3fZIKskELbzG3Kgt7hEJNtud46mKufOX5u8mcQvVukYBDWnYypnAdw3sXSFvPPb8FZ1ibA8g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/PqtlRibQeeRxTePY3fZIKskELbzG3Kgt7vT1lliahl2ccVuMHegania1qUPonaiafhmEfWk196Xzwv6t5t2ACB1ojg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

7、点击“完成”即可

![](https://mmbiz.qpic.cn/mmbiz_png/PqtlRibQeeRxTePY3fZIKskELbzG3Kgt7FhOteic4WRmuTl2YXsIvJ7XE5zQaspDUoibqS6keY9GRgP81bqnqgq9Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/PqtlRibQeeRxTePY3fZIKskELbzG3Kgt7mibhLYe4nyRgAHExDVaaENGlYJmJMMqaFia2KlxMNKbQr46Gn2dSsTwg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/PqtlRibQeeRxTePY3fZIKskELbzG3Kgt7BzyG8Okus7Q6ibQSliaOib0kkJibVqPR1plgPb1fUApSSGm6wReRl1dSlA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**三**｜解密

文件加密后，即使被复制到其他电脑中，若没有该文件的EFS证书，是无法正常访问的。

![](https://mmbiz.qpic.cn/mmbiz_png/PqtlRibQeeRxTePY3fZIKskELbzG3Kgt7215gQFIGkfrvn2JnoNQby7oXd9rTPx8WQChfmE7D3NrtJSTzn4QTZQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

故此，若要在其他系统环境对加密的文件进行解密，则需将对应证书密钥导入当前系统环境方可查看，证书导入过程操作与导出类似，在导出证书的空白位置，鼠标右击选择“所有任务”-“导入”即可开始导入向导，过程中需要输入备份时输入的密码。

![](https://mmbiz.qpic.cn/mmbiz_png/PqtlRibQeeRxTePY3fZIKskELbzG3Kgt7K0PJaUIB8IdyZbTRKeYn7LUue2XFuOicIarbjQt3ZWmXqJhcjic6O5vw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

        以上便是有密钥情况下进行的解密，若无密钥情况下，可从根据用户密码进行校验匹配的方式尝试，但较为复杂且成功率低，故此，如果使用EFS对文件进行了加密，应该及时将秘钥进行备份并妥善保管。

---

转自：[广西南宁平衡信息技术有限公司](https://mp.weixin.qq.com/s?__biz=MzA3MjI1ODc4Mw==&mid=2449670195&idx=1&sn=3ba4e9f0dc81c057b22f7b710d896f39&scene=21#wechat_redirect)

---

![](https://mmbiz.qpic.cn/mmbiz_gif/dDhDhftpRFvypLIddOk8EJNwFmGv5sw40Ty0d9OMXUbicPtzt610wXiaf0l7HdpW9JXT9OZf3JbuNh3FvUPJnAKQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/dDhDhftpRFuouuxbQ44msKkdjic0C8WOQrHEN6rex1hiblHTTIpApR8safvHvB9zXorQTMStvvyN2zO8xjOJd5vg/0?wx_fmt=png)

电子物证

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/dDhDhftpRFuouuxbQ44msKkdjic0C8WOQrHEN6rex1hiblHTTIpApR8safvHvB9zXorQTMStvvyN2zO8xjOJd5vg/0?wx_fmt=png)

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
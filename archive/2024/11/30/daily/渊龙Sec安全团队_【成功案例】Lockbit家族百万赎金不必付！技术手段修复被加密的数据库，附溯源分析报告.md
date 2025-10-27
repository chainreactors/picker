---
title: 【成功案例】Lockbit家族百万赎金不必付！技术手段修复被加密的数据库，附溯源分析报告
url: https://mp.weixin.qq.com/s?__biz=Mzg4NTY0MDg1Mg==&mid=2247485599&idx=1&sn=e85f53946349d2e6bd93baf11c9e2505&chksm=cfa49364f8d31a72994bf473907513adb414c4a2b1c4f65009b360d78609c49cc27a42a19b56&scene=58&subscene=0#rd
source: 渊龙Sec安全团队
date: 2024-11-30
fetch_date: 2025-10-06T19:17:00.035238
---

# 【成功案例】Lockbit家族百万赎金不必付！技术手段修复被加密的数据库，附溯源分析报告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fiajytAx7IbeLbRCrMx202JSLxmsSuzr2I1yOfQNNBHkKjQA1IH5mruSiaVicyxZr6tmicg5DhqXz1gcWL74gibQLZw/0?wx_fmt=jpeg)

# 【成功案例】Lockbit家族百万赎金不必付！技术手段修复被加密的数据库，附溯源分析报告

渊龙Sec安全团队

编者荐语：

对于勒索病毒的解密工作，一直是业内的难题！

今天渊龙Sec安全团队给各位师傅揭露面对勒索病毒解密细节的同时，也介绍了一下兄弟团队~

以下文章来源于solar应急响应团队
，作者索勒安全团队

![](http://wx.qlogo.cn/mmhead/lpHDr05YrISCFNADlEnicj1ic3ia4qiaLqV0CRDdIaPmERmiby2VgWlsx4UtNhZI4xuUmdYQ25iaE26WM/0)

**solar应急响应团队**
.

7×24小时在线服务。专业安全团队，十余年来专注数据恢复，漏洞修补，安全加固。当天完成评估、修复，不成功不收费。同时完成攻击溯源、漏洞排查、漏洞修补，保障您的服务器安全！

# 1.背景

## 1.1 事件背景

11月2日，某科技公司紧急联系我司团队求助，称其公司共有20余台服务器被勒索病毒加密。通过勒索信中提供的TOX（即时通讯软件），该公司尝试与黑客取得联系并展开谈判，在首次谈判中，当用户询问赎金费用时，黑客开出了**20万美元（约合150万元人民币）**的要价。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DxUXemrrntrTsnN8CDctO9kicKYIhptiakiaoX5lV4EsewibNYfkL9VhMxM1J72uf6Lyw0rvnz48fj0ibYacibbG8RAw/640?wx_fmt=jpeg&from=appmsg)

该赎金费用远远超出用户的预算，因此用户再次询问单个ID的恢复费用是否与恢复所有ID的费用一致。黑客的回复是，恢复所有ID的费用为**20万美元（约合150万元人民币）**，而恢复单个ID的费用为**15万美元（约合100万元人民币）**。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DxUXemrrntrTsnN8CDctO9kicKYIhptiakTPLKtcuwCmxXeDgCHc4zaU4SiasPrhO6fGHJBwtYksSMzB7JZryUTkQ/640?wx_fmt=jpeg&from=appmsg)

然而，尽管用户尝试与黑客沟通并表达了经济困难，但黑客并未作出任何回应，且明确表示**15万美元**的赎金费用为最终报价，拒绝接受任何降价方案。由于该赎金金额远远超出了公司的承受范围，且无法确保支付赎金后数据能够成功恢复，公司决定不再与黑客继续交涉，而是转向寻求我司的专业技术支持，希望通过技术手段恢复数据，确保业务能够尽快恢复正常。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DxUXemrrntrTsnN8CDctO9kicKYIhptiakmjFCffm5T5bxVpxBdJlxPFvY9RTN8ZYFuBc6S5uLs6IkzQ1FXYzOiag/640?wx_fmt=jpeg&from=appmsg)

## 1.2 处理结果

在前期排查过程中，我们成功提取到了该加密器样本，并对其进行了深入分析。根据客户的反馈，其受感染数据对于业务运营至关重要，而服务器环境和业务系统则可以重新配置后再导入数据。基于这一实际情况，我们将工作重点明确为优先恢复数据，确保客户关键业务尽快恢复正常，同时为后续环境重建和系统优化做好技术支持准备。

在提取被加密的MSSQL数据库文件后，我们发现受影响的MSSQL数据库文件仅有头部被加密，这为数据恢复提供了可能性。在与客户协商后，我们决定提取所有被加密的数据库文件，集中进行恢复操作。同时，客户配合重置业务环境并重新搭建系统框架，以确保恢复后的数据能无缝导入新环境。整个流程旨在最大限度地缩短业务中断时间，恢复完成后将直接导入数据，确保业务快速回归正常运行。我们的计划不仅提高了数据恢复效率，还为客户节约了宝贵的运营时间。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DxUXemrrntrTsnN8CDctO9kicKYIhptiakoRWFtykkunCAOX1UrV1icQMykQa40BfVzNMcRDicEBXvYMkzlKcg359w/640?wx_fmt=png&from=appmsg)

最终，我们成功交付了恢复后的数据库文件，客户在验证后确认，恢复的数据库文件完整无误，可正常导入且未发现数据缺漏，各项功能均可正常使用。后续，文章将简要讲解本次数据库恢复的技术细节、入侵全流程的溯源分析，以及所采取的加固措施，旨在为其他遇到类似情况的公司提供有价值的参考与借鉴。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DxUXemrrntrTsnN8CDctO9kicKYIhptiakEAVA9LgTMyAQZ0TYS10n2r9VsgucBgky1cMHNmvnC5Srd8OcQxdcicA/640?wx_fmt=png&from=appmsg)

## 1.3 lockbit家族介绍

LockBit 3.0（也称为 LockBit Black）是LockBit 勒索软件的新变种。前身LockBit最早出现在2019年，安全研究人员一度将其称为ABCD（因为早期变种将加密文件的扩展名改为.abcd）。2021年，发布Lockbit2.0版本，也称Lockbit RED，加入了双重勒索攻击、删除磁盘卷影和日志文件等新功能。同时还内置了一款名为StealBit的数据窃取木马，该木马是为了支持LockBit Raas附属机构从受害者公司快速窃取敏感数据。被加密后的文件以.lockbit结尾，留下文档Restore-My-Files.txt。2022年，Lockbit3.0发布，又名LockBit Black，成为全球规模最大的勒索软件变种，且在2023年、2024年继续肆虐。

## 1.4 lockbit构建器泄露

在 2022 年 9 月，Twitter 用户 3xp0rtblog 宣布该勒索软件的构建器已被 ali\_qushji 泄露，可以从 GitHub 上下载。

"招募合作伙伴"：是指LockBit勒索软件运营者主动寻找和吸纳其他人或组织作为合作伙伴或下属，共同参与勒索软件攻击活动。

针对lockbit构建器泄露的分析文章可参考[Lockbit 3.0勒索病毒加密程序分析](https://mp.weixin.qq.com/s?__biz=MzkyOTQ0MjE1NQ==&mid=2247484119&idx=1&sn=b3b542dbaef7bbb5bd014ed848d69d7a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DxUXemrrntrTsnN8CDctO9kicKYIhptiakmBcDHS63bRgSFyew1M01cbxe2ULT2iaqPoQCjNCwgA4NE0zjFSP2Cfg/640?wx_fmt=png&from=appmsg)

LockBit 3.0 Builder 在 Twitter 上泄露

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DxUXemrrntrTsnN8CDctO9kicKYIhptiakq4sOVGH8SSPKIibfVZxtOicqFHFS7VKCodTa6V6gEGveehRoQyylSWGg/640?wx_fmt=png&from=appmsg)

LockBit 3.0 构建器

## 1.5 家族特征

通过对本次捕获的加密器样本和勒索信内容的分析，我们发现其与正版 LockBit 3.0 家族存在明显差异：首先，勒索信的语言以中文版为主，缺少 LockBit 3.0 常见的多语言支持；其次，勒索信中未标注家族名称，暗网地址不具备 LockBit 家族的典型特征且目前无法访问；此外，信中额外提供了 TOX 和邮箱等多种联系方式，但对比 LockBit 3.0 官方暗网中的 TOX ID，发现其并不一致。综合这些差异，我们初步判断这是一个基于 LockBit 3.0 加密器泄露版本的构造样本，非正版家族攻击行为。

### 1.5.1 勒索信对比

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DxUXemrrntrTsnN8CDctO9kicKYIhptiakBIfky7ctpJ1ibsFaP1aIiaIEiaY4iapaPMKjWw1zHuzqvhVDPab2QCXFNg/640?wx_fmt=png&from=appmsg)

**原始勒索信内容**

```
~~ LockBit 3.0 the world's fastest and most stable ransomware from 2019~~~

>>>>> Your data is stolen and encrypted.

BLOG Tor Browser Links:
http://lockbitxxxxxxiocyo5epmpy6klmejchjtzddoekjlnt6mu3qhxxxxxx.onion/
http://lockbitxxxxxx3katajf6zaehxz4h4cnhmz5t735zpltywhwpcxxxxxx.onion/
http://lockbitxxxxxxetlc4tl5zydnoluphh7fvdt5oa6arcp2757r7xxxxxx.onion/
http://lockbitxxxxxxki62yun7z5nhwz6jyjdp2c64j5vge536if2exxxxxx.onion/
http://lockbitxxxxxxuquhoka3t4spqym2m3dhe66d6lr337glmnlggxxxxxx.onion/
http://lockbitxxxxxxuo3qafoksvl742vieqbujxw7rd6ofzdtapjb4rxxxxxx.onion/
http://lockbitxxxxxxdgtojeoj5hvu6bljqtghitekwpdy3b6y62ixtxxxxxx.onion/

>>>>> What guarantee is there that we won't cheat you?
We are the oldest ransomware affiliate program on the planet, nothing is more important than our reputation. We are not a politically motivated group and we want nothing more than money. If you pay, we will fulfill all the terms we agree on during the negotiation process. Treat this situation simply as a paid training session for your system administrators, because it was the misconfiguration of your corporate network that allowed us to attack you. Our pentesting services should be paid for the same way you pay your system administrators salaries. You can get more information about us on Ilon Musk's Twitter https://twitter.com/hashtag/lockbit?f=live

>>>>> You need to contact us on TOR darknet sites with your personal ID

Download and install Tor Browser https://www.torproject.org/
Write to the chat room and wait for an answer, we'll guarantee a response from us. If you need a unique ID for correspondence with us that no one will know about, ask it in the chat, we will generate a secret chat for you and give you his ID via private one-time memos service, no one can find out this ID but you. Sometimes you will have to wait some time for our reply, this is because we have a lot of work and we attack hundreds of companies around the world.

Tor Browser personal link for CHAT available only to you (available during a ddos attack):
http://lockbit74beza5z3e3so7qmjnvlgoemscp7wtp33xo7xv7f7xtlqbkqd.onion

Tor Browser Links for CHAT (sometimes unavailable due to ddos attacks):
http://lockbit5eevg7vec4vwwtzxxxxxxap6oxbic2ye4mnmlq6njnpc47qd.onion
http://lockbit74beza5z3e3so7xxxxxxmscp7wtp33xo7xv7f7xtlqbkqd.onion
http://lockbit75naln4yj44rg6exxxxxx7up4kxmmmuvilcg4ak3zihxid.onion
http://lockbit7a2g6ve7etbcy6iyixxxxxxeffz4szgmxaawcbfauluavi5jqd.onion
http://lockbitaa46gwjck2xzmxxxxxx4x3aqn6ez7yntitero2k7ae6yoyd.onion
http://lockbitb42tkml3ipianjxxxxxxhcshb7oxm2stubfvdzn3y2yqgbad.onion
http://lockbitcuo23q7qrymbk6dxxxxxxtspjvjxgcyp4elbnbr6tcnwq7qd.onion

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>> Your personal Black ID:  <<
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>>>> Warning! Do not delete or modify encrypted files, it will lead to problems with decryption of files!

>>>>> Don't go to the police or the FBI for help and don't tell anyone that we attacked you.
```

**泄露版勒索信内容**

```
>>>> 我們是一個駭客組織，您的資料已被竊取並且加密，

為了不擴大損失，您要立即聯絡我們，或寻找资料复原公司联系我们。

不要啰嗦，我们很忙，我們的加密軟體，網路上無法解密!

您需要支付價值人民幣五十萬約等於1BTC 給我們幫您解密被加密檔案。

>>>> 您需要聯絡我們並使用您的個人解密 ID 傳送一個被加密文件給我們，免費幫您解密一個文件

>>>> 發送ID和一個加密檔案到：d6616151321813261@onionmail.org
>>>> 備用信箱：2189321765132@cock.li
>>>> 您的個人解密 ID：

Tox ID:XXXXXX5C6149FC57090DAC622184327326457BCDF5D6C45528083DBBE21A6EC927CFC1F8BD

TOR網站可以看到您洩漏的秘密：http://xxxxxbcqrbkutyrh77nptes44pqzldj5rk5mxnv46mmrapesp565bsyd.onion/
                          http://xxxxxjug4b5uhndzelsf7vgrxygttutc6h5mqzpwp7y6blk6owhxliqd.onion
您可以透過：幣安/火幣，歐易等虛擬貨幣交易所購買比特幣支付，這是一個很方便的過程！

寫信聊天並等待答复，我們將始終答复您。
有時您需要等待我們的答复，因為我們攻擊許多公司。

>>>> 警告！ 不要刪除或修改任何文件，這可能會導致恢復問題！

>>>> 警告！ 如果您不支付贖金，我們將再次多次攻擊您的公司！
```

### 1.5.2 暗网地址对比

**原始暗网地址**

```
http://lockbitxxxxxxcyo5epmpy6klmejchjtzddoekjlnt6mu3qh4de2id.onion/
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DxUXemrrntrTsnN8CDctO9kicKYIhptiakAhzSvlTuKqx3KSvyTnNibibfE8bKx6D2lm7ibY9KXNhSBzJRmCrtJ0Ing/640?wx_fmt=png&from=appmsg)

**泄露版暗网地址**

本次捕获的勒索信中提到的暗网地址均无法访问，返回结果为404，推测这是攻击者采用的虚张声势手段，旨在通过伪造的联系方式增加受害者的恐慌感和可信度，从而更容易迫使其支付赎金。

```
http://xxxsabcqrbkuty...
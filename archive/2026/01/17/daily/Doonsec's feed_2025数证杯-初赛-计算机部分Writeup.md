---
title: 2025数证杯-初赛-计算机部分Writeup
url: https://mp.weixin.qq.com/s/ibMt1FwJnlZUbmzzl-nPkg
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:33:32.945715
---

# 2025数证杯-初赛-计算机部分Writeup

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2WticCqNz2viaEErtTCltk4Lr7KoAgLzBg9qLx8vvaXaD80nlgwHIg8GjUIiaN2GQHFcCfKgQ2iaMEQcA/0?wx_fmt=jpeg)

# 2025数证杯-初赛-计算机部分Writeup

原创

落寞的鱼
落寞的鱼

鱼影安全

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/iabIwdjuHp2WoekX6fnZ3APEKJwyvmf76EZ0Z309yU3fUicsMz4d7aZ7G41VxQPvKcqmzdqnYwcgWW0V6c8LZBiaQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

点击上方蓝字·关注我们

**前言：**

***本来想写一篇总的，奈何题量太大，有些还不是很会，分开记录。***

***最近在复现数证杯写个wp记录下，欢迎指正，感谢观看！***

***csdn主页：https://blog.csdn.net/Aluxian\_?type=lately***

![图片](https://mmbiz.qpic.cn/mmbiz_png/iabIwdjuHp2WMa8ZiaeibibtMaQxuGmK0LC2BicputDMgb6rswic4vmMJRkAZLwjgCW8JzrsAY7z4sl33ibPicsme3ufaw/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

```
解压密码：GQ7aXryvOC*M8qG*eXa19K9*g&jtHS*Gtrimps@Qx*aYt4oRwwK*HeN0A$#EPv*uvx：Yu1yuu1（欢迎交流学习）time：2026.1.17
```

计算机取证：

41、操作系统的Build版本号是？（答案格式：1）

火眼-基本信息-系统 信息

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOcmzdzQXbgaJ3QBP4b9pbqLOLaMQxwWuk8UUDSgpDWgsRe5aLdNcorzw/640?wx_fmt=other&from=appmsg)

正确答案：19044

42、操作系统设置的账户密码最长存留期为多少天？（答案格式：1）

火眼仿真-密码 火眼取证可以查看：Admininstartor/258369

cmd -net accounts 用于查看或修改计算机的密码和账户策略

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOciaSe6ODuL6kv34OkFicszMYkNXr6Uez1UCIo7Qu1Ke0ae4lf2VTMXu7w/640?wx_fmt=other&from=appmsg)

正确答案：68

43、用户2登录密码NT哈希值后六位是？（字母全大写，答案格式：AAAAAA）

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOczic9qC3icianEmOibtopD62icACo9PficajVcobeV2r0Eokj9b5BR9Wtqoicg/640?wx_fmt=other&from=appmsg)

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOckCh3H2NwlylluH9j1QlK15UzRDr9iaPklYZLwSp2VOKOmfjLMwvAWBQ/640?wx_fmt=other&from=appmsg)

正确答案：A9C708

44、蓝牙mac地址是多少？（答案格式：AA-AA-AA-AA-AA-AA）

火眼-基本信息-网络配置-网络连接

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOcAnyREvVmUDmdViaiazuNFASyA7d9ibQaibq7F2HqH2iaM9MaIcBXF0PbYRw/640?wx_fmt=other&from=appmsg)

正确答案：9C-B6-D0-04-C9-CC

45、SafeImager的产品序列号后四位是？（字母全大写，答案格式：AAAAAA）

火眼 -基本信息-USB最近使用记录

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOc6xibOxokAOY9yWhSLQUGpYDB57MEJg7GulRGspGQeh22OoyIHrhZeQA/640?wx_fmt=other&from=appmsg)

正确答案：09C4

46、123.VHD所处的结束扇区是？（答案格式：1 ）

先找到路径，在使用X-Ways读取 找到 123.vhd 先定位文件

在看分区就可以看到全部的扇区了

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOcYuBF3s0L6o4w8cnsftOqYExOcrToEBDNuDQvaE2qBbPt1MphHcZFjQ/640?wx_fmt=other&from=appmsg)

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOccibjReYiaplk9EGh4wKIsuziayzAAHmJOU7s9F6rtmhVfDEu9g4dicEe3g/640?wx_fmt=other&from=appmsg)

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOcM3KdeViciaXxdBq82h528sT3hcjMsvdtnBDYsnd7mySmapNvJgwZBfhA/640?wx_fmt=other&from=appmsg)

正确答案：27445255

47、用户在BitLocker加密分区最后修改的文件是?（答案格式：abcd.txt）

上面看到嵌套了123.vhd 添加新检材分析，找到BitLocker密钥：

```
625075-617309-532576-720302-040975-309232-451924-426679
```

解密分区8仿真也可以通过修改日期发现 最后修改的文件是 资料1.txt

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOchB1qwdC5ic91MS3xqUUYlnB8EWXkJsMdTib7Xia1nEPEicaukNUicZAgz5w/640?wx_fmt=other&from=appmsg)

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOcOvcBogiao0ibiapUibKZZduD6036fnYlEEWHnACqRvIP9TFM7iasJmv1Daw/640?wx_fmt=other&from=appmsg)

正确答案：资料1.txt

48、用户连接192.168.114.129时用的会话名称是？（答案格式：按照实际情况填写）

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOc7QiawqbXujGhFPbW7cnUicqcs7LlTQicJRV1BrticlcWHZecS23mPmJ96g/640?wx_fmt=other&from=appmsg)

正确答案：连接阿里云

49、 用户创建存储虚拟币钱包地址页面的时间是？（使用双位数格式，答案格式：01 月 01 日）

PS：仿真不要重置密码，不然就这样了 打开没东西，保留原密码

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOcl7Cr4woeLoRDCAuRXmXCQ8TA2YrfDg8ibvEJ3DxUta0yEJkvN8ichayw/640?wx_fmt=other&from=appmsg)

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOcC98zLWIhUvPtr7pnZEUTibORaliaa7yVibUBviby7vfdsrW5mvc07DUOrg/640?wx_fmt=other&from=appmsg)

正确答案：10月07日

50、 用户的虚拟币钱包地址是？（答案格式：按照实际情况填写）

```
#base64x4  VkZSQ2IyVldjRWxSYkdoVlZrZG9hRmt5ZEV0V01sSTJZa1JXYTFaSGFIaGFWVkpIVlRKSmQwNVZPVlJsYkhCRVZqSTFiMDB5VFhkaFIzUlFWVlF3T1E9PQ==
```

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOcHev9tGDRsgfWVoZlZM7CWiahANB94SjniajicKWWFEX7FaAhpw8eF2RkQ/640?wx_fmt=other&from=appmsg)

正确答案：3HrdpWM8ZrBVw9yu8jx1RoNNK6BZxwsHd9

51、 用户 VC 加密容器的密码是？（答案格式：按照实际情况填写）

Foxmail邮箱发现最新解压密码：258369

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOc5KRRZRx09zDfdjTS61GxGO3TcGnSq8q6rlLotEp8lTpBDUmbBMCq0g/640?wx_fmt=other&from=appmsg)

发现有part1-3找到paet4-5发现被删了,恢复好像还是打不开

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOctnSxMDF4RIEwwA0TnUavkxCt94zBzMsrqdIKBK52OSib5ibyOheXjicgg/640?wx_fmt=other&from=appmsg)

在公司资料发现login.txt这个发现有账号密码 其实上面火眼分析了

```
User1：2025szbUser2：SZB2025
```

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOcNOKoicZw85Nwc0YVQZmP4DOlWB1XPZRmA7ARoHdp2bRHfkeM1b2UHtg/640?wx_fmt=other&from=appmsg)

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOcmaicjxkGfNF02dIybAJeGawDdNhsOWyZzjQSmicTJ9JFsAKb0pibueQ2Q/640?wx_fmt=other&from=appmsg)

用户1在回收站发现part4但是不行，尝试下part5

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOchGOouQdE0ibTz0tASyJE52I5o9ADWayYOT8Ms8I2CySxHmTgwcvHLDA/640?wx_fmt=other&from=appmsg)

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOc3zwpeTuSuMFfjM6suITIZmAWHXY71U1Suh7WE24Kxsv8Kaeu23bjIg/640?wx_fmt=other&from=appmsg)

佛辣！！上黑科技了，感觉这些都是假的使用Evrtything找到真的解压。

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOcKNsSDnRh1icicggibIBiaRZgt06MNiccug3G4icmNHFa5gRyRon5icoHmicYSQ/640?wx_fmt=other&from=appmsg)

其实可以全部导出 然后恢复压缩包：copy /B 软件.part1.rar+软件.part2.rar+软件.part3.rar+软件.part4.rar+软件.part5.rar

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOceOovyyiahV8jzLLuAKK3K3zhCdXfqtfqib8I90g6zwhSpdtWPIQvBnuQ/640?wx_fmt=other&from=appmsg)

终于找到联系人了，使用命令恢复就可以打开了

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOcDAFm3ITWMBmgd0aNDOvxbcibdbQU31lMslMtQxE4MbrT3GQZ9B09PQQ/640?wx_fmt=other&from=appmsg)

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOc83xszgkYnvdwZWSh48IMBicS15xflBiaPOWUTnaaiaZh7tuE8niaY0B2Gw/640?wx_fmt=other&from=appmsg)

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOcpTttBGj3liahIXTf4E6CJczDCNp3L1G55YboeX0cK1Gs4lPjZdXdVzw/640?wx_fmt=other&from=appmsg)

正确答案：SHUZHENGBEIctzy2025

52 、用户在生活中使用的代号是？（答案格式：按照实际情况填写）

导出桌面代号.wav 放入Audacity 音频隐写查看频谱图得到代号：小胖

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOcLIEic1KsJico6Jv4L73HVl4OxnQxKibbSDUYGWribh6YFn16UsOWKs6cwQ/640?wx_fmt=other&from=appmsg)

正确答案：小胖

53、 李安东的银行卡归属哪个银行？（答案格式：农业银行）

这个在资料也发现了直接爆6位纯数字 密码：688561

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOc0WlKicKasPWswricOweOeadr44ictMhDP1zzYU666FN0yYElzD8Ir6tYA/640?wx_fmt=other&from=appmsg)

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOcQDGhc4YE6n0uwAkV7ZNAVBaX9IcUbuHJ4orcuicia2LL6Hia5WFxbz7FA/640?wx_fmt=other&from=appmsg)

正确答案：交通银行

54、 请分析某市 10 月 6 日最高气温是？（答案格式：1）

压缩包可以打开但是要输入密码，伪加密 直接使用工具09改00也行

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOcebGYAQeFVg3sich9Jd5ibw3aIaNQemOjylywxylR4quWNeib5W9QnOH7A/640?wx_fmt=other&from=appmsg)

```
#java -jar ZipCenOp.jar r 气温加密.zip
```

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOcuyRojSqCHicPe3Cicw11HcCpzctUa1CyrTactEpQVuRqZySGPQWkQbicw/640?wx_fmt=other&from=appmsg)

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/iabIwdjuHp2UUkic2dGpPF7pKhOYlP9rOcLEib3fMAXice3TBwnaWClQUNCMRLhj6CDZVoS2ibM3pyMytUiclBUzHMJw/640?wx_fmt=other&from=appmsg)

正确答案：21

55、 用户的 BitLocker 密码...
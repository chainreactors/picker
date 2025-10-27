---
title: 红队武器更新：数据库杀器 MDUT增强版
url: https://mp.weixin.qq.com/s?__biz=MzU0MzkzOTYzOQ==&mid=2247489429&idx=1&sn=7cf9b6320357acb7eda9a44e0a470fb4&chksm=fb029acdcc7513dbd615f9f27c606a003014dae6199e96209c326848ff2567113dfc0118986c&scene=58&subscene=0#rd
source: 黑伞安全
date: 2024-08-13
fetch_date: 2025-10-06T18:07:34.439854
---

# 红队武器更新：数据库杀器 MDUT增强版

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KGyt5Iecd5F4f3Mq26jG6icMShLF2ENxN5KvTr5ibhBAiaHdlAakFRBj9zAoIcUgg3YfzwFVq5cfu4InZH3gzS1dw/0?wx_fmt=jpeg)

# 红队武器更新：数据库杀器 MDUT增强版

S0cke3t

黑伞安全

#### 大家在攻防中使用的一把梭工具觉得不爽的，都可以留言提需求排期二开。留下github链接。

#### 前言

MDUT-相信很多红队的师傅对此工具已经很了解了,笔者在日常的攻防中也经常使用此工具.
但使用时笔者发现此工具在对数据库进行利用时存在诸多问题,以至于不得不手动的去连接数据库进行测试.
对此笔者对原版的MDUT进行了一系列功能上的增强和优化,经过一周的缝缝补补大概修复了近10几处的问题。
现在用起来顺手了不少，为此笔者编译了一版修改后的版本供师傅们使用,希望帮助师傅们在日后的攻防中更加的得心应手.

同时也感谢原工具作者的开源精神

#### 扩展内容

注意: 此扩展版本只对常规连接模式进行了优化和修复,http隧道模式暂未进行更改.

##### 修复

* 修复mysql5.0版本UDF报错问题

  原版在对mysql5.1以下进行udf提权时,由于版本差异会出现提权失败问题

  ![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5F4f3Mq26jG6icMShLF2ENxNxYcIAVxuBkoACr4T0rh4vic2rghiaoJG4u2j5D0Rbu0F6Rd0NceKlmPA/640?wx_fmt=png&from=appmsg)

  扩展版中对5.1以下进行了额外的处理,使其能够正确写入UDF

  ![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5F4f3Mq26jG6icMShLF2ENxNT4Sz8PA9VyjbxcMSwfbZ6wGc4Bu9cHSOmy0yk79tNGIpRedkLGRzKg/640?wx_fmt=png&from=appmsg)
* 修复linux下redis执行ping命令卡死问题

  原版中linux下redis如果执行ping命令没有添加c参数,会导致redis进程卡死无法连接

  扩展版中执行ping命令时需强制指定c参数，防止redis进程卡死

  ![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5F4f3Mq26jG6icMShLF2ENxNJPHkVudb9bViaBypA33PMKTPNL2ElmmibkfVRYfqRMt4IJxJiaZBGD9Jw/640?wx_fmt=png&from=appmsg)
* 修复mssql的CLR激活失败问题

  原版中在对mssql的CLR激活时由于没考虑数据库为空的情况导致CLR激活失败

  ![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5F4f3Mq26jG6icMShLF2ENxNQibb0wGLxKoMjbUyiaGUJ42ep5ocdPsLadZ7pTMpM1gsPXLbAMtaUqqw/640?wx_fmt=png&from=appmsg)

  扩展版中对此情况进行了处理,在未指定数据库时将自动重置数据库为master

  ![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5F4f3Mq26jG6icMShLF2ENxNLcuPLCzEzg368SiamPuxOA0l54MHyB92f893sYactkYib6sYfJq90cCQ/640?wx_fmt=png&from=appmsg)
* 修复redis反弹shell后主进程结束问题

  由于原版自带的redis主从扩展中,反弹shell函数存在问题.在利用此功能反弹shell后,如果结束nc进程会把服务端的redis一并结束

  ![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5F4f3Mq26jG6icMShLF2ENxNrFuaxPUfXLIZ421nWvvEdIkruIFfDsRFXzlCA6aOBIr1UjnA3ia8tFQ/640?wx_fmt=png&from=appmsg)

  扩展版中笔者对redis主从扩展反弹shell函数进行了重写,使其在结束nc进程后不会结束服务端redis

  ![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5F4f3Mq26jG6icMShLF2ENxN4D19UianNsiah5flvBY0ibU6mCWqibTsibyShicibY9DewichqtN16yPhFFEQg/640?wx_fmt=png&from=appmsg)
* 修复oracle连接时ORA-28009问题

  原版中在使用sys账户连接oracle时会出现ORA-28009问题,这是由于使用sys账户连接时需指定账户连接角色

  ![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5F4f3Mq26jG6icMShLF2ENxNJZW4pniclAdAhXHnkccXPYZtzicB7fFuMZAkhP5wjFPYxPBGIkDsTH1w/640?wx_fmt=png&from=appmsg)

  扩展版中对此情况进行了处理，添加了sysdba可选项.当连接出现上述情况时可选择此选项进行连接

  ![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5F4f3Mq26jG6icMShLF2ENxNCNpsEg3wsD0Z1GCA4vqTHIlxBrUBfno7PYnmSGV9icqYiaRC11k7UPVw/640?wx_fmt=png&from=appmsg)
* 修复oracle命令执行前缀问题

  原版中在某些版本的oracle执行命令时会出现结果为null的情况

  ![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5F4f3Mq26jG6icMShLF2ENxNY31LAqua8rO3nWkYmIiaMlxzdSL3ibb9Muaibbl4R5vCKmmVDwLtVic9kg/640?wx_fmt=png&from=appmsg)

  扩展版中添加了无前缀模式,当正常情况出现null时可选择此选项进行尝试

  ![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5F4f3Mq26jG6icMShLF2ENxN5KHGicVOOsuFfwxhK85ZibUlBCwqz8Dc4a5a0CPknIiba1aGR3sicx7zow/640?wx_fmt=png&from=appmsg)
* 修复oracle的ShellUtil外部过程编译错误问题

  原版中在对oracle写入ShellUtil外部过程时，会出现编译错误问题

  ![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5F4f3Mq26jG6icMShLF2ENxNsrUzuOsqcChDcLcbRUQQ2SQnbP9WXUlw9sUFonUDLSfQcuPqLm5T3w/640?wx_fmt=png&from=appmsg)

  笔者在对此情况研究后发现是因为外部过程长度超出varchar2长度限制导致.针对此情况扩展版添加了ShellUtilNoline模式,当出现上述情况是可使用Noline模式写入外部过程

  ![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5F4f3Mq26jG6icMShLF2ENxNjh7ZdT7B9mlPL52ibiaibfovGmjFPtQp3gViabJ8LhKLwkYkYTlia68PmBQ/640?wx_fmt=png&from=appmsg)

##### 优化

* 添加分组管理功能

  添加了分组管理功能，方便对数据进行分类管理

  ![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5F4f3Mq26jG6icMShLF2ENxNicSpPK3xvyLROk0CVEbEz7uEOEJsiaEAibKYasr4SCokFeRmmtV4TfTlA/640?wx_fmt=png&from=appmsg)
* 添加mysql驱动高低版本切换问题

  在设置中实现mysql高低版本驱动快速切换功能

  ![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5F4f3Mq26jG6icMShLF2ENxNR9KklUcftzUtUIANqNjZnMpBcjrBf23LOvb43oumbFHDvIpnOZ2c7g/640?wx_fmt=png&from=appmsg)

  切换后会自动填充驱动jar文件路径,自动修正CalssName。保存后点击重设配置文件即可
* 优化redis的SSHKey功能

  配合扩展版的redis主从模块,现在可实现无损写入SSH key

  ![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5F4f3Mq26jG6icMShLF2ENxNDiaWsFCMFjSqEbW6EoOy175cPD7BJyicjGeYCQ031t88EyHy5rSicsWvw/640?wx_fmt=png&from=appmsg)
* 添加redis无损文件读写功能

  配合扩展版的redis主从模块,现在可实现对服务端任意文件的无损读取和写入

  ![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5F4f3Mq26jG6icMShLF2ENxNiaQVYznRiakV5JgJpCox36gvzI0Yic61eoc2O98ZjG2BR5kfTiaZyO9icHA/640?wx_fmt=png&from=appmsg)
* 其他一些小改动

  去除了原版的启动提示
  去除了原版更新菜单
  优化了一些文字显示和交互的操作

#### TODO

此次是Release1的扩展和修改,以下功能已纳入第二次更新内容

* 实现redis文件管理功能
* 实现postgresql文件管理功能
* .....

#### 下载

回复"0812"获取下载地址

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGr18k2OX2bpFFOefrkkbBpD4vsBhoQarpxbyLrL6uPXZicsFclqF0MRchuR2BqurUicZl69eOTW2wvw/0?wx_fmt=png)

黑伞安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGr18k2OX2bpFFOefrkkbBpD4vsBhoQarpxbyLrL6uPXZicsFclqF0MRchuR2BqurUicZl69eOTW2wvw/0?wx_fmt=png)

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
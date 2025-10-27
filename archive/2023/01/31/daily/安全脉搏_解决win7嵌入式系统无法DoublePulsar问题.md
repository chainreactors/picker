---
title: 解决win7嵌入式系统无法DoublePulsar问题
url: https://www.secpulse.com/archives/195218.html
source: 安全脉搏
date: 2023-01-31
fetch_date: 2025-10-04T05:13:02.140884
---

# 解决win7嵌入式系统无法DoublePulsar问题

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 解决win7嵌入式系统无法DoublePulsar问题

[系统安全](https://www.secpulse.com/archives/category/articles/system)

[黑客前沿](https://www.secpulse.com/newpage/author?author_id=49332)

2023-01-30

36,540

### 0x01 前言

渗透过程中总是会遇到千奇百怪的问题，比如前段时间内网横向时用MS17010打台win7，EternalBlue已经提示win了，可是DoublePulsar就是死活一直报错，最后我查阅大量资料，终于解决了这个问题，于是就有了这篇文章。

### 0x02 踩坑

内网横向，扫到几个MS17010能打

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195218-1675058230.png)

操起家伙对其发起猛烈的进攻，一路披荆斩棘（回车），畅通无阻，EternalBlue成功

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195218-16750582301.png)

然后后面的剧情就是DoublePulsar一路火花带闪电，啪一下，shell就弹回来了，然而意外发生了

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195218-1675058231.png)

报了个错 ：

`ERROR unrecognized OS string`

### 0x03 填坑过程

一开始我以为是x86x64的问题，试了几次发现还是不行，上网搜了一下，看到一篇文章有详细解释了这个错误，标题叫：《修補DoublePulsar支持攻擊Windows Embedded系統》（自行搜索一下）

看完后感觉顿悟了，`Windows Embedded Standard 7601 Service Pack 1`是win7嵌入式系统，工具无法准确判断出win7嵌入式系统，需要反编译修改源码，但是作者没放出修改版的exe，绝知此事要躬行！

把DoublePulsar拖入ida，位置在：

`工具目录windowspayloadsDoublepulsar-1.3.1.exe`，最好先做个备份以免修改出bug还原不了

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195218-16750582311.png)

拖进来后界面如上，然后敲一下空格键，找到原作者说的`0x0040376C`位置

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195218-1675058233.png)

然后右键，选择Graph view，得到图形结构

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195218-1675058235.jpeg)

从图形中可以看出，如果目标计算机正在运行Windows 7，它将走左边的路径，然后继续检测其结构是x86还是x64。如果目标不是Windows 7，它将采取右边路径并执行其他OS检查。由于没有检查Windows Embedded，程序最终输出错误消息`[-] ERROR unrecognized OS string`

因此只需要将指令`jz short loc_403641`修改为`jnz short loc_403641`来强制程序走左边的路径

Edit > Patch program > Change byte 将第一个74（jz操作码）修改成75（jnz操作码）

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195218-1675058236.jpeg)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195218-1675058237.png)

最后创建一个dif文件就可以保存关闭ida了，File > Produce file > Create DIF file…

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195218-16750582371.png)

直接保存的exe是不能使用的，还需要用脚本修补修改后的exe，原文作者的脚本链接已经404了，找了很久，这里就直接贴出来了：

```
#!/usr/bin/env python

# Small IDA .dif patcher

import re

from sys import argv,exit

def patch(file, dif, revert=False):

code = open(file,'rb').read()

dif = open(dif,'r').read()

m = re.findall('([0-9a-fA-F]+): ([0-9a-fA-F]+) ([0-9a-fA-F]+)', dif)

for offset,orig,new in m:

o, orig, new = int(offset,16), orig.decode('hex'), new.decode('hex')

if revert:

if code[o]==new:

code = code[:o]+orig+code[o+1:]

else:

raise Exception("patched byte at %s is not %02X" % (offset, ord(new)))

else:

if code[o]==orig:

code = code[:o]+new+code[o+1:]

else:

raise Exception("original byte at %s is not %02X" % (offset, ord(orig)))

open(file,'wb').write(code)

def main():

if len(argv)<3:

print "Usage: %s <binary> <IDA.dif file> [revert]" % (argv[0])

print "Applies given IDA .dif file to patch binary; use revert to revert patch."

exit(0)

file, dif, revert = argv[1], argv[2], False

if len(argv)>3:

revert = True

print "Reverting patch %r on file %r" % (dif, file)

else:

print "Patching file %r with %r" % (file, dif)

try:

patch(file, dif, revert)

print "Done"

except Exception, e:

print "Error: %s" % str(e)

exit(1)

if __name__ == "__main__":

main()
```

然后命令执行修补一下exe

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195218-1675058238.png)

最后我们把生成的exe拖到工具目录下，重新执行DoublePulsar，完美解决

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195218-1675058239.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195218-16750582391.png)

【黑客前沿】公众号回复：DoublePulsar

获取修改后的exe

**本文作者：[黑客前沿](newpage/author?author_id=49332)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/195218.html**](https://www.secpulse.com/archives/195218.html)

Tags: [DoublePulsar](https://www.secpulse.com/archives/tag/doublepulsar)、[MS17010](https://www.secpulse.com/archives/tag/ms17010)、[win7](https://www.secpulse.com/archives/tag/win7)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![实战记录之曲线救国](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/1675238041202-300x149.png)

  实战记录之曲线救国](https://www.secpulse.com/archives/195261.html "详细阅读 实战记录之曲线救国")
* [![实战记录之曲线救国](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/system.png)

  实战记录之曲线救国](https://www.secpulse.com/archives/193987.html "详细阅读 实战记录之曲线救国")
* [![渗透贯穿始终上篇](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2021/01/2020112415384648-300x173.png)

  渗透贯穿始终上篇](https://www.secpulse.com/archives/152085.html "详细阅读 渗透贯穿始终上篇")

评论  (0)

昵称

必填
您当前尚未登录。
[登录？](https://www.secpulse.com/user_login "登录")
[注册](https://www.secpulse.com/user-register)

邮箱

必填（保密）

快来写下你的想法吧！

upload

|  |  |  |
| --- | --- | --- |
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/16752369406501.jpeg)](https://www.secpulse.com/newpage/author?author_id=49332aaa) | [黑客前沿](https://www.secpulse.com/newpage/author?author_id=49332) | |
| 文章数：6 | 积分： 40 |
| 欢迎关注我的个人公众号：黑客前沿 | |

* [![阿波罗主机安全管理](/wp-content/themes/secpulse2017/img/product-agent.png)](https://linkage.duoyinsu.com)
* [![伏特漏洞扫描云平台](/wp-content/themes/secpulse2017/img/product-fute.png)](https://v.duoyinsu.com)

### 安全问答社区

![安全问答社区](https://www.secpulse.com/wp-content/themes/secpulse2017/img/xcx.png)

### 脉搏官方公众号

![脉搏公众号](https://www.secpulse.com/wp-content/themes/...
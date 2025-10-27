---
title: 【青少年CTF】WP-Misc-你会运算吗
url: https://www.secpulse.com/archives/194742.html
source: 安全脉搏
date: 2023-01-10
fetch_date: 2025-10-04T03:22:37.943214
---

# 【青少年CTF】WP-Misc-你会运算吗

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

# 【青少年CTF】WP-Misc-你会运算吗

[CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)

[青少年CTF](https://www.secpulse.com/newpage/author?author_id=49279)

2023-01-09

16,655

## 你会运算吗

考点：16进制位移，0宽隐写，steghide密码爆破

下载附件得到一张图片和一个需要密码的压缩包。

[![hexo-img%2F202212061939331.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/hexo-img%2F202212061939331.png "hexo-img%2F202212061939331.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/hexo-img/202212061939331.png)

尝试打开图片，未果，使用010editor查看。

[![hexo-img%2F202212061854009.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/hexo-img%2F202212061854009.png "hexo-img%2F202212061854009.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/hexo-img/202212061854009.png)

取反：

```
f=open("1.jpg",'rb')
f1=f.read()#二进制形式
with open('flag.jpg','wb') as f2:
    for i in f1:
        if i==0:
            f2.write(bytes([0x0]))
        #这里的b是int形式，要转换成bytes时，使用bytes(),且里面的内容需要加[]
        else:
            f2.write(bytes([0x100-i]))
f.close()
f2.close()
```

打开生成的图片，获得压缩包密码。

[![hexo-img%2F202212061936699.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/hexo-img%2F202212061936699-1024x934.png "hexo-img%2F202212061936699-1024x934.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/hexo-img/202212061936699.png)

解压后获得两张图和一个txt文本。

[![hexo-img%2F202212061938368.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/hexo-img%2F202212061938368.png "hexo-img%2F202212061938368.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/hexo-img/202212061938368.png)

3.jpg还是运用刚才的16进制取反脚本即可获得后半段flag。

[![hexo-img%2F202212061941840.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/hexo-img%2F202212061941840.png "hexo-img%2F202212061941840.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/hexo-img/202212061941840.png)

查看txt文本，提示给出密码，但是需要爆破，猜测为大小写组合爆破。

[![hexo-img%2F202212061941840.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/hexo-img%2F202212061941840.png "hexo-img%2F202212061941840.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/hexo-img/202212061941840.png)

推测图片2使用steghide隐写。

编写爆破脚本：

```
import os

def all_casings(input_string):
    if not input_string:
        yield""
    else:
        first = input_string[:1]
        if first.lower() == first.upper():
            for sub_casing in all_casings(input_string[1:]):
                yield first + sub_casing
        else:
            for sub_casing in all_casings(input_string[1:]):
                yield first.lower() + sub_casing
                yield first.upper() + sub_casing

if __name__ =='__main__':
    for x in all_casings("qsnctf"):
        os.system("steghide extract -sf 2.jpg -p "+x)
        print(x)
```

[![hexo-img%2F202212061944827.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/hexo-img%2F202212061944827.png "hexo-img%2F202212061944827.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/hexo-img/202212061944827.png)

查看flag1.txt。

[![hexo-img%2F202212061944827.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/hexo-img%2F202212061944827.png "hexo-img%2F202212061944827.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/hexo-img/202212061944827.png)

发现0宽隐写。

[![hexo-img%2F202212061946397.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/hexo-img%2F202212061946397-1024x697.png "hexo-img%2F202212061946397-1024x697.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/hexo-img/202212061946397.png)

使用在线网站提取，获得前半部分flag。：<http://330k.github.io/misc_tools/unicode_steganography.html>

[![hexo-img%2F202212061947133.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/hexo-img%2F202212061947133-1024x470.png "hexo-img%2F202212061947133-1024x470.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/hexo-img/202212061947133.png)

**本文作者：[青少年CTF](newpage/author?author_id=49279)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/194742.html**](https://www.secpulse.com/archives/194742.html)

Tags: [ctf](https://www.secpulse.com/archives/tag/ctf)、[Misc](https://www.secpulse.com/archives/tag/misc)、[ｗｐ](https://www.secpulse.com/archives/tag/%EF%BD%97%EF%BD%90)

点赞：
1
[评论：0](#goComment)
收藏：
0

积分 20
*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![CTF中RSA常见攻击方法](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/1678785929506-300x205.png)

  CTF中RSA常见攻击方法](https://www.secpulse.com/archives/197505.html "详细阅读 CTF中RSA常见攻击方法")
* [![探究SMC局部代码加密技术以及在CTF中的运用](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/1678429569077-300x190.png)

  探究SMC局部代码加密技术以及在CTF中…](https://www.secpulse.com/archives/197285.html "详细阅读 探究SMC局部代码加密技术以及在CTF中的运用")
* [![CTF中的神兵利刃-foremost工具之文件分离](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/图片111-300x156.png)

  CTF中的神兵利刃-foremost工具…](https://www.secpulse.com/archives/196849.html "详细阅读 CTF中的神兵利刃-foremost工具之文件分离")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/1670568845919.png)](https://www.secpulse.com/newpage/author?author_id=49279aaa) | [青少年CTF](https://www.secpulse.com/newpage/author?author_id=49279) | |
| 文章数：8 | 积分： 60 |
|  | |

*...
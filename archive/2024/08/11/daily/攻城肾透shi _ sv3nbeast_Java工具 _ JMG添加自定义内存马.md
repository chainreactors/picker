---
title: Java工具 | JMG添加自定义内存马
url: https://www.svenbeast.com/post/HDu5nl4VC/
source: 攻城肾透shi | sv3nbeast
date: 2024-08-11
fetch_date: 2025-10-06T17:59:17.798912
---

# Java工具 | JMG添加自定义内存马

[攻城肾透shi | sv3nbeast](https://www.svenbeast.com)

[首页](/)
[📃文章列表](/posts)
[📖归档](/archives)
[🏷️标签](/tags)
[🔥关于](/post/about)
[ ]

[攻城肾透shi | sv3nbeast](https://www.svenbeast.com)

Dark

\u6697\u9ED1

☰ Menu

☰ 菜单

[首页](/)
[📃文章列表](/posts)
[📖归档](/archives)
[🏷️标签](/tags)
[🔥关于](/post/about)

# Java工具 | JMG添加自定义内存马

Author:
[斯文](/)

Date: 2024-08-10
Reading Time:1.1 mins
words:317

Category:
[红队](https://www.svenbeast.com/tag/kroo8dSGd/)
[java](https://www.svenbeast.com/tag/_-7fKgIlP/)
[工具](https://www.svenbeast.com/tag/R1ylSx8fb/)

share:

作者:
[斯文](/)
日期: 2024-08-10
阅读时间:1.1 分钟
字数:317
分类:
[红队](https://www.svenbeast.com/tag/kroo8dSGd/)
[java](https://www.svenbeast.com/tag/_-7fKgIlP/)
[工具](https://www.svenbeast.com/tag/R1ylSx8fb/)

分享:

## 0x01 原因

​ 因为哥斯拉默认版本触发流量设备告警的几率较高，所以大部分场景都是使用二开过的哥斯拉及shell进行管理webshell，不过在一些java内存马注入的漏洞上面使用jmg生成内存马时还是会需要先使用默认版本哥斯拉shell再注入二开版本的哥斯拉shell，增加告警风险，所以得把自己的shell加到jmg里直接生成。

## 0x02 添加JMG生成shell选项

### 1.jmg-gui模块

添加Filter\_Image按钮

![image-20240810170834596](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202408101843346.png)
![image-20240810171026385](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202408101843117.png)
![image-20240810174451338](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202408101843352.png)

添加结果输出

![image-20240810171722777](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202408101843270.png)

### 2.jmg-core模块

添加Shell类型，起名SHELL\_FILTER\_IMAGE

![image-20240810171505815](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202408101843571.png)

添加生成逻辑

![image-20240810171906234](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202408101843483.png)

添加生成逻辑

![image-20240810172122267](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202408101843397.png)

### 3.jmg-godzilla

添加指向shell类的代码

![image-20240810180704418](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202408101843319.png)

新建个内存马类，类名和前面加的对应上，转换你用来bypass流量设备的jsp代码为Filter类型的java代码，我这里肯定是哥斯拉类型的shell咯，加密方法和解密方法照搬，其他也都是照搬过来，需要注意的是我这里当属性为null时，setAttribute属性的代码用原本的即可

![image-20240810181502262](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202408101844931.png)

## 0x03 添加完成

最终效果，帮助你内存马场景下防止使用普通哥斯拉shell触发流量检测设备的告警

![image-20240810181320633](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202408101844764.png)

* + [0x01 原因](#0x01-%E5%8E%9F%E5%9B%A0)
  + [0x02 添加JMG生成shell选项](#0x02-%E6%B7%BB%E5%8A%A0jmg%E7%94%9F%E6%88%90shell%E9%80%89%E9%A1%B9)
    - [1.jmg-gui模块](#1jmg-gui%E6%A8%A1%E5%9D%97)
    - [2.jmg-core模块](#2jmg-core%E6%A8%A1%E5%9D%97)
    - [3.jmg-godzilla](#3jmg-godzilla)
  + [0x03 添加完成](#0x03-%E6%B7%BB%E5%8A%A0%E5%AE%8C%E6%88%90)

Author:
斯文

Permalink:
<https://www.svenbeast.com/post/HDu5nl4VC/>

License:
MIT License

作   者:
斯文

永久链接:
<https://www.svenbeast.com/post/HDu5nl4VC/>

协   议:
MIT License

Tag(s):

[# 红队](https://www.svenbeast.com/tag/kroo8dSGd/)
[# java](https://www.svenbeast.com/tag/_-7fKgIlP/)
[# 工具](https://www.svenbeast.com/tag/R1ylSx8fb/)

back

标签:

[# 红队](https://www.svenbeast.com/tag/kroo8dSGd/)
[# java](https://www.svenbeast.com/tag/_-7fKgIlP/)
[# 工具](https://www.svenbeast.com/tag/R1ylSx8fb/)

返回

[不上线你是这个👍](https://www.svenbeast.com/post/E0Bcu3tVli/)
[Nodejs审计 | 某演练入口点的二次注入RCE](https://www.svenbeast.com/post/b_Y7hJQKj/)

赏  ![support](https://www.svenbeast.com/media/images/alipay.png)**支付宝**   ![support](https://www.svenbeast.com/media/images/wechat.png)**微信**

[京ICP备19028185号](http://beian.miit.gov.cn/)

攻城肾透shi | sv3nbeast ©Copyright
 ![dandan](https://i.loli.net/2020/03/31/kG71rUoEW5YQq4h.gif)

/\*
\*/

召唤伊斯特瓦尔
---
title: 实战中一处有趣的MySQL正则盲注
url: https://zgao.top/%e5%ae%9e%e6%88%98%e4%b8%ad%e4%b8%80%e5%a4%84%e6%9c%89%e8%b6%a3%e7%9a%84mysql%e6%ad%a3%e5%88%99%e7%9b%b2%e6%b3%a8/
source: Zgao's blog
date: 2023-05-07
fetch_date: 2025-10-04T11:36:36.564693
---

# 实战中一处有趣的MySQL正则盲注

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# 实战中一处有趣的MySQL正则盲注

* [首页](https://zgao.top)
* [实战中一处有趣的MySQL正则盲注](https://zgao.top:443/%E5%AE%9E%E6%88%98%E4%B8%AD%E4%B8%80%E5%A4%84%E6%9C%89%E8%B6%A3%E7%9A%84mysql%E6%AD%A3%E5%88%99%E7%9B%B2%E6%B3%A8/)

[5月 6, 2023](https://zgao.top/2023/05/)

### 实战中一处有趣的MySQL正则盲注

作者 [Zgao](https://zgao.top/author/zgao/)
在[[渗透测试](https://zgao.top/category/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/)](https://zgao.top/%E5%AE%9E%E6%88%98%E4%B8%AD%E4%B8%80%E5%A4%84%E6%9C%89%E8%B6%A3%E7%9A%84mysql%E6%AD%A3%E5%88%99%E7%9B%B2%E6%B3%A8/)

最近的攻防项目中挖掘到了一处SQL注入，但由于存在waf过滤了select和like等关键字，导致无法通过常规手段进行注入。经测试发现waf并没有拦截regexp正则函数关键字，于是有本文的正则盲注分析。

因为项目敏感，就不放burp的截图，用MySQL执行演示正则注入流程。

文章目录

[ ]

* [正则判断字段长度](#%E6%AD%A3%E5%88%99%E5%88%A4%E6%96%AD%E5%AD%97%E6%AE%B5%E9%95%BF%E5%BA%A6 "正则判断字段长度")
* [正则判断字段中包含哪些字符](#%E6%AD%A3%E5%88%99%E5%88%A4%E6%96%AD%E5%AD%97%E6%AE%B5%E4%B8%AD%E5%8C%85%E5%90%AB%E5%93%AA%E4%BA%9B%E5%AD%97%E7%AC%A6 "正则判断字段中包含哪些字符")
* [正则判断每一位字符的值](#%E6%AD%A3%E5%88%99%E5%88%A4%E6%96%AD%E6%AF%8F%E4%B8%80%E4%BD%8D%E5%AD%97%E7%AC%A6%E7%9A%84%E5%80%BC "正则判断每一位字符的值")
* [总结](#%E6%80%BB%E7%BB%93 "总结")

## 正则判断字段长度

语法：

```
.{字段长度}
```

![](https://zgao.top/wp-content/uploads/2023/05/image-831x1024.png)

## 正则判断字段中包含哪些字符

语法：

```
[a-zA-Z0-9]+
[a-z]+
[A-Z]+
[0-9]+
[^\w\s]+
```

这一步是可以省略的，但是判断字符串中包含哪些字符？可以节省后面二分判断的次数。

![](https://zgao.top/wp-content/uploads/2023/05/image-1-1018x1024.png)
![](https://zgao.top/wp-content/uploads/2023/05/image-2-1024x679.png)

## 正则判断每一位字符的值

![](https://zgao.top/wp-content/uploads/2023/05/image-3-737x1024.png)

后面就是同样的步骤判断依次判断每一位的值。

![](https://zgao.top/wp-content/uploads/2023/05/image-4-707x1024.png)

## 总结

实战遇到waf过滤了select感觉没什么好的思路，但是利用正则盲注出数据库的系统变量是可行，反正刷src是够用的。

Post Views: 745

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 发表评论 [取消回复](/%E5%AE%9E%E6%88%98%E4%B8%AD%E4%B8%80%E5%A4%84%E6%9C%89%E8%B6%A3%E7%9A%84mysql%E6%AD%A3%E5%88%99%E7%9B%B2%E6%B3%A8/#respond)

Δ

版权©2020 Author By : Zgao
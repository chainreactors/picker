---
title: 书生大模型实战营闯关 第三关：Git基础知识
url: https://mp.weixin.qq.com/s?__biz=MzAwMTMzMDUwNg==&mid=2650889164&idx=2&sn=f0cb936ced0a2b1e2e65f30bf7e48d2d&chksm=812ea7e9b6592efff38d4855cb5e4a6fbae94b22679c11a2b6e40f791fd90804fded835d6838&scene=58&subscene=0#rd
source: 网安杂谈
date: 2024-10-31
fetch_date: 2025-10-06T18:54:41.700345
---

# 书生大模型实战营闯关 第三关：Git基础知识

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgf505MLTME3XAMKUsLb2eibFHO8Dasv4diaTKXyXSibFfVicRssfYialpx6Q/0?wx_fmt=jpeg)

# 书生大模型实战营闯关 第三关：Git基础知识

网安杂谈

网安杂谈

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgichzau3fnMFSic2pFIVamY8HovMFlCENmnN2MCbEs1yyoVdzUKXBAicZg/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

本次闯关任务内容：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgC8icicPvHG4SMbKdYdd7dTYxwoD97HsabBylzp34vst75NE0TDGXJGPg/640?wx_fmt=png)

任务一：Git的基本使用

提交一份自我介绍。提交地址：https://github.com/InternLM/Tutorial 的 class 分支～

要求：

命名格式为.md，其中是您的报名问卷UID。

文件路径应为 ./icamp4/。

【大家可以叫我】内容可以是 GitHub 昵称、微信昵称或其他网名。

在 GitHub 上创建一个 Pull Request，提供对应的 PR 链接。

1.注册一个github账号

2.将本项目直接fork到自己的账号下

项目地址：https://github.com/InternLM/Tutorial/tree/camp4

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhg4icsgiad7Yyiaiauiauv17pnJSH5HaEicurocUQfEZuS8ZVdicndYHlp6sPLQ/640?wx_fmt=png)

 3.配置git并克隆项目到InternStudio本地

git clone https://github.com/random-zhou/Tutorial.git

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgnuGUbYTnCq4iaTibDd3sibBLHeGZibHERIe1rOac2hQy8PXkYawLEs68JQ/640?wx_fmt=png)

cd Tutorial/

git branch -a

git checkout -b class origin/class

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgmxDOn9gPPwzTwWwMDUZY0JNMHlM4Gx7qbZtFpTA37Va8MHBusfENaQ/640?wx_fmt=png)

4.创建分支

git checkout -b class\_3929 # 自定义一个新的分支

#git checkout -b class\_id 分支名字改为你的uid分支名称

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhg4dzK8kyiabWKic2KGekR1h6vskoRF9hSBibicBFd46voWuDEXicbhHNEmiag/640?wx_fmt=png)

5.创建自己的介绍文件

注意在这个目录下，建一个md文件，内容按模板填一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgfuVC0CiaVNMAX9A6f6NyKNzJxqk7NeIyE6zhvrUCibeon1rX1mnvYTlA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgJMVc3bYuhSJiaWOjf01h1rOYUGfHEaWQjdQ54ZYcibuAIibIU2yzaYYdA/640?wx_fmt=png)

6.提交更改分支

git add .

git commit -m "add git\_camp4\_3929\_introduction" # 提交信息记录,这里需要修改为自己的uid

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgOLDpqKYJbuqmkJjkjjS3CLMk6kt6C99226lYgHgJySAxz7AGSlOOYw/640?wx_fmt=png)

7.推送分支到远程仓库

git push origin class\_3929

#注意，这里要改为自己的分支名称

#提交使用英文，避免同步错误

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgYibpicRib7djCRefXYic2EMsE1Aalav498RTHBcK78QtHW3kpGh46voF9Q/640?wx_fmt=png)

分支已经被推送到远程仓库，点击右上角Compare & pull request

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgPoGFTCnvUeQjhOEHicpJhPs7eaIVdNacwFqfuicOQjP8Eyan8ya8IoOA/640?wx_fmt=png)

选择合适的分支提交就行了，最终效果就是这样啦。后面就等管理员审核合并了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgB1VXEpk3Q1oGNq6YKGeZ3D8FF9558q3zAIQw1A9xLw1bMXRMZDYmtg/640?wx_fmt=png)

任务二：创建并提交一个项目

这个项目叫CyberDefender,具体功能有待开发

今天就到这里了，这一天天的要学的太多了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgWA4CPNT882eRbHNxIEgogwMHvicJTJiaPzBiaNOichWoJyL4oPia2YGZ8gw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgicgLxianEOvyNGt5BRoL3cBiaALV4vk3XyK7H1I9zauQfBdf31DPHp3CA/640?wx_fmt=png)

扫二维码报名一起学吧

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Z4jKmMQicbWP0nM8PnhZtqI4yFWpIJ8KdgxKg1XsbSjljI4kic5C0oAfDRiaXCJmmsl66ro1fY3eDJVUAcoib2PRDg/0?wx_fmt=png)

网安杂谈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Z4jKmMQicbWP0nM8PnhZtqI4yFWpIJ8KdgxKg1XsbSjljI4kic5C0oAfDRiaXCJmmsl66ro1fY3eDJVUAcoib2PRDg/0?wx_fmt=png)

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
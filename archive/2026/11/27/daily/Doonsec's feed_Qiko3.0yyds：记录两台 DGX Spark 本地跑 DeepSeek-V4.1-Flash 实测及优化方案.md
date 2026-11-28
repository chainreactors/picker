---
title: Qiko3.0yyds：记录两台 DGX Spark 本地跑 DeepSeek-V4.1-Flash 实测及优化方案
url: https://mp.weixin.qq.com/s/pS_aAJ6KD_9cZ7uwEBzHrw
source: Doonsec's feed
date: 2026-11-27
fetch_date: 2026-11-28T09:35:42.043057
---

# Qiko3.0yyds：记录两台 DGX Spark 本地跑 DeepSeek-V4.1-Flash 实测及优化方案

# Qiko3.0yyds：记录两台 DGX Spark 本地跑 DeepSeek-V4.1-Flash 实测及优化方案

原创

小谢
小谢

小谢取证

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

两台 DGX Spark 本地跑 DeepSeek-V4.1-Flash 实测：美亚杯取证题测评实录

DeepSeek V4.1 Flash 1017 · Tensorfold · 512K 上下文 · 4 路并发

机缘巧合下得到了吴老师两台spark的支持，所以就想实测一下两台spark跑deepseek v4.1flash1017版本的威力。在此也很感谢吴老师所提供的算力。

![1](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcFy7y4uNvojEwtbZCpicEQ2uXB1kHTTsJAawryZjWmXia7L8lZib8PQz91MoyKXtiaGD5BESdicWYXssJCDEJJMBEWGsyCrKuo0gX0o/640?wx_fmt=png&from=appmsg)

然后也很感谢钱老师和范老师的指点。按钱老师的话来说本地测试非常耗时间，因为一套题来跑基本就要1小时以上。

以下文章内容都为自己的观点和真实感受，各位大佬有更优解也欢迎在评论区留言。

测评环境：两台DGX Spark并联

部署的大模型：Deepseek V4.1 flash 1017

部署方式：Tensorfold

本地大模型所设置的上下文：512K

并发线路：4路

其他参数：

![2](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcHyZDnQljvqIghlic7a7YsbqLpUoz34T0pwSp8PXib6H9rwZjToHBouJHMQGCBsJVNiapEYBNg8ickicM8jia8HSI7ellvPrJDjcLRfI/640?wx_fmt=png&from=appmsg)

一、Opencode · 初测 2026 美亚杯资格赛（两台树莓派检材）

步骤 1

登场：Opencode 直接跑两台树莓派检材

接下来直接开始测评：先登场的是使用Opencode跑2026年美亚杯资格赛的两台树莓派的检材：

![3](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcEA4W5cSqbIGkK4YpbZuJM0s4wAVof8Lem9MOHKd73Yd8v3hVRfjqFNLmfSzeaDYjdKLYhPFon1kv3KibbF360uDZCJJjZqvriaw/640?wx_fmt=png&from=appmsg)

做出的答案：

![4](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcEh9dlLSrecR0199SEibIYUxmvw0pmqXTalHXwrSEicWMTs3eSKe9d25icLibp4CZcx83iaMfZcTTVGtOpcmLXmCtvJrZxvstsDdKicE/640?wx_fmt=png&from=appmsg)

![5](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcF22GqUUvErqn9lEoSACErDrIoeGyl9ZuB2cHYNR2zsGRsq9wELZ8FfBP1OibbcFnChb3MkySjZSC6mJsXrR6icv5jluhb6wmMdA/640?wx_fmt=png&from=appmsg)

![6](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcGwf4icCtkAhiczBYGICMzCQW7C4xK34putvPyakSGK2XfPUkmPCQAYibUSRkwQHlicoXldhYLnozwhXToSxaGStptibsngjatcibaQw/640?wx_fmt=png&from=appmsg)

![7](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcHvfK4ck2HTwC1icrNFnnP632XvmicWYyvU53KxT2iaCXalylLcibicDKJBeZicJM2Ntibc2JMola8RQKCkBpliavGnKZLicjIABc4s37e4/640?wx_fmt=png&from=appmsg)

花费时间久的原因：

![8](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcE0bicudibFT0e0DXOibAkojZ7IGZYg6jbEyEEVUzLMYtAxwicMYMDoAqyXRCQwJfmfjyTtiaiapNmvYtB8PgticMNfHwib6fSDpnqtJDU/640?wx_fmt=png&from=appmsg)

步骤 2

优化方案一：镜像解压后独立作答

优化方案：

![9](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcEyial0vibXzh8oxl893kibZibBAHpZU8wRIDRorbUgq6o3CvwsIcry0WmGObT8LZcs6S4VNjBiaXOsMR6CBDxIkoJMsHk4fpaTYLdw/640?wx_fmt=png&from=appmsg)

根据优化的方案，镜像给它解压好之后再独立做一次：

![10](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcEvgPic4Dk9NOt7DHPjBKvxUxN3abJkbd8C3JqbKYKO2fHcnrsicAHKqdGllYU8s5rZkoUlShgvhZhxFOQtXL0RlCGbx25zGL1BA/640?wx_fmt=png&from=appmsg)

耗时：

![11](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcEvmRMpbbOmXFPYqAdNRBaDp3mCpZT2B9Miagojhl1ouwlA6XdXm83fJKqbNv1HZ68uqOSOKicrMk9MfsvmmjtCMqLf3fKPL6L0U/640?wx_fmt=png&from=appmsg)

做的答案：

![12](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcGibpbzWgtVs2Uq9D4eicuMibrxNpUgSgCnib1dUnorbzkaGRYG2JVTJCmjBtONpXe7CiawlwzAFxeG67bgjg0hAibCiaUODI3JWJzFwA/640?wx_fmt=png&from=appmsg)

![13](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcHyyyPt6sS4mGqgvcsIibHicAWZLf4kicwPDe5W3vmZGZC3rAiasR5KaLiakMVs5E1Jht7hTUIO3jMHIOGtEibPV8OnGoKdcNBv8c4CQ/640?wx_fmt=png&from=appmsg)

![14](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcFzGCJKzVr2AP2xbDSEZ1ViaclTTZNfsLJ1EicxY0ywviaKPaeE0Hg5USFT0wvXczDY33pIW9589Yz9AhrrYwWbCzCjQd1kQ66NR8/640?wx_fmt=png&from=appmsg)

![15](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcEttzhiaXZg2jSPdGyd3UAJ8rK4LnbT1eEab8qlSAkZiagpTORRVmLb4YIBBx6MvRHOSzKyF2Moiay1yAPNOPq4t6icXCXR8W0xmoE/640?wx_fmt=png&from=appmsg)

![16](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcHK6Edv8tew3Uz56hxOfxAckYBcbYZibs7FVp94zcagI5Y3eSebUFRoe12D0IKKCoNeGQzvK9DDf2ficGfLw3XWZmkmwcn1AzGibI/640?wx_fmt=png&from=appmsg)

![17](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcGTj2QjXiccTciaMO9ZoopSibhib5e50PCxCOM5PDbxkLb8VDVxoJ8lYp84ldOc6DicV4vlZMNcvib7w0euq5rKo5aicnI6yIydnTDAvE/640?wx_fmt=png&from=appmsg)

步骤 3

形成 skill 后重跑

直接让它形成skill：

![18](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcEF2vhHEZVY5CTkAXvp2DTMicjoBdobIPOpxbwGFcRGG4qlWo92ib7o9oDworK5sIYib8gSEQBIMzXwMqZniaeLmBMHJMM7zVO5URA/640?wx_fmt=png&from=appmsg)

完成：

![19](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcEmUAta7UWQic00kGcTvaA4ROGXXIR0RmKsOcya3S4MfDwicIY4IxyBz6VVEP5PE6bGzKxFUbFDa7Vic8Bu5duntlzuFqzhIJLfEY/640?wx_fmt=png&from=appmsg)

但为什么会做这么快？？？我们来问下他。

果然有猫腻。重新让他再跑一次。

![20](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcHws1hLQYjqD6rap515I4NN2ciaicybicmRLypv8I5Cfeiac2wUjfF3jT4BOBRd082nva4kEemfpzcV25NlVuqYnvenLicgK8yPicaJg/640?wx_fmt=png&from=appmsg)

![21](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcEicYPpCYQP2WKIvxuxGgRQg4o7h93bhoM1aY9PE5iahOAfxgAoA7x1KdkNpb8aK5tnQdS2qJLH13X1djibHMGAb89LpKqxeT9iay8/640?wx_fmt=png&from=appmsg)

这回就独立完成了：

![22](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcFC6T12ibIyX7yuyA77r5ticrDtAVmW3bl826wpLLdJiaiaffcb5KY99Sznm6U5HDn5NoRiaOeJngApPz153LrHugADywwNplvuSVTI/640?wx_fmt=png&from=appmsg)

![23](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcEntcI736zUIicrsIFH9GnBysqCCLQU2bic4qg3fgOn6eJ8w23AjIEVcSbRexnTEODjPfQibv0DGqo9ibe4CVhu0oGkUz6YGT2DZIo/640?wx_fmt=png&from=appmsg)

![24](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcG9HrJd2VgfNDPfuibbvn8bDibnBN0aicxhPL70oGKFKa67atFEPdemFdypvA063CCZaswK4dKTufibzA5KTGyjMDYQ2ZAMIz1DI9s/640?wx_fmt=png&from=appmsg)

![25](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcG7hyRs5PPp2rR21asXudmA1NBXia9P2XuuVTnDxLy5kiaJXKFrpprxe8qFLjMhfPALKQmgAIQJeVicKXkZH5V1J3Z2ib0ekvgMbvE/640?wx_fmt=png&from=appmsg)

![26](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcENOesl0ic5Z4MzJQM09YELgxfCyAL5s08cXAX9Tyia6236yZQ0QVeoHhgMiaMyTmETJhNQdibtmflQJ44j6dkzatLnRvVCXiahR7gU/640?wx_fmt=png&from=appmsg)

总耗时为19分钟06秒。

![27](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcGFWeUrIzl2Bic4Lc4c8EBFib3DszYNVibXXcgiaE03Xp04b27KmpaQSoh6SaTiaoCUPGjraGn4Nr7lWrUeSuULxmZ8WLzQbA9siaOYE/640?wx_fmt=png&from=appmsg)

但是感觉token速度不准，所以让他重新测了下：

![28](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcFSOAPyjWY6CiaJriahk6W1lCV4licY1ZE6VJglkCH1hZO8ocNGoU8GpATC3r4DsoLOBT2q9SbbJicCfbnCJ6BvAPG6IqanTEPPSG8/640?wx_fmt=png&from=appmsg)

两个树莓派的检材总共是57题，只做错3题，总分为159分，最终得分为149分。

![29](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcG7vSDicgbkCvBMHiaElDDeYtUNDeEy97JO7vrx27CKRe2wXfXyOLRvib0Rec8AalNibNXWY6wrIL8CnoHzopXQ51cBv9tfjFtVCRY/640?wx_fmt=png&from=appmsg)

步骤 4

切换本地大模型，跑整套 128 题

先切换到本地大模型，接下来我们直接测评一下，直接让他跑128题。

![30](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcH2XnhviaJ3AzgJUoPrNXZ6T8N15DicaI0GBTZ1CnryguyduIgww5Uib8BDG1fQfc21TUg8iaLc1Ym6ibLLiaOHtmtCskkzQR2fnrgM8/640?wx_fmt=png&from=appmsg)

![31](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcHmOO4BPLKX4184YkEuOSFAiaGHsJ5Ks8qHcSfn3eia8KrQW0v59Jqj8dryeeaibwjLWBVSUNQBeaoHSzkwYEJaJUkyd5lCrQE8Qw/640?wx_fmt=png&from=appmsg)

![32](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcEMMnzZlYicx474cMQIIhfQoNXIFRTkEhZzG9fvDA06aTn2BFxv2YlcXYkuR4vVHvDfUyqMjdFCfzgjsibR98vmMjibWQz40OsRn0/640?wx_fmt=png&from=appmsg)

![33](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcF1OrphZyPciccMlyWu2KssaUtyRdHt9vvza7iaSkkzLoujxCkYTClYFVeQUjdlDKicUI7cl2eIhRagicUMWL2HnD1mAdu6CFBNVcM/640?wx_fmt=png&from=appmsg)

或是手动执行：按 Ctrl+P 打开命令面板，搜索并执行 Compact session

![34](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcELG32YrHE9ibzGnIcJBia2oymPvFnhx7BHVfhM9OII63QDNCOMnBBSSBaMZ36NhtYZSc1Lsnh7HiagqF0D388UYDX6KPUFNFu0KI/640?wx_fmt=png&from=appmsg)

上下文成功压缩：

![35](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcHoUjW4QgREWZpFUBA3mBDT9PqvxZqXQbfdQiaDjCewOvNEia8oPMfoVAoSPAHJmG4lQrvm4ePGS0RtYYTJumxVWzYQTBWDyOrhI/640?wx_fmt=png&from=appmsg)

![36](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcGX6BiaKKn8ibIMm0MfricskSXJjeXBd8DnWbjL5F6g0CuOswA7MH7zcfbYEkTqcGLreOtIMrMUkC2UgibicMgGajciav5bHts6jxicKo/640?wx_fmt=png&from=appmsg)

完成：

![37](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcGPmsiaW7YlqzjFaOfbRCg7XA9wz5xvXqcSXqLp9uuicyxQyLTgwHKYqh1LmT05E1nazia5DhMaeAC35Z4PeIAjdKTE8vCGFjPakI/640?wx_fmt=png&from=appmsg)

![38](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcGZuZ2NkrIwF9DtURccrC4Etn89VWkyvOSjiaGia0BUkChg7TKbP7zaibS4msibPA059ickepjCEhCPtmIBOg6Fzj0EQeIZviamZyrd0/640?wx_fmt=png&from=appmsg)

![39](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcGra2EXwhHH15icqb2DGB11X6ariaZUUxzKzwIPaokLISlh5XXP03P20w8ZEnGrBK2HQAvH3IjlRDNBUgB9zYFXv9joiaVb1...
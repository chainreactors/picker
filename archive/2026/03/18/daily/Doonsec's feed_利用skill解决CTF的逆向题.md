---
title: 利用skill解决CTF的逆向题
url: https://mp.weixin.qq.com/s/MdQf4ED9ROVQ8cqQ5v-7rQ
source: Doonsec's feed
date: 2026-03-18
fetch_date: 2026-03-19T04:15:30.248532
---

# 利用skill解决CTF的逆向题

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oQ0sWhcqsVnEyPhBjCrISr6BAb95kSMHgXMkI5vf9mQCicDgCiafsqicQ3Q9ibZiaIXKVvF0FejrAUoQib5MWGNWZPspNwrk6bBvzGMnPQ6W4t2LA/0?wx_fmt=jpeg)

# 利用skill解决CTF的逆向题

原创

进击的HACK
进击的HACK

进击的HACK

![]()

在小说阅读器中沉浸阅读

> 字数 433，阅读大约需 3 分钟

## 前言

项目地址：https://github.com/ljagiello/ctf-skills

用于解决 CTF 竞赛挑战的智能体技能——Web 漏洞利用、二进制漏洞利用、密码学、逆向工程、取证、开源情报收集等。可与任何支持智能体技能规范的工具配合使用，包括 Claude Code。

![137d9671aa54ff31728b70cd9932ef7a.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnKibHSlU5CUemW0GzA3YqGQmuHTagn8icfC4XsEUH0qnhDXO660FndIXDt7K5YKIcbxMZN7xp1krjHibt1ibL50VoUDpv3RtX4erA/640?from=appmsg "null")

137d9671aa54ff31728b70cd9932ef7a.png

> 其中的 Skill，很多是基于 Linux 或者 mac 的，如果使用 Windows，可能出现不适配的情况。建议用 Linux 或者 mac。

## 安装与配置

### TRAE

这里用 TRAE 演示，其他大模型工具配置都差不多。

新建一个文件夹，里面新建一个目录

```
.trae/skills
```

![5f0d163d0cdd9d54682c5e6ba2b8c62a.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnSjP60AiavkUHFrlJALQnznzzu8AhnWG42XlcJOmRsIoZBMgCxMyftNTL2rseHxp7u9Eu9gw5UGhM5wickoy1q2YwXoRwyqmEoo/640?from=appmsg "null")

5f0d163d0cdd9d54682c5e6ba2b8c62a.png

下载项目，然后将项目中的目录复制到`.trae/skills`下
![1a2dfe3545ecc8a30fdc05b6bf030382.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkGhCFJ7aA215jPO084UjdQx7iaiaLAJdby3ribUiaFlWBx5iacbuiaExWZgLtUTGic68EjDDpicBsFRpplMdN9Ntb7Zdnawqhtz1w7ULA/640?from=appmsg "null")

1a2dfe3545ecc8a30fdc05b6bf030382.png

打开 TRAE 验证
![e2a4d0edc56d18e4552b910ea47c3699.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVn6I4prFLicUcwT2cKuNIzkBcNmbwboqABVHGRPFF5kMticBYoPVCjEpT8uibfpMm9upC3nKDuLVSL2HhqjpdXoJwO4tVLFQ8koF4/640?from=appmsg "null")

e2a4d0edc56d18e4552b910ea47c3699.png

### opencode

opencode skill 配置参考：
![29057af702e711e3e8cf2bb9b9d46a24.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmehI31ka8tNMoVicdvrnc1QIBkDJMIrzgOFYoNF3OEyrrrReLPEwg9wgBcHnLQwqZUCE8QFaZptfr2IPFkt7W12jthsiaLhpPTs/640?from=appmsg "null")

29057af702e711e3e8cf2bb9b9d46a24.png

## Skills 逆向二进制应用获取 flag

skill 介绍

```
/solve-challenge 介绍该skill
```

![8ae787be9af50e0776fb1536eab6c510.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVl5tYsLKDTiaHQU2XialBsmrMvRlfnvzcEUAwORbnibG0uJBUe8hKwcjoYwdDTDjKfvPsHutqeHZSibP6dB6iaK6rN0lQR1hflA3hSs/640?from=appmsg "null")

8ae787be9af50e0776fb1536eab6c510.png

选一道攻防世界的 reverse 练习题
https://adworld.xctf.org.cn/history-exam/exercise-flag-detail/8d1930fb1e7f4ec3b637d68f0392cf59/995a4dc998864e26af4f34b4a48668bb

下载附件，并将其上传到当前项目下

![b4c356167ba9b1355c7d348923455a02.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnrWVYxypwNY0xDXkia8M7frLlfWHIKq7rAea2OibJ3kHfeicXeWDpugDicpL4BTiaQblNnrOfxzicl6BHU40EEC0OTcK48YNbnBHvoA/640?from=appmsg "null")

b4c356167ba9b1355c7d348923455a02.png

```
/solve-challenge 逆向分析文件 xor，获取flag
```

![6161f6f31c7e35ca417c576485ff25a7.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmicrQd8icPQtYY9VlRevG7I1nia7fKW21spRib9Zn2LywAfOdUcQX1jQUbBdLRPVFhdJ3GQibCn2fRT0cSLWk4AjpYjGBb6y4u3bu0/640?from=appmsg "null")

6161f6f31c7e35ca417c576485ff25a7.png

因为我用的是免费的自带大模型，所以速度有些慢，但最后还是解出来了
![570c61254a395391d8cd3541c88b4848.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVl9bQBZw38pf5ibsnCEv0ZbuM5onS3SicljiaNicse12HusEbczdWhOXzoAd9vdouGtB2Zp8hHVarA0RjzmiboYibRlwQZ2ZFEmJ6ibQ8/640?from=appmsg "null")

570c61254a395391d8cd3541c88b4848.png

验证
![0a8c038d468f5c557a96ecea2dbb76ed.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmQwQ7Q6vvxoQgwiasAxcgIq16YR5h8ibTShHceo9YZjKfgUBAibicXzrAIpvMeZZ9W9GRAVDW3SRE4Q7Nialm6glTibdHD7sxZ9TUyY/640?from=appmsg "null")

0a8c038d468f5c557a96ecea2dbb76ed.png

## 小结

当前的 skill 适配 Windows 的比较少，要想用的顺手，要想用的顺手，建议还是在 MacOS 或 Linux 上使用。

大模型+Skills+MCP，很适合辅助我们处理一些稍微复杂的问题了。

同时面对我们不熟悉的领域，大模型的深度思考方式和采用的方法也是很好的学习对象。遇到看不懂的步骤，也可以询问大模型，让其讲解。

对初学者来说，大模型作为技能学习的老师可能是更好的选择。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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
---
title: 科技｜MiniMax 公布内部模型密码分析成果，探索 AI4S 前沿密码学问题
url: https://mp.weixin.qq.com/s/lNpZCHzdRISW2pv0gylxXA
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:44:17.174722
---

# 科技｜MiniMax 公布内部模型密码分析成果，探索 AI4S 前沿密码学问题

# 科技｜MiniMax 公布内部模型密码分析成果，探索 AI4S 前沿密码学问题

信息安全研究

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**点击蓝字 关注我们**

2026年11月22日晚，通用人工智能科技公司 MiniMax 公布基于最新内部模型的密码分析研究成果。研究团队利用一款内部研究模型（官方称 MiniMax's Internal Model，简称 MIM），对现代密码方案开展系统性的自动化密码分析，发现多处此前未知的算法构造缺陷，并将多项原本停留在理论阶段的攻击，推进到秒级至分钟级即可完成的高效破解。该事件近期受到央广网、新民晚报、上海证券报、中国经营报等多家媒体关注。

![](https://mmbiz.qpic.cn/mmbiz_png/buQvkZfsTH8GIFmqJK85TaHQRdDc8icEHuQxk7Yz4tMuWIIF3kIjib7UmxeRXqwAruPL9815P9YNcWJlHwiaopdt5HS4PP5gcKEr5T8klmMS9o/640?wx_fmt=png&from=appmsg)

据官方网站显示，这次自动分析主要对准三类对象。先是**历届 NIST 密码标准化竞赛留下的候选算法**，其中好几个此前从没有过公开的实际攻击记录，模型给出了第一次实用分析。其次是**近年登上密码学顶会顶刊、以及竞赛获奖的方案**，团队在多个经过同行评审的构造上实现了高效的密文伪造或密钥恢复，还把一种新型分组密码被攻破的轮数纪录又往前推了一步。最后是**支撑公钥密码的经典数学难题**，模型把挖掘算法背后的代数结构和工程层面的代码优化结合起来，在公开挑战赛里解出几十个此前没人解开的高阶实例，比目前最好的求解算法快了几百到几万倍。

从官方技术报告看，几个例子比较有代表性。SHA-3候选算法Waterfall-256，过去只停留在理论推导，没人真正造出过碰撞消息对；这次盲测中，模型单核只用0.045 秒就找到了碰撞。另一个 SHA-3候选 Blender-256自提交以来全轮碰撞一直没被攻破，模型在0.36到 2.3秒内算出了全轮碰撞。后量子候选 LOCKER 的求解矩阵原本要占42PB内存，被压到58MB，2秒就恢复了共享密钥；ROLLO-I-128也在单核上约6秒从公钥推出了等价私钥。TII McEliece 挑战里，模型一共恢复94个实例的私钥，其中55个是头一回被解出；在有公开纪录的实例上，提速约 6,180 到 43,400 倍。HAWK 的安全强度估计还被再压低了9.3到23.8比特。

边界也要划清楚。MiniMax强调，这次打的都是学术设计、历史竞赛候选和公开挑战参数，不会影响目前正在使用的主流密码标准。发现的问题已提前通知对应方案作者，实验留下的推理轨迹整理成技术报告和验证代码，放在官方研究仓库公开。模型本身还没对外开放，团队欢迎密码学和安全领域的研究者、开发者申请试用，一起摸一摸自动化密码分析的能力边界。

密码算法藏在网络通信、金融交易和数字基础设施背后。所谓密码分析，就是在算法公开、条件明确的前提下，找出里面可利用的数学弱点，再看看要多少算力才能用上这些弱点。放到大模型身上，既得能一步步推数学，又得把推导写成跑得起来的程序，在有限算力下给出能被验证的结果。眼下AI在科研里扮演的角色，正从查资料、跑数据，慢慢走到提方法、参与形成可验证结论这一步。11月20日，Anthropic 数学家Levent Alpöge公布了和 Claude 合作完成的黎曼猜想形式化证明，随后通过了Lean 与Mathlib社区的核验，AI4S（人工智能辅助科学研究）也因此被更多人关注。

需要提醒的是，上面这些攻击实例、提速倍数和密钥恢复结果，都是MiniMax 及其技术报告自己公布的口径，截至发稿还没有外部团队公开复现；这些方案真正的安全边界，仍要靠密码学界进一步核验。

##

**参**考与原文链接 >>>

![](https://mmbiz.qpic.cn/mmbiz_gif/buQvkZfsTHiboQplGPbcdjcRBptrWEv6wbcbGwXCtDCMpPM8ydZKasUoagsT9c0gZUygxIaGicGbDUjqqSdsibXdRoHETrxe6aT0VgGRUNJfco/640?wx_fmt=gif&from=appmsg)

MiniMax Research官方研究博客: Practical cryptanalysis with MiniMax's latest Internal Model

https://www.minimax.io/blog/practical-cryptanalysis-with-minimaxs-latest-internal-model

MiniMax 官方 GitHub 研究仓库（技术报告与概念验证代码）

https://github.com/MiniMax-AI/Research

央广网: MiniMax进军人工智能辅助科学研究,公布密码分析研究成果

https://tech.cnr.cn/techph/20261123/t20261123\_527880637.shtml

新民晚报:大模型竞赛进入AI4S深水区,"沪牌"模型在密码学领域取得重要突破

https://news.qq.com/rain/a/20261123A02XEQ00

上海证券报·中国证券网:MiniMax进军AI4S研究 公布密码分析研究成果

http://m.toutiao.com/group/7711168671066767910/

中国经营报:大模型协助人类证明黎曼猜想！国内这家大模型在前沿密码学研究中取得重要突破

https://cj.sina.com.cn/articles/view/1650111241/625ab30904001i9mr?froms=ttmp

证券时报·e公司:MiniMax 披露内部模型密码分析成果

http://m.toutiao.com/group/7710993154145419786/

36氪: 中国AI刷爆全球纪录，比Claude快四万倍，多个密码学难题被破解

https://36kr.com/p/4081531539723397

IT 时代网（微博）: MiniMax 内部模型 MIM 实现多项实用密码攻击

https://m.weibo.cn/detail/5367668657882514

##

##

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WicaKuMLeYl3l23eSpOn1tBIbdC0Z6pRUzaRLw6Xdg6H5JggcVxceibhpPE7GLBwib6bIDMiaKsouqKQaJQWc2cF5Q/640?wx_fmt=jpeg&from=appmsg#imgIndex=15)

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/buQvkZfsTH9JJ8uorUK00MGWd546U8ZB2Kl7OdEYPoUy6ArPVq362SblVaA3icjFwoStTAC8sO80VjiaGvZlSK01VJ0sSAj938SxNrtfgsxVc/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过
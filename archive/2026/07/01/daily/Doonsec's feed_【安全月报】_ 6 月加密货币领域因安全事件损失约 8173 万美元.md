---
title: 【安全月报】| 6 月加密货币领域因安全事件损失约 8173 万美元
url: https://mp.weixin.qq.com/s/xAR95_afjdfdAQhxciYcxw
source: Doonsec's feed
date: 2026-07-01
fetch_date: 2026-07-02T05:56:25.253044
---

# 【安全月报】| 6 月加密货币领域因安全事件损失约 8173 万美元

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uxthuhh3eXyRiafDo8p0iaYBpSNrmZ0iaxgs3GvehULkuKBqFl4wUVrGGeE0lpeu8GFqIMOCtibe96ibMYm4TH0YoCZBOCI67lvcz2KX9oztncuk/0?wx_fmt=jpeg)

# 【安全月报】| 6 月加密货币领域因安全事件损失约 8173 万美元

原创

零时科技
零时科技

零时科技

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uxthuhh3eXxnVm7rpupMeRmPNxkTEiahicAML5V9MEpBsCicW77Vz1LS6tRpCQJTRRzSYOWMicuKrribRPqISQAaOvHnwUhkxN0YOLOMWOj4iak4A/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uxthuhh3eXxrDfTORMn92o0RuJ4C0BiaBUfXZ03lC2xuye5ng3VtNsiaMEFnu9Gvtqmharzueo1m0vZoBVExweOcJFia9jzQz75tiaQvkLECSLE/640?wx_fmt=jpeg)

零时科技每月安全事件看点开始了！据多家区块链安全监测平台统计，2026 年 6 月加密货币领域安全态势呈现“攻击频率创年内新高，钓鱼攻击占比显著上升”的特点。**当月因安全事件造成的总损失约 8173 万美元，其中黑客攻击与合约漏洞相关损失约 6900 万美元，钓鱼攻击造成约 1270 万美元损失。**

协议相关安全事件共发生 67 起，创下 2026 年初以来的单月最高纪录。攻击手法持续迭代，MEV 机器人定向攻击、供应链前端注入、ZK 证明验证缺陷等新型攻击路径集中爆发。跨链桥相关攻击持续构成主要威胁，Axelar 跨链桥损失 467 万美元。黑客组织攻击重心从传统合约漏洞转向自动化系统授权管理、跨链基础设施及社会工程学攻击等多方向扩散。

**黑客攻击方面**

典型安全事件 ***6*** 起

**• Humanity Protocol 私钥泄露攻击**

**时间：**6 月 9 日 **损失金额：**约 3200 万美元

**事件详情：**去中心化身份验证协议 Humanity Protocol 遭攻击，攻击者通过受感染设备获取内部权限，铸造并转移大量 $H 代币，导致代币单日暴跌约 89%。Quantstamp 调查显示攻击工具具有朝鲜黑客特征，通过伪装成 Bithumb 交易所的钓鱼邮件渗透。攻击者至今仍控制着 BNB 链上的部署合约。

![](https://mmbiz.qpic.cn/mmbiz_jpg/uxthuhh3eXx8g6TaNWBXiaRbqGXCf8ib1T7hgdPbiaCBtMzIxATaSic7NyMEtby7Cwmu2HoFk97d2VTJVbBsfcqPxQPCxjic5xic8o7Z24hKo9vt8/640?wx_fmt=jpeg)

**• Syscoin Bridge 跨链桥验证漏洞攻击**

****时间：****6 月 7 日 **损失金额：**约 1000 万美元

**事件详情：**Syscoin 跨链桥中继验证链路存在逻辑缺陷，攻击者利用该漏洞伪造跨链交易证明，成功绕过系统校验机制，在 UTXO 侧无抵押、无销毁对应资产的情况下，非法铸造巨额 SYS 代币。黑客将被盗代币拆分转移至多组地址规避追踪，事件直接造成代币行情短时大跌。项目方第一时间紧急关停全部跨链桥服务，启动安全应急排查，后续完成漏洞修复、追回并销毁被盗代币，恢复链上代币正常流通总量。

**👉 阅读完整事件分析：**

https://syscoin.org/news/technical-postmortem-syscoin-bridge-incident-recovery-and-remediation

**• JaredFromSubway.eth MEV 机器人授权管理漏洞攻击**

****时间：****6 月 20 日 **损失金额：**约 750 万美元

**事件详情：**以太坊知名 MEV 机器人运营商 JaredFromSubway.eth 遭攻击，攻击者构建虚假MEV套利环境（蜜罐），诱骗机器人自动批准恶意合约，通过 transferFrom 函数提取机器人钱包内资产。JaredFromSubway.eth 最初提供 300 万美元赏金，后提高至 750 万美元以追回 50% 被盗金额。

![](https://mmbiz.qpic.cn/mmbiz_jpg/uxthuhh3eXxickXxQiceI3OwL9m3SpUbjdqDAXEd1zHW8LGEAUS3zzjIO5Fv4okMSkgUZ4XsbxmtgboGnUfWbKmheibXohm7ghq8NFE1iaP6Irw/640?wx_fmt=jpeg)

**• Secret Network-Axelar 跨链桥验证漏洞攻击**

****时间：****6 月 10 日 **损失金额：**约 467 万美元

**事件详情：**黑客利用 Secret Network 与 Axelar 跨链桥合约验证漏洞，伪造存款并铸造无抵押代币后套现。攻击持续七天未被察觉，直至一笔正常跨链转账因托管账户资金不足才暴露。漏洞合约自 2023 年初部署以来从未进行外部审计。

![](https://mmbiz.qpic.cn/mmbiz_jpg/uxthuhh3eXza8iceewz3icJpu3B7rIPLTiaNaPIAZeHjnmWf9ZPicWLqW53OlRroExPg4daHz4uVHDWymxjyfeajibDzKLY5FcdLyAva9LV1nIYU/640?wx_fmt=jpeg)

**• Polymarket 供应链前端注入攻击**

****时间：****6 月 25 日 **损失金额：**约 300 万美元

**事件详情：**预测市场 Polymarket 遭供应链攻击，攻击者入侵第三方前端服务并植入恶意脚本，诱导用户签署涉及 EIP-7702 委托执行的恶意授权交易，从而转移钱包内资产。此次攻击未影响平台智能合约，而是利用前端被篡改实施攻击，导致至少 11 个用户钱包受影响。Polymarket 迅速移除恶意代码并承诺全额赔付。该事件也反映出当前新兴授权机制（如 EIP-7702）在用户理解和安全验证方面仍存在较大缺口。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uxthuhh3eXye8r0icDkT64frhicsEEnmTdN39Xxcg78ibF0Ma3cw6yAqXEolV8uib23bicXULlW3FK1FoXrPnN9VoyRPgkCgNUPNhmJOYficGMhws/640?wx_fmt=jpeg)

**• Aztec Connect 验证逻辑漏洞攻击**

****时间：****6 月 14 日（第二次攻击） **损失金额：**约 210 万美元（两次合计约 430 万美元）

**事件详情：**以太坊隐私 Rollup 协议 Aztec Connect 在 6 月内遭受两次攻击，漏洞根源在于 ZK 证明验证路径与 L1 结算路径之间的参数未绑定，导致状态不一致。该漏洞代码已上线超过两年。

**Rug Pull / 钓鱼诈骗**

典型安全事件 ***3*** 起

(1)  **韩国KOL Jadoodoo X账号被盗钓鱼攻击**

**损失金额：**约 5000 美元

**事件性质：**6 月 1 日，韩国加密 KOL“西八姐”@jadoodoo\_的 X 账号被黑客盗取，攻击者以合作名义向粉丝私信发送钓鱼链接。目前已有多名 KOL 中招，总损失约 5,000 美元。安全机构提醒用户不要点击链接、连接钱包或下载恶意软件。

(2)  **Gnosis X 账号入侵钓鱼**

**损失金额：**暂未披露

**事件性质：**6 月 25 日，Gnosis 官方 X 账号遭入侵，黑客发布虚假投票、奖励活动等内容诱导用户点击恶意链接。安全机构发布警告，提醒用户不要与该账号互动、点击链接、连接钱包或签署交易。已与钓鱼网站交互的用户需立即撤销钱包授权并将资产转移至安全钱包。

(3)  **假冒 MetaMask 插件钓鱼**

**损失金额：**暂未披露

**事件性质：**6 月初，出现假冒的 MetaMask 浏览器插件，通过第三方应用商店及钓鱼网站传播，诱导用户导入助记词以完成资产清空。安全机构已就此发布多次预警，提醒用户仅从官方渠道下载钱包插件。

**总结**

2026 年 6 月安全态势核心变化：攻击目标从传统协议向 MEV 机器人、跨链桥扩展，新型攻击路径（供应链注入、ZK 验证缺陷、EIP-7702 委托授权钓鱼）集中爆发。跨链桥持续“失守”，Secret Network 攻击持续 7 天未被发现，暴露链间验证机制的结构性脆弱性。

个人用户需警惕恶意授权和钓鱼链接，高价值资产使用独立钱包隔离风险；项目方应取消跨链桥单点验证设计，对 MEV 类自动化系统实施严格授权管控；行业层面需建立跨链桥安全标准，推动 APT 威胁情报共享。

零时科技安全团队建议：

**• 个人：**定期检查并撤销钱包授权，警惕钓鱼链接和恶意签名请求；高价值资产使用独立钱包隔离风险；遇可疑交易第一时间保留链上证据。

**• 项目方：**加强跨链桥验证机制的多层校验；对自动化交易系统实施严格的授权管理；确保合约代码开源并接受第三方审计；建 立7×24 小时异常监测与熔断机制。

**• 行业：**推动跨链桥更完善的验证标准；加强APT威胁情报共享；推动全球监管协作，加大对国家级黑客的联合打击力度。零时科技安全团队将持续关注链上安全态势，为行业提供前沿安全预警与解决方案。

若需了解更多产品信息或有相关业务需求，可扫码关注公众号或移步至官网：

![](https://mmbiz.qpic.cn/mmbiz_jpg/uxthuhh3eXx7lkKqD6mvrq6ic4XI2AaSGLicgGJYZS3PZfYEZROxBDUgqNnSpqoJhUu0awS7PficRPuqcPic8efAN78HpsdZFGhSMPBgGZcL6fM/640?wx_fmt=jpeg)

**微信号****｜**noneage

**官方网址****｜**https://noneage.com/

**推荐阅读**

**REVIEW**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/uxthuhh3eXx8RJkIfkcCahBH40W3cWicq2omyGAFmhcQjicxOcRFDw12OElyiamqwzNMhaO8PHqDzKqRgEm26qDsQC0P0UiagG9ys7v1yXibaic30/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzU1OTc2MzE2Mg==&mid=2247489933&idx=1&sn=2a660544a85dcd7f42c81e4bbba15dee&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MzU1OTc2MzE2Mg==&mid=2247489933&idx=1&sn=2a660544a85dcd7f42c81e4bbba15dee&scene=21#wechat_redirect")[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uxthuhh3eXw2IYNXIibrnUCn5rufsqticmnzQDBfc2xtkBgP1gE7ibZXyWEFiaaeTzZH63usHlbiazdEGexpzNtYjjOUWlXLlaWqoMkcgbX1FlW0/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzU1OTc2MzE2Mg==&mid=2247490049&idx=1&sn=472418a728531cd1552336437b49ebfd&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MzU1OTc2MzE2Mg==&mid=2247490049&idx=1&sn=472418a728531cd1552336437b49ebfd&scene=21#wechat_redirect")[![](https://mmbiz.qpic.cn/mmbiz_jpg/uxthuhh3eXz74MVEmxfUK0o34Qx7Qgv3iaZTDrpPZrnfseS5jgXtKOxHYT6V3jSssicpLxt13rLAbqnM4EaaktY3CVEwic6tmv2MhEicia6THdTY/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzU1OTc2MzE2Mg==&mid=2247490073&idx=1&sn=ed8510159e9db4f04f57df115573a828&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MzU1OTc2MzE2Mg==&mid=2247490073&idx=1&sn=ed8510159e9db4f04f57df115573a828&scene=21#wechat_redirect")[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uxthuhh3eXwfbm8WNrweFicuI81ww3IuPXX1fGH5ibzdlWHicTXGdlp1mvTxX1BY5sCl6L5Epq1UIQzg021eQLyVBkvGKZwTuk3Ys52FOtsRsU/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzU1OTc2MzE2Mg==&mid=2247489632&idx=1&sn=0a3029d9651d252d0be5e6c3089ad91b&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MzU1OTc2MzE2Mg==&mid=2247489632&idx=1&sn=0a3029d9651d252d0be5e6c3089ad91b&scene=21#wechat_redirect")

END

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uxthuhh3eXwo4TQrBM35Rf9xA5w5RicFlwCKoxwUgEjcu4ibg0aKuEXzI9qsGrCFEvGQUGJ5OUmSiaML8m4JrSibjj1a3l6OdzNyC4KGc7qcv1M/640?wx_fmt=jpeg)

**点击阅读全文 立刻直达官网**

/www.noneage.com/

![](https://mmbiz.qpic.cn/mmbiz_gif/S9WiaEibMtP2jMSTib9czK3UfPsBh0fJscaqZMFhTOvKNaJnEte4bETdtREaSQB3YIA71icwDtrr4oZWAR938LXGcw/640?wx_fmt=gif)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/bsePwevmNNzShTOArXjWb1zTPdQ33kGnGZLCkh0Y01w9wUdtDx1F4PHvBfWosmMuTGzWZkYAjbhUdEZfwvYE9g/0?wx_fmt=png)

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
---
title: Phoenix僵尸网络
url: https://mp.weixin.qq.com/s/5JjRop6UWAwXBbVfZLsDOw
source: Doonsec's feed
date: 2026-03-16
fetch_date: 2026-03-17T04:12:36.402306
---

# Phoenix僵尸网络

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/bwEZ9Cr5wgJrmuW46O3sMvysmm84gBsBgfx3py4OOmL34npO82KM6VwAPofLvxbYUC47QcRNrzwDCowSCNZsfhB8ib6k3CoLKhxEKsLsibib88/0?wx_fmt=jpeg)

# Phoenix僵尸网络

原创

kelvin
kelvin

Mimi is Cat

![]()

在小说阅读器中沉浸阅读

**事件经过**

发现主机发起大量外联

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bwEZ9Cr5wgKBAxib9SOhh5lYfJT6wG6u0ggCBzUTCkW2nMYE2iaVqWWVrgwgjNic4HUkuNtd65qR3icW2PLfUJOSD4CgY0asxK2F0EWS8Hqic3UA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bwEZ9Cr5wgKVgTxktbkSjeKialA0iaaDFOmKkW94vrpDgcicNhaxcXzicslC5EMhOVKztNwvOCzJJAy0Cd9SyWgdIDWB4icOgdxwpn87E2iaJEN5o/640?wx_fmt=png&from=appmsg)

隐藏文件执行、写入注册表run键，文件隐藏及持久化。

![](https://mmbiz.qpic.cn/mmbiz_png/bwEZ9Cr5wgKQicG7eHkLvScfH0icOoKb4vCBSTlfXrYUZgFckSyN5iaia8DkwWV1ulkgh8B1yyN5hHiaULAESibiaUBibvur9LsdA9q1uhbFFlibAvnw/640?wx_fmt=png&from=appmsg)

文件复制为Syswinprdrvc.exe

![](https://mmbiz.qpic.cn/mmbiz_png/bwEZ9Cr5wgKaewMIxFRM1yiawMPCJQzibSf3kJ4kuHXQgCS2gYKdCUQ0qoC9mWs5KmwLvFyLtd5PSt7ayodyiclytt2aAgqILvwxq2DVpDsdFM/640?wx_fmt=png&from=appmsg)

可以看到F盘drvmgr.exe运行启动了sysplurbrsvc.exe后又启动了1969311955.exe

![](https://mmbiz.qpic.cn/mmbiz_png/bwEZ9Cr5wgJico2pfyeOJB0SvYXzHhEgeBMfwnxWndXYAPl7xEHVHFCkzX6ibW2ib1KsLeibfQvUXK8tpkZE9MJeF1WZZ0RR8PTUazqSTzz6e2M/640?wx_fmt=png&from=appmsg)

继续排查发现F盘为u盘，所以U盘即感染源

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bwEZ9Cr5wgKm1xNeUZ95HPcbJm2U2ibXSIrbRgfhhiaH0icI1ejGNLcj79eYSkG4uShcKqW0Dlw63cTEZWV4ibGpe5lOS6Az6Qrib8sbKgFhMTSk/640?wx_fmt=png&from=appmsg)

cmd /c start %s & start %s\DrvMgr.exe执行挖矿

![](https://mmbiz.qpic.cn/mmbiz_png/bwEZ9Cr5wgIU8yiaejzU2su8ynCQeDAH8KCWrepk4w1ahIS6m2pUHLhVHqaNZIvHLVyPvdOWic7CJCK0o62ylzQ6nWCDnAc6JHurLmDKKAliaM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bwEZ9Cr5wgLuoPFa4KpS0yicU3X6vZN6f0ZLC6adqqePJeGiczZ97t2ia5C14eA90cmAqwMxTanDL4MPiabZtgvA0MFy3Jz7jJzO5x8WbvMiclfY/640?wx_fmt=png&from=appmsg)

远控及矿池信息http://178.16.54.109/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bwEZ9Cr5wgLeywicUgY2ibSeicCjvPtvzzEuicq7x3sibjxbreF9ebiaib0uKmuu62AQIQfelLtsViaI0MZKG98dT1vTIZ61QIOV9sILCcjCAMoQibyc/640?wx_fmt=png&from=appmsg)

写入系统路径%windir%、用户路径%USERPROFILE%、应用数据路径%appdata%持久化

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bwEZ9Cr5wgIae0oAXUbYK65vAHYLfXamvP1YZh10zh4h9hp8iamvsXGw5aB584kRSXzGVkiamNtaN03cicMb3ZKKAJW9oLwJgnLyNw6nsOeqVo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bwEZ9Cr5wgLTCP0yS3McLyZFJibWvPuLb5uHzKPzVIgCTfWtdEejaA5liauUaWccnwlaXV4WFDxwpP63m93ibHOldDR9rO2sxUSwY7BvKFTia5Y/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/bwEZ9Cr5wgIzachql00xUxwQ83uPyoLkTO2jJLAyZ0DB6kRsl8MdzTOr4VJd0RRmBD4QjmIJeB9AyZYpe5BHIl5vulnP21O08Yd8KgVv2t8/640?wx_fmt=png&from=appmsg)

IP验证拒绝本地网络及欧洲德国的IP

![](https://mmbiz.qpic.cn/mmbiz_png/bwEZ9Cr5wgKN4Zib8Flxq8c9WAlWnfkuyVtfUqLZ74Eem5JmD11kSGbogEjmd8RscXvMHULjDajuubc3OHkPsR5yaLWxtIRBiamVvGuVXYgYM/640?wx_fmt=png&from=appmsg)

Twizt关键词Phorpiex僵尸网络变种

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bwEZ9Cr5wgKHndLD0PrHKKLgbeyuic9RNGce7zsqcFFdfmnrvbMKkgeMumvGzNMYweVhz1MN9fOux6OPmiaRLbBKsrYtCUGS9W9QnAIe6icYqA/640?wx_fmt=png&from=appmsg)

50多个钱包地址包含以太坊（ETH）、波场（TRX）、比特币现金（BCH）、门罗币（XMR）、莱特币（LTC）等详细见文末钱包地址清单

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bwEZ9Cr5wgL3WfRCvc3icAklgoa2gTJmhRHKQaTVMjJ5SjPUBDemQUZsLiaXmGVMurXM1BAyQbBzktvs9UGdxLyw4vgomxiax2F9mxdudoDBZA/640?wx_fmt=png&from=appmsg)

Cmd /c start %s & start %s\DrvMgr.exe

![](https://mmbiz.qpic.cn/mmbiz_png/bwEZ9Cr5wgKqT8o7FJpCIRFhVib1kl4JicW6h4g8AJXtY7fCZ5qWUWzPGbEAibN0vMC4HxhDEj6C3suS7IqL10vv8DomYAO0UVEO2ft5Djicibus/640?wx_fmt=png&from=appmsg)

**事件归因**

员工使用了包含Phorpiex僵尸网络的U盘导致感染。

**加固建议**

1、回收计算机管理员权限

2、启用USB白名单限制未授权USB

**钱包地址清单**

|  |  |
| --- | --- |
| 以太坊（Ethereum）- ERC20地址 | |
| 序号 | 地址 |
| 1 | 0x6Df1c493fF422799eA80E1C03531a10DFDFa3Ebe |
| 2 | 0xE9bD31C9452E1942Bf1E473067F7e3cd524983CB |
| 3 | 0x12eF1d224f72CF0ed28A0dc41c8676A5D4bbDab5 |
| 4 | 0xC85bF0a9e59e2370FC26d874f0d0ab92A9E85D14 |
| 5 | 0x8e1086CFb2F7Bc0aDe75E66F1087B8cb81cd9691 |
| 6 | 0xF24bb5CbDE00Fdf6c03299Af0a96d4d98455c4c7 |
| 7 | 0x558dD8832C87f3422Cb4af603e5532017EFF9249 |
| 8 | 0x560AD761B8929eD2aAF2FF6d7B43cC4aE3B7d23f |
| 9 | 0x39495fc8716A4694F0169F92540509dDdE21b347 |
| 10 | 0xdDBc86c6662DF87DA21C7b002fa090F6E6545c62 |
| 11 | 0xDE5619F2fd7dbDe2E5d53541Ca9e59b73D029B36 |
| 12 | 0x65D09b0E8FaCd48f8d813856A1EDF51Ec4415a2e |
| 13 | 0xD38C661D9a30a56A67595f4f026b5812B2c32bd5 |
| 14 | 0xcedc0e98c250c555d0420fba7ba45d9941bf577f00c976d6af2058ccde533a36 |
| 波场（TRON） | |
| 序号 | 地址 |
| 1 | TLL8bgut26VN4ir2cj7RyEtUt3ChHJpX9F |
| 2 | TMjq6VPX1szmWDEtcw6L5YQ2yMCT65f3Lw |
| 3 | TEHwor6szFH2EvTVjNLzXCLnBpr5bUo62Q |
| 4 | TTi3prs3cfgCuWRntP4TsXt3EEVtP24feT |
| 5 | TThGffNJcA3JJP36iL1fUAqPQr2U9rTxJ3 |
| 6 | TFDuTwErXBBhve23cph9d6o5bXYZFWY6zX |
| 7 | TDDVo9sWSKad7if9uKSMX1mJSoMYwJcycB |
| 8 | TU1EUf3tqNDKTm6HSmgsvRPYLtDx97DNFF |
| 9 | TMUdqDjUEDpUJ9zA9RFHmqtmdp9r2xK9oN |
| 10 | TT6f9r5tn7jegM7jiMUw2zUK4qBX4fWYTy |
| 11 | THJoBRFbenoEatwEnLX1eTuaLAHJhaFdgP |
| 12 | TLjcFodME2Ed8Fh9USB1WBFcRqrDwjes7e |
| 13 | TDMysBGndMtr36Zpu1x6ozjJjAMqxccmWX |
| 比特币现金（Bitcoin Cash） | |
| 序号 | 地址 |
| 1 | bitcoincash:qph44jx8r9k5xeq5cuf958krv3ewrnp5vc6hhdjd3r |
| 2 | qph44jx8r9k5xeq5cuf958krv3ewrnp5vc6hhdjd3r |
| 门罗币（Monero） | |
| 序号 | 地址 |
| 1 | mona1qwdqvzuwn6qj7l9xmsfqur2vc7uda0rcpftv9ej |
| 其他加密货币地址 | |
| 币种 | 地址 |
| RSK | rsXCXBf9SagxV8JfC12d8Bybk84oPdMNN9 |
| Qtum | QaBvbNAuoU52qCgbqsgoLAbK5P21L6dn5Y |
| 莱特币（LTC） | RLefLLmDAZZb5ZynfPMjZ475pQdHVZNz9J |
| Viacoin | via1qs8zt7jr4sgru6r8dqtdpc93c5d8wmwu8rkz94z |
| 狗狗币（DOGE） | H42AN3K4hbqdprBnJVG8UFQzRZftKJM1EY |
| 达世币（DASH） | Wdv4zK4Fc9D2PJ9aePL9jUmdjvdQeoKV7Q |
| 比特币黄金（BTG） | uhdnHQRJEBxePpLi6YhiS6Kxgct6vG7Q9f |
| Groestlcoin | grs1qscr354fdfddglta2hgajrcryl4gqh6ey360d3u |
| Peercoin | PCsLUHxdx4nFpp5RSYZ6YyJztgYRcErmQk |
| Aurora | AULzfBuUAPfCGAXoG5Vq14aP9s6fx3AH4Z |
| Lisk | LSPqqgA9VwWqxdrPGBEh1W2hRGkTH8S4qW |
| Monacoin | MMTWwvFAZG2WWbXLFtmFTWe3vpWMugpgyH |
| Solana | 6RXJtDZhpoXSwddTNWfHw1YK28febHjSEPd1jJZCbFzR |
| Stellar | UQAbBKbfkiK3Gjo86zgD3yYO5Njf7zxPTEO4JLqN13ruoGDb |
| Ripple | 4miRRtciy8dvivDC5A4cQWwAwZHYv1TnbDHwGN9TtVv9 |
| Tezos | 4AtjkCVKbtEC3UEN77SQHuH9i1XkzNiRi5VCbA2XGsJh46nJSXfGQn4GjLuupCqmC57Lo7LvKmFUyRfhtJSvKvuw3h9ReKK |
| 雪崩（Avalanche） | X-avax1j8gx8kp4zpldw4rpflyg6zrrl7awv9lg7gq4vt / avax1j8gx8kp4zpldw4rpflyg6zrrl7awv9lg7gq4vt |
| Axelar | axelar100le8y8x7w4uls8dhkuvtzten5jyvxgfweewmz |
| Agoric | agoric1jm5w8w49p289v3vq9x3kpg69puj57qgp5gwf76 |
| Akash | akash125f3mw4xd9htpsq4zj5w5ezm5gags37ylpdqfe |
| Nebulas | NASUHUTM7J5HNOJVZ2EULOP6INPNPSE4KN6AQNRI |
| NKN | NN37YENRSEPDYY2AWEX6A2TGEZ3DD6WJ3L3RCRFF63PZI6PVYK6ANRZBLE |
| Stacks | SP1GK1GES8EXB6E15KQJ0EM169NQQNDZG8A2GDRZQ |
| Zilliqa | zil19delrukejtr306u0s7ludxrwk434jcl6ghpng3 |
| Horizen | zncBgwqwqquPLHrM4ozrtr3LPyFuNVemy4v |
| Elrond | erd1hwcnscv0tldljl68upajgfqrcrmtznth4n6ee46le43cqpe5tatqw96dnx |
| Juno | juno125f3mw4xd9htpsq4zj5w5ezm5gags37yygruho |
| Kava | kava1r9xek0h0vkfra44lg3rp07teh9elxg2n6vsdzn |
| Nillion | nillion100le8y8x7w4uls8dhkuvtzten5jyvxgf3h34mq |
| Neutron | neutron125f3mw4xd9htpsq4zj5w5ezm5gags37yk9f92y |
| Nibiru | n1HHGP3YmZp3YA7VgqVgfJqyKBV86d9SaJo |
| Injective | inj1e2g9nyfjcnvgjpaa3czx2spgf2jx3gp4gk0nl9 |
| Initia | init100le8y8x7w4uls8dhkuvtzten5jyvxgfyp04mp |
| Filecoin | f1sz5wwh6urr3gsycgkki7ns5iino3a7bu3chsgly |
| Fetch.ai | fetch100le8y8x7w4uls8dhkuvtzten5jyvxgfe2xzj5 |
| FIO | FIO8DeiD8sv7xkoaNJn417jH82j3B6mEzsuStYQVKoWZRmyrH6vg3 |
| Digibyte | dgb1qnyphwne0t26mmxh2amyzzxzerxarj6jmf8wpmr |
| Dymension | dym18mekyucze0205xn0ynsm8acjxvhhyvvsetx02s |
| dYdX | dydx100le8y8x7w4uls8dhkuvtzten5jyvxgfrwpzs5 |
| Decimal | dn1q3yrdfjppj9pqxqha4k4a690cd9a3mjkd8jku7m |
| DigiByte | 15TssKwtjMtwy4vDLcLsQUZUD2B9f7eDjw85sBNVC5LRPPnC |
| DigiByte | 1Da44vjcoeDY1jnp7asuYhLLHj9zE3QVk9 |
| Lisk | lskaj7asu8rwp4p9kpdqebnqh6kzyuefzqjszyd5w |
| 莱特币（LTC） | ltc1q4ffymwtgue3nh453g9589ypquprj4arjkd7ue7 |
| Fantom | FAuMfr4eb7CoBdyjru8QMSy3qZ1tarfLbxWT164jxa5b |
| Osmosis | osmo125f3mw4xd9htpsq4zj5w5ezm5gags37y6pnhx3 |
| Harmony | one1...
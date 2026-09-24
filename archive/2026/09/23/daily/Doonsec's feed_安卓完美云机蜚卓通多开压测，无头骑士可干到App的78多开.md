---
title: 安卓完美云机蜚卓通多开压测，无头骑士可干到App的78多开
url: https://mp.weixin.qq.com/s/shm6en2oqBwH_W7g9Hp7eg
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T07:05:20.088333
---

# 安卓完美云机蜚卓通多开压测，无头骑士可干到App的78多开

# 安卓完美云机蜚卓通多开压测，无头骑士可干到App的78多开

原创

非虫
非虫

软件安全与逆向分析

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

Z云手机习惯叫蜚卓通就好了。多叫几遍：蜚卓通！蜚卓通！蜚卓通！

课程来到第3季交付篇了。除了环境支持在macOS与Linux开发板与迷你电脑上完美的GPU加速丝滑开机外，还支持Docker容器部署直接上AWS云。

今天我们讨论一下实例与多开的压测，暂时不讨论游戏多开与性能测试。

多开环境我选择了M4 Pro 24G/M1 Max 64G/O6N 16G与32G/MS-R1 32G/OrangePi6Plus 16G/Rock5B 16G多款设备上跑GSI-16、Pixel6-15以及一款国产机型。

完整的测试报告见云手机课程第3季的02-云机多实例运行App多开压测，本文仅放出部分测试结果，见本文文末。

申明：压测环境公代表本人实际测试环境，产生的结果不是云机最后表现的最优结果，理论上可以优化到更好。

注意：本文帖图内容较多，请连WIFI后观看！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Sq4BUsrXeTibdO05MVRp9RtKkUuKicVsL7NbrXJk4KwI1icR9Ken3tuzOMqmv8wqIW1nYXGjxcljY73Ez7pQeWSg6sxBnJcyJvZGhLmWGWRYKc/640?wx_fmt=png&from=appmsg)

下面是广告时间，学员对蜚卓通云手机给的内测反馈效果符合我的预期。

![](https://mmbiz.qpic.cn/mmbiz_png/Sq4BUsrXeTicduro3YtiaxAHW4dgeoMH647Yp9AJRKk0Z5b52GfpFQH2j2Gj4ia37We3MT2FQrLmTiaYsPQ1MywPpMSz1yibpqxuNcD5QicSyONcA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Sq4BUsrXeT8bbrePeYicqNgFOLdt6eEeJtdYc7EJib38Nk0j7ldXSVticGQqesc3LUVVAuwZQT6SZUZH0NAtPG7LQCGNa4tNicyIAXYd8Wn4PzY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Sq4BUsrXeT9xoFnLvIiaJWIoofyJShD41iaERwab28IwhvYufsBQngz9cqhpJdzRhlXObVOoew8E1waf4B2RS6iaxvmRPOJ66Itu8trI1707Bw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Sq4BUsrXeTicc27Us0OpvcQ4tUksU0C7icagibtE0Hoiccyicbd3ZHia9PNnVIBsSAxdibIHXgu9F86wbVOicsT2HwsEQkUF1dJ3PQVFIaSlynYSRv4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Sq4BUsrXeT8KuTWnC7tgY8TjaWlWvsLMKyasMzPdAbP3e4nqOUYMF0zNk4oZdS1843Qp3ibvQVjnKEpicXKmXUrpCwhIBBpNuCJJsxLr7bwSQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Sq4BUsrXeTibDZWwUvCia7GrZRLKT96uSN5ZUKiaKibBLZjZRiaKmaaUubclDem1ssCOHv3wCAuIF1KXc23HhlibF7GUoibdib2H3AcibpatJXqDljmk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Sq4BUsrXeT9Hm1J9Qk1KCsHa2rOE5kmpfia8zMvTNn8K1OYTz3ic02HLicJG1MhFaJh6rNq1J532xuDqsibgkpdgZibpBDRBNMlBbYlQsyHkP5uo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Sq4BUsrXeT9BJjV6aVia4ZxVl2afDWaYqOkeebcmiaicF7mQBGbDlj7UofQT9EuV60kS8rsacV9R1cW7WtPvyCicZiceVicibUscApgyOogRq0FJ8I/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Sq4BUsrXeT9UXiciaT5BibbbQvEwAXMOgN7ScD8uWhoaI3tRb4UOKvLicWFdYWoM9jhb9uctibD2miaF9KnZicS2X8rZ70QdyJAy1JTkObOC1HOnCw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Sq4BUsrXeT8d99u15kf88AvC6xhfA7a2o0KzQRfogOgp4tF7iaVu5ibqxURlHKFCCoXdDyKzfQ0xBzHGeenwswia8uJrf0nOFwHGkrGo28pC1g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Sq4BUsrXeTicf335Yb7vhbzI0T2CY1ianpm8EicuXxoavz3xUxwp0kuO0su5adZFfqT1or9RfqrPorV6j4xUicmyZK4p4Uyia47RPLb6iblEYqpyU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Sq4BUsrXeTib0mZHcws5M6Dicz6cRsiaYyacibC806y2k94Sny1lybxCNJoHZBlOV6f9QT79X6rVVibR25aWAwJDRJf2FuxicyvRjuucqIBmN4KN4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Sq4BUsrXeT8x0kBRHmSMDHGDluMjFbzych7e3R4D7ksiaxIEr8H9VEIiakh7ia2icvEFPy7HianPcbGrk6MsM47S6dPjmTzPDhFE9eRYenIf7NXk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Sq4BUsrXeTicgPvlIQy8Ovg4viaSticiaceh7tDO0sdcRnciav56OkibrILsRj31uPJibxXDdqEqWNv2VN0T58hsMaaPJR5BR0AeCXfOsuws6JgRRw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Sq4BUsrXeT8ICqY1k2D6k9yMWpsAia2IvCKaR6cgq440paXBuNoWPNibgTrM24WJJic3YcQShKR9YwMHqIaqK0RzgqJ7zA26pNibxp7icH1ebfZ0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Sq4BUsrXeT8f7q888N6X2VmeyVfNFKNKE5faQW9hk7vKdWIBGCXtlDIxicyTicgDZbhZTJVQmDxPXryMRbJDSGzHalq1ynVYolmvgVib8XA9ns/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Sq4BUsrXeT8iaPVaianmicKiaWWG2qMDbDSFgicMJXcKr9OkLAYWCVs7tDr2XpnWCxMiaKjXSLoojrAQnpClHACjfLgKs5lzeWLqPQ9EicgXWXkUEw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Sq4BUsrXeTibZcdUib4qKqiaYzxBS7E4E81evRsxUaibvoDqN1YVvj7A40Zlb7mfzLwicZjKUEic2tkribyHWtal9OTicdJyXJiarRkU5iamRDOMQz3cU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Sq4BUsrXeTic5DdVtQAofPbicZW8wcqWJtAzqEP7l6JFovSnOzpP9sRgRP995VBW4EYSCHJhZdZwHBcwITXBcdwWTpzohzNlB2KtibggsdWJUg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Sq4BUsrXeT9W0uhkzFmH9KdVv3yBMc5N9Hlh0C88ic84UxfiaQF5RFaGRL3k1TN9mg1goy6wrzbE8PWKHqC3JW72SAbOaJmlyVQxuch6oXRhQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Sq4BUsrXeTibzvEovapGVSqvQqNy7EgMh00q8b2XghKSwGNcsR0yLU1wlQ3v5xZuGztzibE4eTyxFAyhxywSd4o3WmtlNNG46zKqgfkagpNho/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Sq4BUsrXeT9WXHsrEXXPcuv5KSypo23tcTJ1icQRibDH3Bic8yskGt0jzxlricnkaA7pegKsSCKpyaIatFC4xmF9uicmxibLcfIRpo9cpjZSic5PWg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Sq4BUsrXeTibudkHBELvVZxWqiaxmNMZicKNbictctnic7ckkFa0HGkd5p4Tq7CDIJ3DBic7oD6vUFkq6ibF9Lic9awjTAvDQhXPUX1p1SPI49LdYwk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Sq4BUsrXeTibjhicQ2Gic49tD03eBgrFk8tb3icqaU1cEQqzbyWAalcHQicU6XAYH0CthsHFWicwaqe0iaYUt5ce6eF6tkpUhMhibicncKdNvVkhfDs4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Sq4BUsrXeT959SEFHbQicN4BAbiaDnf8NtrvNfxqodLoQq52Km7mOEQWvHD3fCPRJfoibFA1K51KL2W6iciaQ2mqsbCdHIy9BicLeakUvDTK3bkGc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Sq4BUsrXeTibI2kBn5PObcYnibibrWQwDJUcwcLEwK3z8xXSaX5gQvnfDf0atPurxeTsm4VQk18cggzpU8PPxMicRpic43fK1g2yibzMIwXwNzNY8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Sq4BUsrXeTicPeuoqJyKHzN0lQO9Aet2RPfGlPxWEWgQITrv1XELwTJrnTpZFw9WTDpt25cnEu47azTMyp75hhD7Va6Zmd8QkgkyrybBrUDc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Sq4BUsrXeTibrNHADbawA9ny3vDPcUcAdT0fPdEI6aB2SeoMKdOYiaaZ7JXkyMjfHYu2Z5jTRiaEJah9Xoe1PAL7h08UzghPNWyKbhQ1nusnicE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Sq4BUsrXeTiclHBg9e67qe04b8ftD1ZjAbgRrib2NWO7dDNlbiclE1NGbibhIaNZq4EEIxobziaHblGYqL6ia3R7jG63m8ibiatiaPDrg7L4gia4Bib2BE/640?wx_fmt=png&from=appmsg)

下面是压测报告截图

详细的CPU GPU 磁盘IO 温度等数据见课程的相关文档。

3588的开发板跑Pixel6-15机型云机3开有一些吃力，但能跑，跑GSI-16就稳定一些。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Sq4BUsrXeT8klhBfb4icFPUHaBVjFwpWEOdWPQxcCbliaOdLliaqOUWz78ibTicZploGM7y7nkgic9WVYYwlPQNKtuVDFkPmial9ZmQ8727lTxNXQQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Sq4BUsrXeTicqyRvCwNqEY9iaqYk2vInhhaPaaUERBplkYicmf0RJz3JzjKxWGf5fWuuFo3S7GvrUgLRoqGxHezQzFibwciaB3A19A3gA0nByJPY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Sq4BUsrXeTibE17UxAEJRz7TopHh1kF6icYI7U7X6RcdhgvyU3ddHXKTZ2UkAOicgibpyCFCdXQxsiboUAErWtl1ZKHe6C3VIppK8OftawicObhlo/640?wx_fmt=png&from=appmsg)

M1Max 64G的苹果电脑可以直接15开Pixel6-15，并且较稳定。这里目前没测试App多开，一个App3开的话，可以 15 \* 3 = 45开。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Sq4BUsrXeT9EZKJOWmGbmJK1Picg7Tdkmgiapu3nOIZ6KLaic3LV0ot6F3jEY4xcQfLib436Z8rl7GI9UWy4PQ3sLyHsPvNNIVJKB06b8DKM4FA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Sq4BUsrXeT83ZIvNhTrYTeH8RziavAsLg8GtjAGNLxBGVNKoxeJa0iaW1MAtFMaFbywAW8EP2X43MBtg79CnMMibR6SYgI8Ayo5n19XVQmtGc8/640?wx_fmt=png&from=appmsg)

22开GSI的镜像应该完全没问题，也就是可以干到22 \* 3 = 66个CPU-Z的App实例。对于大些的App，那稳定15开也是完全无问题的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Sq4BUsrXeTicP0sTiaXTGT6Cwaia6IGrsovgGD4vgicibN2mWTHNdPAwxibCkjJUvCLKAYIIx32xhNRZnyNgkjCMwunibKSoa6WYIk6T2LgRIDAVsY/640?wx_fmt=png&from=appmsg)

操作上不算丝滑，也不算卡，完全可以接受。

MSR1开发板32G跑GSI16，可以与O6N32G与Orangepi32G一样的24开安卓软件CPU-Z

![](https://mmbiz.qpic.cn/mmbiz_png/Sq4BUsrXeT9Y6RrmBAdyPLzyLD2mB11qCqh8pibzricahfQqs0gicYtlO243z5DzygAwVwBXjRGBEWf8ic4nqZ0DcltKhLFvCkNc9nDeutrjVo4/640?wx_fmt=png&from=appmsg)

o6n/msr1/opi6plus的测试上，最稳的还是o6n，可能是我主要使用它的原因，它们在跑GSI镜像是都是32G可以8开，Pixel6-15可6开，测试O6N开发板的16G的话，就是分别GSI的4开与Pixel6的3开。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Sq4BUsrXeTib1hyLFeaAOVtZeuR6tVXAtdqjtvvD6lIaiczK0LVWLodsdSPMNjbW9BRsqvgiaY2orqfMPYXwlHZHmctvsQgc3IMrr6gDnpEYEo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Sq4BUsrXeT9FSJLIEa5xUQ7MmkUI37LjvboRWrSduicpGhGPwRwbOje55GialCMvPLDsIfFPzEyicwibyv3zqgOiaaqNygAia3LmC3edLztWnQyq0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_m...
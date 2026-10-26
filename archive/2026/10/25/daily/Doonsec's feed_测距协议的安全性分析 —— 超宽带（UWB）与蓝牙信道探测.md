---
title: 测距协议的安全性分析 —— 超宽带（UWB）与蓝牙信道探测
url: https://mp.weixin.qq.com/s/TpNJvpYoeboAwbaxy6UGJg
source: Doonsec's feed
date: 2026-10-25
fetch_date: 2026-10-26T07:17:14.643505
---

# 测距协议的安全性分析 —— 超宽带（UWB）与蓝牙信道探测

# 测距协议的安全性分析 —— 超宽带（UWB）与蓝牙信道探测

GRCC
GRCC

IoVSecurity

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/CQb4KERYG3QA0ezCCjgRONQvXCf3wka7je04trwIyMqsDUWBubpwfiahXImiaoia7NnueGomOO28vicSZ5wEFFTa1Q/640?wx_fmt=gif)

点击上方蓝色字体，关注我们

**/******技术交流群******/**

添加微信13918880149\**15021948198(好友已满），申请会员下载ppt & 加入网络信息安全、测试评价、汽车电子、自动驾驶、智能机器人、智能船舶、超级高铁、飞行器、招聘求职、投融资合作群...**

![](https://mmbiz.qpic.cn/mmbiz_png/WvsNkg6cHNx31fksZXqfvbOcTkUH5oxUQiaskxcRibibHsEI4xoFpAict4aOhibU6K9R1vROYGJFiciaWkLrghLclUtPEhDvrGTWDY9fUXia3icFlPKc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/WvsNkg6cHNwz2cw1icSoKzJLo7BYBjV1SXL0kx4hS2yEmJJ7rEic92OYV2fo1j7U2bt4eM5iciakWc6eS60vHmVB5GgbC8cYD0VX5ICf1LwiaG6w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WvsNkg6cHNzDldLUzbR2NJOicExRibYZHljXQY23mtLKicrib23InnhQwIuxMVAvzHmOtkbgMibkiaPqiayUwj56zhfgaFkKyiaSibJ8TOG1mHCZYZWE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WvsNkg6cHNwRfh47GYiaD5h2eZqDgVJYCcQREB0SZOkJI4VXia16NfSBSlQP4OBkHoicUOKicMZADY1eUnDtjichcWpTbOnqcrrAYbhliayQZDhto/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WvsNkg6cHNwueKQWj86oA3eBv47gfZzcbTx7QJLic05U5YlQBmkSSYNNuv7SpzqqZibQTSub23kajBLuwZ3jn6kUvtFhicS1xSVchbaLJ3xqNw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WvsNkg6cHNxneIF4rhRHpyQljGOrnNCicmKbJ4nro4V5bQ9ib7JIyLkjdWXpdWaOqw63LoX8L7LOVP10xAb9x0WlTBibZFUiavRq9w2fqHEC1Ow/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WvsNkg6cHNzQnPVfnoQ3J3lEMVKqPyVcbBmPTUPW5H1nYXM011r86YNCxPIicBgsekibryr2eEV7jnQ0tibBEfApZRhWEysof1ph2L27904srk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/WvsNkg6cHNymYtmGxzwv8Nzb13h0bIZKq6OVhjPmvChfkwWibuJGqmZSJBv8ywP4JEn0Qr1O5G841cLyRInHDIEWz42oX40zT5WzJOLB6PjQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/WvsNkg6cHNxuJmexrhKIic0eBnZu9iatRBmp5GMYPsH5nZeLeEsvW3Ed7TTsWDiaGQic8rFW2Md5yZibnDQZ3N8UB6XaG0ZYMaYDeO13Jib2hWxIY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/WvsNkg6cHNwO8OmjJaTKAjeTLJiczqzZZW3Lg4wkfWSPAqgGxMUcIsTG14mcHoicueMKG4AOVICLntoNAHkXlcqjenqvwmHXr8HPkD1AKuqiaU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WvsNkg6cHNzlJET20GuXKeW3RhBbrXLO1YiaJ2Jic1KloTfUFlAQMLDgodkSgNTicC9Ac0EWXxbu3Ms2C9bhOGmXRCgPgzVHfPNzibD035s89N0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/WvsNkg6cHNy4ssd13Ziccy9qlF3fqU82dibRic9UH51q8zPwEuVfPxnY9fHCxc9cahJXM3Dd1kPSC7CnmThjrBC6G1tHMzwnHTfskOWKe4WHVg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/WvsNkg6cHNwIjuC7WNq7YcsDa1aKriadHLPdvJQ0naRtAMSPcX1ibibMqASaqxmJWNTzVibCBLN650CZvUeX0LZ1WArVrT9TugibjcQRtHWUZFKw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WvsNkg6cHNz9XRMibiatoicwnFYynGrfORVz97RVanqPDCLrpw0CtkZGvrvic9iaZc8dVy7bjian61IA0vbx1pE4tzuMoo3r5Aw08lMD0rrCMxsY8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/WvsNkg6cHNzaXs2PlqvP3aroYQsHdrGNRYQzibfkXATmQuElINia7PQPY4gAExb9qVvyK2Cic8fmk4MslG6oQm23ETwicEHufgaUU5dsqSO3OVw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/WvsNkg6cHNz0cl8y0rdOHkYDZu6j4iarT1b6qQrB2Uobz6AGp7H6YjibgKIy9DbjczeuugOMCxNWR1Hz3WYueicyofj2r6ibb5jYpNGUGLQq9Hs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WvsNkg6cHNzyASUNRibmDCDVLYkiaeXxRQeqmRatJLsVPGibA148o1PH4gNllU4ib7u15RAiabiaoicSrvEztMCePPuT8ibkAP9M2GwB0AWYyD67HFU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WvsNkg6cHNxfY5QM3w3yjPRPCPjzyPAhYzDicxMibiaYR5tUibr34hsP16nHicaibzM7ibQSPys08cOD8okoc3sSLicvA1Km87SMKS8f5VkZSHre440/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WvsNkg6cHNyCA6TzKaagVoCu8ZLbP2icKqv8KXB0bVWFSibD99Q7uNEuw0CPnkhzR1KLOr1m28PuEgd83icfowabpIH5xVFUKfQic5Sf8wPV6mQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/WvsNkg6cHNyPg197ibluMIGyqNjELj4AYj1C8aXhbVnTjXTZCB4jyeT2yg8ybd4RWeaIgFO3UWRmee5PyK7gibXtRAxE3cOIib7EhTfllQ8iaxI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WvsNkg6cHNyJGo0CUYNia1tMWwFEHUg1MEHxtHZooxKicJZ9hHbF03x2QPc6fFzmuFcRztPL2EQ7Y4FTiaEiaWiaX6Syx527wLDetyBrCdlADvw4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/WvsNkg6cHNzzXElKB8iaYP4CLibzh6FC1Z6DlKIThHiatWRM41nPnvur6iaYMk3rNicUpjfOydKLoGKHicQusOplPoQupHRUGOtaMGlfxDjsOYXqw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/WvsNkg6cHNyUMrrRec4GoJOwlpOMJCSDRg89Bp36icOmOG1MWIs2fdRCv522a9A7trem5wyOzhdJngecSQAibibe3H2JlhnxlQxTfdicMrEgnSk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WvsNkg6cHNwr8drhhcUVkTLXibTSkciadDJ4zHOaa5hhciaKdtnFKypNPq1Wssabc0Q6K01arktjnias7PpVN9jpvyBRgicQWAQfokXtrHTfGxPY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/WvsNkg6cHNxPib2HP3wgQgQbLohllqzgGx0N3vFicjVDgAZKg7exGibMxoYIDVn8Qm3zwZaibftXqauDku0GX7ZmINwO9THmjtcR44tykdhnWoQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/WvsNkg6cHNwp8XCuKOcGwxPOvSicQFHDjZxL76mEIjPzbAcEFogxj0xsLULdNgX3a6cqRRXyXcQHxibL5czbvKV7kVWWZUbibStiaiaAxRfhCkRk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/WvsNkg6cHNz9mZOfQLt4XV5Qj9p2S71HibMAnATxrybtgeOAfN3SHIbv6M6WA3xnp6uSkl3SibOHfibAnCgkPdzpPdlJ2sTMjglhAibjia7uSM1Y/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/WvsNkg6cHNxMQKu6lIqhHQfEXAeUWaXEzuBg7haya0EQx8XK0DLvIiaQBib7icVWsCI2bQWqC2aep5xtX4CJbPoib5Qo8gAysVJuZFiaG6dxwhfQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/WvsNkg6cHNxFWINlflrFVt7w1eVM9NTLCd5O16SOWAZUXLZfQgKDDtfQA5zIOn5L0vW1SxV2AzaQB2QLnzUEhxdVkiaDlDY5NIp7n2GReVAg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/WvsNkg6cHNxyQR2ylY9a5tHfBJsl6Bdt7ic0wldALyrbmX7NG4ZMNuX6V7jy31ItD17P1k7yyibrNokektxMcGMwMricX34niaAsOqIlxggVCib8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/WvsNkg6cHNz4Wak41gaMgSxncI8y4kB9ZosYmZnDc8zdlUjvaxHlSDUic3bySG7fLI6ZeMhb8bJQxRZaL3TwJlGpKLBamId4ALa2Xjr4MeYo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/WvsNkg6cHNzXehIs8rcwiaxedKZkws5JlXicHvYCx6ibC4pEiadyFD4Wo0pFGu3FClaX4WiaDkbeFiaT63ycYmO1kicibFtMqiafNmt9HYGBDEs6xce8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/WvsNkg6cHNzf4KBFWL5G4rGXqSTB79Wxx33HyL4QHsXyibzibINuicCy9nVQbeVGlqiaMxzyibuSM1kUdbZXbZQ1uxHpcMojknRdIrCa5DF9cgI4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WvsNkg6cHNyQhgBoLMKT0XGmodSV8ufY9xBollKkaZFqImib8aYgyeFjTiahUkUC2pxclzjI5KqWzlMlibFZFDPPrLKlLZIgTEKyke56et69XE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/WvsNkg6cHNyYtLibodE8qdhdcBruUQibM7e77lkDzMiaTLKNX1tZWXaZw7PlUpDsslCEj7qgToNIaTLLyvlJyHFzXW3t1ahNGo0AtwhVbCQjPw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/b96CibCt70iabwjyojLhA03PtxUnkNPREnt2F48ywfXLpDdDAjicOTPI8Q94tVLbJ58tbRs12iaXDKhUOW9gd4NlFA/640?wx_fmt=gif)

相关文章

# [整车信息安全设计对车企的挑战与一汽奔腾的应对](https://mp.weixin.qq.com/s?__biz=MzU2MDk1Nzg2MQ==&mid=2247625124&idx=1&sn=59b4927682ea50cee36806fd47a874fe&scene=21#wechat_redirect)

# [智能网联汽车安全测评的中国方案与实践](https://mp.weixin.qq.com/s?__biz=MzU2MDk1Nzg2MQ==&mid=2247625164&idx=3&sn=2f238aba3764d28bb9cef471cf7a466c&scene=21#wechat_redirect)

# [国强标下智能网联汽车信息安全检测解决方案](https://mp.weixin.qq.com/s?__biz=MzU2MDk1Nzg2MQ==&mid=2247625164&idx=1&sn=af62fe3a85e6f1e172af7333e1d45218&scene=21#wechat_redirect)

#

![](https://mmbiz.qpic.cn/mmbiz_gif/MfTd6rd9CyvNRMW8I9cvI1CK5gKiaYqg2veTn9t9dAe1GxYic7pAvgvRIKNFickConFyX8AvW2reAq8GchJI6aBpA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_png/WvsNkg6cHNwzJ6g6cwDPWQPkMNSdxNzJNib6icvM2LNjWicc7Jdyzgduy5tKjYjt6ghKmiaHv6XEq28Et5pnOos5Y1icH8Wrx9SX03t7n1mmuE1g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WvsNkg6cHNx3XibDCcEHR7XYayO6ROlXoNkpaTZRl06QHfX1ncLMWf2RAUXM28XIrZIovlhoadFvJvBnZBQWfGeGrKAgZ9X42f3wA999JBZ0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WvsNkg6cHNwGy566FAz6qyctiblp3tMd0ECjDLU2WDiaI8BRricjYnobXF0KVMKf2W5aYoqYvcsCoZAyK4ibLWHL0W4KxgBsgGr0QvVHT8mUbPo/640?wx_fmt=png&from=appmsg)

![](https://...
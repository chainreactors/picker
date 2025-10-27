---
title: SRC挖掘-教育行业平台&规则&批量自动化
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495586&idx=1&sn=f65a14b283bb502d7af269fa1ac7b1db&chksm=e8a5e5c1dfd26cd7cb730c116309785d01361f3617785f807fedb4eaffec195840a85b3a8bc9&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-08-26
fetch_date: 2025-10-06T18:02:05.544747
---

# SRC挖掘-教育行业平台&规则&批量自动化

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj5s5qFRjdOR3d7fOhpjCCEs9pv2fDZh1Tm2C08dfHbduvIMiahlCEc30xzjVJLQZMPVAfVMNtqrI7Q/0?wx_fmt=jpeg)

# SRC挖掘-教育行业平台&规则&批量自动化

order by

迪哥讲事

## SRC挖掘-教育行业平台&规则&批量自动化

思维导图

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5s5qFRjdOR3d7fOhpjCCEsziaPjwB0jac5ut0YcTgEkMIqiawFTQFFCY1RwRzHzic7jLHLQic9gABQTw/640?wx_fmt=png&from=appmsg)

## 正文

案例1：Python-Foda-Xray联动常规批量自动化

写Python脚本，将教育行业漏洞报告平台上的所有学校都爬下来。

```
import requests
import time
from lxml import etree

def get_edu_name():
    for i in range(1,196):
        url = "https://src.sjtu.edu.cn/rank/firm/?page="+str(i)
        try:
            result = requests.get(url).content.decode("UTF-8")
            soup = etree.HTML(result)
            name = soup.xpath('//td[@class="am-text-center"]/a/text()')
            print('->'+str(i))
            print(name)
            name = '\n'.join(name)
            with open(r'edu_name.txt','a+',encoding='utf-8') as f:
                    f.write(name + '\n')
        except Exception as e:
            time.sleep(0.5)
            pass

if __name__ == '__main__':
    get_edu_name()
```

或者也可以在fofa上搜索（需要买会员）

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5s5qFRjdOR3d7fOhpjCCEsZibJw6dAK5uR9yhRe0PhiabJAUqsja08JVFp9a7sQpVYwZgEDex2maqQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5s5qFRjdOR3d7fOhpjCCEsglQjdzftoicysgibPiaiapK76c4XpTajicXoyNEft6L9h4iaInicKgibmkiaI8w/640?wx_fmt=png&from=appmsg)

结果爬下来173861个教育网站地址。

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5s5qFRjdOR3d7fOhpjCCEs1sGy2DnKXRT8B7pUGwS1eCuico8uFxLibe7y3ZXjEYPAfGKjpPmiabYmA/640?wx_fmt=png&from=appmsg)

域名都爬下来之后，用xray，awvs等工具进行批量测试。

案例2：Python-Foda-Exploit联动定点批量自动化

在seebug（https://www.seebug.org/）上找到一个最新的有POC的漏洞，对POC二次开发使之可以批量测试。比如jumpserver远程命令执行漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5s5qFRjdOR3d7fOhpjCCEs1nnbCuSBhzKn015E7MbbGmZ6peSXCL7qDZPnDPCyF9RaVJMEWWfUqQ/640?wx_fmt=png&from=appmsg)

在fofa上搜索使用jumpserver的教育行业网站，找到3个网站使用了jumpserver。

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5s5qFRjdOR3d7fOhpjCCEsibkGYQSvXWS4SeOvIsXdJyCEVL5K7RUiavDC2EPtV8WM3Kvrj8SF8Vlg/640?wx_fmt=png&from=appmsg)

对这3个网站使用poc自动化定点测试。

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

原文:https://blog.csdn.net/qq\_22132931/article/details/127246273?spm=1001.2014.3001.5502

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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
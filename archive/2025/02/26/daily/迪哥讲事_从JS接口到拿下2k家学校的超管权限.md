---
title: 从JS接口到拿下2k家学校的超管权限
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247497187&idx=1&sn=9d9ac4cde6a5b6d735a3e8dd50fd66cf&chksm=e8a5ff80dfd276968d253f3e66ae7f9380865dc9b66940acc2b99e3824061bbf408b19cecdc3&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2025-02-26
fetch_date: 2025-10-06T20:38:14.250712
---

# 从JS接口到拿下2k家学校的超管权限

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj6Nq73p2aYW1M2St5Ep1bwaialjBicEke1ARo6MYvSRxBaaibn88V0KbMgTQP4AzzaKcl7YY7aFtOY3g/0?wx_fmt=jpeg)

# 从JS接口到拿下2k家学校的超管权限

X1ly?S

迪哥讲事

## 0x01 信息收集

首先通过**网站标题**搞清楚了网站的性质，是一个某地的**站群系统**，集合管理着**大量的子网站**

![](https://mmbiz.qpic.cn/mmbiz_png/gxdFmXz8aflpFE3pS8ZKMZfQjETOYFgp3TesVsLktnfLzHkRZmBaLgZDnQZkx7cdZaGFowblBOdXTXxubjicdrA/640?wx_fmt=png&from=appmsg)

通过**Wappalyzer**了解使用的重点技术有：**Java、Swagger-UI、Spring、Vue.js、Webpack**

常用的**前后端分离**架构正是**Vue.js + Java(SpringBoot)，**于是可以初步判断该站点是**前后端分离架构**的。

**而前后端分离的架构，常涉及到前后端之间的数据的传递与调用，如果接口鉴权未做好，很容易出现API接口未授权的安全漏洞**

## 基本测试流程

简单的信息收集之后，接下来开始走一遍登录框的基本测试流程

1. 万能密码
2. 弱口令
3. 用户名枚举
4. 前端登录检验绕过
5. 找前端源码泄露
6. ……

这些基本流程走完后，不出所料，没有任何发现

那么既然是前后端分离的架构，当然得测一测JS中未授权接口了，于是展开对JS中未授权接口的详细测试

## 0x02 API接口提取

对于API接口的测试，前面也提过很多次了，我常用的工具是FindSomeThing、URLFinder并结合手工的方式去测试的

ok，先用FindSomeThing看看接口

![](https://mmbiz.qpic.cn/mmbiz_png/gxdFmXz8aflpFE3pS8ZKMZfQjETOYFgpZjKNvBvPWSDBKuDHotanxic3DVtTBx4IJVkFxVELwEeQcydhibgFGRvw/640?wx_fmt=png&from=appmsg)

好家伙，一个接口也没有，这种时候不要慌，前面信息收集提到了站点使用了**Webpack**，那么JS就被压缩打包了，这可能对该工具提取API接口有影响，或者是该工具的匹配接口的正则不适合于当前站点的写法的原因

**这种情况可以选择用URLFinder看看能不能提取成功，一般是可以的，但是这个工具爬取功能太强大了，爬取到API接口的同时，也会爬取到大量无用的数据和垃圾数据，之后仍然需要手工去把有效的接口筛选出来，数据多的时候反而效率不如手工直接找接口来得快，而且，还有一点，有时API接口不完整，需要拼接baseURL、baseAPI，该工具无法做到正确地拼接接口，也是需要手工去拼接的**

看看js文件

![](https://mmbiz.qpic.cn/mmbiz_png/gxdFmXz8aflpFE3pS8ZKMZfQjETOYFgpafzQmENxhhaHhKC3wQtfYHtMIA8brd2ZiaEo5IEsDWD1MzasOroAqBQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/gxdFmXz8aflpFE3pS8ZKMZfQjETOYFgpa9yT0eEiaMhTs4Wa748ibqR3zibFGhgnwsxic5LSVypyYp84tbUKoh6ezw/640?wx_fmt=png&from=appmsg)

果然有baseURL，是需要手动拼接接口的，于是我选择**手工+自写小脚本来进行API接口的测试**

```
import jsonimport reimport requestsimport sysimport os
headers = {    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
fileurl=sys.argv[1]
filemkdir=fileurl.split('_')[0]if not os.path.exists(filemkdir):    os.makedirs(filemkdir)

# 下载chunk.js# with open (str(fileurl)) as furl:#   url=furl.readlines()#   print(str(url)+"---is---downloading")#   for url in url:#       url=url.strip('\n')#       file=url.split('/')[-1]
#       resp = requests.get(url)#       html = resp.text
#       with open ("./"+filemkdir+"/"+file,"a",encoding="utf-8") as f1:#           f1.write(html)

#get path  + 路径名称paths=[]for dirpath, dirnames, filenames in os.walk('./'+filemkdir):    for file in filenames:        with open("./"+filemkdir+"/"+file,"r",encoding='gb18030', errors='ignore') as f2:            try:                line=f2.readlines()                for line in line:                    line=line.strip('\n').strip('\t')                    #print(line)                    p =  re.findall('''(['"]\/[^][^>< \)\(\{\}]*?['"])''',line)                    #print(p)                    if p != None:                        #print(p)                        for path in p:                            path=path.replace(':"',"").replace('"',"")                            paths.append(file+"---"+path)            except Exception as e:                print(e)

for var in sorted(set(paths)):    with open (fileurl+'_path.txt',"a+",encoding='gb18030', errors='ignore') as paths:        paths.write(var+'\n')
```

先把base路径单独提取出来

然后再去提取后半段的API接口作为字典

然后再放进burp里批量跑一下接口，固定一个base路径然后跑字典，缺参数就去找参数或者猜测FUZZ，请求方法不对就改方法，以此类推

剔除掉一些401的接口，这些接口就是正确地鉴了权的，基本不用看了，除非校验字段可伪造(JWT漏洞，弱cookie等等)

剔除掉一些404的接口，403的接口可以尝试绕一下

然后根据测试结果，手工分类了一下API接口

![](https://mmbiz.qpic.cn/mmbiz_png/gxdFmXz8aflpFE3pS8ZKMZfQjETOYFgpWal8rQY8X9ia9HJibbciavC2dgGFrhtsUs9rlsc9DcCVW6KmTzXHpOOPg/640?wx_fmt=png&from=appmsg)

可以看到收获还是颇丰的，有些接口能**直接看到大量的数据**，但是不是什么很敏感的数据，接下来，就是逐一对这些接口进行**单独测试**，首选一些比较重要的接口，比如upload，password，username，admin，manager，upgrade，newpasswd，post等等之类的

0x03 API接口测试

最开始，这个接口没有填任何参数就SQL报错

![](https://mmbiz.qpic.cn/mmbiz_png/gxdFmXz8aflpFE3pS8ZKMZfQjETOYFgpU3bIZ2OlZjXCp5QhI9P7bhRjJPkK1auBOeSRmS1fpWibb1KLRkkeVPA/640?wx_fmt=png&from=appmsg)

那么这里大概就是缺少一些必要的参数了

于是首先我回到JS源码中去找，全局搜索该接口，看了看**上下文**，没有找到，**简单跟进了一下调用的函数**，还是没有找到

![](https://mmbiz.qpic.cn/mmbiz_png/gxdFmXz8aflpFE3pS8ZKMZfQjETOYFgphdgOh49v72G7Qa9oAxVqlfN2yGC13m7XUL1z8kCXYxREpw1YEq4DFg/640?wx_fmt=png&from=appmsg)

然后我又**手翻遍了整个app.js**，并结合上下文仍然**没有**找到任何一处有API接口的参数定义的地方

那么基本可以确定这里单独凭借对JS的搜索与审计是无法找到参数的，**要么是做了某种混淆要么就是参数压根就没有写在前端！**

这种情况就只能采用**暴力手段**了，**直接FUZZ参数**试试看能不能找到，使用**Arjun**去FUZZ参数，使用**burp**去FUZZ也一样，重要的是字典和哪个更顺手吧

![image-20240819114740469](https://mmbiz.qpic.cn/mmbiz_png/gxdFmXz8aflpFE3pS8ZKMZfQjETOYFgpnIdmNCSceZUE6AWz8NSibhDDgGunzwdqvZMBm0w1FyiaJU0Msc6zJJpQ/640?wx_fmt=png&from=appmsg)成功找到了几个参数，拼接上去试试看吧

> 还有一种方式，就是用自写的小脚本，**提取所有JS文件中的所有单词**，然后再使用**burp**爆破！这样不管你**webpack**打包压缩之后的JS文件有多复杂，参数也大概率就在这些单词之中！但是这次没有找到

经过几个参数的排列组合，最终发现拼接**limit+page**两个参数可以得到大量数据！

![](https://mmbiz.qpic.cn/mmbiz_png/gxdFmXz8aflpFE3pS8ZKMZfQjETOYFgpBVljryVJQx7cSslsvV7gicdxjzfuQP7pk4OFQZ2X5K2qJiaqZP0So1Vw/640?wx_fmt=png&from=appmsg)

得到了大量的学校的数据，一共有312页数据，每一页的数据量相当可观！

**但是只是得到了大量的该区的幼儿园、小学、中学的学校名称(也是子站点的名称)危害很小，而许多的敏感字段数据都是空白的，应该被脱敏了或者定期清理了吧**

```
{"date":0,"updateDate":"","trend":0,"sumNumberSite":0,"siteName":"xxxxxxxxxxxxxx","delFlag":"0","sumNumberArticle":0,"listId":[],"articleNumber":"","updateBy":null,"enable":0,"limit":0,"statusName":"","id":294,"judge":"","createDate":"","trendDate":"","wxArticleNumber":"","site_token":"","count":313,"pageBean":null,"statissList":"","dateNumber":0,"ipSumber":0,"sumNumberVisit":0,"createBy":null,"name":"","siteId":0,"page":0,"remarks":"","startDate":"","stopDate":"","status":false},
```

```
注意到了这里的参数是limit+page，那么肯定想着测测SQL注入咯，于是加单引号触发报错
```

![](https://mmbiz.qpic.cn/mmbiz_png/gxdFmXz8aflpFE3pS8ZKMZfQjETOYFgpcSRb11ZgnXB5dBXZU5HnIIibFT4IPhVwqHqp0cPuHIZWZSGIrZibrzxg/640?wx_fmt=png&from=appmsg)

好吧，这里把参数值进行了**强制数据类型转化**为了**数字型**，SQL注入没戏了

**ok，其他的接口也是如法炮制，逐一测试就行，要有耐心**

## 0x04 测试成果

### 0x001 未授权获取全站所有用户名数据

像这样的数据还有三百多页，每一页的数据量相当可观，前面点的一页有**302条**数据，就算每页**200条**数据，那么粗略估计全站用**siteName**数据就有接近**6w条**，而经过后面的测试发现，**站点登录的用户名正是siteName**，**即该接口可以获取全站接近6w条的用户名！**

![](https://mmbiz.qpic.cn/mmbiz_png/gxdFmXz8aflpFE3pS8ZKMZfQjETOYFgpmtoPwflLbtb7fvWbF9uj6JmsfT2X4UxanFiaoA8OIdcPchz4r2bjAZw/640?wx_fmt=png&from=appmsg)

0x002 未授权删除调查问卷

这个接口通过路由可以看出来是删除调查问卷的，不算很敏感，于是就尝试了删除

![image-20240819135514137](https://mmbiz.qpic.cn/mmbiz_png/gxdFmXz8aflpFE3pS8ZKMZfQjETOYFgpHiauxz0lXFsPbqRAnNplTN24X9yNpzXLqu18DhhX7Z6S5LFicb8MSgGg/640?wx_fmt=png&from=appmsg)

### 0x003 任意用户菜单未授权删除

这个接口是user类的接口，功能是删除，但是还没有确定具体是删除什么东西，由于这个接口比较敏感，便没有轻易尝试FUZZlist的参数值，而是随意填写了参数值，避免对站点数据造成破坏，**但这里存在删除操作的未授权是无疑的**

![](https://mmbiz.qpic.cn/mmbiz_png/gxdFmXz8aflpFE3pS8ZKMZfQjETOYFgpbalJGORHKwD3OBxaeE63OVZCvUqFibPesc6UJ5nGogUy8tDxY2zxFhw/640?wx_fmt=png&from=appmsg)

### 0x004 未授权保存用户权限

![](https://mmbiz.qpic.cn/mmbiz_png/gxdFmXz8aflpFE3pS8ZKMZfQjETOYFgpUhpyDvyicx5nRdTic4Sz7Xo90RBo53TLe7cicYurp8ibARFPicLqN1fyDnQ/640?wx_fmt=png&from=appmsg)

### 0x005 查看全站操作日志

![](https://mmbiz.qpic.cn/mmbiz_png/gxdFmXz8aflpFE3pS8ZKMZfQjETOYFgp881dIs7wYkUV7LaS6HR0fTIaIBILzUXliaA7gdHhFmPfcPmfYLNYLTg/640?wx_fmt=png&from=appmsg)

敏感数据还是被脱敏了，可恶(bushi)

0x006 未授权获取大量超级管理员权限

其中一个接口，**FUZZ**出**site.id**参数名，再去**Burp****FUZZ**参数值，得到如下结果

终于！在手工逐一看了这么多的接口之后，让我找到了敏感信息，**子站点的超级管理员密码+姓名+电话+登录IP**，而且数据量非常可观

![](https://mmbiz.qpic.cn/mmbiz_png/gxdFmXz8aflpFE3pS8ZKMZfQjETOYFgpQBVIxlTHRVjAGUAKc3t7k4YUD3GF3TeSlQiaibXyB1PSZ62Oyiaq6g2eg/640?wx_fmt=png&from=appmsg)

**目测估计有好几百家学校吧**

把得到的密码进行解密(也可以不解密，直接在burp发包)，**登录用户名**绝大都是**学校的名称**，只有少部分是自定义的

因为有些密码解密需要购买点数，而且有些密码无法被解密，于是我不想买(穷)，**于是采用直接burp发包的方式登录**

![image-20240819161739057](https://mmbiz.qpic.cn/mmbiz_png/gxdFmXz8aflpFE3pS8ZKMZfQjETOYFgpRBiclplPpKMaJbdmyeRoOk1lwg3Fziciabo7dYoSQUibrCYuYOyRsbaA9A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/gxdFmXz8aflpFE3pS8ZKMZfQjETOYFgpkEnFRJ9qKmrcicf0wTPQ7YLvgu4qXZGLbB528zQO1xSkmjibw43sibhzg/640?wx_fmt=png&from=appmsg)

**非常好，密码是可用的！返回了token！**

...
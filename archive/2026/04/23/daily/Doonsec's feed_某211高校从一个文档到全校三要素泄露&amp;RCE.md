---
title: 某211高校从一个文档到全校三要素泄露&amp;RCE
url: https://mp.weixin.qq.com/s/XNe2xRx_yVgJtwfMgDxolg
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:53:50.686115
---

# 某211高校从一个文档到全校三要素泄露&amp;RCE

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboRSHA8FSQIibqZJYOcLjjRJaSQiaEQrgDYAk3vKr9yiaSiakUicspZqbPAGKILRm6Eq7Re8WccG3WuaTJZugZY9iaRE6iaJLO4NByEFC4/0?wx_fmt=jpeg)

# 某211高校从一个文档到全校三要素泄露&RCE

陌笙
陌笙

陌笙不太懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

```
作者:byname原文链接:https://xz.aliyun.com/news/91869
```

# 一个非同寻常的信息泄露

开局一个登录框：

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQpq64gcq553p8uamrzoUicexMrwEe0NySRAqbNEKoChHdQPibqicR5UE7HrluOx23kdka0Wqfh6XfDZMDKFO9d7K1160V700Dgl4/640?wx_fmt=png&from=appmsg)

右下角有一个"点击查看操作手册"就很显眼，让人很有想点击的欲望。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSia6iagia6t4wznluzlTpKv9YFrs66kB0dDuTczXynS2JFVUOt8onUxvKUcAwMUYnzATDIOicc4gdYCYwVOqmyj2CZKYHcZGz2ORs/640?wx_fmt=png&from=appmsg)

现在了然了账号和密码的默认格式，于是便很兴奋地谷歌尝试搜索**site:xxx.edu.cn filetype:pdf 学号**的相应信息，但一无所获。

又去看看网站的前端代码，测测SQL注入，插件找一波接口...同样很正常地没用任何进展。

正当感到无计可施，想要切换下一个站点之际，一不小心又点进了刚才的"操作手册.doc"文档，然后随便地往下翻动：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRRIKWSpZJ9Pv7fmpeoiabc6yXXaxibGGj7kia67xEKK8uJmKoGwC7ClZXzT7Y4bILTDMp9FCXDPmfJjbqicYQoaVOJn06f4IPbeibc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSpia85mCwlsQgDEMzSicUVXSBPrW695DoZcqeLHwGicwQckdb5LjSNQIEjeHkE5jZA73ib4eicOS2OicDQImGtaWPEx78ic5YwT0UDpQ/640?wx_fmt=png&from=appmsg)

除却姓名学号这种每个学校的文件都随处可见的信息，敏感信息都打上了🐎，不得不说，二幺幺高校就是不一样，安全意识确实做得很到位。

...

不对，好像掠过去了什么东西？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQxXvhxnicYMd0fGlSo5mVeuuIdyGAObN37FHib4e19PKWrdYshA5x86YWjBLeMficwuvtS14WpvfBIPUc0C2wXribv1HHDhRtxUsk/640?wx_fmt=png&from=appmsg)

利用泄露出来的学生信息成功登录！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTPcm4l9aetc7FMHXNZRACnibRxNPIG69UCCLicYEwGyFctJ6QIQ6883d3pl1ZPSppnIZzdKJGPJqAvGX5n3CViaicdp3ObrZII1ibA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQDPc81c6DRwagXTXbs3T03B4b537exg3iarFnALy137Kblapz7n62Ko7Pe2ShOibsgNoUqJZGnepNQZo5YtyIKDiaSh3XDGYdFR4/640?wx_fmt=png&from=appmsg)

然后就可以愉快地测试了^^

# 初步测试

## 垂直越权

返回登录框，抓包。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRA6oODOkk3EVIKDQSPlqjI7ZDll2DicwpBvuXM9o9IVtMskJ78iaSxDKBibg0qN2TPnwFbD1gxSs6TLhjMSQFbgntorHhgUylBibI/640?wx_fmt=png&from=appmsg)

经典roleId，常用来表示用户权限。也可以翻下前端找一下哪个数字代表哪个权限，这里就懒得翻了。

一般数字越小权限越大，这里直接改成1。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR80vD9dY2ymFThibtykYicTjkJjC0SHx3yFpvicROjQNvoJQHANMosQ3ictQbenZtPWttLgKwNdlRu6t7GVCic04SGZhp71sarDbLE/640?wx_fmt=png&from=appmsg)

提示用户不存在。

也就是where roleId=1没有查到，鉴权做得很棒啊！

试试改成2呢：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboS8CHY084USxnWegpoW7hWIIXIqycXwB7Tsh9VyVMrnWhaYfiblBjKSbBAJwrnIDVaybvmDL4YXkrRQ6jcJX2TJMeSRSFYQh6Po/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSCZrpaS3s3FpgiaLYI2s7h2DjcAAOaux1WjibfyBXxOzia3jytjGwlgHYvLlYcLhmdvlSP0nK1FwYgjhw4mGGacxxrOB06dBYKIU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSMszpJCEaYicB9KMV1TsA4kA6iaNcXqWsIx8fmtD5ic034QaTNHtDLsR3eouuB6egZECyTibmPFwOvTUqu0tgrSpWq6JQiaMFla1d0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR6syQg8Lo3auvKfgVsR7FBqX7VGDCRq6Sdtdqnc3icx6VxYib7ZNSgfYgdTzIia1icRIfZoicfKbh4s9yyBUqicrnOnTzUV6ohX4ma4/640?wx_fmt=png&from=appmsg)

新增成功！

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQGiaODicdm6FaAx2GE5JaklwKBAQV5CIMXOCKUZhQLQ7GFcII5xZm1vrbr73ty3g98twTpxFutiaA9ribjpMzsosEISQWZrstH6Lc/640?wx_fmt=png&from=appmsg)

新增一个管理员账户，回看前端登录的样式知道肯定学生用户和管理员后台登录是分开的，那么下一步便是寻找登录接口。

看一眼Findsomething插件，刚好存在一个/loginadmin的接口。

拼接一下url，成功得到管理员后台登录入口：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSBTgp2JtOqy0dePd0TY1fzZRVrwmqarpLkIRibUibws9AIys9qicqlNoDxpXOXS2MnAS3fHFibzVRE93ibuSC5jYW5UXDyXSsiaNAFo/640?wx_fmt=png&from=appmsg)

登录刚刚新建的管理员账号：

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRdqfmLBia7jwO9VI2v1lYBSn5WZJIZMZuP9P7rprmRvZ5p22b8T9xcdiaIs5kx12Ggf4oAuG2Nydicic3vBEZTI9W5hFGiaV5GQHu4/640?wx_fmt=png&from=appmsg)

这里能看的东西就挺多了，在申请记录里存在大量学生申请的含有敏感信息的文件：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboT4VldyXN95ibbFgHwVoLtoU104ZVPvIIbg7u2k082IkUXjDgYicWM0y5mnyfsbypTBOAYkqDk5iazVibkDGayTx2gnSJu1OKpwq9M/640?wx_fmt=png&from=appmsg)

还能修改申请文件、印章的收费：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRZiadYOEprXCun977xb7NZ5oBYDcvT8AKO8VZgaQF9SB7sunXh1z4fxyiaRa0Y06O7FjZY8srucnZiaa8XRjZHvVAMfib4KeprCtc/640?wx_fmt=png&from=appmsg)

## 一些踩坑

一个普通的账号常见的还有水平越权，比如对于这种情况下的学生账号，可以请求文件时抓包看看请求的参数是否可控，就可以通过修改参数如学号去查看其他人的敏感文件。

这是一个请求文件的数据包：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboS3pjHh221aYPBPIo18eE4XDEBH41aSFsvYd9UH0wwAemVJ8Vn2whG93cqAsljDjiaDX5lDXLSuuHGWv0icDCNMeNbPDc2ibXu92s/640?wx_fmt=png&from=appmsg)

有一个X-Authorization字段，解码可知是JWT验证，记录了user信息包括学号等，极大概率是控制返回文件的字段；userId为学号，修改后发包无果。

因为又没抓到其它有有效内容的返回包，所有的参数只有可能是从前端传出，便有些突发奇想尝试一下：也许这个fileProperty是这里控制返回文件的参数，比如是通过一些加密算法将学号加密成这样的形式，只要我能逆向定位到加密JS，用其它的学号加密然后发包就能越权看到其它人的文件。

于是开始了漫长的JS逆向之路，由于网站前端是webpack打包，还去学习了一下相应的逆向技术。

后面才想起，坏了，这好像是UUID。。。它是数据库后端生成的而非前端加密学号生成的。。。

它之所以不在接口的返回包出现，是因为这里的UUID就像表单CSRF-Token一样，从一开始登录就自动附着在html元素之中了。

# 越权超级管理员

借用管理员权限测试时，某些特殊功能还是会弹出一个权限不足的提示，比如改变邮箱模块等等。

于是猜测到这个站点还应该存在一个超级管理员权限。

只是回头看之前添加用户的功能点：

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQp2E5GWpxNLXBOXTxZmhuJeXh9zgpZwlpWytxH5iaTN7p63SqicszmgBVNCPtWy9gV7vnlrG8233wVAHsGuvfn9EcTDJ8HN7c2Y/640?wx_fmt=png&from=appmsg)

网站是对添加超级管理员这个功能进行限制了的。

但是结合之前测得的这个网站的特性，添加一个任意账号，抓包看添加用户的数据包：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQM9N9vnAQ1GKHyhsXXhpDicYJwxnXicKlF8YlXPXw87GqnTabx3B287AfYppBo4eOv9KcLfzpckbHF3oUAfywxHBdmRKAiaJC97s/640?wx_fmt=png&from=appmsg)

修改roleIds参数为1。

添加成功！

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRgpoCibLx6mnWvXeyFiblvQ6zkBoKocSriaCE1CSibKNHoNprHxqwsu2YFmb0Cia9RkQrcxdSicibiaNO5sZZbib6ZBxdmcAvOMznyS48I/640?wx_fmt=png&from=appmsg)

切回管理员登录接口，登录该账号：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTFwvQjibwPFdDJg20fibrEf88D8LmZBKpClOGBOsCeULiaQk4ac65V4JysMOTticVrjrDYKE8LjdEJEfb24dmNLHl8mVzJHSbb6yo/640?wx_fmt=png&from=appmsg)

菜单的功能又多出了很多，其中，在某个菜单下，**暴露了该校所有18w学生的sfz号码！**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSKjZXHgwZibWlk7XeXjMToibBos8e3YLVlaqksdVGD3HjZNPftzz8thqFdFdkfpgNg2b0iclWNMMDLfdtuhF0udJDjQwvlhavib9g/640?wx_fmt=png&from=appmsg)

# RCE

深入每个功能都测了测，也得到了其它的一些敏感数据，但是大多却没什么用。

难道就止步于此了吗。。

都拿到了超管权限，信息泄露只是苟且，RCE才是梦想。

终于在茫茫多的功能中找到了一个很特殊的地方：

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTkuibhWWNcQdSQuicfPAjJGTtTrPrbBKFiaicBTXvbJ3tPr4hPbLZicfMjQd4zIkib44vSo9pBs3K7wexax9hicpU48XoMZMVoM3B00Y/640?wx_fmt=png&from=appmsg)

可以编辑SQL语句。

且看文件名称，与学生用户端前台的"文件请求"一致：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTdJPXf0HAmq1RL2c4m1DkGnIiaRFsHh2It1fswFOF2OgAW2icl2tUGnQhwsSTaAT14L94hnzfkl8uCrdNc2fCpVWojbVZ1ONvB0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboS0aa4Vf0XVAdkzQolxy7FxsLA9HXlsuwJhle8aXcXdgjrOeBZ1zjdbOUib3gKZVZVAafHGE7IRhPpaodwUfyiaUX5Zj3ibBz0GDk/640?wx_fmt=png&from=appmsg)

那么便很容易猜测，前台用户每点击一次文件，后端就肯定会执行一下所谓"报表SQL""菜单SQL"的语句并返回结果。

如果是这样的话，添加些恶意的SQL，比如外带数据库名等等，可能也会回显到得到的文件里。

不多说，开始测试。

由于这个网站的用户量还挺大，为了不影响学校网站的正常运行便拉着一个访问量最小的文件类型进行尝试。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTlDqf82BKS7wrfz82h9FZibnuh1l7XgXaBm4E20BMCEA3oKn0VjzHLm5b63Bu4CEUMia8wNQ69haicibTLLgSm9kcdbRwQnpvxzzI/640?wx_fmt=png&from=appmsg)

这一试花费的时间可就太多了，也遇到了挺多问题：

这个网站的报表SQL、菜单SQL还有前端都有牵连，字段甚至语法都不能弄错，否则很容易就会出问题，执行不了一点。

更让测试受阻的是每个用户申请文件，如果申请成功(但大多数时候数据库名都不会回显到文件里)，**网站都会对申请到的文件进行缓存**，并沿用上一次SQL请求的返回结果，意味着我的每一次尝试都可能要换一个新的账户(只能说还好之前获取的账号很多).......

终于，尝试了无数个payload，终于外带了一次数据：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQAI5D0DHt0icVqukwgXlnDOlbFdPpl5nY75o9iaibBDDxEibnToHibnlO6sicUzaOJe9dB9DQ6jKawKI7yUfgtP9E8QeTEPH55dxOhU/640?wx_fmt=png&from=appmsg)

```
SELECT xbFROM dbo.cxsyxm aLEFT JOIN z_V_xsjbxxb b ON a.xh = b.xhWHERE a.xh = '学号' AND a.rn = '选中值' UNION SELECT db_name();
```

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR5ohZ1YGuBDibBicJ4CH1dI1GbDwFDnmUHQ0hMkpaNLYnRZqtuNjBpJYePG7PYrYVlUoeQO7WjLnufiaNKQpNYOOwM1WBfYB3rTU/640?wx_fmt=png&from=appmsg)

某211高校从一个文档到全校三要素泄露和RCE

![](https://mmbiz.qpic.cn/sz_mmbi...
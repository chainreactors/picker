---
title: 2026FIC初赛（服务器+互联网+U盘）
url: https://mp.weixin.qq.com/s/VHc7HgA4OBNOVjLgVBjh7A
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:23:59.427886
---

# 2026FIC初赛（服务器+互联网+U盘）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/T5C6icTcSx9OOiaoKOIDiaGMiabuypI3pC2Yd8KrnqNiaTrtJtbRcQzibTia04sgAHeXdUaMS75Jzzpz3iagDyjreJB5Xh5NxOpZBglwHknEdOLPO9E/0?wx_fmt=jpeg)

# 2026FIC初赛wp（服务器+互联网+U盘）

原创

Serendipity
Serendipity

Serendipity的小屋

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

检材密码：`FIC-{e404d6e66586e9460c23755afab5a872bcf78ab4}`

完工✌️！

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9Pic3M1O5cvT6r5EEbpN8ibp8V34jlnKKtj8OhiaB6kRqh7qlAO0P10HIib4Th6cicNagP3Fqr1L4SL3kz9eFCxBQicz8PgwQQg3JlD4/640?wx_fmt=png&from=appmsg)

> did平台上有些答案是错的或者是格式不对

## 服务器部分

> 这个服务器主要就是难在了仿真这块，当然也可以不仿真直接ai做，这里我还是仿真做法

仿真的时候把两个镜像都放进去

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9NNGUqpKcGflK4ibx42ZKicFkhWWlJQ40IJiaZURTIfFJicSlC4FKRPwaoAdrbABF78ebl04IqMOoANYia0j8veMrCRvz8n76Ob5xzg/640?wx_fmt=png&from=appmsg "null")

会显示操作系统检测失败，有人说最新版可以检测到，但是我就是最新版，不知道为什么

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9MUsDy09YeD0ia8konGBhyG0GfjRPibHyVLVJeUc8ECVsk7qjztuu7X2JO4ibCbe6rpxMia5GUDicdRgKzTNic5ZdicaUjxrsA0wPOxhs/640?wx_fmt=png&from=appmsg "null")

自定义选择操作系统，选择其他仿真即可。

启动虚拟机可能有一段时间是黑屏，这是正常的，因为太卡了，我启动了一下3D图形好像会好一点

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9Muicia6iaSk6V7z5RIGAuiaxVrhSO7ibb5m6u3lIcyZ3kqrVjPicC9DCs9kNiazZnXXzIRW84unYQow5ueAzeR15icqIWoaianjicYusnqI/640?wx_fmt=png&from=appmsg "null")

成功仿真

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9PAoqHVkvBe1L2lAFqjT0zEDNicYqeryXn9je4IOAk4VzIlFVw8uvicC5HlIM6AFf87GYhoZSKh3VgjyhQm6AlzL4f26tPENMe7Y/640?wx_fmt=png&from=appmsg "null")

用finalshell连接的时候发现没有ssh，所以装一下ssh（可以先往后看，少走弯路，因为我要干坏事）

```
sudo apt updatesudo apt install openssh-serversudo systemctl status ssh / service ssh start如果系统防火墙已启用，需要开放SSH端口sudo ufw allow ssh
```

这里输命令的时候别管他卡不卡，直接输了按回车就行

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9Pj4LJPrIaKMFEyGtvu73Jlsw2pZichVE5Sqr5AV7klweJ98iaIuM6Ga3E7U7NicZsccP6OAicZ21SlnwzKrr9iceWs9TcibUYWBZsuU/640?wx_fmt=png&from=appmsg "null")

用finalshell连接一下，不然太折磨了，这里注意账号为mac密码为123456

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9Nicibz0ayatbCzAoE92GU1eST4nibJowarJxHENj0k7ec7VkCjwiaMzxH7Qchwt8PRROc1Ir7yL8NvlPLYCFOptD3N76OqdNhL80k/640?wx_fmt=png&from=appmsg "null")

很好，你以为这就结束了吗，其实刚刚那一切都在容器里，因为做题的时候发现什么都没有，甚至不能用systemctl还有用ls的时候蹦出来的东西![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9MnGIIemwbm0VdTpDAVObMOibpr9OJO19xTDGZwKeyWaVTSBy3YucowvrCYGibXnW6FoWvBKoc7D9DUNVUGficXVvDnQvqghbGdPI/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9OAibdNCZ6TVsYiaD5DG3icHK54NXSWkElUY9BvG97ysuf6pp9oGR3JVgxsumA2WOULVyD0e1wfNcsNk6GbufYEPiayRwUGbZSbY6k/640?wx_fmt=png&from=appmsg "null")出题人真恶心啊，所以我们需要按ctrl+alt+f2退出容器（在按之前，记得先把容器里的ssh卸载掉，不然会冲突的，如果已经按了，可以重启一下然后卸载`apt-get remove --purge openssh-server`，如果不行，重新仿真一下虚拟机）
退出容器之后，进入虚拟机，这就对味了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9PhBVa39tL1vMHhx70POib0MZVdibk8jOiaic5cna3uaMriaVq5V4lefY8o6batiaPACo4wxbiatibV2qxJkkqgticDOTdtia3KibhxSa7alc/640?wx_fmt=png&from=appmsg "null")

重新安装ssh吧😼 安装好之后，编辑一下配置文件`vim /etc/ssh/sshd_config`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9OXuRjsDF8gYxo9CrvVlUaP5MJFDicrFVHEEvcxmLQgl1FdRiaZ6MeWGWplyiapvtzhBjibYAvtwODxYkzNoyn2BbtmIY28za8lRvA/640?wx_fmt=png&from=appmsg "null")
然后重启ssh`service ssh restart`这样就可以用root身份连接了

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9MUASk9wgTFWXcqBdZuQicUt6ADwECWZskwJwe5zuIRLX1Qy9RqCr1aWUoibmBvytJ9X3Rt3JgJ3u9bBfWibCPKYfdEZZic40JSjJg/640?wx_fmt=png&from=appmsg "null")

现在就可以让ai用ssh连上服务器大放光彩了😁

### 1. 该服务器主机操作系统版本为 【参考格式：0.9】

**Debian GNU/Linux 13 (trixie)**

查看系统版本`cat /etc/os-release`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9M4B4LqRLBtib23puibpPnE4bB9bicKXiakznhdgXKYRVJJj8BhFkGVict2p1tTic7UD5HcyOS5pHtyiapBYlhKeyrVquXLNnrJicoroLM/640?wx_fmt=png&from=appmsg "null")

### 2. 该服务器根分区硬盘的uuid号为 【参考格式：a1b2-c3】

**3231e52f-5e15-44c4-b224-e29cb4201c0e**

`cat /etc/fstab`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9PDkIa4HnJE8MV9mMlBXHTbwY2snujEodAg4YrGr22wSzm99GJevMYwYWOnU99uWAxr4Z1HORh3vut11Epa6gSIicFOKjKTNvqc/640?wx_fmt=png&from=appmsg "null")

### 3. 该服务器中最新的docker镜像创建时间为 【参考格式：2020-01-01T00:00:00.012345678Z】

**2026-04-16T07:15:50.535713491Z**

查看Docker镜像列表及创建时间

`docker images --format "{{.Repository}}:{{.Tag}} {{.CreatedAt}}"`

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9MC3CeakOtEicW1Nkzwib2eIDuicfPeribzKdGictfGbFlBj4WoHDRtpzHfPJLQdFLcXHwFV19yu9gg88mAtWwmUR425z10cdb73wkk/640?wx_fmt=png&from=appmsg "null")

### 4. 该服务器根分区快照路径为 【参考格式：/abc/def】

**/root/history**

查看根分区文件系统类型`df -Th /`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9NXb5rJx6EibqcaNgcN4PfR4fZrTyGlqcfGVH1Pj55Klmp0FCYcsicUF5lEovhcd6N3TwriaOyL43EmmF6QPxPfFKwGSNdeGT3dhE/640?wx_fmt=png&from=appmsg "null")

列出所有btrfs子卷`btrfs subvolume list /`

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9PPBoe6Flm8Jia0YBu1V6MW1lTN1qfVWMclSMCe7Kiaovuwlzsp6oyRV15MzsicdAALIhjYFST8sKJ2q5ljB5ZpNQglbNSZVtRibqc/640?wx_fmt=png&from=appmsg "null")

查看子卷详细信息，确认 `root/history` 为快照`btrfs subvolume show /root/history`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9O2C9MXtJZVU9WJ0Znw5hNSg8gJ1lJjAQt5hwiarr41beD0qaiaWDZzv3FnEPrlSh466f6EL2libCqgCBqx5n9sw1WXkjgN9v3mw8/640?wx_fmt=png&from=appmsg "null")

### 5. 该网站后台管理入口对应的文件名为 【参考格式：123.txt】

**user.php**

在`/etc/nginx/sites-enabled/default`中找到网站根目录`root /var/www/html/maccms10`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9OnHibhqNsvSpJBia6RMFBx6nI4h6L4ZzkooGPaGQe8ThoEE85amLiadrFlWxQic3nG7IJHyMNeREgA8ibYz44xRRicLM9ia9Zts95HRc/640?wx_fmt=png&from=appmsg "null")

去网站根目录找一下后台管理文件`/var/www/html/maccms10/`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9OwU5c8FfXcFwRHF61kZhyczrwTQkEfVQo3NtUhAcspsG5xLzKXy7IWGCicITvIy5oq7ESwEia6CibcOnhYAttYeyYBzLeIicEw93w/640?wx_fmt=png&from=appmsg "null")

看到一个user.php文件

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9OjGcAeqoq9CcG3LNpHoV3ZsT99OVBtiaUiatzHBlzHnX6FFlt45yoCcnQvex6Psc2Zew4woJzdDuP82qG6iaUPly8XAyEcsuOccU/640?wx_fmt=png&from=appmsg "null")

说明是改名改成user.php的

### 6. 该网站设置的icp备案号为 【参考格式：icp123】

**icp1919810**

查看MacCMS站点配置文件`/var/www/html/maccms10/application/extra/maccms.php`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9OGvSTf4MOrDibDsicUmNNEK8wJIt5gWibP7wjXR4fMrLcvXqQ2on8hibhjsK1utZeWbpbj0F0AGDBNbvd5FSibGhArYB6ntic42ia16Q/640?wx_fmt=png&from=appmsg "null")

### 7. 该网站设置的主域名为 【参考格式：abc.com】

**www.2026fic.forensix**

由上题可知

### 8. 该网站分类3中，视频的拼音为 【参考格式：abc】

**sipaanshe**

在`/var/www/html/maccms10/application/database.php`找到数据库信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9MbbVolcb7XDXiaUROdaicD1KnEKicib4ACBiaVicuddsffvFS2b85F8lzEJs8TuWHbQoK5uOR8Gp4Tyx7tNwmengeVtszEvDiamKFcwU/640?wx_fmt=png&from=appmsg "null")

连接数据库

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9Mk05aRXOwZPXUqoFEJjCUGdscbg50yK8esrE7icqJrcEWObfVVbLk6vJibE8vXQlPp5haGmfEekIKO0BCGl4IrNd99FfCHrpiaDA/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9OD7zYxOJuNOdhhib1U81jWbrjlx3y69XdorOzOpibE5jgZSYxJbP8AKXy0KiciaBtONdAk07Q762oNLTeUMoKIOcPLpySZuuMDQRQ/640?wx_fmt=png&from=appmsg "null")

成功连接数据库

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9M3KrIicehibHG3m9VxDRwBINgg7bv6ElcOz4y61U8NpNxM0TYvaol5licSsYdb0IQiciaxfcCdZDibOu3fulzBSic4QBy5uiagFpLeliao/640?wx_fmt=png&from=appmsg "null")

```
SELECT vod_id, type_id, type_id_1, vod_name, vod_enFROM mac_vodWHERE type_id=3 OR type_id_1=3;
```

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9N7qgD9o0hgR3lSzteickEweypPYUOicKXJDspNMvwVIDFv6baI173iciawsRRgPkGsT1ucgUP6aYhicZAuEvM5jI2TibLXu2y8N8DL4/640?wx_fmt=png&from=appmsg "null")

### 9. 该站点设置页面中，被使用的前端模板来自于哪个源文件？ 【参考格式：abc.def】

**info.ini**

查看当前使用的前端模板配置`/var/www/html/maccms10/application/extra/maccms.php`

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9Pg5zfaq18HqWVXmesmYZhSPmRRicCnwegCYjDkDOxmQeib6yNJkcPO07FmdlXZxNXpBdhmlSeVuiao1e4pxicTTicbg8PiazVH0Xicdw/640?wx_fmt=png&from=appmsg "null")

去`/var/www/html/maccms10/template/001tep/`找文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9MlX0h5tQr7C1aiaOSZlcKF5TmhpubWicuHjc2WEMj1LlTHysmcLnv7tkKhiaAsk6Lu7nGFJzcAHoicIl1LicnXLpicb7TeJG2rrh2AU/640?wx_fmt=png&from=appmsg "null")

打开...
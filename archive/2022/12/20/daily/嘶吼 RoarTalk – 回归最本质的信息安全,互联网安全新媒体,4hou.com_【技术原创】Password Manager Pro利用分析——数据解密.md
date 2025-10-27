---
title: 【技术原创】Password Manager Pro利用分析——数据解密
url: https://www.4hou.com/posts/RBD0
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-20
fetch_date: 2025-10-04T01:58:13.497398
---

# 【技术原创】Password Manager Pro利用分析——数据解密

【技术原创】Password Manager Pro利用分析——数据解密 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 【技术原创】Password Manager Pro利用分析——数据解密

3gstudent
[技术](https://www.4hou.com/category/technology)
2022-12-19 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)117826

收藏

导语：在上篇文章《Password Manager Pro漏洞调试环境搭建》介绍了漏洞调试环境的搭建细节，经测试发现数据库的部分数据做了加密，本文将要介绍数据解密的方法。

**0x00 前言**

在上篇文章《Password Manager Pro漏洞调试环境搭建》介绍了漏洞调试环境的搭建细节，经测试发现数据库的部分数据做了加密，本文将要介绍数据解密的方法。

**0x01 简介**

本文将要介绍以下内容：

数据加密的位置

解密方法

开源代码

实例演示

**0x02 数据加密的位置**

测试环境同《Password Manager Pro漏洞调试环境搭建》保持一致

数据库连接的完整命令："C:\Program Files\ManageEngine\PMP\pgsql\bin\psql" "host=127.0.0.1 port=2345 dbname=PassTrix user=pmpuser password=Eq5XZiQpHv"

数据库连接成功，如下图

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665286719150376.png "1665284369201129.png")

**(1)Web登录用户的口令salt**

查询Web登录用户名的命令：select \* from aaauser;

查询Web登录用户口令的命令：select \* from aaapassword;

结果如下图

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665286721855714.png "1665284396991378.png")

password的加密格式为bcrypt(sha512($pass)) / bcryptsha512 \*，对应Hashcat的Hash-Mode为28400

其中，salt项被加密

**(2)数据库高权限用户的口令**

查询命令：select \* from DBCredentialsAudit;

输出如下：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665286722129263.png "1665284462194438.png")

password项被加密

**(3)保存的凭据**

查询命令：select \* from ptrx\_passbasedauthen;

结果如下图

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665286722133585.png "1665284497726658.png")

password项被加密

导出凭据相关完整信息的查询命令：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665286723156494.png "1665284561143947.png")注：

该命令引用自https://www.shielder.com/blog/2022/09/how-to-decrypt-manage-engine-pmp-passwords-for-fun-and-domain-admin-a-red-teaming-tale/

**0x03 解密方法**

加解密算法细节位于C:\Program Files\ManageEngine\PMP\lib\AdventNetPassTrix.jar中的com.adventnet.passtrix.ed.PMPEncryptDecryptImpl.class和com.adventnet.passtrix.ed.PMPAPI.class

解密流程如下:

**(1)计算MasterKey**

代码实现位置：C:\Program Files\ManageEngine\PMP\lib\AdventNetPassTrix.jar->com.adventnet.passtrix.ed.PMPAPI.class->GetEnterpriseKey()

如下图

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665286724152259.png "1665284629161206.png")

首先需要获得enterpriseKey，通过查询数据库获得，查询命令：select NOTESDESCRIPTION from Ptrx\_NotesInfo;

输出为：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665286724107220.png "1665284709282765.png")

这里可以得到enterpriseKey为D8z8c/cz3Pyu1xuZVuGaqI0bfGCRweEQsptj2Knjb/U=

解密enterpriseKey的实现代码：

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665286725144710.png "1665284754894386.png")跟进一步，如下图

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665286725154449.png "1665284966132895.png")

解密的密钥通过getPmp32BitKey()获得，对应的代码实现位置：C:\Program Files\ManageEngine\PMP\lib\AdventNetPassTrix.jar->com.adventnet.passtrix.ed.PMPAPI.class->get32BitPMPConfKey()

代码实现细节如下图

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665286727186908.png "1665285005103086.png")

这里需要先读取文件C:\Program Files\ManageEngine\PMP\conf\manage\_key.conf获得PMPConfKey的保存位置，默认配置下输出为：C:\Program Files\ManageEngine\PMP\conf\pmp\_key.key

查看C:\Program Files\ManageEngine\PMP\conf\pmp\_key.key的文件内容：

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665286728183687.png "1665285056330266.png")

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

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665286729183170.png "1665286215204292.png")

这里直接获得了明文口令N5tGp!R@oj，测试该口令是否有效的命令："C:\Program Files\ManageEngine\PMP\pgsql\bin\psql" "host=127.0.0.1 port=2345 dbname=PassTrix user=postgres password=N5tGp!R@oj"

连接成功，证实口令解密成功，如下图

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665286729127130.png "1665286246238342.png")

解密保存凭据的命令示例：select ptrx\_account.RESOURCEID, ptrx\_resource.RESOURCENAME, ptrx\_resource.DOMAINNAME, ptrx\_resource.IPADDRESS, ptrx\_resource.RESOURCEURL, ptrx\_password.DESCRIPTION, ptrx\_account.LOGINNAME, decryptschar(ptrx\_passbasedauthen.PASSWORD,'u001JO4dpWI(%!^#') from ptrx\_passbasedauthen LEFT JOIN ptrx\_password ON ptrx\_passbasedauthen.PASSWDID = ptrx\_password.PASSWDID LEFT JOIN ptrx\_account ON ptrx\_passbasedauthen.PASSWDID = ptrx\_account.PASSWDID LEFT JOIN ptrx\_resource ON ptrx\_account.RESOURCEID = ptrx\_resource.RESOURCEID;

输出如下图

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665286730163602.png "1665286280923857.png")

提取出数据为PcQIojSp6/fuzwXOMI1sYJsbCslfuppwO+k=

**(3)使用PMPConfKey解密得到最终的明文**

通过解密程序，最终可计算得出明文为iP-6pI24)-

登录Web管理后台，确认解密的明文是否正确，如图

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665286730154432.png "1665286316170168.png")

解密成功

**0x03 开源代码**

以上测试的完整实现代码如下：

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665286731166893.png "1665286594886665.png")![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665286732198677.png "1665286609168559.png")![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665286733653776.png "1665286622209358.png")![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665286734184619.png "1665286636457223.png")![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665286735146271.png "1665286648726150.png")![21.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665286736623239.png "1665286662197790.png")![22.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665286737646430.png "1665286681978755.png")![23.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221009/1665286738166168.png "1665286697143714.png")

代码修正了https://www.shielder.com/blog/2022/09/how-to-decrypt-manage-engine-pmp-passwords-for-fun-and-domain-admin-a-red-teaming-tale/中在解密MasterKey时的Bug，更具通用性

**0x04 小结**

本文介绍了Password Manager Pro数据解密的完整方法，修正了https://www.shielder.com/blog/2022/09/how-to-decrypt-manage-engine-pmp-passwords-for-fun-and-domain-admin-a-red-teaming-tale/中在解密MasterKey时的Bug，更具通用性。

本文为 3gstudent 原创稿件，授权嘶吼独家发布，如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://...
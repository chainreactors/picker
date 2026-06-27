---
title: 在 Excel 中结合 Copilot 技能，完成重复性任务
url: https://mp.weixin.qq.com/s/RVHQvUlr9MH_wyvssyZ__g
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:49:14.935722
---

# 在 Excel 中结合 Copilot 技能，完成重复性任务

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5BBJWJhb0eibbOGp0cWQTOJEgvUr1Jb1qlg6TqMDNNIIsw1NenhqU2ULoNHw9MnXicr4t1L9sdiblFe7q3hKSID7jUxibWulJn9ujWypwQnZZh8/0?wx_fmt=jpeg)

# 在 Excel 中结合 Copilot 技能，完成重复性任务

原创

copilot
copilot

AI技术笔记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 技能可以扩展 AI 模型的能力。技能会为 Excel 中的 Copilot 提供所需信息，帮助它完成重复性任务。在 Excel 中使用 Copilot 时，你可以从 Copilot 窗格中选择已有技能，也可以创建自己的自定义技能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5BBJWJhb0eichNSWjm1hVm7vpggWic1DZ6VsCs2wvuWS6nJRx4YbhQeZX0B56Hd6L1TiaVptqFqz9iaqeXUwxya83wyNbGZFU0ffj94o5yrGiaSE/640?wx_fmt=png&from=appmsg)

## 使用技能

要使用某个技能，请打开 Excel 中的 Copilot，在提示词输入框中选择“添加工作内容”菜单，然后选择“所有技能”。

“所有技能”列表会显示 Excel 中 Copilot 提供的技能，以及你已上传的自定义技能。若要了解如何创建自己的自定义技能，请参阅“创建自定义技能”。

![Screenshot of the Copilot in Excel 'Add work content' menu, with 'All skills' highlighted.](https://mmbiz.qpic.cn/sz_mmbiz_png/5BBJWJhb0eicEn5Cf56hfDriborKAnAOuCnzWIicCbDQF81xiaepKBjIaK7GO1ey0aeLlXEZ8BicsQwCAZcqys85w4pbO8yxMzxdZ1YJbwyJ4LPc/640?wx_fmt=png&from=appmsg)

如果想在请求中调用某个特定技能，你可以从“所有技能”菜单中选择该技能，也可以直接使用 @ 提及的方式输入它。

例如，要调用名为“datapack-builder”的技能，可以在给 Copilot 的提示词中输入 @datapack-builder

![](https://mmbiz.qpic.cn/mmbiz_png/5BBJWJhb0e97eRia3OE2DLjh3o7xB6cD7uKtumzRfvJdzbHUO2rNFEqReC1znPiaAdxwBUPteZuwLceyFibviaqyej39nL9Mqcm5AZL1icCliaJgs/640?wx_fmt=png&from=appmsg)

## 管理技能

你可以开启或关闭技能，以控制 Excel 中的 Copilot 默认使用哪些技能。要管理技能，请选择“设置”菜单，也就是右上角的“…”按钮，然后选择“管理技能”。

![](https://mmbiz.qpic.cn/mmbiz_png/5BBJWJhb0eiblPS5gZqVUB4lAxgcsEp4eUJHCqmqKDlib5INSuDUUjeSXdibuE8HGJFFUQIqfia0vwENcr4jibez72DXBt5WO3uhtAGbjzFzHH1o/640?wx_fmt=png&from=appmsg)

在“管理技能”对话框中关闭某个技能后，Copilot 将不会自动使用该技能。不过，即使该技能已被禁用，你仍然可以在提示词中通过直接 @ 提及的方式使用它。

![](https://mmbiz.qpic.cn/mmbiz_png/5BBJWJhb0eic3Dwlqciat0WmoKqllPLectuVUJhibssdsCMQJzD1mkMU2W55qtPDzbMHKquLWK1t0xjSWk6fUicYb82S2qrtDkmeWtaeWjiaBIPc/640?wx_fmt=png&from=appmsg)

## 创建自定义技能（尚未上线）

自定义技能由你上传，并会保存到你 OneDrive 账户中的指定文件夹。如果你经常让 Copilot 执行同一类请求，可以将这个请求转换成一个技能。你可以随时编辑自定义技能，也可以随时启用或禁用它们。

要创建自定义技能，请按照以下步骤操作：

在 Copilot 窗格中，选择“设置”菜单，也就是右上角的“…”按钮。
选择“管理技能”。
选择“自定义技能”。
选择“创建 OneDrive 文件夹”。Copilot 会创建 OneDrive 技能文件夹。
选择“打开技能文件夹”。Copilot 会在你的 OneDrive 中打开新的技能文件夹。
将你的技能添加到该文件夹中。你可以使用所在组织创建的自定义技能，也可以创建自己的技能。有关如何创建自定义技能的详细信息，请参阅“自定义技能格式要求”。

## 自定义技能格式要求（尚未上线）

自定义技能必须遵循行业标准格式，才能被 Excel 中的 Copilot 识别。每个技能都需要一个独立文件夹，并且该文件夹中必须包含一个用于定义技能的 SKILL.md 文件。

SKILL.md 包含两个部分：

第一部分是元数据区域，位于文件顶部两个三短横线分隔符（—）之间，称为 frontmatter。它包含技能名称和描述，用来告诉 Copilot 在什么情况下使用该技能。这个部分是必需的。

第二部分是正文区域，也就是你的具体说明，用来告诉 Copilot 如何完成任务。这一部分没有格式限制。

下面是一个简单的 SKILL.md 示例，对应的技能名称为 create-table-bold-first-column。要让 Excel 中的 Copilot 识别该技能，这个 SKILL.md 文件必须放在名为 create-table-bold-first-column 的文件夹中。

---
name: create-table-bold-first-column
description: Use when I ask Copilot to create a table in a worksheet. After the table is created, bold the first column.
---

# 创建表格时加粗第一列

当 Copilot 创建表格时，请将第一列加粗，以便让行标签更加突出。

## 步骤

1. 按照请求创建表格。
2. 选择新表格的第一列。
3. 对该列应用加粗格式。

有关标准技能格式的更多信息，请参阅《Agent skills: Specification》。

## 编辑或移除技能（尚未上线）

##

如果你在 OneDrive 中添加或重命名了某个技能，请在“自定义技能”对话框中选择“刷新”，这样 Copilot 才能识别相关变更。

![Excel自定义技能对话框中高亮刷新按钮的副驾驶截图。](https://mmbiz.qpic.cn/mmbiz_png/5BBJWJhb0e8sUSLkHoAytcqv5JMxMn2nsPuJfAvTpqURg4VLSbhfFmpuxVBbnz1t2wLtKlibAczxKmSxFsThicZ82P7ANQxZxrW3SwkQ8LMLc/640?wx_fmt=png&from=appmsg)

如果想从 Copilot 的技能列表中移除某个技能，但不删除 OneDrive 中对应的文件夹，可以更改该技能文件夹的名称。Copilot 会跳过任何文件夹名称与 SKILL.md 中技能名称不匹配的文件夹。

目前该功能只能在英文界面上使用，中文界面还不支持，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5BBJWJhb0e82V0L25SOKwbX8F2M8GYqvw7o3GvGAibx0xN4eqywWhh8oWfKAKAQtLP4PUNNzcPfEYLcico0Hf9oPIcSBEXrZDsXQ78WPRH6Cw/640?wx_fmt=png&from=appmsg)

如图所示，中文界面打开“管理技能”时一直处于加载中，无法使用。

![](https://mmbiz.qpic.cn/mmbiz_png/5BBJWJhb0eic30J4KZZTickodh0xNdqgvkhycot4gOjbC0NEKuI0LP8lZ04rrhlCcEfiaDEyibnLkjewgdaHC65PibVGKmRtkwsQncxYufvHqKy4/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/7G5SkFzrbOV2KI6NT8PiaTy5BKZSxN3mf3dcRoEDA1hxhr1sptAnY2kgjbTXb4u3gEXFEyc31q3wZTrCSyqycWw/0?wx_fmt=png)

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
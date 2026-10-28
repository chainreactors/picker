---
title: U盘反病毒抢救数据
url: https://blog.nsfocus.net/u%e7%9b%98%e5%8f%8d%e7%97%85%e6%af%92%e6%8a%a2%e6%95%91%e6%95%b0%e6%8d%ae/
source: 绿盟科技技术博客
date: 2026-10-27
fetch_date: 2026-10-28T07:47:59.661871
---

# U盘反病毒抢救数据

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)
* [登录](https://blog.nsfocus.net/wp-login.php)

* [首页](https://blog.nsfocus.net)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* U盘反病毒抢救数据

# U盘反病毒抢救数据

[0](https://blog.nsfocus.net/u%E7%9B%98%E5%8F%8D%E7%97%85%E6%AF%92%E6%8A%A2%E6%95%91%E6%95%B0%E6%8D%AE/#comments)

![](https://secure.gravatar.com/avatar/99bcec439a2a5078218073d2459e8069eb89b5ce5cbf840afef1c3ed7395d75c?s=40&d=identicon&r=g) [NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "written 2026-10-2716:34") 发布于 23 小时前

![](https://blog.nsfocus.net/wp-content/uploads/2026/05/封面-25.jpg)

阅读： 37

### 场景介绍

前段时间给张三处理过一次U盘病毒，Windows Defender报了两个高危

Trojan:Win32/Fragtor.ARA!MTB
Backdoor:Win64/ToneShell.A!dha

报警界面中出现两个DLL，其中一个是

X:\\\\$WinUpdate\RBGUIFramework.dll

另一个当时没记下来。

这种只看路径，就知道异常。正常情况下，路径中不可能出现连续反斜杠，视觉上出
现这种效果时，路径中必含不可见的零宽Unicode字符。

资源管理器去X盘根目录，看不到异常子目录。从Windows Defender复制上述路径，
粘贴到资源管理器中，回车，可进入$WinUpdate子目录，下面一堆EXE、DLL。恶意代
码主要集中在被报警的两个DLL中，其余EXE算载体。

这款U盘病毒感染U盘后，将U盘上原始数据转移到名字畸型、多层嵌套的目录里；沿
线各级目录均带系统、隐藏双属性，目录名携带不同零宽Unicode字符；只在X盘根目
录留一个文件，名为

USB Disk(117 GB).exe

若资源管理器未设置成始终显示扩展名、文件类型，那此文件看起来是

USB Disk(117 GB)

其图标被精心构造过，看不出是EXE。张三看到这枚U盘时，以为自己未打开U盘，对
之双击或右键打开，殊不知实际执行了EXE，将加载恶意DLL。

追溯U盘动向，张三曾在自己之外的多台不可控电脑上插入过该枚U盘。由于不具备技
术背景，他完全无法有效回忆，已然说不清最早在哪台电脑上染毒，溯源失败。

此EXE除了加载恶意DLL，另有一主要功能，自动打开U盘原始数据被迁移后的目录，
让普通用户以为双击此EXE就是打开U盘。张三正是深陷此种骗局而不自知，多次双击
此EXE，四处传播病毒。

此U盘病毒并非高度定向，张三属于范围感染者之一，病毒特征早已位于各大杀软特
征库中。现代Windows默认自带Windows Defender并启用中，因此张三莽撞之际，万
幸在某台电脑上被拦截，出现前述高危报警，但张三并未意识到。后来张三找我，谈
及每次都要双击前述EXE才能看到U盘内容，觉得有点奇怪，病毒这才彻底暴露。

简单看了一下$WinUpdate目录下的其他PE，明显带远控、文件传输等功能。不知张三
实际受损情况几何？不幸中的万幸是，此病毒以窃取数据为主要目的，可能并不疯狂
感染其他PE。手工处置时，这种病毒算是最”友好”的。若是勒索软件，上来二话不说
就加密本地文件，请来神仙也没招，交钱还得看对方讲不讲究，大概率不讲究。

在特定单位、特定人群中，会存在未自带Windows Defender的老旧操作系统，即使自
带，也未必能联网更新病毒特征库，它们亦未禁止”可移动介质自动执行”功能，
autorun.inf仍有机会。这些电脑是U盘病毒极佳宿主，特别利于横向传播。至少在相
当一段时间内，U盘病毒并未远去，它们只是在等待机会。

另一方面，自己电脑处于高防状态，架不住要与低防电脑共用U盘。我的建议是，对
外始终用一枚容量不大的专用U盘，务必不将高价值数据置于这种对外交换U盘中。只
要它在其他电脑上插过，回到自己电脑时，先用杀软过一遍，甭管你觉得里面是空与
否。有条件的话，资源管理器设置成始终显示扩展名、文件类型，养成打开文件前看
一眼”文件类型”列的习惯。若非绝对必要，这枚U盘只对外提供数据，不从外部回收
数据。取回U盘后，上下文允许时，直接快速格式化，简单粗暴但有效。万一这些做
不到，至少要做到另一条，意识到异常后，不抱任何侥幸心理，第一时间封存，找懂
行之人协助处置。

### 抢救数据

遭遇这类U盘病毒，除了杀毒，可能还需要抢救U盘数据。若按我前述建议，就不会面
临此困境，但有些人会。

抢救数据的基本操作是

a. 找出存放U盘原始数据的隐藏目录，可用dir或PowerShell
b. 卸掉系统、隐藏双属性，可用attrib或PowerShell
c. 对含有畸形Unicode字符的目录、文件重命名，可用ren或PowerShell

上述操作均为命令行形式，不要在资源管理器中干这些事，阻碍太多。

1) cmd内部命令dir

dir /a /r /q /t:a X:\

检查X盘根目录是否含隐藏项，注意最后一次访问时间

dir /a /r /q /t:a /s X:\\*.exe

在整个X盘遍历查找exe，可换dll等其他扩展名

dir /a:sh /r /q /t:a /s X:\

病毒一般会创建带系统、隐藏双属性的目录、文件，找出它们

2) attrib.exe

attrib /d /l X:\\*.\*

检查X盘根目录所有项的属性

attrib /s /d /l X:\\*.\*

在整个X盘遍历，显示目录、文件的属性

attrib -s -h -r /s /d /l X:\\*.\*

在整个X盘遍历，卸掉系统、隐藏、只读属性

3) PowerShell

可用PowerShell脚本完成dir、attrib、ren的工作，下面是分步示例，实战时让AI写
个整合版。

————————————————————————–
# 指定目标路径，比如X盘根目录
$target = ‘X:\’
$items = @(Get-ChildItem -LiteralPath $target -Force -ErrorAction Stop)
$report = for ($i = 0; $i -lt $items.Count; $i++) {
$item = $items[$i]

$units = (
$item.Name.ToCharArray() |
ForEach-Object { ‘{0:X4}’ -f [int]$\_ }
) -join ‘ ‘

[pscustomobject]@{
Index = $i
Type = if ($item.PSIsContainer) { ‘Directory’ } else { ‘File’ }
VisibleName = ‘[‘ + $item.Name + ‘]’
UTF16 = $units
Attributes = $item.Attributes
# 反引号续行
VisibleFullName `
= ‘[‘ + $item.FullName + ‘]’
}
}
$report | Format-List
————————————————————————–
-Force

同时枚举隐藏项和系统项

-LiteralPath

将输入路径按字面值处理，不把其中的\*、?当作通配符

-Recurse

递归遍历
————————————————————————–

注意VisibleName、UTF16、VisibleFullName，是否包含恶意Unicode字符，比如零宽
空格。

————————————————————————–
# 从前述脚本得到的 $items 中选择目标，指定目标项的索引，比如2
$entry = $items[2]
$longPath = ‘\\?\’ + $entry.FullName
$attrs = [System.IO.File]::GetAttributes($longPath)
$attrs
# 示例输出
# ReadOnly, Hidden, System, Directory
————————————————————————–
$mask = [int](
[System.IO.FileAttributes]::System -bor
[System.IO.FileAttributes]::Hidden -bor
[System.IO.FileAttributes]::ReadOnly
)

$newAttrs = [System.IO.FileAttributes](
[int]$attrs -band (-bnot $mask)
)

[System.IO.File]::SetAttributes($longPath, $newAttrs)
————————————————————————–

上述脚本相当于”attrib -s -h -r”指定项。后续操作均假设目标项已卸掉SHR属性。

————————————————————————–
# 可能含恶意Unicode字符
$oldPath = ‘\\?\’ + $entry.FullName
$parent = $entry.FullName.Substring(
0,
$entry.FullName.Length – $entry.Name.Length
)
# 指定只含普通字符的名字
$newPath = ‘\\?\’ + $parent + ‘recovered\_001’

if ([System.IO.File]::Exists($newPath) -or
[System.IO.Directory]::Exists($newPath)) {
throw ‘New name already exists, try another one.’
}

if ($entry.PSIsContainer) {
[System.IO.Directory]::Move($oldPath, $newPath)
} else {
[System.IO.File]::Move($oldPath, $newPath)
}
————————————————————————–

假设$items[2]名字含恶意Unicode字符，无法正常操作，上段代码将$items[2]重命
名为”recovered\_001″。

### 畸形/恶意目录、文件名

资源管理器中创建、修改item name，结尾不会出现空格、点号，这是explorer.exe
自己加的限制，不是底层文件系统的限制。通过适当的Win32 API可生成这种畸形
item name，在资源管理器中无法对之进行有效操作，经常报”找不到”。多年来，U盘
病毒、恶意软件常利用这点阻止用户访问、删除它们。

只用Windows自带工具处理这种item name时，需利用\\?\前缀，比如

ren “\\?\X:\path\taildot.” foo.bar

但是，rename目录名时，源目录不支持”\\?\”语法，所以ren可修正异常文件名，无
法修正异常目录名。

更多细节参看

————————————————————————–
CreateFileA function
https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilea

File Streams (Local File Systems)
https://learn.microsoft.com/en-us/windows/win32/fileio/file-streams

Naming Files, Paths, and Namespaces
https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file

Path prefixes \??\ and \\?\ – Eryk Sun [2017-09-03]
https://stackoverflow.com/questions/23041983/path-prefixes-and
————————————————————————–

### 畸形/恶意Unicode字符

常用恶意字符

U+200B ZWSP (Zero Width Space) 零宽空格
U+200C 零宽
U+200D 零宽
U+202E RLO (Right-to-Left Override) 从右到左强制覆盖
U+202C PDF (Pop Directional Formatting) 终止符

这些恶意字符零宽、不可见，在资源管理器中肉眼无法察觉其存在，甚至产生误导性
视觉效果。比如”U+202E”，导致其后所有字符整体反序显示，于是

ann[U+202E]txt.exe

产生视效

annexe.txt

你以为这是个TXT，双击实际执行EXE。

cmd dir倒是可以发现异常，但不够直观。可用PowerShell脚本处理这些情形。

1) 在线不可见字符查看工具

https://sosec.io/tools/text-inspector
https://originality.ai/blog/invisible-text-detector-remover

在cmd或资源管理器中F2复制item name，贴到上述网页，可查看item name中不可见
Unicode字符。

2) U盘病毒实例

用在线工具查看前面那个路径

X:\\\\$WinUpdate\RBGUIFramework.dll

显示

X:\[U+200D]\[U+200D]\[U+200C]\$WinUpdate\RBGUIFramework.dll

其中三级目录的名字是单个零宽Unicode字符，同时这些目录带有系统、隐藏属性。

最后修改日期: 2026-10-27

### 作者

![](https://secure.gravatar.com/avatar/99bcec439a2a5078218073d2459e8069eb89b5ce5cbf840afef1c3ed7395d75c?s=96&d=identicon&r=g)

[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/)

## 最新发布

* [精彩回顾 | 绿盟科技2026 TechWorld智慧安全大会高光时刻](https://blog.nsfocus.net/%E7%B2%BE%E5%BD%A9%E5%9B%9E%E9%A1%BE-%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%802026-techworld%E6%99%BA%E6%85%A7%E5%AE%89%E5%85%A8%E5%A4%A7%E4%BC%9A%E9%AB%98%E5%85%89%E6%97%B6%E5%88%BB/)
* [U盘反病毒抢救数据](https://blog.nsfocus.net/u%E7%9B%98%E5%8F%8D%E7%97%85%E6%AF%92%E6%8A%A2%E6%95%91%E6%95%B0%E6%8D%AE/)
* [“一底座两主线”助力水电工控系统安全联防联控——绿盟科技参与第七届水电、新能源工业控制系统安全技术交流会](https://blog.nsfocus.net/%E4%B8%80%E5%BA%95%E5%BA%A7%E4%B8%A4%E4%B8%BB%E7%BA%BF%E5%8A%A9%E5%8A%9B%E6%B0%B4%E7%94%B5%E5%B7%A5%E6%8E%A7%E7%B3%BB%E7%BB%9F%E5%AE%89%E5%85%A8%E8%81%94%E9%98%B2%E8%81%94%E6%8E%A7/)
* [绿盟科技顾杜娟博士获评 “2026中国网络安全十大人物”，前沿研发实力获行业认可](https://blog.nsfocus.net/%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E9%A1%BE%E6%9D%9C%E5%A8%9F%E5%8D%9A%E5%A3%AB%E8%8E%B7%E8%AF%84-2026%E4%B8%AD%E5%9B%BD%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E5%8D%81%E5%A4%A7%E4%BA%BA/)
* [针对PHP高危漏洞，绿盟科技更新8类安全产品规则，守护用户业务安全](https://blog.nsfocus.net/%E9%92%88%E5%AF%B9php%E9%AB%98%E5%8D%B1%E6%BC%8F%E6%B4%9E%EF%BC%8C%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E6%9B%B4%E6%96%B08%E7%B1%BB%E5%AE%89%E5%85%A8%E4%BA%A7%E5%93%81%E8%A7%84%E5%88%99%EF%BC%8C/)

## 文章导航

[上一篇文章 “一底座两主线”助力水电工控系统安全联防联控—...
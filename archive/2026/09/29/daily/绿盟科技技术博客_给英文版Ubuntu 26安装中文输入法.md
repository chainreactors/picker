---
title: 给英文版Ubuntu 26安装中文输入法
url: https://blog.nsfocus.net/%e7%bb%99%e8%8b%b1%e6%96%87%e7%89%88ubuntu-26%e5%ae%89%e8%a3%85%e4%b8%ad%e6%96%87%e8%be%93%e5%85%a5%e6%b3%95/
source: 绿盟科技技术博客
date: 2026-09-29
fetch_date: 2026-09-30T07:42:42.698885
---

# 给英文版Ubuntu 26安装中文输入法

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
* 给英文版Ubuntu 26安装中文输入法

# 给英文版Ubuntu 26安装中文输入法

[0](https://blog.nsfocus.net/%E7%BB%99%E8%8B%B1%E6%96%87%E7%89%88ubuntu-26%E5%AE%89%E8%A3%85%E4%B8%AD%E6%96%87%E8%BE%93%E5%85%A5%E6%B3%95/#comments)

![](https://secure.gravatar.com/avatar/99bcec439a2a5078218073d2459e8069eb89b5ce5cbf840afef1c3ed7395d75c?s=40&d=identicon&r=g) [NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "written 2026-09-2914:38") 发布于 1 天前

![](https://blog.nsfocus.net/wp-content/uploads/2026/06/11.png)

阅读： 23

最近需要在英文版Ubuntu 26 GUI主控台输入中文，只能后续加装中文输入法，记录
备忘。

apt update
apt purge ibus-table-cangjie-big ibus-table-cangjie3 ibus-table-cangjie5
rm -rf ~/.cache/ibus-cangjie
rm -rf ~/.config/ibus-cangjie
apt install ibus-table-wubi ibus-libpinyin
dpkg -l | grep ‘ii ibus’

不知为何，系统里已有仓颉输入法，大陆地区用不上，卸掉。安装五笔、拼音两种输
入法。

————————————————————————–
Settings
Keyboard
Input Sources
Add Input Source
Other
English (US)
Chinese (WuBi-Jidian-86-JiShuag-6.0)
Chinese (Intelligent Pinyin)
Keyboard Shortcuts
View and Customize Shortcuts
Typing
Switch to next input source
Super+Space (Super即Win键)
Switch to previous input source
Shift+Super+Space (只能在前者基础上增加Shift，无法真正独立设置)
System
Region & Language
Manage Installed Languages
Keyboard input method system
none (另有IBus、XIM可选，但保持默认值none，不影响原始需求)
————————————————————————–

做完这些设置，建议立即重启OS使之生效，避免一些莫名其妙的BUG。若中途有些设
置无法进行，很可能是之前的设置尚未生效，重启再试。

一切正常的话，GUI右上角区域出现”en”，点击它，下拉列表里有五笔、拼音输入法
可选。除了鼠标选输入法，还可快捷键选输入法，默认用”Win+空格”，不是”Ctrl+空
格”，这个快捷键最坑，之前不知道，死活呼不出中文输入法。

.bashrc中设有两个环境变量:

export LANG=en\_US.UTF-8
export LC\_ALL=en\_US.UTF-8

在GNOME Terminal中测试中文输入法，成功。

Ubuntu 26默认终端不再是传统的gnome-terminal，而是GTK4应用ptyxis。

dpkg -l | grep ptyxis

描述是”Modern terminal emulator for GNOME”。

进入GNOME Terminal时，GNOME桌面自动向之注入下列环境变量:

QT\_IM\_MODULE=ibus
QT\_IM\_MODULES=wayland;ibus
XMODIFIERS=@im=ibus
COLORTERM=truecolor
TERM=xterm-256color

不需要也不应该在/etc/environment、.bashrc等文件中显式设置它们。SSH会话没有
这些环境变量。QT\_IM\_MODULE给Qt应用看；QT\_IM\_MODULES给Qt 6应用(Wayland)看；
XMODIFIERS给X11应用看。不建议全局设置:

GTK\_IM\_MODULE=ibus

建议动作:

mkdir -p ~/.config/gtk-3.0
vi ~/.config/gtk-3.0/settings.ini

mkdir ~/.config/gtk-4.0
vi ~/.config/gtk-4.0/settings.ini

[Settings]
gtk-im-module=ibus

仅当GTK应用的中文输入出现问题时，尝试上述设置，否则先不要做。

对Ubuntu 26来说，中文输入法的所有配置通过GUI完成即可，无需关心下列文件:

~/.xinputrc
/usr/bin/im-config
/usr/bin/ibus-setup
/etc/X11/Xsession.d/70im-config\_launch
/usr/share/im-config/im-config\_setting
/etc/default/im-config
/usr/share/im-config/xinputrc.common

最后修改日期: 2026-09-29

### 作者

![](https://secure.gravatar.com/avatar/99bcec439a2a5078218073d2459e8069eb89b5ce5cbf840afef1c3ed7395d75c?s=96&d=identicon&r=g)

[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/)

## 最新发布

* [四次进化，绿盟科技将开拓怎样的安全新境？](https://blog.nsfocus.net/%E5%9B%9B%E6%AC%A1%E8%BF%9B%E5%8C%96%EF%BC%8C%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E5%B0%86%E5%BC%80%E6%8B%93%E6%80%8E%E6%A0%B7%E7%9A%84%E5%AE%89%E5%85%A8%E6%96%B0%E5%A2%83%EF%BC%9F/)
* [微软9月安全更新多个产品高危漏洞通告](https://blog.nsfocus.net/%E5%BE%AE%E8%BD%AF9%E6%9C%88%E5%AE%89%E5%85%A8%E6%9B%B4%E6%96%B0%E5%A4%9A%E4%B8%AA%E4%BA%A7%E5%93%81%E9%AB%98%E5%8D%B1%E6%BC%8F%E6%B4%9E%E9%80%9A%E5%91%8A/)
* [微软8月安全更新多个产品高危漏洞通告](https://blog.nsfocus.net/%E5%BE%AE%E8%BD%AF8%E6%9C%88%E5%AE%89%E5%85%A8%E6%9B%B4%E6%96%B0%E5%A4%9A%E4%B8%AA%E4%BA%A7%E5%93%81%E9%AB%98%E5%8D%B1%E6%BC%8F%E6%B4%9E%E9%80%9A%E5%91%8A/)
* [Fastjson 2.x远程代码执行漏洞通告](https://blog.nsfocus.net/fastjson-2-x%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E%E9%80%9A%E5%91%8A/)
* [Fastjson 1.2.x无需gadget远程代码执行漏洞通告](https://blog.nsfocus.net/fastjson-1-2-x%E6%97%A0%E9%9C%80gadget%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E%E9%80%9A%E5%91%8A/)

## 文章导航

[上一篇文章 绿盟科技入选Gartner®《2026中国网络安全技术成熟度曲线》11项细分领域](https://blog.nsfocus.net/%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E5%85%A5%E9%80%89gartner%E3%80%8A2026%E4%B8%AD%E5%9B%BD%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E6%8A%80%E6%9C%AF%E6%88%90%E7%86%9F%E5%BA%A6%E6%9B%B2%E7%BA%BF/)

[下一篇文章 使用Ubuntu 26远程桌面](https://blog.nsfocus.net/%E4%BD%BF%E7%94%A8ubuntu-26%E8%BF%9C%E7%A8%8B%E6%A1%8C%E9%9D%A2/)

著作权 © 2026 **[绿盟科技技术博客](https://blog.nsfocus.net/)**. 保留一切权利。 本站采用的布景主题为 [Mynote](https://terryl.in/).
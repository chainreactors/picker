---
title: wxbot
url: https://buaq.net/go-150998.html
source: unSafe.sh - 不安全
date: 2023-02-26
fetch_date: 2025-10-04T08:08:10.706157
---

# wxbot

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/706cfeb19bb5b53eb304a09b35bcf187.jpg)

wxbot

What's this?已对接框架已对接API已有插件指令大全How to use?本地运行Releases包Docker运行Actions编译
*2023-2-25 23:10:8
Author: [github.com(查看原文)](/jump-150998.htm)
阅读量:55
收藏*

---

* [What's this?](#whats-this)
  + [已对接框架](#%E5%B7%B2%E5%AF%B9%E6%8E%A5%E6%A1%86%E6%9E%B6)
  + [已对接API](#%E5%B7%B2%E5%AF%B9%E6%8E%A5api)
  + [已有插件](#%E5%B7%B2%E6%9C%89%E6%8F%92%E4%BB%B6)
  + [指令大全](#%E6%8C%87%E4%BB%A4%E5%A4%A7%E5%85%A8)
* [How to use?](#how-to-use)
  + [本地运行](#%E6%9C%AC%E5%9C%B0%E8%BF%90%E8%A1%8C)
  + [Releases包](#releases%E5%8C%85)
  + [Docker运行](#docker%E8%BF%90%E8%A1%8C)
  + [Actions编译](#actions%E7%BC%96%E8%AF%91)
* [How to develop?](#how-to-develop)
  + [制作插件或接入其他框架](#%E5%88%B6%E4%BD%9C%E6%8F%92%E4%BB%B6%E6%88%96%E6%8E%A5%E5%85%A5%E5%85%B6%E4%BB%96%E6%A1%86%E6%9E%B6)
  + [参考案例](#%E5%8F%82%E8%80%83%E6%A1%88%E4%BE%8B)
  + [调试-环境变量](#%E8%B0%83%E8%AF%95-%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F)
  + [提交Pr注意项](#%E6%8F%90%E4%BA%A4pr%E6%B3%A8%E6%84%8F%E9%A1%B9)
* [Feature](#feature)
* [Thanks](#thanks)
* [License](#license)

## What's this?

一个还算有意思的wechat robot项目，理想将其设计成一个多功能的机器人助手 😈

* 🤨框架可无侵入扩展，现已接入`千寻框架`和`vlw框架`，请参考`framework`目录
* 🤨功能可无侵入扩展，现已集成`plugins`目录下的功能，请参考`plugins`目录

**🔔 注意：**

1. 使用本项目之前需要您已经配置好相关的 `微信的hook` 类软件，那么只需要在这类软件上设置回调地址即可
2. 本项目已接入`vlw`、`千寻`两个框架，如果您有其他框架，可自行添加(参考`framework`目录，实现`IFramework`接口即可)，或联系我添加
3. 本项目不提供任何`hook`类软件，您需要利用搜索引擎自行寻找
4. 本项目暂时只支持HTTP协议，关于websocket协议支持目前不考虑
5. 简而言之，本项目是一个消息处理的中间件，微信消息监听获取是从框架获取
6. 本项目仅供学习交流使用，不得用于商业用途，否则后果自负
7. 使用本项目造成封禁账号等后果（项目立项到现在，作者还没出现过异常），本项目不承担任何责任，实际上您使用任何非官方的微信机器人都有可能造成账号封禁，所以请谨慎使用
8. 如果您阅读了上面的内容，觉得没有问题，那么请继续阅读下面的内容

**功能示例：**

[![img](https://github.com/y35uishere/wxbot/raw/hook/docs/screenshots.jpg)](https://github.com/y35uishere/wxbot/blob/hook/docs/screenshots.jpg)

### 已对接框架

🎁 已接入框架，展开看👇

### 已对接API

🎁 已对接API，展开看👇

```
// IFramework 这是接入框架所定义的接口
type IFramework interface {
	// Callback 这是消息回调方法，vx框架回调消息转发给该Server
	Callback(func(*Event, IFramework))

	// GetMemePictures 获取表情包图片地址(迷因图)
	// return: 图片链接(网络URL或图片base64)
	GetMemePictures(message *Message) string

	// SendText 发送文本消息
	// toWxId: 好友ID/群ID
	// text: 文本内容
	SendText(toWxId, text string) error

	// SendTextAndAt 发送文本消息并@，只有群聊有效
	// toGroupWxId: 群ID
	// toWxId: 好友ID/群ID/all
	// toWxName: 好友昵称/群昵称，留空为自动获取
	// text: 文本内容
	SendTextAndAt(toGroupWxId, toWxId, toWxName, text string) error

	// SendImage 发送图片消息
	// toWxId: 好友ID/群ID
	// path: 图片路径
	SendImage(toWxId, path string) error

	// SendShareLink 发送分享链接消息
	// toWxId: 好友ID/群ID
	// title: 标题
	// desc: 描述
	// imageUrl: 图片链接
	// jumpUrl: 跳转链接
	SendShareLink(toWxId, title, desc, imageUrl, jumpUrl string) error

	// SendFile 发送文件消息
	// toWxId: 好友ID/群ID/公众号ID
	// path: 本地文件绝对路径
	SendFile(toWxId, path string) error

	// SendVideo 发送视频消息
	// toWxId: 好友ID/群ID/公众号ID
	// path: 本地视频文件绝对路径
	SendVideo(toWxId, path string) error

	// SendEmoji 发送表情消息
	// toWxId: 好友ID/群ID/公众号ID
	// path: 本地动态表情文件绝对路径
	SendEmoji(toWxId, path string) error

	// SendMusic 发送音乐消息
	// toWxId: 好友ID/群ID/公众号ID
	// name: 音乐名称
	// author: 音乐作者
	// app: 音乐来源(VLW需留空)，酷狗/wx79f2c4418704b4f8，网易云/wx8dd6ecd81906fd84，QQ音乐/wx5aa333606550dfd5
	// jumpUrl: 音乐跳转链接
	// musicUrl: 网络歌曲直链
	// coverUrl: 封面图片链接
	SendMusic(toWxId, name, author, app, jumpUrl, musicUrl, coverUrl string) error

	// SendMiniProgram 发送小程序消息
	// toWxId: 好友ID/群ID/公众号ID
	// ghId: 小程序ID
	// title: 标题
	// content: 内容
	// imagePath: 图片路径, 本地图片路径或网络图片URL
	// jumpPath: 小程序点击跳转地址，例如：pages/index/index.html
	SendMiniProgram(toWxId, ghId, title, content, imagePath, jumpPath string) error

	// SendMessageRecord 发送消息记录
	// toWxId: 好友ID/群ID/公众号ID
	// title: 仅供电脑上显示用，手机上的话微信会根据[显示昵称]来自动生成 谁和谁的聊天记录
	// dataList:
	// 	- wxid: 发送此条消息的人的wxid
	// 	- nickName: 显示的昵称(可随意伪造)
	// 	- timestamp: 10位时间戳
	// 	- msg: 消息内容
	SendMessageRecord(toWxId, title string, dataList []map[string]interface{}) error

	// SendMessageRecordXML 发送消息记录(XML方式)
	// toWxId: 好友ID/群ID/公众号ID
	// xmlStr: 消息记录XML代码
	SendMessageRecordXML(toWxId, xmlStr string) error

	// SendFavorites 发送收藏消息
	// toWxId: 好友ID/群ID/公众号ID
	// favoritesId: 收藏夹ID
	SendFavorites(toWxId, favoritesId string) error

	// SendXML 发送XML消息
	// toWxId: 好友ID/群ID/公众号ID
	// xmlStr: XML代码
	SendXML(toWxId, xmlStr string) error

	// SendBusinessCard 发送名片消息
	// toWxId: 好友ID/群ID/公众号ID
	// targetWxId: 目标用户ID
	SendBusinessCard(toWxId, targetWxId string) error

	// AgreeFriendVerify 同意好友验证
	// v3: 验证V3
	// v4: 验证V4
	// scene: 验证场景
	AgreeFriendVerify(v3, v4, scene string) error

	// InviteIntoGroup 邀请好友加入群组
	// groupWxId: 群ID
	// wxId: 好友ID
	// typ: 邀请类型，1-直接拉，2-发送邀请链接
	InviteIntoGroup(groupWxId, wxId string, typ int) error

	// GetObjectInfo 获取对象信息
	// wxId: 好友ID/群ID/公众号ID
	// return: User, error
	GetObjectInfo(wxId string) (*User, error)

	// GetFriends 获取好友列表
	// isRefresh: 是否刷新 false-从缓存中获取，true-重新遍历二叉树并刷新缓存
	// return: []*User, error
	GetFriends(isRefresh bool) ([]*User, error)

	// GetGroups 获取群组列表
	// isRefresh: 是否刷新 false-从缓存中获取，true-重新遍历二叉树并刷新缓存
	// return: []*User, error
	GetGroups(isRefresh bool) ([]*User, error)

	// GetGroupMembers 获取群成员列表
	// groupWxId: 群ID
	// isRefresh: 是否刷新 false-从缓存中获取，true-重新遍历二叉树并刷新缓存
	// return: []*User, error
	GetGroupMembers(groupWxId string, isRefresh bool) ([]*User, error)

	// GetMPs 获取公众号订阅列表
	// isRefresh: 是否刷新 false-从缓存中获取，true-重新遍历二叉树并刷新缓存
	// return: []*User, error
	GetMPs(isRefresh bool) ([]*User, error)
}
```

### 已有插件

🎁 已有插件 👇

* [百度百科-点击查看使用说明](https://github.com/y35uishere/wxbot/blob/hook/plugins/baidubaike)
  + `import _ "github.com/yqchilde/wxbot/plugins/baidubaike"`
* [ChatGPT聊天-点击查看使用说明](https://github.com/y35uishere/wxbot/blob/hook/plugins/chatgpt)
  + `import _ "github.com/yqchilde/wxbot/plugins/chatgpt"`
* [KFC疯狂星期四骚话-点击查看使用说明](https://github.com/y35uishere/wxbot/blob/hook/plugins/crazykfc)
  + `import _ "github.com/yqchilde/wxbot/plugins/crazykfc"`
* [获取表情原图-点击查看使用说明](https://github.com/y35uishere/wxbot/blob/hook/plugins/memepicture)
  + `import _ "github.com/yqchilde/wxbot/plugins/memepicture"`
* [摸鱼办-点击查看使用说明](https://github.com/y35uishere/wxbot/blob/hook/plugins/moyuban)
  + `import _ "github.com/yqchilde/wxbot/plugins/moyuban"`
* [查拼音缩写-点击查看使用说明](https://github.com/y35uishere/wxbot/blob/hook/plugins/pinyinsuoxie)
  + `import _ "github.com/yqchilde/wxbot/plugins/pinyinsuoxie"`
* [获取美女图片-点击查看使用说明](https://github.com/y35uishere/wxbot/blob/hook/plugins/plmm)
  + `import _ "github.com/yqchilde/wxbot/plugins/plmm"`
* [查天气-点击查看使用说明](https://github.com/y35uishere/wxbot/blob/hook/plugins/weather)
  + `import _ "github.com/yqchilde/wxbot/plugins/weather"`
* [获取每日早报-点击查看使用说明](https://github.com/y35uishere/wxbot/blob/hook/plugins/zaobao)
  + `import _ "github.com/yqchilde/wxbot/plugins/zaobao"`
* [管理相关-点击查看使用说明](https://github.com/y35uishere/wxbot/blob/hook/plugins/manager)
  + `import _ "github.com/yqchilde/wxbot/plugins/manager"`
* [公众号监控转发-点击查看使用说明](https://github.com/y35uishere/wxbot/blob/hook/plugins/ghmonitor)
  + `import _ "github.com/yqchilde/wxbot/plugins/ghmonitor"`
* [聊天热词云-点击查看使用说明](https://github.com/y35uishere/wxbot/blob/hook/plugins/ghmonitor)
  + `import _ "github.com/yqchilde/wxbot/plugins/wordcloud"`
* [查ID-点击查看使用说明](https://github.com/y35uishere/wxbot/blob/hook/plugins/chaid)
  + `import _ "github.com/yqchilde/wxbot/plugins/chaid"`
* [有道翻译-点击查看使用说明](https://github.com/y35uishere/wxbot/blob/hook/plugins/youdaofanyi)
  + `import _ "github.com/yqchilde/wxbot/plugins/youdaofanyi"`
* [coser-点击查看使用说明](https://github.com/y35uishere/wxbot/blob/hook/plugins/coser)
  + `import _ "github.com/yqchilde/wxbot/plugins/coser"`

### 指令大全

[点击查看机器人有哪些指令](https://github.com/y35uishere/wxbot/blob/hook/docs/command.md)

...
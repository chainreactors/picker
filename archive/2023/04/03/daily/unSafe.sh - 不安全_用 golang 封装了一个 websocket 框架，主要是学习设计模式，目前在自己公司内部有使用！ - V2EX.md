---
title: 用 golang 封装了一个 websocket 框架，主要是学习设计模式，目前在自己公司内部有使用！ - V2EX
url: https://buaq.net/go-156577.html
source: unSafe.sh - 不安全
date: 2023-04-03
fetch_date: 2025-10-04T11:29:37.692702
---

# 用 golang 封装了一个 websocket 框架，主要是学习设计模式，目前在自己公司内部有使用！ - V2EX

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

![]()

用 golang 封装了一个 websocket 框架，主要是学习设计模式，目前在自己公司内部有使用！ - V2EX

代码地址： https://github.com/Xuzan9396/zinx-ws目标?维护 golang 版 websocket 版本, 打算跟 zinx tcp 版本同步，然后无偿开源为
*2023-4-2 21:6:50
Author: [v2ex.com(查看原文)](/jump-156577.htm)
阅读量:53
收藏*

---

代码地址： <https://github.com/Xuzan9396/zinx-ws>

#### 目标?

##### 维护 golang 版 websocket 版本, 打算跟 zinx tcp 版本同步，然后无偿开源

#### 为什么做这个项目？

`做这个项目初衷，主要因为自己公司做直播平台的，之前公司写了一套，websocket 封装的框架，主要做房间服务器,和 h5 小游戏服务器，但是由于感觉随着业务增大，后面感觉某些设计有缺陷，看了冰哥的设计模式， 打算跟着冰哥设计模式重写一个 websocket`

#### 打算项目使用？

```
后续会在自己的项目中使用，打算在直播间的小游戏，准备上线使用
```

#### 具体怎么使用

##### 参数说明

```
  "Name": "zin-ws -------gitxuzan",
  "Host": "127.0.0.1",
  "端口": "端口",
  "TcpPort": 8999,
  "最大连接数": "最大连接数",
  "MaxConn": 1000,
  "最大的包大小": "最大包大小",
  "MaxPackageSize": 4096,
  "worker 池子": "worker 池子 10 个并发处理读的数据",
  "WorkerPoolSize": 10
```

##### 数据发送格式简单说明(后续修改成格式定义)

| MsgId | len | body |
| --- | --- | --- |
| 协议号 ID | body 长度 | 二进制 body 长度 |
| uint32 | uint32 | []byte |

##### 服务端配置设置

```
wsconfig.SetWSConfig("127.0.0.1", 8999, wsconfig.WithName("gitxuzan ----- websocket"))
还有其他设置例如:
wsconfig.WithWorkerSize(10) // 设置 10 个 worker 处理业务逻辑
wsconfig.WithMaxPackSize(4096)  // 每个发送的包大小 4k
wsconfig.WithMaxConn(1000)	// 同时在线 1000 个连接
wsconfig.WithVersion()	        // 自定义本地版本
```

##### 定义业务逻辑协议

```
type LoginInfo struct {
	znet.BaseRouter
}

例如上面写的 LoginInfo 继承 znet.BaseRouter
重写三个方法依次执行:
PreHandle
Handle
PostHandle
```

##### 设置 router 映射到具体的方法上

```
同时要设置 router
	// 登录
s.AddRouter(1001, &LoginInfo{})
1001 代表协议号，相当于协议投里面的 msgId,映射到具体某个业务，发送端需要发送对应的协议号
```

##### request 的一些功能，例如下面的案例，模拟登入验证等等

```
func (l *LoginInfo) PreHandle(request ziface.IRequest) {
request 中 目前有发送，断开，获取当前属性，获取当前连接
}
```

##### 完整的服务端使用代码

```
package main

import (
	wsconfig "github.com/Xuzan9396/ws/config"
	"github.com/Xuzan9396/ws/ziface"
	"github.com/Xuzan9396/ws/znet"
	"log"
	"time"
)

func init() {
	log.SetFlags(log.Lshortfile | log.LstdFlags)
}

type LoginInfo struct {
	znet.BaseRouter
}

// 模拟登录逻辑
func (l *LoginInfo) PreHandle(request ziface.IRequest) {
	auth := false
	<-time.After(5 * time.Second) // 模拟业务
	if auth == false {
		// 模拟登录认证失败，然后断开连接
		request.GetConnetion().Stop()
	}
}

type PingInfo struct {
	znet.BaseRouter
}
type HelloInfo struct {
	znet.BaseRouter
}

func (p *PingInfo) PreHandle(request ziface.IRequest) {
	log.Printf("pre:%s,conntId:%d,msgId:%d", request.GetData(), request.GetConnetion().GetConnID(), request.GetMsgID())
}

func (p *PingInfo) Handle(request ziface.IRequest) {
	log.Printf("Handle:%s,conntId:%d,msgId:%d", request.GetData(), request.GetConnetion().GetConnID(), request.GetMsgID())

}

func (p *PingInfo) PostHandle(request ziface.IRequest) {
	log.Printf("post:%s,conntId:%d,,msgId:%d", request.GetData(), request.GetConnetion().GetConnID(), request.GetMsgID())
	request.GetConnetion().SendMsg(request.GetMsgID(), []byte("回复 ping!"))
}
func (p *HelloInfo) PreHandle(request ziface.IRequest) {
	log.Printf("pre:%s,conntId:%d,msgId:%d", request.GetData(), request.GetConnetion().GetConnID(), request.GetMsgID())
}

func (p *HelloInfo) Handle(request ziface.IRequest) {
	log.Printf("Handle:%s,conntId:%d,msgId:%d", request.GetData(), request.GetConnetion().GetConnID(), request.GetMsgID())

}

func (p *HelloInfo) PostHandle(request ziface.IRequest) {
	log.Printf("post:%s,conntId:%d,,msgId:%d", request.GetData(), request.GetConnetion().GetConnID(), request.GetMsgID())
	request.GetConnetion().SendMsg(request.GetMsgID(), []byte("回复 hello!"))

}

// 创建链接后初始化函数
func SetOnConnetStart(conn ziface.IConnection) {
	conn.SetProperty("name", "xuzan")
	res, bools := conn.GetProperty("name")
	if bools {
		log.Println("name", res.(string))
	}
	conn.RemoveProperty("name")
}

func GetConnectNum(s ziface.IServer) {
	go func() {
		ticker := time.NewTicker(5 * time.Second)
		defer ticker.Stop()
		for {
			select {
			case <-ticker.C:
				connNumTotal := s.GetConnMgr().Len()
				log.Println("连接数量:", connNumTotal)
			}
		}
	}()
}

func main() {
	//设置配置
	wsconfig.SetWSConfig("127.0.0.1", 8999, wsconfig.WithName("gitxuzan ----- websocket"))
	// 创建一个 server 句柄
	s := znet.NewServer()
	// 启动 sever
	s.SetOnConnStart(SetOnConnetStart)
	// 测试业务
	s.AddRouter(1, &HelloInfo{})
	// 其他业务
	s.AddRouter(2, &PingInfo{})
	// 登录
	s.AddRouter(1001, &LoginInfo{})

	// 监控长连接数量
	GetConnectNum(s)
	s.Server()
}
```

##### 完整的客户端案例代码

```
package main

import (
	"flag"
	"github.com/Xuzan9396/ws/znet"
	"github.com/gorilla/websocket"
	"log"
	"net/http"
	"net/url"
	"os"
	"os/signal"
	"time"
)

var addr = flag.String("addr", "127.0.0.1:8999", "http service address")

func main() {
	flag.Parse()
	log.SetFlags(0)

	interrupt := make(chan os.Signal, 1)
	signal.Notify(interrupt, os.Interrupt)

	u := url.URL{Scheme: "ws", Host: *addr, Path: "/"}
	log.Printf("connecting to %s", u.String())
	c, _, err := websocket.DefaultDialer.Dial(u.String(), http.Header{"User-Agent": {""}})
	if err != nil {
		log.Fatal("dial:", err)
	}
	defer c.Close()

	log.Println("ws 连接成功")
	ticker := time.NewTicker(3 * time.Second)
	defer ticker.Stop()

	p := znet.NewDataPack()
	by := []byte{'h', 'e', 'l', 'l', 'o'}
	resBytes, err := p.Pack(&znet.Message{
		Id:      1,
		DataLen: uint32(len(by)),
		Data:    by,
	})

	byPing := []byte("ping")
	resPingBytes, _ := p.Pack(&znet.Message{
		Id:      2,
		DataLen: uint32(len(byPing)),
		Data:    byPing,
	})
	timer := time.NewTimer(30 * time.Second)

	go read(c)
	for {
		select {
		case <-timer.C:
			// 模拟认证登录
			sendMsg := []byte("login")
			sendMsgPack, _ := p.Pack(&znet.Message{
				Id:      1001,
				DataLen: uint32(len(sendMsg)),
				Data:    sendMsg,
			})
			err := c.WriteMessage(websocket.BinaryMessage, sendMsgPack)
			if err != nil {
				log.Println("write:", err)
				timer.Stop()
				return
			}
			log.Println("login 写入成功:", string(sendMsg))
			timer.Stop()
		case <-ticker.C:
			sendMsg := resBytes
			err := c.WriteMessage(websocket.BinaryMessage, sendMsg)
			if err != nil {
				log.Println("write:", err)
				return
			}
			log.Println("写入成功:", string(by))

			err = c.WriteMessage(websocket.BinaryMessage, resPingBytes)
			if err != nil {
				log.Println("write:", err)
				return
			}

			log.Println("写入成功:", string(resPingBytes))
		case <-interrupt:
			log.Println("interrupt")
			err := c.WriteMessage(websocket.CloseMessage, websocket.FormatCloseMessage(websocket.CloseNormalClosure, ""))
			if err != nil {
				log.Println("write close:", err)
				return
			}

		}
	}

}

func read(c *websocket.Conn) {
	for {
		_, message, err := c.ReadMessage()
		if err != nil {
			log.Println("read:", err)
			return
		}
		p := znet.NewDataPack()
		img, err := p.Unpack(message)
		if err != nil {
			log.Println("read:", err)
			return
		}
		log.Printf("msgId:%d,recv: %s", img.GetMsgId(), img.GetData())
	}
}
```

###### 参考链接

<https://github.com/aceld/zinx> 来自冰哥

文章来源: https://v2ex.com/t/929092#reply9
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
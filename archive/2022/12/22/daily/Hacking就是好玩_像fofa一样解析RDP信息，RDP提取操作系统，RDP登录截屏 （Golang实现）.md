---
title: 像fofa一样解析RDP信息，RDP提取操作系统，RDP登录截屏 （Golang实现）
url: https://mp.weixin.qq.com/s?__biz=MzU2NzcwNTY3Mg==&mid=2247484625&idx=1&sn=ce265b78bf8b08b8d618958140c51c42&chksm=fc986df6cbefe4e094a1c20d53621cd2a83e01656c3459bfbd856eac5bd59c85921742b33ea0&scene=58&subscene=0#rd
source: Hacking就是好玩
date: 2022-12-22
fetch_date: 2025-10-04T02:14:14.474659
---

# 像fofa一样解析RDP信息，RDP提取操作系统，RDP登录截屏 （Golang实现）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/eLgL5R4W3FhIIcdU538E59RDMJNfTzicW19MplHpKBZaQ9YY6ib2KvLO2YiaTpyScEUbtNOMQ0xyBXL88yAWJkibJw/0?wx_fmt=jpeg)

# 像fofa一样解析RDP信息，RDP提取操作系统，RDP登录截屏 （Golang实现）

原创

w8ay

Hacking就是好玩

从fofa中搜索RDP，会看到它会解析出RDP的信息。

![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3FhIIcdU538E59RDMJNfTzicWL4u1WOhm5BicS63wMRUhwWh7YZaD772jllwYBRFj290v6SB2fJvIiaOw/640?wx_fmt=png)

本文探索如何自己实现一个。

## 1. Nmap指纹

在https://raw.githubusercontent.com/nmap/nmap/master/nmap-service-probes 可以找到关于RDP发包的定义

```
##############################NEXT PROBE##############################
# This is an RDP connection request with the MSTS cookie set. Some RDP
# listeners (with NLA?) only respond to this one.
# This must be sent before TLSSessionReq because Windows RDP will handshake TLS
# immediately and we don't have a way of identifying RDP at that point.
Probe TCP TerminalServerCookie q|\x03\0\0*%\xe0\0\0\0\0\0Cookie: mstshash=nmap\r\n\x01\0\x08\0\x03\0\0\0|
rarity 7
ports 3388,3389
fallback TerminalServer

Probe TCP TerminalServer q|\x03\0\0\x0b\x06\xe0\0\0\0\0\0|
rarity 6
ports 515,1028,1068,1503,1720,1935,2040,3388,3389

# Windows 2000 Server
# Windows 2000 Advanced Server
# Windows XP Professional
match ms-wbt-server m|^\x03\0\0\x0b\x06\xd0\0\0\x12.\0$|s p/Microsoft Terminal Service/ o/Windows/ cpe:/o:microsoft:windows/a
match ms-wbt-server m|^\x03\0\0\x17\x08\x02\0\0Z~\0\x0b\x05\x05@\x06\0\x08\x91J\0\x02X$| p/Microsoft Terminal Service/ i/Used with Netmeeting, Remote Desktop, Remote Assistance/ o/Windows/ cpe:/o:microsoft:windows/a
match ms-wbt-server m|^\x03\0\0\x11\x08\x02..}\x08\x03\0\0\xdf\x14\x01\x01$|s p/Microsoft NetMeeting Remote Desktop Service/ o/Windows/ cpe:/a:microsoft:netmeeting/ cpe:/o:microsoft:windows/a
match ms-wbt-server m|^\x03\0\0\x0b\x06\xd0\0\0\x03.\0$|s p/Microsoft NetMeeting Remote Desktop Service/ o/Windows/ cpe:/a:microsoft:netmeeting/ cpe:/o:microsoft:windows/a

# Need more samples!
match ms-wbt-server m|^\x03\0\0\x0b\x06\xd0\0\0\0\0\0| p/xrdp/ cpe:/a:jay_sorg:xrdp/
match ms-wbt-server m|^\x03\0\0\x0e\t\xd0\0\0\0[\x02\xa1]\0\xc0\x01\n$| p/IBM Sametime Meeting Services/ o/Windows/ cpe:/a:ibm:sametime/ cpe:/o:microsoft:windows/a

match ms-wbt-server m|^\x03\0\0\x0b\x06\xd0\0\x004\x12\0| p/VirtualBox VM Remote Desktop Service/ o/Windows/ cpe:/a:oracle:vm_virtualbox/ cpe:/o:microsoft:windows/a

match ms-wbt-server-proxy m|^nmproxy: Procotol byte is not 8\n$| p/nmproxy NetMeeting proxy/
```

它在tcp连接上之后会发包 `\x03\0\0*%\xe0\0\0\0\0\0Cookie: mstshash=nmap\r\n\x01\0\x08\0\x03\0\0\0`，nmap关于rdp的版本指纹比较少，而且发的包还有特征。

nmap有一个`rdp.lua`，封装了rdp连接的前几层协议，后面深入学习协议时可以对照着看。

## 2. 深入协议

官方文档：https://learn.microsoft.com/en-us/openspecs/windows\_protocols/ms-rdpbcgr/023f1e69-cfe8-4ee6-9ee0-7e759fb4e4ee  有协议的交互流程图

![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3FhIIcdU538E59RDMJNfTzicWQkNibIgaOzfskGQnUzxaibicttwwvWMX2dqFACfRlQNEDYHehlY1uak1g/640?wx_fmt=png)

### 2.1. 发包

看了文档后，发现连接顺序分为十个不同的阶段，但是获得一些基础信息，只用看第一阶段`Connection Initiation`就行了。

> Connection Initiation：客户端通过向服务器发送  X.224 连接请求 PDU（第2.2.1.1节）来启动连接。服务器响应 0 类 X.224 连接确认 PDU（第2.2.1.2节）。
>
> 从这一点开始，客户端和服务器之间发送的所有后续数据都包装在 X.224 数据协议数据单元 (PDU) (1) 中。

请求结构

![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3FhIIcdU538E59RDMJNfTzicWMib89flFSyrQB2dUxQicp1w6baCFvg6ica8SPc9y71oLgpUyMkW0nKdmA/640?wx_fmt=png)

结构体如下：

「tpktHeader（4 字节）：」 TPKT 标头，如[T123]第 8 节中所指定。

![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3FhIIcdU538E59RDMJNfTzicWjDEDhpzVG9MrP8icqhD68IO8L6HKOGVsyBicibp2stbVsw3CQv3Sfq32w/640?wx_fmt=png)

nmap中的定义

```
__tostring = function(self)
  return string.pack(">BBI2",
    self.version,  //  一般是3
    self.reserved or 0, // 一般是0
    (self.data and #self.data + 4 or 4)) // 整个结构体的大小，包括后面的数据
  ..self.data  // 后面的数据
```

「x224Crq（7 字节）：」 一个 X.224 类 0 连接请求传输协议数据单元 (TPDU)，如[X224] 第 13.3 节中所指定。

![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3FhIIcdU538E59RDMJNfTzicW7AGJBJkflAGrfy27OZiao0bhSoiaMXjfktlhw3iakIibIibEGx7PNibES8SA/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3FhIIcdU538E59RDMJNfTzicWMzSqCNumlK8SbicPB7UrYEcBSkictBIIsNQbxILEH2UU9UygiaJ9sexAg/640?wx_fmt=png)

* 第一个是后面结构体长度，第二个是hex(int('11100000',2)),即0xe0 ,后面5个字节都是0，这个数据结构即length+0xe0,0x0,0x0,0x0,0x0,0x0

「routingToken（可变）：一个可选的可变长度路由令牌（用于负载平衡），由 0x0D0A 两字节序列终止。有关路由令牌格式的详细信息，请参阅」「[MSFT-SDLBTS]」\*\* “路由令牌格式”。路由令牌和 CR+LF 序列的长度包含在「X.224 连接请求长度指示符 字段中。如果此字段存在，则」cookie\*\*字段不得存在。

「cookie（变量）：可选且长度可变的」「ANSI」\*\* 字符串，以 0x0D0A 两字节序列结尾。此文本字符串必须是“Cookie：mstshash=IDENTIFIER”，其中 IDENTIFIER 是一个 ANSI 字符串（示例 cookie 字符串显示在第\*\*「4.1.1」「节中）。整个 cookie 字符串和 CR+LF 序列的长度包含在」X.224 连接请求长度指示符字段中。如果「routingToken」字段存在，则该字段不得存在。

「rdpNegReq（8 字节）：一个可选的」RDP 协商请求（第2.2.1.1.1节）结构。该字段的长度包含在「X.224 连接请求长度指示符」字段中。

![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3FhIIcdU538E59RDMJNfTzicWSyZvFefBV1JicygEr3icFHLRkqLEePKS8JXFq3B994Q1QCGxKBlLHflg/640?wx_fmt=png)

* 文档描述很详细了，这个结构体很重要，用于设置请求协议

![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3FhIIcdU538E59RDMJNfTzicWb3G5YPuA6wXLQktnC2TPvpMPpG4baeLcBhicTuJERbeplfIF9uqPrbQ/640?wx_fmt=png)

「rdpCorrelationInfo（36 字节）：一个可选的」关联信息（第2.2.1.1.2节）结构。该字段的长度包含在「X.224 连接请求长度指示符」字段中。如果在RDP 协商请求结构的「标志」字段中设置了 CORRELATION\_INFO\_PRESENT (0x08) 标志，则该字段必须存在，封装在可选的「rdpNegReq」 字段中。如果未设置 CORRELATION\_INFO\_PRESENT (0x08) 标志，则该字段不得存在。

* 这个结构体没啥用，不用写

用golang实现这个结构体

```
type RdpReq struct {
  requestedProtocols uint32
  cookie             []byte
}

func NewReq(protocol uint32, cookie []byte) *RdpReq {
  return &RdpReq{requestedProtocols: protocol, cookie: cookie}
}
func (r *RdpReq) Serialize() []byte {
  buff := &bytes.Buffer{}
  // cookie
  if r.cookie != nil {
    cookie := []byte(fmt.Sprintf("Cookie: mstshash=%s\r\n", r.cookie))
    buff.Write(cookie)
  }
  // rdpNegReq
  buff.Write([]byte{0x1, 0x0, 0x8, 0x0})
  requestedProtocolData := make([]byte, 4)
  binary.LittleEndian.PutUint32(requestedProtocolData, r.requestedProtocols)
  buff.Write(requestedProtocolData)

  buff2 := &bytes.Buffer{}
  // x224Crq (7 字节)
  buff2.Write([]byte{
    uint8(buff.Len() + 6),
    0xe0,
    0x00, 0x00,
    0x00, 0x00, 0x00,
  })
  buff2.Write(buff.Bytes())

  // tpktHeader（4 字节）
  buff3 := &bytes.Buffer{}
  buff3.Write([]byte{3, 0})
  lengthData := make([]byte, 2)
  binary.BigEndian.PutUint16(lengthData, uint16(buff2.Len()+4))
  buff3.Write(lengthData)
  buff3.Write(buff2.Bytes())
  return buff3.Bytes()
}
```

测试

```
func main() {
  rdp := NewReq(PROTOCOL_RDP|PROTOCOL_SSL|PROTOCOL_HYBRID, []byte("w8ay"))
  buff := rdp.Serialize()
  fmt.Println(hex.Dump(buff))
}
```

输出

![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3FhIIcdU538E59RDMJNfTzicWj7almMGlT7wdWaYUUVloiasK8O4YS5HGBSPUZMntAZjsv2tTanSKCKA/640?wx_fmt=png)

和nmap的probe`\x03\0\0*%\xe0\0\0\0\0\0Cookie: mstshash=nmap\r\n\x01\0\x08\0\x03\0\0\0`也能对应上

### 2.2. 收包

在发包完毕后，会收到如下结构体

![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3FhIIcdU538E59RDMJNfTzicW3miclgDoDao82KFXsqsOQGqMSb2xdnibgP5QjNPeV4fIiagjNLlLBFu1g/640?wx_fmt=png)

前面的结构可以跳过，直接看`rdpNegData`结构

文档：https://learn.microsoft.com/en-us/openspecs/windows\_protocols/ms-rdpbcgr/b2975bdc-6d56-49ee-9c57-f2ff3a0b6817

成功的话，它会返回一个服务器指定的通信协议。

![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3FhIIcdU538E59RDMJNfTzicW0FeVKaf98m0dw0vGPl869j7IyEZDU88bpWvibWxB95LXbXlJvuBBdcA/640?wx_fmt=png)

根据结构用golang写个解析程序

```
type RdpResp struct {
  data   []byte
  Type   int
  Flags  int
  Result uint32
}

func ParseRdpResp(data []byte) (*RdpResp, error) {
  GenericRDPSignature := []byte{
    0x03, 0x00, 0x00, 0x13, 0x0e, 0xd0, 0x00, 0x00, 0x12, 0x34, 0x00,
  }
  if !checkSignature(data[:11], GenericRDPSignature) {
    return nil, errors.New("not rdp response")
  }
  reader := bytes.NewReader(data)
  reader.Seek(11, io.SeekStart)
  r := new(RdpResp)
  r.data = data
  _type, err := reader.ReadByte()
  if err != nil {
    return r, err
  }
  r.Type = int(_type)
  _flag, err := reader.ReadByte()
  if err != nil {
    return r, err
  }
  r.Flags = int(_flag)
  reader.Seek(2, io.SeekCurrent)
  result := make([]byte, 4)
  _, err = reader.Read(result)
  if err != nil {
    return r, err
  }
  r.Result = binary.L...
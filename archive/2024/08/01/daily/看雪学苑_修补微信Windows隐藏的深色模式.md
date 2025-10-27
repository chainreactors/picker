---
title: 修补微信Windows隐藏的深色模式
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458565420&idx=1&sn=c479eb0abdac2be9033e0dcfc79155d4&chksm=b18d8ba686fa02b0cbaa765b5b7c4c1e8cd79a3caae8cc20882dc532d3fe42052042f511b3a0&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-08-01
fetch_date: 2025-10-06T18:05:18.309901
---

# 修补微信Windows隐藏的深色模式

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8G2nMPJ7zumttib3WJQoNLMyPg3zFtsDO6S3aGbK8yibaeibfjOyftuO2jQx5TT6X4uLkusOYNNCpDqg/0?wx_fmt=jpeg)

# 修补微信Windows隐藏的深色模式

GhHei

看雪学苑

##

```
一

用逆向做点正向
```

MacOS版本的微信在2021年已经支持深色模式：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8G2nMPJ7zumttib3WJQoNLMyiccZThwrXeFaX1UZ7RIbUqWGs9h7g5dLpYV8R7r9aGpGia1x6jia4Zyqw/640?wx_fmt=jpeg&from=appmsg)

Windows版本的微信到2024年还没有深色模式，看到下面链接说到：眼睛畏光的低视力人一直在反馈。

期盼尽快更新Windows版本（PC版本）微信深色模式（暗色、黑暗、暗夜、黑夜模式*（https://developers.weixin.qq.com/community/develop/article/doc/00082aeaf0ca4009b620ec37e6b813）*

试着用逆向去实现Windows版本的微信也支持深色模式，发现微信其实隐藏了深色模式，可惜不完善，修补之后效果如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8G2nMPJ7zumttib3WJQoNLMyHjpKg3IY6tI1yFZtQ870D2E3W7IpvF1bTIqM7LPLdbC9ibdfjnqpOUw/640?wx_fmt=jpeg&from=appmsg)

---

#

##

```
二

隐藏的深色模式
```

先试着用IDA搜素深色模式的关键词dark，发现确实有深色模式：'weui\theme\dark\theme.xml'

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8G2nMPJ7zumttib3WJQoNLMyFYZ82LmY04rpSkphbSjNtf5aoFLnFhcEYvG0iaJOFGuQg7lEfNVpYXA/640?wx_fmt=jpeg&from=appmsg)

交叉索引一下引用字符串的地方：

```
int sub_1F35D30()
    sub_1F33C40(dword_32C5500, L"weui\\theme\\dark\\theme.xml");
    sub_1F33C40(dword_32C54F4, L"Theme\\dark\\theme_dark.xml");
```

再看下sub\_1F35D30调用的地方，dword\_32C5500便是深色模式的资源路径：

```
int sub_1F35D00()
    if ( !dword_32C5500 ) sub_1F35D30();
    return dword_32C5500;
```

再看下sub\_1F35D00调用的地方，可以看出byte\_32B5474控制是否用深色模式：

```
int __thiscall sub_1EF62E0(_DWORD *this)
    if ( byte_32B5474 ) sub_1F35D00();
    else sub_1F35CF0();
```

交叉索引byte\_32B5474，有两个地方写入byte\_32B5474：

```
01EBC2ED 8A47 61			mov al, [edi+61h]
01EBC2F2 A2 74542B03        mov byte_32B5474, al

01EBCCE3 C605 74542B03 00	mov byte_32B5474, 0
```

在X86dbg上修改一下汇编：

```
7A47C2ED | B0 01                | mov al,1                                 |
7A47C2EF | 90                   | nop                                      |

7A47CCE3 | C605 7454877B 01     | mov byte ptr ds:[7B875474],1
```

修改之后还是浅色模式，但个人名片从白色是黑色，说明深色模式有效且不完善。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8G2nMPJ7zumttib3WJQoNLMyXwsibCjRmN74IDmxRITOJ9lYPk4JQeb9RlkTg25FVKzbMseZcoibNorQ/640?wx_fmt=jpeg&from=appmsg)

---

#

##

```
三

深色模式的原理
```

为了了解为什么深色模式不完善，需要梳理一下深色模式的底层原理。

1、微信里面有两个主题模式：

```
浅色：theme\default\theme.xml

深色：theme\dark\theme.xml
```

2、不同主题模式的颜色配置文件不同：

```
浅色：theme\default\theme.xml
<!-- color -->
<IncludeTheme source="weui/Theme/default/colors.xml" />

深色：theme\dark\theme.xml
<!-- color -->
<IncludeTheme source="weui/Theme/dark/colors.xml" />
```

3、同id不同主题模式下，具体值不同：

```
浅色：theme\default\theme.xml
<!-- color -->
<IncludeTheme source="weui/Theme/default/colors.xml" />
<!-- 文字颜色 -->
<Color id="Text_1" opacity="1" color="#161616" /> // 浅色模式的文字比较深

深色：theme\dark\theme.xml
<!-- color -->
<IncludeTheme source="weui/Theme/dark/colors.xml" />
<!-- 文字颜色 -->
<Color id="Text_1" opacity="1" color="#F7F7F7" /> // 深色模式的文字比较浅
```

4、界面的属性值改为从固定值变成变量值：

```
textcolor="#FF000000"
改成
textcolor="@color:Text_1"
```

可以看出微信的底层已经有一套更换模式的基建，而深色模式之所以不完善是因为深色资源文件不完整。

```
theme\default\colors.xml    5150 字节
theme\dark\colors.xml       4370 字节
```

---

#

##

```
四

修改界面的资源
```

如果要完善深色模式，就需要修改界面资源，先了解一下原生Duilib生成界面的流程。

1、界面生成从OnCreate开始：

```
LRESULT WindowImplBase::OnCreate(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL& bHandled)
    switch (GetResourceType())
    case UILIB_ZIP:
        m_pm.SetResourceZip(GetZIPFileName().GetData(), true);

    CControlUI* pRoot = builder.Create(xml, _T("xml"), this, &m_pm);
```

2、builder.Create加载界面资源：

```
CControlUI* CDialogBuilder::Create(STRINGorID xml, LPCTSTR type, IDialogBuilderCallback* pCallback, CPaintManagerUI* pManager, CControlUI* pParent)
    if( !m_xml.Load(xml.m_lpstr) ) return NULL;
    if( !m_xml.LoadFromFile(xml.m_lpstr) ) return NULL;
    if( !m_xml.LoadFromMem((BYTE*)::LockResource(hGlobal), ::SizeofResource(dll_instence, hResource) )) return NULL;
    return Create(pCallback, pManager, pParent);

bool CMarkup::LoadFromMem(BYTE* pByte, DWORD dwSize, int encoding)
    DWORD nWide = ::MultiByteToWideChar( CP_UTF8, 0, (LPCSTR)pByte, dwSize, NULL, 0 );
    ::MultiByteToWideChar( CP_UTF8, 0, (LPCSTR)pByte, dwSize, m_pstrXML, nWide );
```

3、最后是解析界面资源的内容：

```
CControlUI* CDialogBuilder::Create(IDialogBuilderCallback* pCallback, CPaintManagerUI* pManager, CControlUI* pParent)
    CMarkupNode root = m_xml.GetRoot();
    for( CMarkupNode node = root.GetChild() ; node.IsValid(); node = node.GetSibling() )
        "linkhoverfontcolor"
```

根据这个流程，就可以定位微信Duilib对应的函数：

1、搜索关键词"linkhoverfontcolor"

```
int __thiscall sub_1EDDBE0(_DWORD *this, int pCallback, int pManager, int pParent)
    "linkhoverfontcolor"
```

2、再查看sub\_1EDDBE0的引用

```
int __thiscall sub_1EDDB80(_DWORD *this, wchar_t *Source, int a3, int a4, int a5, int a6)
    wcXMLData = sub_1F20210(wcXMLPath, 1);
    if ( wcXMLData && sub_1EE0BE0(this, *(wcXMLData + 0x2000), *(wcXMLData + 0x2004), v8) )
        return sub_1EDDBE0(this, a4, a5, a6);
```

3、sub\_1F20210就是CMarkup::LoadFromMem

把界面资源的路径（wcXMLPath）变成界面资源的内容（wcXMLData ）：

```
char __thiscall sub_1EE0BE0(WCHAR **this, LPCCH lpMultiByteStr, unsigned int cbMultiByte, int a4)
    v6 = MultiByteToWideChar(65001u, 0, v5, v4, 0, 0);// CP_UTF8
    MultiByteToWideChar(65001u, 0, v5, cbMultiByte, v7, v6);
```

用Frida的js脚本拦截修改（需要修改很多地方），就可以实现深色模式：

```
const targetFunctionAddress = WeChatWin.add(0x1F20210);
Interceptor.attach(targetFunctionAddress,
...
ModifyAttribute(this.wsXMLDataArray, '', 'bkcolor', '#FF000000');
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8G2nMPJ7zumttib3WJQoNLMyHjpKg3IY6tI1yFZtQ870D2E3W7IpvF1bTIqM7LPLdbC9ibdfjnqpOUw/640?wx_fmt=jpeg&from=appmsg)

---

#

##

```
五

修改业务的代码
```

修改资源的属性，发现了一个问题：编辑框的文字属性修改无效。原本是是白色背景加黑色字体，现在是黑色背景加黑色字体，看不清。这就意味着：控件的属性，不是完全依赖界面资源，还需要修改业务代码。

1、修改字体颜色的接口是SetAttribute：

```
void CRichEditUI::SetAttribute(LPCTSTR pstrName, LPCTSTR pstrValue)
    if( _tcscmp(pstrName, _T("textcolor")) == 0 )
        if( *pstrValue == _T('#')) pstrValue = ::CharNext(pstrValue);
        DWORD clrColor = _tcstoul(pstrValue, &pstr, 16);
        SetTextColor(clrColor);

void CRichEditUI::SetTextColor(DWORD dwTextColor)
    m_pTwh->SetColor(dwTextColor);

void CTxtWinHost::SetColor(DWORD dwColor)
    cf.crTextColor = RGB(GetBValue(dwColor), GetGValue(dwColor), GetRValue(dwColor));
    pserv->OnTxPropertyBitsChange(TXTBIT_CHARFORMATCHANGE, TXTBIT_CHARFORMATCHANGE);
```

注入DLL调用SetAttribute确实能改变字体颜色，但再编辑编辑框RichEdit的文本，颜色又变成黑色。

```
DWORD pControl = 0x15a72bb8;
const wchar_t* wcAttr = L"textcolor";
const wchar_t* wcValue = L"#FFFFFFFF"; // 白色
SetAttribute(pControl, wcAttr, wcValue);
```

2、修改字体颜色的另一接口是SetSelectionCharFormat：

```
#define WM_USER                 0x0400
#define EM_GETCHARFORMAT		(WM_USER + 58)  // 0x43A
#define EM_SETCHARFORMAT		(WM_USER + 68)  // 0x444
#define SCF_SELECTION			0x0001

DWORD CRichEditUI::GetSelectionCharFormat(CHARFORMAT2 &cf) const
    cf.cbSize = sizeof(CHARFORMAT2);
    TxSendMessage(EM_GETCHARFORMAT, SCF_SELECTION, (LPARAM)&cf, &lResult);

bool CRichEditUI::SetSelectionCharFormat(CHARFORMAT2 &cf)
    cf.cbSize = sizeof(CHARFORMAT2);
    TxSendMessage(EM_SETCHARFORMAT, SCF_SELECTION, (LPARAM)&cf, &lResult);

HRESULT CRichEditUI::TxSendMessage(UINT msg, WPARAM wparam, LPARAM lparam, LRESULT *plresult) const
    return m_pTwh->GetTextServices()->TxSendMessage(msg, wparam, lparam, plresult);
```

X86dbg对TxSendMessage下条件断点并打印参数：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8G2nMPJ7zumttib3WJQoNLMyDe78CKul1bWQk9cnUkNtWXCtj8VVK0VsqvoefVFtlZk3GA14ibTW47A/640?wx_fmt=jpeg&from=appmsg)

发现编辑文本的时候调用了GetSelectionCharFormat：

```
#define EM_GETCHARFORMAT (WM_USER + 58)  // 0x43A
CRichEditUI::TxSendMessage this=15AA51E0 msg=43A wparam=1
```

添加暂停条件：[esp+4]==0x43A，看下哪里调用GetSelectionCharFormat：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8G2nMPJ7zumttib3WJQoNLMyAC83KI29eVMg7N9UdDT2gc77ZxfItS8rBfcME3vC3JHTITvgeycFPA/640?wx_fmt=jpeg&from=appmsg)

发现确实调用了SetSelectionCharFormat：

```
#define EM_GETCHARFORMAT		(WM_USER + 58)  0x43A
...
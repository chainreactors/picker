---
title: 用zig编写Windows的shellcode
url: https://guage.cool/zig-2-windows-shellcode.html
source: 半块西瓜皮
date: 2024-07-25
fetch_date: 2025-10-06T17:43:29.855391
---

# 用zig编写Windows的shellcode

[![](/img/avatar.jpg)](/about/)[氓聧聤氓聺聴猫楼驴莽聯聹莽職庐](/)

忙虏隆忙聹聣忙聣戮氓聢掳氓聠聟氓庐鹿茂录聛

忙聹卢忙聳聡莽聸庐氓陆聲

1. [氓聡聠氓陇聡氓路楼盲陆聹](#%E5%87%86%E5%A4%87%E5%B7%A5%E4%BD%9C)
   1. [PEB](#PEB)
   2. [莽禄聯忙聻聞盲陆聯](#%E7%BB%93%E6%9E%84%E4%BD%93)
   3. [PE盲赂颅莽職聞氓聹掳氓聺聙猫陆卢忙聧垄](#PE%E4%B8%AD%E7%9A%84%E5%9C%B0%E5%9D%80%E8%BD%AC%E6%8D%A2)
   4. [hash莽庐聴忙鲁聲](#hash%E7%AE%97%E6%B3%95)
   5. [氓拢掳忙聵聨API氓聨聼氓聻聥](#%E5%A3%B0%E6%98%8EAPI%E5%8E%9F%E5%9E%8B)
2. [氓庐聻莽聨掳盲赂禄猫娄聛茅聙禄猫戮聭](#%E5%AE%9E%E7%8E%B0%E4%B8%BB%E8%A6%81%E9%80%BB%E8%BE%91)
   1. [茅聙職猫驴聡PEB茅聛聧氓聨聠猫聨路氓聫聳DLL忙篓隆氓聺聴莽職聞氓聹掳氓聺聙](#%E9%80%9A%E8%BF%87PEB%E9%81%8D%E5%8E%86%E8%8E%B7%E5%8F%96DLL%E6%A8%A1%E5%9D%97%E7%9A%84%E5%9C%B0%E5%9D%80)
   2. [忙聬聹莽麓垄DLL忙篓隆氓聺聴莽職聞氓炉录氓聡潞猫隆篓猫聨路氓聫聳茅聹聙猫娄聛莽職聞API](#%E6%90%9C%E7%B4%A2DLL%E6%A8%A1%E5%9D%97%E7%9A%84%E5%AF%BC%E5%87%BA%E8%A1%A8%E8%8E%B7%E5%8F%96%E9%9C%80%E8%A6%81%E7%9A%84API)
   3. [茅聙職猫驴聡API氓庐聻莽聨掳莽聣鹿氓庐職莽職聞氓聤聼猫聝陆](#%E9%80%9A%E8%BF%87API%E5%AE%9E%E7%8E%B0%E7%89%B9%E5%AE%9A%E7%9A%84%E5%8A%9F%E8%83%BD)
3. [忙聻聞氓禄潞忙聫聬氓聫聳shellcode](#%E6%9E%84%E5%BB%BA%E6%8F%90%E5%8F%96shellcode)
   1. [忙聻聞氓禄潞忙碌聥猫炉聲莽篓聥氓潞聫](#%E6%9E%84%E5%BB%BA%E6%B5%8B%E8%AF%95%E7%A8%8B%E5%BA%8F)
   2. [忙聫聬氓聫聳shellcode](#%E6%8F%90%E5%8F%96shellcode)
4. [忙碌聥猫炉聲shellcode](#%E6%B5%8B%E8%AF%95shellcode)
5. [氓庐聦忙聲麓盲禄拢莽聽聛](#%E5%AE%8C%E6%95%B4%E4%BB%A3%E7%A0%81)
6. [忙聙禄莽禄聯](#%E6%80%BB%E7%BB%93)

氓聸聻氓聢掳茅隆露茅聝篓氓聫聜盲赂聨猫庐篓猫庐潞

[![](data:image/png;base64...)](https://github.com/howmp)[![](data:image/png;base64...)](https://weibo.com/howmp)[![](data:image/png;base64...)](https://guage.cool/atom.xml)![](data:image/png;base64...)

[盲赂禄茅隆碌](/)
[忙聳聡莽芦聽](/)[莽录聳莽篓聥](/categories/%E7%BC%96%E7%A8%8B/)

氓聫聭氓赂聝盲潞聨茂录職2024-07-24忙聸麓忙聳掳盲潞聨茂录職2024-07-24

# 莽聰篓zig莽录聳氓聠聶Windows莽職聞shellcode

Windows盲赂聥shellcode莽職聞茅聙職莽聰篓忙碌聛莽篓聥忙聵炉

1. 茅聙職猫驴聡PEB茅聛聧氓聨聠猫聨路氓聫聳DLL忙篓隆氓聺聴莽職聞氓聹掳氓聺聙
2. 忙聬聹莽麓垄DLL忙篓隆氓聺聴莽職聞氓炉录氓聡潞猫隆篓猫聨路氓聫聳茅聹聙猫娄聛莽職聞API
3. 茅聙職猫驴聡API氓庐聻莽聨掳莽聣鹿氓庐職莽職聞氓聤聼猫聝陆

忙聴漏忙聹聼氓戮聢氓陇職忙聲聶莽篓聥氓聙聼氓聤漏忙卤聡莽录聳忙聺楼氓庐聻莽聨掳茂录聦盲陆聠莽聨掳氓聹篓氓聡聽盲鹿聨茅聝陆忙聵炉茅芦聵莽潞搂猫炉颅猫篓聙莽聸麓忙聨楼莽录聳氓聠聶

忙炉聰氓娄聜忙聹聙盲陆鲁氓庐聻猫路碌茂录職[donut](https://github.com/TheWover/donut)茂录聦盲赂聤猫驴掳3盲赂陋忙碌聛莽篓聥氓聫炉盲禄楼氓聹篓盲禄楼盲赂聥盲禄拢莽聽聛盲赂颅忙聣戮氓聢掳

<https://github.com/TheWover/donut/blob/v1.0/loader/peb.c>

C猫炉颅猫篓聙猫聝陆氓聠聶莽職聞茂录聦Zig盲鹿聼盲赂聙氓庐職猫聝陆氓聠聶茂录聦忙聹卢忙聳聡盲陆驴莽聰篓zig莽聣聢忙聹卢0.11.0茂录聦氓掳聠氓赂娄盲陆聽盲赂聙忙聺隆茅戮聶氓庐聻莽聨掳shellcode

## 氓聡聠氓陇聡氓路楼盲陆聹

### PEB

猫聨路氓聫聳PEB

|  |  |
| --- | --- |
| ``` 1 ``` | ``` std.os.windows.peb() ``` |

### 莽禄聯忙聻聞盲陆聯

盲赂聙盲潞聸氓赂赂猫搂聛莽職聞windows盲赂聤莽職聞莽禄聯忙聻聞盲陆聯茅聝陆氓聹篓 `std.os.windows` 盲赂颅忙聹聣氓拢掳忙聵聨茂录聦盲陆聠莽录潞氓陇卤盲赂聨shellcode莽聸赂氓聟鲁莽職聞忙聹聣盲赂陇茅聝篓氓聢聠

盲赂聙忙聵炉PEB盲赂颅莽職聞`LDR_DATA_TABLE_ENTRY`莽禄聯忙聻聞茂录聦盲潞聦忙聵炉PE忙聽录氓录聫莽聸赂氓聟鲁莽職聞莽禄聯忙聻聞

莽聜鹿氓聡禄忙聼楼莽聹聥win32.zig

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 ``` | ``` const std = @import("std"); const windows = std.os.windows;  pub const LDR_DATA_TABLE_ENTRY = extern struct {     InLoadOrderLinks: windows.LIST_ENTRY,     InMemoryOrderLinks: windows.LIST_ENTRY,     Reserved2: [2]windows.PVOID,     DllBase: ?windows.PVOID,     EntryPoint: windows.PVOID,     SizeOfImage: windows.ULONG,     FullDllName: windows.UNICODE_STRING,     Reserved4: [8]windows.BYTE,     Reserved5: [3]windows.PVOID,     DUMMYUNIONNAME: extern union {         CheckSum: windows.ULONG,         Reserved6: windows.PVOID,     },     TimeDateStamp: windows.ULONG, };  pub const IMAGE_DOS_HEADER = extern struct {     e_magic: windows.WORD,     e_cblp: windows.WORD,     e_cp: windows.WORD,     e_crlc: windows.WORD,     e_cparhdr: windows.WORD,     e_minalloc: windows.WORD,     e_maxalloc: windows.WORD,     e_ss: windows.WORD,     e_sp: windows.WORD,     e_csum: windows.WORD,     e_ip: windows.WORD,     e_cs: windows.WORD,     e_lfarlc: windows.WORD,     e_ovno: windows.WORD,     e_res: [4]windows.WORD,     e_oemid: windows.WORD,     e_oeminfo: windows.WORD,     e_res2: [10]windows.WORD,     e_lfanew: windows.LONG, };  pub const IMAGE_DATA_DIRECTORY = extern struct {     VirtualAddress: windows.DWORD,     Size: windows.DWORD, }; pub const IMAGE_OPTIONAL_HEADER32 = extern struct {     Magic: windows.WORD,     MajorLinkerVersion: windows.BYTE,     MinorLinkerVersion: windows.BYTE,     SizeOfCode: windows.DWORD,     SizeOfInitializedData: windows.DWORD,     SizeOfUninitializedData: windows.DWORD,     AddressOfEntryPoint: windows.DWORD,     BaseOfCode: windows.DWORD,     BaseOfData: windows.DWORD,     ImageBase: windows.DWORD,     SectionAlignment: windows.DWORD,     FileAlignment: windows.DWORD,     MajorOperatingSystemVersion: windows.WORD,     MinorOperatingSystemVersion: windows.WORD,     MajorImageVersion: windows.WORD,     MinorImageVersion: windows.WORD,     MajorSubsystemVersion: windows.WORD,     MinorSubsystemVersion: windows.WORD,     Win32VersionValue: windows.DWORD,     SizeOfImage: windows.DWORD,     SizeOfHeaders: windows.DWORD,     CheckSum: windows.DWORD,     Subsystem: windows.WORD,     DllCharacteristics: windows.WORD,     SizeOfStackReserve: windows.DWORD,     SizeOfStackCommit: windows.DWORD,     SizeOfHeapReserve: windows.DWORD,     SizeOfHeapCommit: windows.DWORD,     LoaderFlags: windows.DWORD,     NumberOfRvaAndSizes: windows.DWORD,     DataDirectory: [16]IMAGE_DATA_DIRECTORY, }; pub const IMAGE_OPTIONAL_HEADER64 = extern struct {     Magic: windows.WORD,     MajorLinkerVersion: windows.BYTE,     MinorLinkerVersion: windows.BYTE,     SizeOfCode: windows.DWORD,     SizeOfInitializedData: windows.DWORD,     SizeOfUninitializedData: windows.DWORD,     AddressOfEntryPoint: windows.DWORD,     BaseOfCode: windows.DWORD,     ImageBase: windows.ULONGLONG,     SectionAlignment: windows.DWORD,     FileAlignment: windows.DWORD,     MajorOperatingSystemVersion: windows.WORD,     MinorOperatingSystemVersion: windows.WORD,     MajorImageVersion: windows.WORD,     MinorImageVersion: windows.WORD,     MajorSubsystemVersion: windows.WORD,     MinorSubsystemVersion: windows.WORD,     Win32VersionValue: windows.DWORD,     SizeOfImage: windows.DWORD,     SizeOfHeaders: windows.DWORD,     CheckSum: windows.DWORD,     Subsystem: windows.WORD,     DllCharacteristics: windows.WORD,     SizeOfStackReserve: windows.ULONGLONG,     SizeOfStackCommit: windows.ULONGLONG,     SizeOfHeapReserve: windows.ULONGLONG,     SizeOfHeapCommit: windows.ULONGLONG,     LoaderFlags: windows.DWORD,     NumberOfRvaAndSizes: windows.DWORD,     DataDirectory: [16]IMAGE_DATA_DIRECTORY, }; pub const IMAGE_FILE_HEADER = extern struct {     Machine: windows.WORD,     NumberOfSections: windows.WORD,     TimeDateStamp: windows.DWORD,     PointerToSymbolTable: windows.DWORD,     NumberOfSymbols: windows.DWORD,     SizeOfOptionalHeader: windows.WORD,     Characteristics: windows.WORD, }; pub const IMAGE_NT_HEADERS64 = extern struct {     Signature: windows.DWORD,     FileHeader: IMAGE_FILE_HEADER,     OptionalHeader: IMAGE_OPTIONAL_HEADER64, };  pub const IMAGE_NT_HEADERS32 = extern struct {     Signature: windows.DWORD,     FileHeader: IMAGE_FILE_HEADER,     OptionalHeader: IMAGE_OPTIONAL_HEADER32, };  pub const IMAGE_OPTIONAL_HEADER = if (@sizeOf(usize) == 4) IMAGE_OPTIONAL_HEADER32 else IMAGE_OPTIONAL_HEADER64; pub const IMAGE_NT_HEADERS = if (@sizeOf(usize) == 4) IMAGE_NT_HEADERS32 else IMAGE_NT_HEADERS64;  pub const IMAGE_EXPORT_DIRECTORY = extern struct {     Characteristics: windows.DWORD,     TimeDateStamp: ...
---
title: 跨平台底层网络库libdnet源码分析系列(十六)
url: https://mp.weixin.qq.com/s/azBxaRvEpVXSGf0xIU-Msg
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:26:05.001181
---

# 跨平台底层网络库libdnet源码分析系列(十六)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBnuBo5TrFsK3FlJ1vd5yyx6TLq9ara74oIje0ic124sqYCLtiaT10MTBTdGvbZdXf9zrrjicP4W3RhP4KflBibSJDBdeW0snaC97PYo/0?wx_fmt=jpeg)

# 跨平台底层网络库libdnet源码分析系列(十六)

原创

haidragon
haidragon

安全狗的自我修养

![]()

在小说阅读器中沉浸阅读

# 官网：http://securitytech.cc

#

# 源码分析mettle后门工具学习 所使用的依赖库

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnuA88j4IPSjia35QS2cTU4Z810ia05TXT3U1QRO9l2mcrO7CwXwbs5hIYUk6nPBUPDkPsEQm4slxibZZjiaZF0QDZeFqJ6eopNAJick/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

#

# 第 16 章：IPv6 完整支持探析

## 16.1 IPv6 协议概述

### 16.1.1 IPv6 的产生背景

随着互联网的飞速发展，IPv4 地址空间逐渐枯竭。IPv6（Internet Protocol version 6）作为 IPv4 的继任者，由 IETF 于 1995 年标准化（RFC 2460），提供了以下关键改进：

* **巨大的地址空间**：从 IPv4 的 32 位扩展到 128 位，提供 2^128 个地址
* **简化的报文头**：固定 40 字节头部，提高路由处理效率
* **内置安全性**：原生支持 IPsec
* **自动配置**：无状态地址自动配置（SLAAC）
* **更好的 QoS 支持**：流标签字段支持

### 16.1.2 libdnet 中的 IPv6 支持架构

libdnet 库在底层网络编程层面提供了完整的 IPv6 支持，主要包含以下模块：

```
1. IPv6支持模块结构
2. ├──IPv6地址处理（addr.c, addr-util.c）
3. ├──IPv6报文头封装（ip6.h）
4. ├──ICMPv6协议支持（icmpv6.h）
5. ├──IPv6校验和计算（ip6.c）
6. └──跨平台接口适配（intf-win32.c, intf-linux.c 等）
```

## 16.2 IPv6 数据结构深度分析

### 16.2.1 IPv6 地址结构定义

**源码位置**： `include/dnet/ip6.h`

```
1. #define IP6_ADDR_LEN    16/* IPv6 地址长度（128 位/8 = 16 字节） */
2. #define IP6_ADDR_BITS   128/* IPv6 地址位数 */

4. typedefstruct ip6_addr {
5. uint8_t data[IP6_ADDR_LEN];
6. } __attribute__((__packed__))ip6_addr_t;
```

**关键技术点**：

1. **紧凑内存布局**：使用 `__packed__` 属性确保结构体无内存对齐填充
2. **灵活的访问方式**：可通过 `data` 数组直接访问原始字节
3. **跨平台兼容**：支持大端和小端字节序

### 16.2.2 IPv6 报文头结构

**源码分析**：

```
1. struct ip6_hdr {
2. union{
3. struct ip6_hdr_ctl {
4. uint32_t ip6_un1_flow;/* 20 位流标识符 + 8 位流量类别 */
5. uint16_t ip6_un1_plen;/* 有效载荷长度 */
6. uint8_t  ip6_un1_nxt;/* 下一个头部类型 */
7. uint8_t  ip6_un1_hlim;/* 跳数限制 */
8. } ip6_un1;
9. uint8_t ip6_un2_vfc;/* 4 位版本 + 4 位流量类别高 4 位 */
10. } ip6_ctlun;
11. ip6_addr_t ip6_src;/* 源 IPv6 地址 */
12. ip6_addr_t ip6_dst;/* 目的 IPv6 地址 */
13. } __attribute__((__packed__));
```

**字段详解**：

| 字段 | 位数 | 说明 |
| --- | --- | --- |
| Version | 4 | IPv6 版本号（固定为 6） |
| Traffic Class | 8 | 流量类别（类似 IPv4 的 ToS） |
| Flow Label | 20 | 流标签，用于 QoS |
| Payload Length | 16 | 有效载荷长度（不包括 IPv6 头部） |
| Next Header | 8 | 下一个头部类型（TCP/UDP/ICMPv6 等） |
| Hop Limit | 8 | 跳数限制（类似 IPv4 的 TTL） |
| Source Address | 128 | 源 IPv6 地址 |
| Destination Address | 128 | 目的 IPv6 地址 |

### 16.2.3 统一的地址结构

**源码位置**： `include/dnet/addr.h`

```
1. struct addr {
2. uint16_t addr_type;/* 地址类型：ADDR_TYPE_IP6 = 3 */
3. uint16_t addr_bits;/* 地址前缀长度 */
4. union{
5. eth_addr_t __eth;
6. ip_addr_t __ip;
7. ip6_addr_t __ip6;/* IPv6 地址 */
8. uint8_t __data8[16];
9. uint16_t __data16[8];
10. uint32_t __data32[4];
11. } __addr_u;
12. };
```

**设计优势**：

* **统一接口**：通过 `addr_type` 区分 IPv4/IPv6/MAC 地址
* **灵活访问**：支持按 8 位、16 位、32 位、64 位访问地址数据
* **多播支持**：可方便地判断组播地址（首字节为 0xFF）

## 16.3 IPv6 核心功能实现分析

### 16.3.1 IPv6 报文头快速打包函数

**源码位置**： `include/dnet/ip6.h`

```
1. staticinlinevoid ip6_pack_hdr(void*buf,uint8_t c,uint32_t l,
2. uint16_t plen,uint8_t nxt,uint8_t hlim,void*src,void*dst)
3. {
4. struct ip6_hdr {
5. uint32_t ip6_v_c_l;/* 版本 + 流量类别 + 流标签 */
6. uint32_t ip6_plen_nxt_hlim;/* 载荷长度 + 下一头部 + 跳限制 */
7. ip6_addr_t ip6_src;
8. ip6_addr_t ip6_dst;
9. }*hdr =(struct ip6_hdr *)buf;

11. hdr->ip6_v_c_l =(6<<28)|(c <<20)|(IP6_FLOWLABEL_MASK & l);
12. hdr->ip6_plen_nxt_hlim =(htons(plen)<<16)|(nxt <<8)| hlim;
13. memcpy(&hdr->ip6_src, src, IP6_ADDR_LEN);
14. memcpy(&hdr->ip6_dst, dst, IP6_ADDR_LEN);
15. }
```

**实现要点**：

1. **内联优化**：使用 `inline` 减少函数调用开销
2. **字节序转换**： `plen` 使用 `htons()` 转换为网络字节序
3. **位域操作**：精确控制每个字段的位偏移
4. **内存拷贝**：直接使用 `memcpy` 复制 128 位地址

### 16.3.2 IPv6 地址字符串转换

#### （1）IPv6 地址转字符串（ip6\_ntop）

**源码位置**： `src/addr-util.c`

```
1. char*ip6_ntop(constip6_addr_t*ip6,char*dst,size_t len)
2. {
3. uint16_t data[IP6_ADDR_LEN /2];
4. struct{int base, len;} best, cur;
5. char*p = dst;
6. int i;

8. // 复制到 16 位数组（网络字节序）
9. for(i =0; i < IP6_ADDR_LEN /2; i++){
10. data[i]= ip6->data[2* i]<<8;
11. data[i]|= ip6->data[2* i +1];
12. }

14. // 查找最长的连续零段（RFC 5952）
15. best.len = cur.len =0;
16. best.base = cur.base =-1;

18. for(i =0; i < IP6_ADDR_LEN; i +=2){
19. if(data[i /2]==0){
20. if(cur.base ==-1){
21. cur.base = i;
22. cur.len =0;
23. }else
24. cur.len +=2;
25. }else{
26. if(cur.base !=-1){
27. if(best.base ==-1|| cur.len > best.len)
28. best = cur;
29. cur.base =-1;
30. }
31. }
32. }

34. // 生成压缩格式的 IPv6 字符串
35. if(best.base !=-1&& best.len <2)
36. best.base =-1;

38. if(best.base ==0)
39. *p++=':';

41. for(i =0; i < IP6_ADDR_LEN; i +=2){
42. if(i == best.base){
43. *p++=':';
44. i += best.len;
45. }elseif(i ==12&& best.base ==0&&
46. (best.len ==10||(best.len ==8&& data[5]==0xffff))){
47. // IPv4 映射地址 (::ffff:10.0.0.1)
48. if(ip_ntop((ip_addr_t*)&data[6], p, len -(p - dst))== NULL)
49. return(NULL);
50. return(dst);
51. }else
52. p += sprintf(p,"%x:", data[i /2]);
53. }

55. // 处理末尾字符
56. if(best.base +2+ best.len == IP6_ADDR_LEN){
57. *p ='\0';
58. }else
59. p[-1]='\0';

61. return(dst);
62. }
```

**算法亮点**：

* **零压缩算法**：自动查找最长连续零段并使用 `::` 压缩
* **RFC 5952 合规**：遵循 IPv6 地址文本表示最佳实践
* **IPv4 映射支持**：自动识别并转换为 `::ffff:x.x.x.x` 格式
* **边界检查**：确保输出缓冲区足够大（至少 46 字节）

#### （2）字符串转 IPv6 地址（ip6\_pton）

```
1. int ip6_pton(constchar*p,ip6_addr_t*ip6)
2. {
3. uint16_t data[8],*u =(uint16_t*)ip6->data;
4. int i, j, n, z =-1;// z 记录 :: 的位置
5. char*ep;
6. long l;

8. if(*p ==':')
9. p++;

11. for(n =0; n <8; n++){
12. l = strtol(p,&ep,16);

14. if(ep == p){
15. // 遇到 :: 压缩标记
16. if(ep[0]==':'&& z ==-1){
17. z = n;
18. p++;
19. }elseif(ep[0]=='\0'){
20. break;
21. }else{
22. return(-1);
23. }
24. }elseif(ep[0]=='.'&& n <=6){
25. // IPv4 后缀格式（如 ::ffff:192.168.1.1）
26. if(ip_pton(p,(ip_addr_t*)(data + n))<0)
27. return(-1);
28. n +=2;
29. ep ="";
30. break;
31. }elseif(l >=0&& l <=0xffff){
32. data[n]= htons((uint16_t)l);

34. if(ep[0]=='\0'){
35. n++;
36. break;
37. }elseif(ep[0]!=':'|| ep[1]=='\0')
38. return(-1);

40. p = ep +1;
41. }else
42. return(-1);
43. }

45. // 验证格式并填充零段
46. if(n ==0||*ep !='\0'||(z ==-1&& n !=8))
47. return(-1);

49. // 复制 :: 之前的部分
50. for(i =0; i < z; i++){
51. u[i]= data[i];
52. }

54. // 填充零段
55. while(i <8-(n - z -1)){
56. u[i++]=0;
57. }

59. // 复制 :: 之后的部分
60. for(j = z +1; i <8; i++, j++){
61. u[i]= data[j];
62. }

64. return(0);
65. }
```

**关键技术**：

* **灵活的输入解析**：支持完整格式、压缩格式、IPv4 映射格式
* **错误检测**：严格验证输入格式，防止非法地址
* **零填充算法**：正确计算并填充 `::` 代表的零段

### 16.3.3 IPv6 校验和计算

**源码位置**： `src/ip6.c`

```
1. void ip6_checksum(void*buf,size_t len)
2. {
3. struct ip6_hdr *ip6 =(struct ip6_hdr *)buf;
4. struct ip6_ext_hdr *ext;
5. u_char *p, nxt;
6. int i, sum;

8. nxt = ip6->ip6_nxt;

10. // 跳过所有扩展头部
11. for(i = IP6_HDR_LEN; IP6_IS_EXT(nxt); i +=(ext->ext_len +1)<<3){
12. if(i >=(int)len)return;
13. ext =(struct ip6_ext_hdr *)((u_char *)buf + i);
14. nxt = ext->ext_nxt;
15. }

17. p =(u_char *)buf + i;
18. len -= i;

20. // 根据下一头部类型计算校验和
21. if(nxt == IP_PROTO_TCP){
22. struct tcp_hdr *tcp =(struct tcp_hdr *)p;
23. if(len >= TCP_HDR_LEN){
24. tcp->th_sum =0;
25. sum = ip_cksum_add(tcp, len,0)+ htons(nxt +(u_short)len);
26. sum = ip_cksum_add(&ip6->ip6_src,32, sum);// 伪头部
27. tcp->th_sum = ip_cksum_carry(sum);
28. }
29. }elseif(nxt == IP_PROTO_UDP){
30. struct udp_hdr *udp =(struct udp_hdr *)p;
31. if(len >= UDP_HDR_LEN){
32. udp->uh_sum =0;
33. sum = ip_cksum_add(udp, len,0)+ htons(nxt +(u_short)len);
34. sum = ip_cksum_add(&ip6->ip6_src,32, sum);
35. if((udp->uh_sum = ip_cksum_carry(sum))==0)
36. udp->uh_sum =0xffff;// UDP 校验和不能为 0
37. }
38. }elseif(nxt == IP_PROTO_ICMPV6){
39. struct icmp_hdr *icmp =(struct icmp_hdr *)p;
40. if(len >= ICMP_HDR_LEN){
41. icmp->icmp_cksum =0;
42. sum = ip_cksum_add(icmp, len,0)+ htons(nxt +(u_short)len);
43. sum = ip_cksum_add(&ip6->ip6_src,32, sum);
44. icmp->icmp_cksum = ip_cksum_carry(sum);
45. }
46. }
47. }
```

**IPv6 校验和特点**：

1. **伪头部包含源和目的地址**：增强端到端完整性检查
2. **扩展头部处理**：自动跳过 Hop-by-Hop、Routing、Fragment 等扩展头
3. **UDP 特殊处理**：校验和为 0 时设置为 0xFFFF（RFC 2460 要求）
4...
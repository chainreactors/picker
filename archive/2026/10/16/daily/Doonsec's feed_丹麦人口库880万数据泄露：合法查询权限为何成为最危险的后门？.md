---
title: 丹麦人口库880万数据泄露：合法查询权限为何成为最危险的后门？
url: https://mp.weixin.qq.com/s/6nzMixw_ob6rvfqCBzKnWg
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:31:46.033514
---

# 丹麦人口库880万数据泄露：合法查询权限为何成为最危险的后门？

# 丹麦人口库880万数据泄露：合法查询权限为何成为最危险的后门？

美创资讯

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/ib9aljs9x2mc2KErXn6CH8HJJP1WJD4vVjibrq7vEK1X8Hl99vHdLnEw0icqgMZFiaAabSee69uLoOMk7B3RfSsKaA/640?wx_fmt=gif&from=appmsg)

**![image001.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ltPKBia2A81lGjQDOuvTPH04dz5x88Nic2KiblYGp9qyohrOwicRniaVYqablWW1cyc6s8Woj5ZJJmmAEfdK4SluHclAqHWSv4GLj0KTUkh0O9I4/640?wx_fmt=png&from=appmsg)

**弱口令攻破丹麦CPR系统****

据媒体报道，近期丹麦中央人口登记册（CPR）被发现遭入侵，约880万人的姓名、住址及CPR号泄露，约占系统的80%。

丹麦中央人口登记册（CPR）几乎覆盖所有丹麦人的姓名、地址、CPR编号等信息，私营企业因业务需要可申请获得合法查询权限。这意味着，风险被分散到数百家规模与安全预算各不相同的小企业。此次攻击者仅利用一家小公司合法的CPR系统查询权限，用最简单的弱口令完成“破门”，再用自动化程序批量枚举并取数。

涉事企业Pays ApS公司仅2名雇员，却拥有查询CPR的合法权限，至少3个账户使用弱口令「123456」作为登录密码，其中一个拥有管理员权限。

**![image003.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ltPKBia2A81m1wzSqVOeDiceFPich1XHA81XuPUL8KpfiaL5PVtWbXDOcaA9JUJl4C0AW3gRwBLlcnSX8Yw5kPSdwWh7uafc3JupozgNLRFZNLA/640?wx_fmt=png&from=appmsg)**

本次入侵值得关注的两个细节是：

****其一，访问始于泄露的前员工密码****

一名自称黑客者表示最初“借”前员工的弱密码进入系统。

**![image005.png](https://mmbiz.qpic.cn/mmbiz_png/ltPKBia2A81nk4iaR4j4JbicOfdPVZAH2s1auTSIFusVuKdqDkYcelkSbODIDJmP8IK4PXXbh88zlhznP2gn7QALS90ZDlIraPeAnek5ZiblM6o/640?wx_fmt=png&from=appmsg)

**其二，拿到权限后持续批量取数****

攻击者编写程序批量枚举并提取CPR数据，驻留时间达21天17小时，这期间没有任何告警。这一过程暴露出合法账号访问路径上的风险：如果缺少针对查询频次、累计取数规模和访问行为的监测与限制，具备合法权限的账号可能被用于非法批量获取数据。

![image007.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ltPKBia2A81kozcF5d5byxPfNpxUApFibibPia9vkqIfE5kfdjjw6YURT7pZW0TLRMeoO1JGNMFsJtkZvUuvN6plpFr1ICjvdtfXufypkzcDO6Y/640?wx_fmt=png&from=appmsg)

**数据安全启示**

这一安全事件再次说明，第三方账号的“信任传递”和访问入口的薄弱，会增加数据被滥用的风险。 当数据安全的合法查询权限下放给成百上千家规模、预算各异的小企业时，整体安全水位便取决于最薄弱的环节。权限越分散，越需要统一的安全基线兜底。

![丹麦9.jpg](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ltPKBia2A81lYsXepMUvMJdCgrzibLlbuQ6BWERtPDyfkpSCf293A0cPK7mjVfpeEdHa1vlpTlTU8mDXu4NRcht1UuI0cVHYLSOp3g1rj5k6M/640?wx_fmt=jpeg&from=appmsg)

合法账号的非法访问易成最大盲区。事件中，攻击者仅通过冒用合法账户便达到了目的。对拥有合法查询/运维权限的账户而言，每次批量导出、非常规时段访问、异常调用，都可能是攻击痕迹——这恰恰是单靠权限管理难以覆盖的地方。

![image011.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ltPKBia2A81lLGE9K02839L1Z7VI679icxlmjspRKoL9icJlUJnvzBCIk9HN5gibWloEK0AnqLM40sO9BkB7O988hYtfCdAXpgqUG4rYDW4R5ZE/640?wx_fmt=png&from=appmsg)

****美创建议**

**加强第三方访问授权管理****

根据业务用途、数据敏感程度及访问风险实施分级授权，仅开放完成业务所必需的数据范围，并结合业务量、业务频次设置查询配额。

**![image013.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ltPKBia2A81mMqD86cS5ibN0DKfoeoj5sPDHAvQc6IdG7wZicfia40rXF2lTCVuPLrQAqB1K5YskoVdjoFsP7F6k14TISjqDiahBuZjbJbU9ncos/640?wx_fmt=png&from=appmsg)**

为临时访问授权设置有效期，到期后停止相应访问。离职时及时停用相关账号，撤销访问授权，并处理共享凭据及存量会话。

**![image015.png](https://mmbiz.qpic.cn/mmbiz_png/ltPKBia2A81nmQ4joK2tXQofWlHUFqnLpFtu7WDnEbRqbq15XHJeD0NjEt5zMuYsgrRqqyfo8SaibUjsTCBsCicqYIReBiagoRicPjb8x8YZNrm4/640?wx_fmt=png&from=appmsg)

**建立行为基线****

行为基线即不只按“请求是否合法”判断，还要按主体历史基线判断查询时间分布、返回字段组合、被查记录之间的相关性等。

**![image017.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ltPKBia2A81mAkW9icib96HecnwXISPGiaia33QduqSwBnZAQUktPib5hD9DzVQy5M7M6ibPogPtXpxiclh3jWs7szwibRVGOibcbhnZO6RcUzhrYXSSI/640?wx_fmt=png&from=appmsg)**

根据实际业务量、批处理任务及历史访问特征设置配额和阈值。

**![image019.png](https://mmbiz.qpic.cn/mmbiz_png/ltPKBia2A81nmTHjP2AaLUCmMmSwLM7c1elzRz6RkpnDlVGF92gd0JWMoCx6z4BEOXiaAyY72tvg5xtYetSnUshhG4nWApKzTliarpc8ulhHP4/640?wx_fmt=png&from=appmsg)**

批量导出审批与二次授权。

**![image021.png](https://mmbiz.qpic.cn/mmbiz_png/ltPKBia2A81ly5uhvmk5XORcJbbue0icJLvQz8klOtDPXXap7CsB7X9yUwVXyGD30bOIBPzoAgh8PyO5fcMFBnB3J5yLX8NK5QFxGkeIOlTPY/640?wx_fmt=png&from=appmsg)

**治理特权账号****

丹麦安全事件中，“正常登录”和攻击者在同一视角下无法区分。

**![image023.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ltPKBia2A81ldlS4neHYKVCjNU4SvK9tKoq7V9Ue5GZzKcsNur5f1tOxVXOWCrbsYpHMQ0jOMZUbD45iaBwalO3wJH6Rog69vMeLchIjvqCR4/640?wx_fmt=png&from=appmsg)**

对数据库运维、开发测试及第三方人员访问，应落实身份认证、账号托管、最小权限、授权有效期和操作审批。

**![96ebad79e0c3a52f9cac28c653ec62b8.png](https://mmbiz.qpic.cn/mmbiz_png/ltPKBia2A81mevJ76Y0Gib2xozJPtibc9EKO8bcAIACL8xF1O1aEz9EWNmHU5cqEnKNz0d1MVWt71K1MHmqoy0hlOw9icOMeicrmItAvfD56gutM/640?wx_fmt=png&from=appmsg)**

对业务系统及对外查询账号，由账号所属系统或统一身份平台落实多因素认证、密码策略和离职撤权。

**![丹麦27.jpg](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ltPKBia2A81mwrQFIzgibEMuLsoib6EXclmlm04EjSnxSmDqGF9ibNmpGfIPEM16Se4dGmfMzn02t3alUSjMicibONqGvUSdZaFRLQ8fULVYLGcmM/640?wx_fmt=jpeg&from=appmsg)**

对账号的全生命周期进行管理，如离职流程必须包含“权限核销”这一动作，而不是只交回电脑。

![美创丹麦29.jpg](https://mmbiz.qpic.cn/mmbiz_jpg/ltPKBia2A81nZmhaaDXNYM1nSaMF2Fvm0hdpVjUrRLiaYqrw98SDRFmL3ic0XIx10J266zr2S4T9BokIBwj98KhL8hibgR5Sdss3UTght82UvxY/640?wx_fmt=jpeg&from=appmsg)

这些正是美创防水坝、API审计、API防控、数据库审计等产品的典型应用场景。

****数据库人员访问管控****

针对运维、开发测试及第三方人员直接访问数据库的场景，美创Ng防水坝通过身份认证、账号托管和免密访问，减少真实数据库凭据直接暴露与多人共用带来的风险。按照人员身份、数据库资产、敏感对象和操作类型配置最小访问权限，并为临时授权设置有效期，到期后停止相应访问，降低长期持有权限和超范围访问的风险。

![丹麦31.jpg](https://mmbiz.qpic.cn/mmbiz_jpg/ltPKBia2A81mjvJ9F3MwmPq9feone9o89bsoXozvXhMvniaQxJ0Epnq9MluNA3U7RmuKUwhOTAU0Nup4vZ3iccse6062tBrNbaPDEapCwXjn1c/640?wx_fmt=jpeg&from=appmsg)

对于敏感数据查询、高危SQL及临时提权，Ng防水坝可结合工单审批执行授权控制，并按策略限制访问频次和数据访问量。在SQL窗口导出数据时，进一步落实导出授权与控制，同时记录访问、审批和阻断过程，为追溯人员操作提供依据。离职账号停用及源系统权限撤销，则需与账号所属系统或统一身份平台协同落实。

![image033.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ltPKBia2A81licSR8iaGbASGP87eiaXhs2icn2zgaXSfNSTuEN5vZGFKTNdUibuR3kHRIWXOnzJd8hoRFEGN7iahelA61cqxvAJaibPCIKs6BTC5EPY/640?wx_fmt=png&from=appmsg)

****API敏感数据管控****

针对第三方通过API查询和获取敏感数据的场景，美创NgAPI防控基于API资产和访问身份，对应用及接口设置访问授权与有效期，明确哪些身份能够在什么时间访问哪些接口。通过请求频次、请求次数及敏感数据获取次数等策略，限制单个访问主体的持续调用，降低合法查询权限被用于自动化批量取数的风险。

![image035.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ltPKBia2A81kAn6TZkAQFDpnQhNic5hKM7g3IfLSxFBdUicsS0jCXfSYaSSicWxuoGUJDBhFkwTiaOz6Yia8bng93Cy3I9dqgP0j40lCiaT8Atb3H8/640?wx_fmt=png&from=appmsg)

对于接口返回的敏感信息，NgAPI防控可按资产、身份和敏感数据类型配置动态脱敏策略，减少共享交换过程中敏感数据的直接暴露。访问授权、调用限制与动态脱敏协同执行，使第三方访问范围与业务需求相匹配。当调用触发配置的限制条件时，按策略实施管控并留存相关记录，为后续异常研判和策略调整提供依据。

![丹麦37.jpg](https://mmbiz.qpic.cn/mmbiz_jpg/ltPKBia2A81l8xNrjCBynib4ibPC1HVkzvM0G3pl0dgtKGxGkiabJ45jpTwonh4Mm2xnydFJPJJJztvuWo6hUuibMW58EcEcHHlI9odw3FqkrX7M/640?wx_fmt=jpeg&from=appmsg)

****API异常访问监测与追溯****

针对合法账号被冒用后持续调用接口的风险，美创NgAPI审计通过API资产盘点、访问日志审计和异常行为检测，观察接口调用中的访问主体、调用时间、请求频次及敏感数据访问情况。结合实际业务特征配置检测规则，关注调用频次突增、非常规时段访问和敏感接口集中调用等异常线索，为发现持续取数风险提供依据。

![丹麦39.jpg](https://mmbiz.qpic.cn/mmbiz_jpg/ltPKBia2A81k4ricmsZAN2Y6dlkCCRSibWW2BXqdbRJZX72x3NX2b89nv7sodAdVJQOWlypXZF9H03ouibeARz3KfFs6Nrtvqck7H7U7XBAuttU/640?wx_fmt=jpeg&from=appmsg)

****数据库异常访问审计****

对于分散在多个会话中的小批量查询，美创Ng数据库审计结合身份画像，按照数据库账号、终端、应用、敏感对象和时间范围关联分析会话日志，并通过事件回溯提取SQL及其执行顺序。由此，可发现频繁变换查询条件、连续分页、反复访问同一敏感对象以及累计访问量异常等数据遍历迹象。

![丹麦41.jpg](https://mmbiz.qpic.cn/mmbiz_jpg/ltPKBia2A81mibal09ibmria27d2yiayueicPbiad2amL5nWJw3Ae7z44qUs8EMKhRvJKPQlr8PibLhITJ33gUgNGUZOIdmUyz6o4qItQRhUluyWia8A/640?wx_fmt=jpeg&from=appmsg)

通过数据库账号、客户端 IP、终端 IP、应用工具、访问时间和操作轨迹，美创Ng数据库审计可发现账号共用、异常终端访问、非工作时间访问和访问习惯偏离等风险。结合安全客户端和三层身份关联，可进一步关联终端、系统用户、应用用户和实际人员，为疑似账号冒用的研判及责任追溯提供身份依据。

![丹麦43.jpg](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ltPKBia2A81l6UovDxG31sNCNhXwicwp7bp2BDjXLZDbLq2fzXGRY5JPemwZ46eJKbialFuga7rLc4sY3WRqQNnmfcMPXleWibmagnvFu3g077k/640?wx_fmt=jpeg&from=appmsg)

****结语****

丹麦的教训提醒我们：数据共享与合法授权正在成为常态，安全建设也应当从“守大门”转向“守每一个有权限的人”，守住“每一次访问”。

![丹麦45.jpg](https://mmbiz.qpic.cn/mmbiz_jpg/ltPKBia2A81nRWLqpjWexCJD6ciciceHpDSfcv2QBpzEzIw4aDKorB7whicVGP99Kaia8ctia7xfNdwKeITXvmmkB997H6EvyKGEZHNqsZCXzGiavw/640?wx_fmt=jpeg&from=appmsg)

![丹麦47.jpg](https://mmbiz.qpic.cn/mmbiz_jpg/ltPKBia2A81llbKzXAp13pzB46nibQpKmCxxTdoWQEjpJ234TJ2chctB0AR8DPicKhHHXia6dVlRicp1N67ugpWCRQbPWgvZ8Cfuau3zCO4zRPWI/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/pJjOS4MSntVSQRXIHuHeHvW0Klr3u9EiaeB9lxKt3WOPVv7rnRqQbicn8gCnbRzMKrsrnLdaBtVe8ZxemVBSK8XQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC7IHABFmuMlWQkSSzOMicicfBLfsdIjkOnDvssu6Znx4TTPsH8yZZNZ17hSbD95ww43fs5OFEppRTWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ib9aljs9x2mfD4buRKuU8ZMSge8IZuFiauFQ3paMGootiaYqZ5iasxia90dFfQhlWlYTQuvoScDJt6gibOTIT82aHLBA/640?wx_fmt=jpeg "ÉãÍ¼Íø_401931611_wx_¿Æ¼¼ÔÆ¼ÆËã£¨ÆóÒµÉÌÓÃ£©.jpg")

[半夜两点数据库被 “偷家”，你的数据库审计管用吗？](https://mp.weixin.qq.com/s?__biz=MzA3NDE0NDUyNA==&mid=2650822409&idx=1&sn=ce04c0ababab14a05a3ee361e1bbd6e9&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ib9aljs9x2mfD4buRKuU8ZMSge8IZuFiauHDdqRibcn...
---
title: 从用户注销到优惠券复用：一次应用逻辑漏洞的完整剖析!
url: https://mp.weixin.qq.com/s/DqF_MytTbd3AlPO4b6_ocQ
source: Doonsec's feed
date: 2026-08-24
fetch_date: 2026-08-25T02:58:37.265444
---

# 从用户注销到优惠券复用：一次应用逻辑漏洞的完整剖析!

# 从用户注销到优惠券复用：一次应用逻辑漏洞的完整剖析!

w4nk3r
w4nk3r

神农Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

课程培训

扫码咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic)

#

专注于SRC漏洞挖掘、红蓝对抗、渗透测试、代码审计JS逆向，CNVD和EDUSRC漏洞挖掘，以及工具分享、前沿信息分享、POC、EXP分享。不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（课程培训限时优惠）。

#

文章作者：w4nk3r

文章来源：https://xz.aliyun.com/news/92682

01

0x1 从用户注销到优惠券复用：一次应用逻辑漏洞的完整剖析!

## 前言

各类互联网产品的新用户福利场景，极易出现业务逻辑漏洞。攻击者可利用设计缺陷绕过营销限制，反复领取限时权益，若免费权益为付费资源，则直接造成运营资损。

**这类问题几乎都源于四大底层设计疏漏：**

1. 用户身份校验体系单一，缺少多维度追溯能力；
2. 权益发放判断逻辑简单，未核查历史操作记录；
3. 注册、注销、营销三大业务模块完全割裂，无状态联动；
4. 数据库存储模型设计不合理，数据丢失导致风控失效。

本文以一款会员时长类应用作为研究样本，完整拆解因账号注销物理删库带来的权限校验缺陷，复现 “注销 - 重注册” 无限领取新人权益的攻击链路，同时搭配抽象伪代码定位底层代码问题，给出通用化修复与审计思路。

> 文中演示代码均为抽象伪 Demo，仅用于还原设计缺陷，非业务原始源码。

## 漏洞实战复现（抽象业务场景描述）

**测试目标为一款提供付费时长服务的会员应用，新注册用户可自动领取两天免费使用时长。（由于该APP较为敏感，这里用的平替图）**

1. 全新临时账号登录，系统自动下发两天免费时长；

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUpxibMSyS55Oecve7JVRLfKwuRfvwV64U5uVkRdgjdTNYVy9AT2GrLNYkBWhRosBKQgIjEnN9kh2Z8ug6ByUia6gyQGmSyibzIH0/640?wx_fmt=png&from=appmsg)

2. 等待权益剩余时长缩减至 1 天，复现真实用户使用场景；

   ![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QWyztmaqOZmsgibkXqic9yUxOErdBWQicGnv7xujotolkwtxFNcek0D594Lx0EFfexicbpLzPnAjOb6T5mkZGMUG0pXetrvrGKCBMI/640?wx_fmt=png&from=appmsg)

3. 执行账号注销、清空本地缓存，服务端物理删除当前账号全部数据；

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXT1BbzX8IlQCHu3iapbCMr2zdkiaLzUjvP6N4QCaXNic5bs7zJqoN25Jr0MIGUJnT6rSthFTJ0ibkBHgcH9VKaSbM8icktKVUpowsY/640?wx_fmt=png&from=appmsg)

4. 让系统二次下发临时账号；

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXKcw9Hu9JTYRM1tItgM6IibGujWzib4xjpSiahMHudLaCCBzVUvJ0BLcyQzvS9yXTOvrtmJBXlo32X5icYEP0ZMiaB1ZHjTavjX2mw/640?wx_fmt=png&from=appmsg)

5. 系统识别为全新用户，再次下发完整两天新人免费时长，循环操作可无限重置权益。

   ![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QVKnwzpSic0zsiaFSIqoKAACtSQ1icPABtMsDzIuianQEYnN94oQzborDF5OcLfndRedTdkgDnHmnsgHIQVwLRXMvA9Qo7jZXBfap8/640?wx_fmt=png&from=appmsg)

整体流程大概就是

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXltia2bdNwKgajIAy9PoZpgjBdXKsUo1BNcxlLeribw0YLdpUsicicFFpGgR12icEfycQkAicClqttfLlg2KKIEFKgplgdlf9pPOJeg/640?wx_fmt=png&from=appmsg)

## 下面进行讲解，啥情况下会导致该漏洞产生

## 一、用户身份校验体系存在短板

### 1. 仅依靠单一字段区分用户

系统仅通过邮箱、手机号作为判定新用户的唯一依据，未叠加设备指纹、IP、实名信息等辅助校验维度。一旦账号注销后数据被彻底清除，使用同一手机号 / 邮箱二次注册，系统会直接判定为全新用户。与某src的业务审核人员交流后发现，该问题在中小型应用中十分普遍：业务接口仅查询当前有效账号，完全忽略已注销的历史身份。

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXgeKqQaMepauSSBaaWjiaCeQ4alZ2aRQ2jwNLibibAAf5ibj2xO4b2eQnxBqibmfNGCY2SDVnU1qFnB2OFdmPVicSNPNfzuPlxJkcmY/640?wx_fmt=png&from=appmsg)

### 2. 注销数据无持久化留存

产品执行账号注销时，直接物理删除整条用户数据，没有留存注销台账、权益领取记录。本次分析的样本应用存在同类缺陷：临时测试账号数据无长期持久化机制，注销清空数据后，系统彻底丢失该身份的历史行为记录，无法做二次风控拦截。

#### 配套缺陷演示：

```
@Service
public class VulnerableUserService {

@Autowired
private UserRepository userRepository;

// 注册逻辑：仅检查邮箱是否存在
public User register(String email, String password) {
    // 漏洞点：仅通过邮箱判断用户是否存在，未考虑已注销账户
    if (userRepository.findByEmail(email) != null) {
        throw new RuntimeException("邮箱已注册");
    }
    User newUser = new User(email, password);
    return userRepository.save(newUser);
}

// 注销逻辑：直接删除所有数据
public void deleteAccount(Long userId) {
    userRepository.deleteById(userId);
  }
}
```

## 二、权益发放校验逻辑片面化

### 1. 新用户判定标准仅看当前账号状态

发放新人福利时，系统只判断当前账号是否为首次注册，没有考虑账号注销重置身份的攻击场景，攻击者循环注销重注册就能反复领取权益。

### 2. 不追溯身份历史领取记录

权益下发逻辑仅绑定当前有效账号，不会检索该手机号、邮箱过往所有领券行为；账号被删除后，对应的权益领取记录同步消失，风控完全失效。

#### 缺陷发放逻辑演示：

```
@Service
public class VulnerableCouponService {

    @Autowired
    private UserRepository userRepository;

    // 发放新人权益接口
    public Coupon grantCoupon(String email) {
        User user = userRepository.findByEmail(email);
        if (user == null) {
            throw new RuntimeException("用户不存在");
        }
        // 风险点：仅校验当前账号领券状态，无全生命周期历史核查
        if (user.getCoupons().isEmpty()) {
            Coupon coupon = new Coupon("NEW_USER_100");
            user.getCoupons().add(coupon);
            userRepository.save(user);
            return coupon;
        } else {
            throw new RuntimeException("当前账号已领取新人权益");
        }
    }
}
```

## 三、业务流程模块割裂，缺少风控兜底

### 1. 注销与营销模块无状态联动

产品设计时将账号注销、权益发放拆分为独立模块，两者数据完全不互通。注销操作不会同步更新营销活动的风控台账，无法拦截重置身份重复领福利的行为。

### 2. 缺少注册频率冷却风控

接口未限制同一 IP、设备、手机号的短时间注册次数，无自动化行为拦截策略，攻击者可批量脚本循环注册注销，大批量消耗运营权益。

#### 无任何风控的注册接口演示：

```
@RestController
public class VulnerableAuthController {

    @Autowired
    private VulnerableUserService userService;

    @PostMapping("/register")
    public User register(@RequestParam String email,
                         @RequestParam String password) {
        // 风险点：无设备指纹校验、无IP注册频次限制
        return userService.register(email, password);
    }
}
```

## 四、底层数据库模型设计缺陷

1. 未使用软删除机制，账号注销直接执行物理删除；
2. 用户表与权益记录表采用级联删除，账号销毁后，所有领券记录同步清除，永久丢失审计凭证；
3. 查询接口仅过滤有效账号，无法检索历史注销身份。

#### 数据库实体缺陷演示:

```
@Entity
public class User {
    @Id
    @GeneratedValue
    private Long id;
    private String email;

    // 风险点：无is_deleted、deleted_at软删除标记；级联删除连带清除权益记录
    @OneToMany(mappedBy = "user", cascade = CascadeType.ALL)
    private List<Coupon> coupons = new ArrayList<>();
}

public interface UserRepository extends JpaRepository<User, Long> {
    // 仅查询现存有效账号，已物理删除数据无法追溯
    User findByEmail(String email);
}
```

### 用流程图总结一下，大概就是

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWYokFjiaUYusicgWyGRPzMKibsELtVaJWK0WBPxgVxrk2XYxQbbiaoXasl4paS0zd2y13xoacjxSWS6OtY92hVKyt3FX5ic3ImzlrY/640?wx_fmt=png&from=appmsg)

## 五、漏洞总结与标准化修复方案

### 漏洞根因总结

该时长会员应用出现重复领权益漏洞，核心问题是**账号数据生命周期与营销风控体系脱节**。物理删除注销用户数据，导致系统无法追溯身份历史行为；叠加单一字段校验、模块数据隔离、无多层风控多重缺陷，最终形成可无限复用新人福利的业务漏洞。此类逻辑漏洞无法通过扫描器发现，攻击流量和正常用户操作高度相似，是业务安全审计的重点排查对象。

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXqqBzBnj83VlQDSrtibplmXTzAYBluAtqObHEbqxibpELtOnWREU3jdsUP6k5eqVico3OUR59pRrM97evuKZE0Zxt6zFXuWZBgiak/640?wx_fmt=png&from=appmsg)

### 分层修复落地建议

1. **多维度身份识别**叠加手机号、邮箱、设备指纹、IP 地址多维度做身份判定，不单一依靠账号表存在性判断新用户；
2. **数据持久化追溯机制**放弃纯物理删除，采用is\_deleted、deleted\_at软删除字段；独立搭建权益领取历史台账，账号注销不删除台账记录，永久留存领券审计数据；
3. **打通模块状态联动**注销操作同步更新营销风控台账，下发权益前优先查询身份全历史领券记录，而非仅校验当前账号；
4. **增加接口风控兜底**对注册接口增加频次限制、短时间注册冷却机制，拦截自动化批量注销注册行为。

02

0x2 培训课程介绍

26

**SRC漏洞挖掘培训课程**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6cIuvSQkkicOHhYFkQLTibYAMUR9rfZ9eUrI78toIC4V2304G909O6s6CnVrAGiaYLEJM9XuUARhzNfxCtYKQfQ83wfPSlqpshSScfoYzSKzgY/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&watermark=1&tp=wxpic#imgIndex=4)

**1.课程价格目前是575（后面也会随着人数越多，涨价）🌟师傅们还可以上车补票，冲冲冲！**

**2.报名成功送知识星球一个，拉内部小圈子交流群+SRC直播通知群！✨**

**3.一周2节课程，直播+录播形式，课程内容大家可以看课表，目前是第一期，一次报名永久无限听课！❤️**

**4.目前是第一期课程，后面比如说开了二、三期，都是不用在花钱的！**

**5.上课结束后，会把视频录播+课件笔记一起打包发直播群！**

**6.哔哩哔哩SRC课程公开课，链接🔗直达：**

**https://space.bilibili.com/642258933**

SRC课程详情🔎：[学了一堆理论，还是挖不到漏洞？你缺的是实战！](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247509438&idx=1&sn=1b5c5c14bef52f1a4fd8319fea73a0cb&scene=21#wechat_redirect)

内部小圈子知识星球详情🔎：[50 元封顶！渗透攻防 + SRC 漏洞星球限时开放！](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247509408&idx=1&sn=2e12452dfc2d34631af5109af28a6758&scene=21#wechat_redirect)

欢迎关注公众号：神农Sec，报名咨询添加VX：routing\_love

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mcko8AHj6QVcCkxIUpaBmNic17zibGfXMWrr9z89gE0DFtbOu3QYzD5d62zsp6qwc38Pssk60mLq8VKthcMOmctVlHU716S5G4KYmrKVrEj5c/640?wx_fmt=other&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6)

开课快五个月时间，课程目前已经累计加入了960+个学员了，课程培训招生任火热持续中，师傅们对于我们课程感兴趣的，想要学习技术，找工作的可以咨询我报名。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVmdLBDlbl5p4Teyw5qqFOIFTIUxIxRay83I5qDXG690XI61gRj8MXTvTaibC4q2cCb1CbM4XS2FK6X4KYhPTX2ibgvA363YYwcE/640?wx_fmt=png&from=appmsg)

课程培训记录📝，每次上车在1-3小时之间，上课包括课程内部群大家交流氛围很好！

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mcko8AHj6QV7iczVHowN13BzCTraG8jDUoe5hluiaZ90RUy7FjW398DictcrZhHrYpMgw4polRqvlGua6iakYdARPI3Jkiahhjvrvkviblm19U4F0/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

课程上课笔记课件📒都会打包给师傅们，笔记都非常详细，很多几k价格的培训机构哪...
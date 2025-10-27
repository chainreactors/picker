---
title: B2B Node Pool Functions for SAP CPI using Groovy script – Part2
url: https://blogs.sap.com/2023/07/26/b2b-node-pool-functions-for-sap-cpi-using-groovy-script-part2/
source: SAP Blogs
date: 2023-07-27
fetch_date: 2025-10-04T11:54:35.263546
---

# B2B Node Pool Functions for SAP CPI using Groovy script – Part2

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* B2B Node Pool Functions for SAP CPI using Groovy s...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162811&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [B2B Node Pool Functions for SAP CPI using Groovy script - Part2](/t5/technology-blog-posts-by-members/b2b-node-pool-functions-for-sap-cpi-using-groovy-script-part2/ba-p/13565794)

![BhaskarY](https://avatars.profile.sap.com/f/e/idfec80a39343b5e5ee299d8bd97812cce5727a8235a8efca07a38f2d3ba7fdb5f_small.jpeg "BhaskarY")

[BhaskarY](https://community.sap.com/t5/user/viewprofilepage/user-id/150607)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162811)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162811)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565794)

‎2023 Jul 27
12:20 AM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162811/tab/all-users "Click here to see who gave kudos to this post.")

5,754

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (3)

In this blog, we will be going through few B2BNodePool functions and the corresponding groovy scripts in SAP CPI which will help us to get the required outputs for the given inputs. This Blog can be considered as the part two of the below blog.

Part1: [UDFNodePool Functions for SAP CPI with Groovy Scripting](https://blogs.sap.com/2021/04/25/udfnodepool-functions-for-sap-cpi-with-groovy-scripting/)

In the part one, below are the list of B2B Node Pool functions discussed.

* createIfExistsAndHasValue

* createIfExistsAndHasOneOfSuchValues

* passIfExistsAndHasValue

* passIfExistsAndHasOneOfSuchValues

* existsAndHasValue

* existsAndHasOneOfSuchValues

* simpleUseOneAsMany

* deleteSuppress

* getFirstContextValue

* contextHasOneOfSuchValues

* assignValueByCondition

* getValueByIndex

In the current blog we will be going through the below B2B Node Pool functions.

* concatContextValues

* concatToOneQueue

* concatTwoQueuesToOne

* createMultipleCopies

* createMultipleContextCopies

* useOneContextAsMany

* suppressMultipleContextValues

* deleteMultipleContextValues

* simpleUseOneAsManyAndSplitByEachValue

* rearrangeByKey

**concatContextValues**:

![](/legacyfs/online/storage/blog_attachments/2023/07/Description-1.png)

```
import com.sap.gateway.ip.core.customdev.util.Message;

import com.sap.it.api.mapping.*;

def void concatContextValues(String[] Input, String[] Separator, Output output)

{

	StringBuilder result = new StringBuilder()

	String delimiter = Separator[0];

	if (Input[0] != null){

	    result.append(Input[0])

	}

	for (int i=1; i<Input.size();i++)

	{

    	if (Input[i] != null && Input[i].trim().length() > 0 && !output.isSuppress(Input[i]))

    	{

    	    result.append(delimiter).append(Input[i])

    	}

    	}

	result.toString()

	output.addValue(result)

}
```

![](/legacyfs/online/storage/blog_attachments/2023/07/Mapping-1.png)

![](/legacyfs/online/storage/blog_attachments/2023/07/DisplayQueue.png)

**concatToOneQueue:**

![](/legacyfs/online/storage/blog_attachments/2023/07/Description-2.png)

```
import com.sap.gateway.ip.core.customdev.util.Message;

import com.sap.it.api.mapping.*;

def void concatToOneQueue(String[] queue1, String[] queue2, String[] queue3, String[] queue4, String[] queue5, Output output) throws Exception{

                if (queue1 != null && queue1.length > 0) {

			for (int i = 0; i < queue1.length; i++) {

				output.addValue(queue1[i])

			}

		} else {

			output.addSuppress()

		}

		if (queue2 != null && queue2.length > 0) {

			for (int i = 0; i < queue2.length; i++) {

				output.addValue(queue2[i])

			}

		} else {

			output.addSuppress()

		}

		if (queue3 != null && queue3.length > 0) {

			for (int i = 0; i < queue3.length; i++) {

				output.addValue(queue3[i])

			}

		} else {

			output.addSuppress()

		}

		if (queue4 != null && queue4.length > 0) {

			for (int i = 0; i < queue4.length; i++) {

				output.addValue(queue4[i])

			}

		} else {

			output.addSuppress()

		}

		if (queue5 != null && queue5.length > 0) {

			for (int i = 0; i < queue5.length; i++) {

				output.addValue(queue5[i])

			}

		} else {

			output.addSuppress()

			}

}
```

![](/legacyfs/online/storage/blog_attachments/2023/07/Mapping-2.png)

![](/legacyfs/online/storage/blog_attachments/2023/07/DisplayQueue1.png)

![](/legacyfs/online/storage/blog_attachments/2023/07/DisplayQueue2.png)

Note: The code here has been written for five different queues, but we can edit to our convenience. For example, if you want to concat only two queues, you can refer the next function.

**concatTwoQueuesToOne:**

![](/legacyfs/online/storage/blog_attachments/2023/07/Description-3.png)

```
import com.sap.gateway.ip.core.customdev.util.Message;

import com.sap.it.api.mapping.*;

def void concatTwoQueuesToOne(String[] queue1, String[] queue2, Output output) throws Exception{

        if (queue1 != null && queue1.length > 0) {

			for (int i = 0; i < queue1.length; i++) {

				output.addValue(queue1[i])

			}

		} else {

			output.addSuppress()

		}

		output.addContextChange()

		if (queue2 != null && queue2.length > 0) {

			for (int i = 0; i < queue2.length; i++) {

				output.addValue(queue2[i])

			}

		} else {

			output.addSuppress()

		}

}
```

![](/legacyfs/online/storage/blog_attachments/2023/07/Mapping-3.png)

![](/legacyfs/online/storage/blog_attachments/2023/07/DisplayQueue-1.png)

**createMultipleCopies:**

![](/legacyfs/online/storage/blog_attachments/2023/07/Description-4.png)

```
import com.sap.gateway.ip.core.customdev.util.Message;

import com.sap.it.api.mapping.*;

def void createMultipleCopies(String[] contextValues, String[] copyCounts, Output output) throws Exception {

    if (contextValues == null || contextValues.length == 0) {

        throw new Exception("createMultipleCopies: contextValues is null or empty")

    }

    if (copyCounts == null || copyCounts.length != contextValues.length) {

        throw new Exception("createMultipleCopies: copyCounts is null or has a different length than contextValues")

    }

    for (int i = 0; i < contextValues.length; i++) {

        String value = contextValues[i]

        if (value != null && value.trim().length() > 0) {

            try {
...
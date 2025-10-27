---
title: How to pass parameter to the function from XML view
url: https://blogs.sap.com/2023/03/29/how-to-pass-parameter-to-the-function-from-xml-view/
source: SAP Blogs
date: 2023-03-30
fetch_date: 2025-10-04T11:06:38.239532
---

# How to pass parameter to the function from XML view

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* How to pass parameter to the function from XML vie...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161119&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to pass parameter to the function from XML view](/t5/technology-blog-posts-by-members/how-to-pass-parameter-to-the-function-from-xml-view/ba-p/13556559)

![shubham_c](https://avatars.profile.sap.com/5/c/id5c4c4a8afe8e41e5deeb2b2eb072dd77eff51a83d6b8a0e073e49a338ebb375f_small.jpeg "shubham_c")

[shubham\_c](https://community.sap.com/t5/user/viewprofilepage/user-id/125797)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161119)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161119)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556559)

‎2023 Mar 30
12:28 AM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161119/tab/all-users "Click here to see who gave kudos to this post.")

8,685

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [field masking for SAPUI5 and SAP Fiori](https://community.sap.com/t5/c-khhcw49343/field%2520masking%2520for%2520SAPUI5%2520and%2520SAP%2520Fiori/pd-p/73554900100800000794)
* [SAP Web IDE](https://community.sap.com/t5/c-khhcw49343/SAP%2520Web%2520IDE/pd-p/73554900100700001351)
* [User Interface](https://community.sap.com/t5/c-khhcw49343/User%2520Interface/pd-p/378427990965467211484671270864901)

* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAP Web IDE

  Software Product](/t5/c-khhcw49343/SAP%2BWeb%2BIDE/pd-p/73554900100700001351)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [User Interface

  Topic](/t5/c-khhcw49343/User%2BInterface/pd-p/378427990965467211484671270864901)
* [field masking for SAPUI5 and SAP Fiori

  field masking](/t5/c-khhcw49343/field%2Bmasking%2Bfor%2BSAPUI5%2Band%2BSAP%2BFiori/pd-p/73554900100800000794)

View products (5)

**Hello everyone**,

This is my first blog,

In it, I am about to explain How to pass the parameter to function in the controller from XML view in SAP UI5. I hope my blog will help.

most of the time we write separate (multiple) functions for performing actions based on how and where we are triggering the object or action. in simple words, we are passing the parameters to the function at the time function call.

let's create a scenario for it suppose we have two buttons one is **Save as Draft** and the second is **Submit**.

suppose on Save as draft we are sending the API call with Record id 1 and on Submit we are sending it with 0.

for these, we usually write two functions and write the other logic in the same manner.

but with the help of passing parameters to a function we can achieve it with a single function.

let's get started.

## 1. **Introduction**

Before starting let me explain why and in which case we can use these pass parameters from XML method. -

* To reduce the number of calls to internal functions which helps to achieve different conditions.

* function functionality is dependent upon a particular parameter.

* We can you this in functions in which logic is the same but depends on parameters conditions are changing and functionality is the same.

## 2. **Prerequisite**

* SAP UI5 version 1.56 and above.

* <https://sapui5.hana.ondemand.com/#/controls>

## 3. **Controller Code**

In the controller, we write the function logic and conditions required to perform the action as per the event triggered.

Here is one of the functions which perform the action required as per condition or parameter.

```
	onPressFun: function (oEvent, SecondPara, sActionValue) {

			var BtnEvent = oEvent.getSource();

			var SecondParameter = SecondPara;

			if (SecondParameter === "1") {

				sap.m.MessageBox.information(sActionValue);

			} else if (SecondParameter === "0") {

				sap.m.MessageBox.information(sActionValue);

			} else {

				sap.m.MessageBox.information("Wrong data Button event triggered");

			}

		}
```

## 4. **XML Code**

From the XML View function, we need to pass the parameter where we are calling the function like mentioned in below XML code.

with the help of parameter in function call we can avoid multiple functions which have the same logic but depends upon a different parameter.

See the code below:

```
<mvc:View controllerName="com.tc.xmlparameter.XMLParameter.controller.Worklist" xmlns="sap.m" xmlns:mvc="sap.ui.core.mvc"

	xmlns:semantic="sap.f.semantic">

	<semantic:SemanticPage >

		<semantic:content >

			<VBox class="sapUiLargeMargin">

				<HBox class="sapUiLargeMargin">

					<Button class="sapUiLargeMargin" text="Save as Draft" press="onPressFun($event ,'1','Saved')"/>

					<Button class="sapUiLargeMargin" text="Submit" press="onPressFun($event ,'0','Submitted')"/>

				</HBox>

			</VBox>

		</semantic:content>

	</semantic:SemanticPage>

</mvc:View>
```

* $event is passed as an event that triggers upon the button being clicked(oEvent).

* ' ' (single quotes) help to pass the parameter value as required.

* we can pass multiple parameters at a single time.

as you can see that we write the same function but can trigger a different condition which depends upon the parameter every time. it reduces internal function calls and helps to achieve code optimization.

passing parameters from a function can reduce the 'n' numbers of the internal function call.

## 5. **Output**

below I attaching the ScreenShot of the output.

First SS- when we press the save as draft button.

Second SS - when we press submit button.

![](/legacyfs/online/storage/blog_attachments/2023/03/Annotation-2023-03-30-011422.png)

Img for Save as Draft save

![](/legacyfs/online/storage/blog_attachments/2023/03/Annotation-2023-03-30-011521.png)

Image for Submit

## 6. **Conclusion**

From the above scenario, we learn how to pass the parameters to the function from the XML view in SAP UI5. in this we can add multiple parameters for multiple conditions, and with the help of the event we can also trigger the event handler.

It’s not that complex but very useful. I use it in some of my projects which helps me a lot to optimize my code and hope it can help others too.

If you are stuck between any topic feel free to ask and suggest to me to improve.

please share your feedback or thoughts in a comment.

Thank you, everyone, Happy learning!!!

*Regards,*

Shubham C

* [parameterisedfield](/t5/tag/parameterisedfield/tg-p/board-id/technology-blog-members)
* [sap.ui.core.mvc.XMLView](/t5/tag/sap.ui.core.mvc.XMLView/tg-p/board-id/technology-blog-members)
* [SAPUI5](/t5/tag/SAPUI5/tg-p/board-id/technology-blog-members)
* [xml](/t5/tag/xml/tg-p/board-id/technology-blog-members)
* [xmlview](/t5/tag/xmlview/tg-p/board-id/technology-blog-members)

2 Comments

You must be a registered user to add a comment. If you've...
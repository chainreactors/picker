---
title: XML To JSON conversion on SAP CI and JSON Conventions and why they are so Important!
url: https://blogs.sap.com/2023/01/28/xml-to-json-conversion-on-sap-ci-and-json-conventions-and-why-they-are-so-important/
source: SAP Blogs
date: 2023-01-29
fetch_date: 2025-10-04T05:07:38.147906
---

# XML To JSON conversion on SAP CI and JSON Conventions and why they are so Important!

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* XML To JSON conversion on SAP CI and JSON Conventi...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161073&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [XML To JSON conversion on SAP CI and JSON Conventions and why they are so Important!](/t5/technology-blog-posts-by-members/xml-to-json-conversion-on-sap-ci-and-json-conventions-and-why-they-are-so/ba-p/13556361)

![vinaymittal](https://avatars.profile.sap.com/a/6/ida67175bb9d6c01d6452c9710944c8e53c095e40f6e2c7452c5170cc2ba4afb02_small.jpeg "vinaymittal")

[vinaymittal](https://community.sap.com/t5/user/viewprofilepage/user-id/187725)

Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161073)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161073)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556361)

‎2023 Jan 28
5:14 PM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161073/tab/all-users "Click here to see who gave kudos to this post.")

2,313

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [SAP Process Integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Integration/pd-p/01200615320800000719)

* [SAP Process Integration

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BProcess%2BIntegration/pd-p/01200615320800000719)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (2)

## **Introduction**

We all have come across scenarios where while Integrating between SAP and third party systems we have to convert from

JSON to XML - So that SAP understands the JSON data being sent by the third party

or from

XML to JSON -so that the third party system that understands(or prefers to Understand) only JSON can consume the XML data being sent by SAP.

You should not do these conversions without knowing the supported JSON Conventions by the third party system and then comparing it with SAP CI standard JSON convention as it would be as ridiculous as generating a XSD out of an XML via same online tool.

SAP CI XML to JSON convertor by default supports Rabbit Fish Convention while most of the platforms accept Badger Fish JSON Convention.

## **Overview**

Let's understand and educate ourselves of the differences between the various JSON conventions.

There are 4 major JSON conventions

1. Badger Fish - Most popular but memory intensive in terms of storage

2. Rabbit Fish - Best representation of fields and Attributes

3. Ray Fish

4. Plain JSON

To understand the difference let's have a look at some examples

|
 **JSON Convention** |
 **JSON Representation** |
 **XML Data** |

|
 Badger Fish |
 ``` {  	"FirstLevel": {  		"@Source": "InService",  		"Task": {  			"@nodeAttribute": 234,  			"JobNumber": {  				"$": "J918290"  			},  			"JobDescription": {  				"$": "This is a temp job"  			},  			"LineOfBusiness": {  				"$": "Supply Restoration"  			},  			"TaskType": {  				"@elementAttribute": "eA",  				"$": "Miscellaneous"  			}  		}  	}  } ``` |
 ``` <FirstLevel Source="InService">  	<Task nodeAttribute="234">  		<JobNumber>J918290</JobNumber>  		<JobDescription>This is a temp job</JobDescription>  		<LineOfBusiness>Supply Restoration</LineOfBusiness>  		<TaskType elementAttribute ="eA">Miscellaneous</TaskType>  		  	</Task>  </FirstLevel> ``` |

|
 Rabbit Fish |
 ``` {  	"FirstLevel": {  		"@Source": "InService",  		"Task": {  			"@nodeAttribute": 234,  			"JobNumber": "J918290",  			"JobDescription": "This is a temp job",  			"LineOfBusiness": "Supply Restoration",  			"TaskType": {  				"@elementAttribute": "eA",  				"$": "Miscellaneous"  			}  		}  	}  }​ ``` |
 ``` <FirstLevel Source="InService">  	<Task nodeAttribute="234">  		<JobNumber>J918290</JobNumber>  		<JobDescription>This is a temp job</JobDescription>  		<LineOfBusiness>Supply Restoration</LineOfBusiness>  		<TaskType elementAttribute ="eA">Miscellaneous</TaskType>  		  	</Task>  </FirstLevel> ``` |

|
 Ray Fish |
 ``` {  	"#name": "FirstLevel",  	"#text": null,  	"#children": [  		{  			"#name": "@Source",  			"#text": "InService",  			"#children": []  		},  		{  			"#name": "Task",  			"#text": null,  			"#children": [  				{  					"#name": "@nodeAttribute",  					"#text": 234,  					"#children": []  				},  				{  					"#name": "JobNumber",  					"#text": "J918290",  					"#children": []  				},  				{  					"#name": "JobDescription",  					"#text": "This is a temp job",  					"#children": []  				},  				{  					"#name": "LineOfBusiness",  					"#text": "Supply Restoration",  					"#children": []  				},  				{  					"#name": "TaskType",  					"#text": "Miscellaneous",  					"#children": [  						{  							"#name": "@elementAttribute",  							"#text": "eA",  							"#children": []  						}  					]  				}  			]  		}  	]  } ``` |
 ``` <FirstLevel Source="InService">  	<Task nodeAttribute="234">  		<JobNumber>J918290</JobNumber>  		<JobDescription>This is a temp job</JobDescription>  		<LineOfBusiness>Supply Restoration</LineOfBusiness>  		<TaskType elementAttribute ="eA">Miscellaneous</TaskType>  		  	</Task>  </FirstLevel> ``` |

|
 Plain JSON |
 ``` {  	"FirstLevel": {  		"Source": "InService",  		"Task": {  			"nodeAttribute": 234,  			"JobNumber": "J918290",  			"JobDescription": "This is a temp job",  			"LineOfBusiness": "Supply Restoration",  			"TaskType": {  				"elementAttribute": "eA",  				"$": "Miscellaneous"  			}  		}  	}  }​ ``` |
 ``` <FirstLevel Source="InService">  	<Task nodeAttribute="234">  		<JobNumber>J918290</JobNumber>  		<JobDescription>This is a temp job</JobDescription>  		<LineOfBusiness>Supply Restoration</LineOfBusiness>  		<TaskType elementAttribute ="eA">Miscellaneous</TaskType>  		  	</Task>  </FirstLevel> ``` |

As you can see Rabbit Fish is the most meaningful and complete representation of attributes and nodes. The only possible way to achieve selective JSON to XML conversion is via XSLT mapping (for formats other than RabbitFish) as SAP CI only supports RabbitFish at the moment I hope that we should get radio buttons in the UI to chose the Convention soon.

If you would like to explore these JSON Conventions by converting your XML's to these JSON formats feel free to use this online tool that I built on [UtilityArena](https://www.utilityarena.com/XMLToJSONConvertor?initial)

PS: I have no idea why all the JSON Conventions end in the word "Fish".

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fxml-to-json-conversion-on-sap-ci-and-json-conventions-and-why-they-are-so%2Fba-p%2F13556361%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657D...
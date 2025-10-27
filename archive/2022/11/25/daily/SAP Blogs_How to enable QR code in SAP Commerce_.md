---
title: How to enable QR code in SAP Commerce?
url: https://blogs.sap.com/2022/11/24/how-to-enable-qr-code-in-sap-commerce/
source: SAP Blogs
date: 2022-11-25
fetch_date: 2025-10-03T23:44:02.360674
---

# How to enable QR code in SAP Commerce?

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [CRM and Customer Experience](/t5/crm-and-customer-experience/ct-p/crm)
* [CRM and CX Blog Posts by SAP](/t5/crm-and-cx-blog-posts-by-sap/bg-p/crm-blog-sap)
* How to enable QR code in SAP Commerce for an Omni-...

CRM and CX Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/crm-blog-sap/article-id/12992&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to enable QR code in SAP Commerce for an Omni-Channel experience?](/t5/crm-and-cx-blog-posts-by-sap/how-to-enable-qr-code-in-sap-commerce-for-an-omni-channel-experience/ba-p/13554598)

![rbhagat](https://avatars.profile.sap.com/6/8/id687a8fd23c1704bca3c59889869a3e12b03fcb84d5d62aaffa873da8e0779aef_small.jpeg "rbhagat")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[rbhagat](https://community.sap.com/t5/user/viewprofilepage/user-id/43758)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=crm-blog-sap&message.id=12992)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/crm-blog-sap/article-id/12992)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554598)

‎2022 Nov 24
1:26 PM

[8
Kudos](/t5/kudos/messagepage/board-id/crm-blog-sap/message-id/12992/tab/all-users "Click here to see who gave kudos to this post.")

2,901

* SAP Managed Tags
* [SAP Commerce](https://community.sap.com/t5/c-khhcw49343/SAP%2520Commerce/pd-p/67837800100800007216)
* [SAP Commerce Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Commerce%2520Cloud/pd-p/73555000100800001224)

* [SAP Commerce

  SAP Commerce](/t5/c-khhcw49343/SAP%2BCommerce/pd-p/67837800100800007216)
* [SAP Commerce Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BCommerce%2BCloud/pd-p/73555000100800001224)

View products (2)

*In this blog I would like to showcase how I created capability to generate a Barcode of QR code type and how you can use similar steps to enable and generate QR codes in SAP commerce.*

Barcodes are used to convey information visually. We'll most likely provide an appropriate barcode image in a web page, email, or a printable document.

**QR(Quick Response) Codes** are becoming the most widely recognised 2D barcodes worldwide.

The big benefit of the QR code is that **we can store large amounts of data in a limited space.**

**Business Use Case** : *Creating an Omni-Channel Experience where we can scan QR code and navigate to PDP page on mobile devices.
This can be extended to attach QR code with In-store products and navigate directly to online store creating a seamless experience.*

**Technical Use Case** : *Generate a QR code on Product details page(PDP) which can be scanned using a Barcode/QR code scanner on mobile device in order to navigate PDP from your website/In-store product to mobile device, creating an omni-channel experience.*

> **Note** : *For simplicity purpose I have used link of PDP inside a QR code although you can have any type of link like a Wishlist or paragraph information as well concealed in it.*

### **Technical Details:**

### **Pre-requisite/Setup:**

I have created myprojectstorefront using modulegen and enabled Electronics storefront in my local system for demo.
*In case you want to understand how modulegen is used to generate electronics storefront please check this SAP Help page:* [Customizing the B2C Accelerator to Have B2B and B2C Storefronts](https://help.sap.com/docs/SAP_COMMERCE/4c33bf189ab9409e84e589295c36d96e/6b3c400939a046cd9ff4b80bf6ab6d80.html?version=2011&locale=en-US)

**Barcode Library Used**

I have used the following  Open Source Java Barcode Libraries can be used to generate barcodes in custom extension in SAP commerce:

* **Barcode4j :** *It offers 2D barcode formats – like QR code , DataMatrix and PDF417 – and more output formats.*

**Note**: *There are other open source libraries such as ZXing also available at your disposal to accomplish similar task, but for out article we are going forward with Barcode4j.*

### Solution:

* Add **Barcode4j** library to ****external-dependencies.xml of myprojectfacades****as shown below code snippet:

  ```
          <dependency>

  		    <groupId>net.sf.barcode4j</groupId>

  		    <artifactId>barcode4j</artifactId>

  		    <version>2.1</version>

  		</dependency>
  ```

  **Important** : To generate barcode4j.2.1.jar on ant build you need to make sure that ***usemaven="true" in /*****myprojectfacades*****/extensioninfo.xml.***

  Result : Run ant clean all and you should be able to see barcode4j.2.1.jar in lib folder in lib folder.

* **Generate QR code On Load of Product data**
  Generate QR code in myprojectFacades extension by creating *Custom Facade and extending DefaultProductFacade<ProductModel>* and over-ridding ***getProductForCodeAndOptions*** function.

* Create a ***BarcodeMediaModel*** ( which is an Out-of-Box(OOB) Model provided in SAP Commerce ) on load of each product and add link of product as data of QR code to be scanned.

* ***Assign that BarcodeMediaModel  to ProductModel****I have added new attribute to store barcode media model in myprojectcore-items.xml for* product model.
  Below is code snippet for the same:

  ```
  <attribute autocreate="true" qualifier="productQRCode" type="BarcodeMedia">

  					<modifiers read="true" write="true" search="false"

  						optional="true" />

  					<persistence type="property" />

  				</attribute>
  ```

  ***IMPORTANT**: Please run System update after this change*.

* ***Populate and Show BarcodeMediaModel to Frontend PDP page*** by adding it to ProductData by *converting BarcodeMediaModel to MediaData using OOB mediaModelConverter*
  as shown below.

* ***Custom Java Code Snippet:***

```
public class CustomProductFacade extends DefaultProductFacade<ProductModel>

{

	private static final Logger LOG = Logger.getLogger(CustomProductFacade.class);

	@Resource(name = "mediaService")

	MediaService mediaService;

	@Resource(name = "mediaModelConverter")

	Converter<MediaModel, MediaData> mediaModelConverter;

	@Override

	public ProductData getProductForCodeAndOptions(final String code, final Collection<ProductOption> options)

	{

		final ProductModel productModel = getProductService().getProductForCode(code);

		try

		{

			if (null == productModel.getProductQRCode())

			{

				final BufferedImage QRImage = this.generateQRCodeImage("https://localhost:9002/myprojectstorefront/en/USD/p/" + code);

				LOG.info("finished generateQRCodeImage  ");

				final String filePath = "productQRCode.png";

				final int size = 125;

				final File qrFile = new File(filePath);

				final ByteArrayOutputStream outputStream = new ByteArrayOutputStream();

				ImageIO.write(QRImage, "png", outputStream); // Passing: ​(RenderedImage im, String formatName, OutputStream output)

				final InputStream inputStream = new ByteArrayInputStream(outputStream.toByteArray());

				LOG.info("Created Input stream  ");

				final BarcodeMediaModel barcodeMediaModel = getModelService().create(BarcodeMediaModel.class);

				barcodeMediaModel.setCatalogVersion(productModel.getCatalogVersion());

				barcodeMediaModel.setCode("productQRCode" + productModel.getCode());

				barcodeMediaModel.setRealFileName("productQRCode" + productModel.getCode() + ".png");

		...
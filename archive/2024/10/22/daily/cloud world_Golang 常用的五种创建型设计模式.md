---
title: Golang 常用的五种创建型设计模式
url: https://cloudsjhan.github.io/2024/10/21/Golang-%E5%B8%B8%E7%94%A8%E7%9A%84%E4%BA%94%E7%A7%8D%E5%88%9B%E5%BB%BA%E5%9E%8B%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F/
source: cloud world
date: 2024-10-22
fetch_date: 2025-10-06T18:50:23.545727
---

# Golang 常用的五种创建型设计模式

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## Golang 常用的五种创建型设计模式

posted

2024-10-21

|

visitors:

|

|

wordcount:

1,700
|

min2read ≈

8

![](https://)

在 Go 中，创建设计模式有助于管理对象的创建，并控制对象的实例化方式。这些模式在对象创建过程复杂或需要特殊处理时特别有用。以下是 Go 中常用的主要创建模式：

### 单例模式

单例模式确保一个类只有一个实例，并提供一个全局访问点。

#### 如何实现

1. 定义一个结构，并将其作为单个实例。
2. 为该结构创建一个全局变量，但不要立即将其初始化。
3. 使用 sync.Once 确保实例只创建一次，即使在多线程情况下也是如此。
4. 提供一个全局函数来返回实例。

以下是实现单例模式的基本示例:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 ``` | ``` package main  import (  "fmt"  "sync" )  type (  singleton struct {   data string  } )  var instance *singleton var once sync.Once  // Function to return the single instance func GetInstance() *singleton {  // Use sync.Once to ensure the instance is created only once  once.Do(func() {   instance = &singleton{data: "This is a singleton"}  })   return instance }  func main() {  s1 := GetInstance()  s2 := GetInstance()   // Both should point to the same instance  fmt.Println(s1 == s2) // true  fmt.Println(s1.data)  // "This is a singleton" } ``` |

sync.Once 可确保实例只创建一次，即使在并发调用 GetInstance 的情况下也是如此。

### 工厂方法模式

工厂方法模式定义了创建对象的接口，但允许子类改变将创建的对象类型。在 Go 中，这可以通过创建工厂函数来实现。这种设计模式提供一种将实例化逻辑委托给子类的方法，从而可以灵活地创建对象。

实现步骤：

1. 创建一个为不同对象定义通用行为的接口。
2. 创建多个实现此接口的结构体。
3. 创建一个函数（工厂方法），接收一些输入（如类型）并返回相应结构的实例。

以下是实现工厂方法模式的基本示例:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 ``` | ``` package main  import (  "fmt" )  type Animal interface {   Speak() string  }   Dog struct{}  Cat struct{} )  func (d Dog) Speak() string {  return "Woof!" }  func (c Cat) Speak() string {  return "Meow!" }  func AnimalFactory(animalType string) Animal {  if animalType == "dog" {   return &Dog{}  } else if animalType == "cat" {   return &Cat{}  }  return nil }  func main() {  dog := AnimalFactory("dog")  fmt.Println(dog.Speak()) // Woof!   cat := AnimalFactory("cat")  fmt.Println(cat.Speak()) // Meow! } ``` |

工厂方法允许创建不同类型的对象，但用户端隐藏了创建逻辑。当对象创建过程比较复杂，需要进行抽象时，这种模式尤其有用。

### 抽象工厂模式

抽象工厂（Abstract Factory）提供了一个接口，用于创建相关或依赖对象的族，而无需指定它们的具体类。在 Go 中，可以通过定义不同的工厂接口来实现它。

当系统需要独立于其对象的创建、组成和表示方式时，它就非常有用。它允许创建相关对象族。

以下是实现抽象工厂模式的基本示例:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 ``` | ```  package main  import (  "fmt" )  // Define an abstract factory type (  GUIFactory interface {   CreateButton() Button   CreateCheckbox() Checkbox  } )  // Define interfaces for products type (  Button interface {   Press() string  }   Checkbox interface {   Check() string  }   // Implement concrete products for Windows  WindowsButton   struct{}  WindowsCheckbox struct{}   // Implement concrete products for Mac  MacButton   struct{}  MacCheckbox struct{}   // Implement factories for each platform  WindowsFactory struct{}  MacFactory     struct{} )  func (w *WindowsButton) Press() string { return "Windows Button Pressed" }  func (w *WindowsCheckbox) Check() string { return "Windows Checkbox Checked" }  func (m *MacButton) Press() string { return "Mac Button Pressed" }  func (m *MacCheckbox) Check() string { return "Mac Checkbox Checked" }  func (w *WindowsFactory) CreateButton() Button     { return &WindowsButton{} } func (w *WindowsFactory) CreateCheckbox() Checkbox { return &WindowsCheckbox{} }  func (m *MacFactory) CreateButton() Button     { return &MacButton{} } func (m *MacFactory) CreateCheckbox() Checkbox { return &MacCheckbox{} }  func main() {  // Get a Windows factory  var wf GUIFactory = &WindowsFactory{}  button := wf.CreateButton()  checkbox := wf.CreateCheckbox()   fmt.Println(button.Press())   // Output: Windows Button Pressed  fmt.Println(checkbox.Check()) // Output: Windows Checkbox Checked   var mf GUIFactory = &MacFactory{}  button = mf.CreateButton()  checkbox = mf.CreateCheckbox()   fmt.Println(button.Press())   // Output: Mac Button Pressed  fmt.Println(checkbox.Check()) // Output: Mac Checkbox Checked } ``` |

### Builder 模式

构建器模式将复杂对象的构建与其表示分离开来，允许同一构建过程创建不同的表示。它能解决问题：复杂的对象通常是一步一步构建的。构建器模式为创建此类对象提供了灵活的解决方案，分解了实例化过程。

以下是实现构建器模式的基本示例:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 ``` | ``` package main  import (  "fmt" )  // Product to be built type House struct {   windows string   doors   string   roof    string  }   // Concrete builder for a villa  type VillaBuilder struct {   house House  }   // Director controls the building process  type Director struct {   builder HouseBuilder  } )  // Builder interface type HouseBuilder interface {   SetWindows() HouseBuilder   SetDoors() HouseBuilder   SetRoof() HouseBuilder   Build() *House  }   func (v *VillaBuilder) SetWindows() HouseBuilder {  v.house.windows = "Villa Windows"  return v }  func (v *VillaBuilder) SetDoors() HouseBuilder {  v.house.doors = "Villa Doors"  return v }  func (v *VillaBuilder) SetRoof() HouseBuilder {  v.house.roof = "Villa Roof"  return v }  func (v *VillaBuilder) Build() *House {  return &v.house }  func (d *Director) Construct() *House {  return d.builder.SetWindows().SetDoors().SetRoof().Build() }  func main() {  director := &Director{}   // Build a villa  v_builder := &VillaBuilder{}  director.builder = v_builder  villa := director.Construct()  fmt.Println(*villa) // Output: {Villa Windows Villa Doors Villa Roof} } ``` |

在创建需要大量可选配置的复杂对象时，创建者模式非常有用。

### 原型模式

原型模式允许通过复制现有对象（原型）来创建新对象，而不是从头开始创建。
当创建一个新对象的成本很高，而现有对象又可以克隆重用时，原型模式就派上用场了。

以下是实现原型模式的基本示例

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 ``` | ``` package main  import (  "fmt" )  // Cloneable interface type (  Cloneable interface {   Clone() Cloneable  } )  // Concrete struct (prototype) type (  Product struct {   name     string   category string  } )  // Clone method creates a copy of the Product func (p *Product) Clone() Cloneable {  return &Product{name: p.name, category: p.category} }  func (p *Product) SetName(name string) {  p.name = name }  func (p *Product) GetDetails() string {  return fmt.Sprintf("Product Name: %s, Category: %s", p.name, p.category) }  func main() {  // Original product  original := &Product{name: "Phone", category: "Electronics"}  fmt.Println(original.GetDetails()) // Output: Product Name: Phone, Category: Electronics   // Clone the product and change its name  cloned := original.Clone().(*Product)  cloned.SetName("Smartphone")  fmt.Println(cloned.GetDetails()) // Output: Product Name: Smartphone, Category: Electronics } ``` |

当创建对象的成本很高，而你又想通过复制现有对象来创建多个类似对象时，原型模式就很有效。这种模式通过克隆现有实例来简化对象的创建，而不是从头开始创建新实例。

### 总结

每种模式都有其特定的用例，选择恰当的设计模式会使代码更有条理、可重用且更易于维护！

---

-------------The End-------------

Title:[Golang 常用的五种创建型设计模式](/2024/10/21/Golang-%E5%B8%B8%E7%94%A8%E7%9A%84%E4%BA%94%E7%A7%8D%E5%88%9B%E5%BB%BA%E5%9E%8B%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F/)

Author:[cloud sjhan](/ "visit cloud sjhan blog")

Publish Time:2024年10月21日 - 14:10

Last Update:2024年10月21日 - 14:10

Original Link:[https://cloudsjhan.github.io/2024/10/21/Golang-常用的五种创建型设计模式/](/2024/10/21/Golang-%E5%B8%B8%E7%94%A8%E7%9A%84%E4%BA%94%E7%A7%8D%E5%88%9B%E5%BB%BA%E5%9E%8B%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F/ "Golang 常用的五种创建型设计模式")

License: [By-NC-ND 4.0 international](https://creativecommons.org/licenses/by-nc-nd/4.0/ "Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)")。

![cloud sjhan wechat](/images/wechat-qcode.jpg)

keep going, keep coding

donate

![cloud sjhan 微信支付](/images/wechatpay.jpg)

微信支付

![cloud sjhan 支付宝](/images/alipay.jpg)

支付宝

[Go](/tags/Go/)

(>给这...
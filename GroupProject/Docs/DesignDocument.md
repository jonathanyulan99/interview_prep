# Design Document

**Author**: Team1
**Written By**: Davron Ochilov, Lin Shi, Jonathan Yulan

## 1 Design Considerations

### 1.1 Assumptions

Team 1's Android application is designed to be supported by: Nougat, version 7.1, API level 25. Running the application on an older version API may produce significant bugs and errors causing the application to fail. The application will make use of the "The Room" persistence library, which is an abstraction layer over SQLite. Applicaiton will be scripted in primarily Java, as the SQLite implementation can bind.The architecture component Room, requires a working knowledge of the SQLite database, and the SQLite query language.  

### 1.2 Constraints

Use of the "Room" persistence library will save all of our application related data in a local database, on the android mobile device itself. The application should not require complex queries, or have a need for sophisticated forms of concurrency. The application required the ability to add items, item types and hold multiple different list. The application required us to implement a hierachial structure based on items and item types. In addition the applicaiton will display items by type in a container, which will require the use of this library. 

### 1.3 System Environment

The application will be designed and only functional with a cellular device running Nougat. This application will require the device to be able to input keystrokes, as a way of communicating with the application. The use of the Room persistence library will require the cellular device to have a certain amount of memory in order for the database functionality to be operational. Due to our embedded client-side database, not having enough memory on the android device may cause certain functionality, specific to the database, to fail. 

## 2	Architectural Design

### 2.1	Component Diagram

![component diagram](https://i.imgur.com/wdAeyUp.png)

We created 5 components. User Interface component depends on ListHolder component. GroceryList Management and GroceryItem Management components provide interfaces for listHolder component to manipulates list and creates newItem. Database component provides interface for GroceryItem Management component to search items. The implementation of GroceryList Management component depends on GroceryItem Management and Database component.

### 2.2	Deployment Diagram

![deployment diagram](https://i.imgur.com/PfD5NxB.png)

We designed 3 parts for deployment diagram. The implementation of User Interface bases on Application Functions part. Application Functions collects all manipulations of GroceryLists and GroceryItems by ListHolder, for example, component ListHolder contains method like createList, component GroceryList Management contains method like addItem, component GroceryItem Management contains method like setQty for a item. Application Functions connects to Database Server, which provides supports for new item creation, looking up items and so on.

## 3	Low-Level Design

### 3.1	Class Diagram

![class diagram](https://i.imgur.com/YLdfmaw.png)

Team 1's class diagram represents all the necessary functions, attributes and relationships required for the application to function as intended. The simplicity of the relationships and overall design were intended with a server-side client database in mind. The *ListHolder* class will manage all the instances of the different *GroceryList*s) that our user creates. The design indicates that *ListHolder* can contain zero or many instances of *GroceryList*, and all instances of *GroceryList* are associated with one(1) *ListhHolder*. The same relationship design is applied to all aspects of Team 1's class diagram. Specifically between *GroceryList* and *GroceryItem*; and then again between *GroceryItem* and *GroceryItemType*. This is intended as a way to implement a simple, client-side database schema to our application. One that is intended to not be memory intensive, with our client's mobile storage in mind. 

### 3.2	Other Diagrams

#### Database Diagram

![database diagram](https://i.imgur.com/VwAReky.png)

Team 1's database diagram; Integration of a client-side database and our **GroceryList Application**. The overall design of our application's database is simple, this was intended as to keep the user's device memory in mind. Team 1's database design accomplishes all necessary requirments; it allows the user to create multiple different grocery list(s) that are able to be sorted via grocery type, and item. This funtionality is accomplished by the use of foreign keys that ensure said relationships as laid out in our design our enforced. The database design indicates all of the necessary entity-relationship(s), as well as the labeling of all necessary keys(primary,foreign). The GList entity will make up all of the objects that the ListHolder class works on. 

#### Sequence Diagram

![sequence diagram](https://raw.githubusercontent.com/jonathanyulan99/Assignment5/main/Sequence%20Diagram.jpeg)

The GroceryList application's typical sequence of events is depicted through the above sequence diagram. The application was created for the use of only one user. The above diagram captures only the typical sequence of events that would occur in our application, and does not represent every possible sequence that can occur. 

## 4	User Interface Design

![ui diagram](https://imgur.com/fuTGLb1.png)
![ui diagram](https://imgur.com/zvnV8Cx.png)
![ui diagram](https://imgur.com/vcRGURJ.png)
![ui diagram](https://imgur.com/vehpV2w.png)

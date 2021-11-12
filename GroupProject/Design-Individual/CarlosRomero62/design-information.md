# Assignment 5: Software Design
**Note: getters and setters are assumed to exist for all classes and their attributes**

1. A grocery list consists of items the users want to buy at a grocery store. The application must allow users to add items to a list, delete items from a list, and change the quantity of items in the list (e.g., change from one to two pounds of apples).
To start off the application, I added a class named GroceryList. This class contains the methods **addItem**, to add items to the grocery list, **removeItem** to remove items from the list, and **changeQuantity** to change the quantity of a specific item on the list.
2. The application must contain a database (DB) of items and corresponding item types.
Before getting to the database, I created classes **Item** and **ItemType**. **ItemType** has the attribute **typeName** which will hold the name of the item type. The **Item** class is a child of the **ItemType** class. This class has the attributes **itemName** for the name of the item and **byWeight** to point out if the quantity of the item is measured by the weight of the item. I created a class called **Database** that acts as a database of the items that can be placed in the grocery list. **Database** is a collection of **Items**.
3. Users must be able to add items to a list by picking them from a hierarchical list, where the first level is the item type (e.g., cereal), and the second level is the name of the actual item (e.g., shredded wheat). After adding an item, users must be able to specify a quantity for that item.
The hierarchical list is addressed by the structure of **Item** and **ItemType**. How exactly the items to be added to the list are located does not affect the design. The only change made is adding parameters to the **addItem** method in the **GroceryList** class. The method will take in the item and an interger amount for the quantity of that item.
4. Users must also be able to specify an item by typing its name. In this case, the application must look in its DB for items with similar names and ask the users, for each of them, whether that is the item they intended to add. If a match cannot be found, the application must ask the user to select a type for the item and then save the new item, together with its type, in its DB.
Most of this does not affect the design but a new method is added to the **Database** called **newDBEntry**. This will allow the user to add a new item to the DB if they could not find it when trying to add an item to the grocery list.
5. Lists must be saved automatically and immediately after they are modified.
This does not affect the design directly.
6. Users must be able to check off items in a list (without deleting them).
This brings a couple of changes. The **GroceryList** class gets it's first attribute, **listEntry**, who's type is a new class named **GroceryEntry**. GroceryEntry is an association class for the association between Database and GroceryList that was not stated before. This class will have the attributes **itemWanted** for the item that the person is putting into their list, **quantity** for the how much of that item they plan on buying, and **checkOff** which is a Boolean to signify if the item was checked off the user's list. In the GorceryList class, we add a new method **checkItem** which will ask the user to name the item they want checked off the list.
7. Users must also be able to clear all the check-off marks in a list at once.
I added a method in GroceryList, **clearChecks**, that will clear off all the checks on the list.
8. Check-off marks for a list are persistent and must also be saved immediately.
Does not affect the design directly.
9. The application must present the items in a list grouped by type, so as to allow users to shop for a specific type of product at once (i.e., without having to go back and forth between aisles).
This also does not affect the design directly.
10. The application must support multiple lists at a time (e.g., “weekly grocery list”, “monthly farmer’s market list”). Therefore, the application must provide the users with the ability to create, (re)name, select, and delete lists.
To allow the creation of multiple lists, **GroceryList** now has the attribute **listName** to differentiate the lists. To allow renaming a list, the method **renameList** is introduced. Creation and deletion of a list does not affect the design directly.
11. The User Interface (UI) must be intuitive and responsive.
This does not affect the design directly.
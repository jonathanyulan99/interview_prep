Jonathan Yulan CS 370 ASSIGNMENT 5 design-information.pdf

1. A grocery list consists of items the users want to buy at a grocery store. The application must allow users to add items to a list, delete items from a list, and change the quantity of items in the list (e.g., change from one to two pounds of apples).

I implemented this requirment by creating the main groceryList class which has methods to: 1) addItem(item_Name) 2) deleteItem(item_Name) 3) editItem(item_Name) 4) checkOffItem(item_Name) and finally 5) to clearCheckOff(). The 4th and 5th method respectively allow the user to check off the items on the groceryList as they obtain such items and also the ability to clear all the checks via the clearCheckOff method.

2. The application must contain a database (DB) of items and corresponding item types.

I implemented this via the Database structure in my UML model, in order to utilize the database that contains not only all the grocery specific items but also the groceryList(s) that can be instantiated by the user.

3. Users must be able to add items to a list by picking them from a hierarchical list, where the first level is the item type (e.g., cereal), and the second level is the name of the actual item (e.g., shredded wheat). After adding an item, users must be able to specify a quantity for that item.

The user utilizes the addItems(item_Name) method; which add items labeled as 'item_name' but the item class is the 2nd level and it's type is inherited via the 'itemType' class which allows users to create categories of itemTypes(e.g...Milk, Cereal, Bread) into the Database that is labeled/modeled in the UML here. The user is able to categorize their groceries('item' class) and create newItems and inehrit the itemType from the itemTypeSet class.

4. Users must also be able to specify an item by typing its name. In this case, the application must look in its DB for items with similar names and ask the users, for each of them, whether that is the item they intended to add. If a match cannot be found, the application must ask the user to select a type for the item and then save the new item,together with its type, in its DB.

This functionality is not one that needs to be fully implemented/featured in the UML as this is more of a user interface feature that works with the back-end database of all the groceryList and groceryItems. We have shown the searchItems(item_Name) which will utilize the groceryListview to search for the items represented in the DB and with the UI functionality that is described here (the finishing and auto complete feature of the DB).

5. Lists must be saved automatically and immediately after they are modified.

Once a groceryList is instantiated via the groceryList() class, the creation,replacment, update, deletion (CRUD) updates for the database are made. Thus the database not only holds the specific items, itemTypes but also in addition the list that are created via the user.

6. Users must be able to check off items in a list (without deleting them).

We have added the boolean(1/0) primitive to the declared attribute isChecked, which is represented in the 2nd level of the hierarchy view and the item class.

7. Users must also be able to clear all the check-off marks in a list at once.

There is a method in the groceryList class called +clearCheckOff() which doesn't take any parameters and its only job is it remove the check-off marks of the items in the specific groceryList object.

8. Check-off marks for a list are persistent and must also be saved immediately.

the +isChecked:boolean attribute of our 'item' class is carried with the itemType class that populates the groceryList class. As soon as the groceryList is created with the item_Names those items are create, read, update or delete as the groceryList is instantiated with the objects of the item class.

9. The application must present the items in a list grouped by type, so as to allow users to shop for a specific type of product at once (i.e., without having to go back and forth between aisles).

Another User Interface feature that needs implementing but not necessarily represented in the UML. This feature is somewhat intutive as the item object has a itemType which the item class inherits thorugh the itemType class. This implies that the item needs to be grouped or charcterized with a specific itemType which can be set through the itemTypeSet class, which is the class that contains the method addItemType(itemType).

10. The application must support multiple lists at a time (e.g., “weekly grocery list”, “monthly farmer’s market list”). Therefore, the application must provide the users with the ability to create, (re)name, select, and delete lists.

Our groceryListView class is all the collection of all the user created objects of the groceryList objects. This will inevitable have to include the list as well as the items_Names(attribute) and the item_Types which are necessary and inherited from the itemType to the item class. We have implemented the groceryList class with the following methods...

i. createg_List(listName)
ii. renameg_List(listName, newListName)
iii. deleteg_List(listName)
iv. searchItems(item_Name) which returns the items represented/found in our DB. This DB will update, as needed and can be updated through the creatNewItem() method in the itemType class as well through the addItemType() method found in the itemTypeSet class.

11. The User Interface (UI) must be intuitive and responsive.

This is another User Interface requriment that really isn't meant to be displayed or shown on a UML. The User Interface should always aim to be intutive and responsive which is why software engineers go to great lengths to set up the system properly in order to implment, adapt, scale and re-innovate as needed.
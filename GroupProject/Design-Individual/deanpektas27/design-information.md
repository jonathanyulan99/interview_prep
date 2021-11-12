# Assignment 5 Design information by Dean Pektas

1. ***A grocery list consists of items the users want to buy at a grocery store. The application must allow users to add items to a list, delete items from a list, and change the quantity of items in the list (e.g., change from one to two pounds of apples).***

   ​	The class "**GroceryList**" was created to allow for management of a grocery list and adds the key functions as requested, including adding and deleting items as well as changing the quantity per item. A class called "**Item**" is attached to the GroceryList class to allow it to be added to the list and it specifies the components of an item in the list, including the name of the item, a check mark and the quantity of that item.

2. ***The application must contain a database (DB) of items and corresponding item types.***

   ​	This was not and does not need to be addressed in the UML diagram.

3. ***Users must be able to add items to a list by picking them from a hierarchical list, where the first level is the item type (e.g., cereal), and the second level is the name of the actual item (e.g., shredded wheat). After adding an item, users must be able to specify a quantity for that item.***

   ​	A class called **TypeOfItem** and **SpecificType** are created to allow for different types of items to be added to this list.

4. ***Users must also be able to specify an item by typing its name. In this case, the application must look in its DB for items with similar names and ask the users, for each of them, whether that is the item they intended to add. If a match cannot be found, the application must ask the user to select a type for the item and then save the new item, together with its type, in its DB.***

   ​	The class **Item** includes a Name string that allows for specifying the item a user wants by its name.

5. ***Lists must be saved automatically and immediately after they are modified.***

   ​	This was not and does not need to be addressed in the UML diagram.

6. ***Users must be able to check off items in a list (without deleting them).***

   ​	The **Item** class includes the ability to check off an item if needed with **isCheckMarked**.

7. ***Users must also be able to clear all the check-off marks in a list at once.***

   ​	The **GroceryList** method includes a method called **ClearAllChecks** that allows for all check marks to be removed at once.

8. ***Check-off marks for a list are persistent and must also be saved immediately.***

   ​	This was not and does not need to be addressed in the UML diagram.

9. ***The application must present the items in a list grouped by type, so as to allow users to shop for a specific type of product at once (i.e., without having to go back and forth between aisles).***

   ​	This was not and does not need to be addressed in the UML diagram.

10. ***The application must support multiple lists at a time (e.g., “weekly grocery list”, “monthly farmer’s market list”). Therefore, the application must provide the users with the ability to create, (re)name, select, and delete lists.***

    ​	Multiple lists can be created using the **CreateList** method as they have their own individual names that can be attached to each list.

11. ***The User Interface (UI) must be intuitive and responsive.***

    ​	This was not and does not need to be addressed in the UML diagram.


# GroceryListManager

## Requirements

1. A grocery list consists of items the users want to buy at a grocery store. The application must allow users to add items to a list, delete items from a list, and change the quantity of items in the list (e.g., change from one to two pounds of apples).

   **Required: To realize this requirement, I created User Class and GroceryList Class and GroceryItem Class. A groceryItem can be created in GroceryItem Class. I added to the design a Class GroceryList with private attrribute listName. In Class GroceryList, user can add items to a list by passing GroceryItem to function addItem(), can delete items from a list by passing the groceryItem name and the function deleteItem(String) returns the groceryItem deleted, can change the quantity of items in the list by passing the changing groceryItem and new quantity to function changeQty(GroceryItem, int), then this function will call another function setQty(int) in Class GroceryItem to finish qty setting.**

   

   **Optional: I added getListName(), which returns the GroceryList name in String type. Function setListName(String) can set the name of a groceryList**

   

2. The application must contain a database (DB) of items and corresponding item types.

   **To realize this requirement, I created Class GroceryDB. The database will be used later to look up items or show all available items by GroceryList when adding items to the groceryList.**

   

3. Users must be able to add items to a list by picking them from a hierarchical list, where the first level is the item type (e.g., cereal), and the second level is the name of the actual item (e.g., shredded wheat). After adding an item, users must be able to specify a quantity for that item.

   **To satisfy this requirement, I added to the design a Class ItemType with private attribute name. In GroceryDB Class, I added private attributes groceryItems and itemTypes both in array type. When the user look up one item in hierarchical list, function getAllItemTypes() return a itemType array which includes all itemTypes. Then the user can get a groceryItem array which includes all items inside this itemType by passing a itemType to function getItemOfType(ItemType).**

   

4. Users must also be able to specify an item by typing its name. In this case, the application must look in its DB for items with similar names and ask the users, for each of them, whether that is the item they intended to add. If a match cannot be found, the application must ask the user to select a type for the item and then save the new item,
   together with its type, in its DB.

   **To realize this requirement, I added function lookUpItemByName(String) to GroceryDB Class. By passing the item name in String type, the function gives groceryItems with similar names. And if no such items found, function addItem(String, String) can be used to add a new item by passing a new itemName with its itemType to database.**

   

5. Lists must be saved automatically and immediately after they are modified.

   **To fullfill this requirement, I added saveList(GroceryList) method in User Class, which should be automatically called after groceryList modification.**

   

6. Users must be able to check off items in a list (without deleting them).

   **To realize this requirement, I added private attribute checked in boolean type and a function setChecked(Boolean) in GroceryItem Class. I also added checkOffItem(String) function in GroceryList Class. When user checks off items in a list, checkOffItem(String) is called by passing the name of a item, then setChecked(Boolean) is called to finish setting the status of that item.**

   

7. Users must also be able to clear all the check-off marks in a list at once.

   **To realize this requirement, I added clearAllChecks() function in GroceryList Class which can clear all marks at once.**

   

8. Check-off marks for a list are persistent and must also be saved immediately.

   **This can be implemented by automatically calling the function saveList(GroceryList) in User Class.**

   

9. The application must present the items in a list grouped by type, so as to allow users to shop for a specific type of product at once (i.e., without having to go back and forth between aisles).

   **To implement this feature, I designed to add groupItemByType() function in GroceryList Class. This function should sort the items by types.**

   

10. The application must support multiple lists at a time (e.g., “weekly grocery list”, “monthly farmer’s market list”). Therefore, the application must provide the users with the ability to create, (re)name, select, and delete lists.

    **Required: In order to satisfy this requirement, I added some functions in User Class. User can create a groceryList by passing a groceryList to createList(GroceryList), can rename a groceryList by passing a groceryList and its new name to renameList(GroceryList, String), can select a groceryList by passing its name to selectList(String), can delete a groceryList by passing a groceryList to deleteList(GroceryList).**

    

    **Optional: I added userId as a private attribute in User Class, which can ensure users' uniqueness. In GroceryItem Class, function getName() can be used to return the name of a item in String type. Function getType() return the ItemType of a item. Function getQty() can be used to check the quantity of current item in a groceryList.**

    

11. The User Interface (UI) must be intuitive and responsive.

    **Not considered because it does not affect the design directly.**

## Relationships In My Design

Aggregation between User & GroceryList. One user can have 0..many groceryLists. One groceryList only belongs to one user.

Aggregation between GroceryList & GroceryItem. One groceryList can include 0..many groceryItems. One groceryItem may occur in 0..many groceryLists.

Association between GroceryItem & ItemType. One GroceryItem only has one itemType.

Dependency between GroceryDB & GroceryList. Class GroceryList uses GroceryDB to add items to a groceryList.

Dependency between GroceryDB & GroceryItem & ItemType. Class GroceryItem and Class ItemType are used by GroceryDB when calling getAllItemTypes() and other functions.
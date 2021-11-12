# Use Case Model

## 1 Use Case Diagram

![](https://i.imgur.com/D5fArYP.png)

## 2 Use Case Descriptions

**Requirements**: The app must allow the user to do most of the functions that are listed in the requirements. To begin with, the application must allow the user to create one or more shopping lists. The user should also be able to select which lists they want to interact with. The user must also be able to delete lists they no longer want, and rename existing lists to whatever they want. Within each list, a user is allowed to add items to their list. This will ask the user if they want to look at a hierarchical list of items from a database, presented as a list of types, then a list of items from that type. If they would rather, they can input the name of the item, and similarly named items will be presented to them form them to choose. Both of these adding methods ask for how much of the item they want. If the user want to change the quantity of an item in their list, they are allowed to. Items added to a list could be deleted by the user. Individual items can be "checked-off" by the user to represent crossing-off an item from a paper list. Along with checking-off items, the user can also clear all the check-offs from the list.

**Pre-conditions**: The user opens the app.

**Post-conditions**: One or more lists have been created and any changes made to the list(s) are saved. Lists that the user deleted no longer exist and thus do not show up for the user.

**Scenarios**: 

- The user is planning a trip to the grocery store and wants to create a grocery list of items they plan to pick up. 
- The user might want to edit(add item, remove item, change quantity) the contents of an existing list. They might want to also change the name of an existing list.
- The user has already created a list(s) and is currently in the store, checking-off the items that they picked up.
- The user might be reusing a previously used list and wants to uncheck all the checked off items.
- The user might want to get rid of a list that is no longer being used.
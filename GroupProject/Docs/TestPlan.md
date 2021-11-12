# Test Plan

**Author** : \<Team 1\> 

**Written By** : Mohammed Chowdhury, Dean Pektas, Carlos Romero

## 1 Testing Strategy

### 1.1 Overall Strategy

**Strategies for Unit-Test:**

The way we plan on doing unit tests is by isolating each class and making sure they function properly standing alone.
We plan to accomplish this by isolating the GroceryList, GroceryListItem, and ListHolder classes and doing manual tests on them.
The JUnit tests will make sure if all of the specific methods for each class are functioning properly.

**Strategies for Integration Testing:**

For our integration Testing, we will be using the Big bang and bottom down approach. For the bottom-up approach, we will test the low-level modules first and then test the high-level modules after. This will be done by first developing a low-level module (such as GroceryList) and have it be called by a dummy high-level module (listHolder). The listHolder in this case will be the "Driver"[a driver is a temporary module for integration testing].

Once we are finished with the bottom-up approach and all of the modules are complete, we will conduct a big bang integration testing. This will be conducted on the listHolder module. The reason being is that the listHolder is on the highest level and calls on the modules on the lower levels. if this module is functioning, it implies the app works properly. The big bang integration testing can be done doing Unit Tests on the listHolder's methods as well as checking if the UI is functioning properly for this page.  

**Strategies for System Testing:**

The way System Testing will be conducted is by simply running the app as a user and using it to see if there are any bugs present from the users' point of view. For this mode of testing, we will NOT look at the code. We will simply look at the description of the software and ensure all requirements were met as we are browsing through the app. 

**Strategies for Regression Testing:**

Regression Testing will take place on the system after new code is introduced or if the old code was refactored to see if the new code causes any problems to the system. To accomplish this, we can run both system tests (depending on the stage of development)  and unit tests on the modified/updated code. 
###### Such activities will be performed by the QA Engineer - Carlos Romero

### 1.2 Test Selection

**Black-Box Testing:**

For our black box testing, we will strictly look at functional testing and regression testing. Non-Functional testing will only check for usability as it is unnecessary to check scalability. Checking scalability is not needed since the app is not needed to scale. The data will be stored on the users personal device. 

For functional testing, we must first identify if the program is in the development stage where some/all the required functionality is implemented. Once at least some functionality is implemented, we can run through the app and identify if the app is functioning properly from the users end. Every time new code is introduced to the codebase, we will perform functional testing once again until project is finished. 

For non-functional testing we will check how useable the app is. In this stage, we will ensure the user experience is smooth and that the app functions as intended.

Regression testing will occur after any bug fixes and after new code is introduced to the code base.

System tests will be performed after the completion of each requirement , until all requirements are complete.  

**White-Box Testing:**

For white box testing, we will perform unit tests. In this stage of testing,we will look  at the code and how it is written. The purpose for white box testing is to  validate internal structure and workings of the code.
In order to cover as much coded behavior as possible we will utilize JUnit to perform unit tests on all the different classes to ensure the code is functioning as intended. 

### 1.3 Adequacy Criterion

The Quality of the test cases will be determined by the following criteria:
- How likely the case is to occur in real life
- How much of the requirements does the test case cover

If the test case covers an entire requirement as well is the test case being highly likely to occur in real life, it is a high quality test. 

The quality of the test cases can be determined with functional testing where each required function is tested all at once. For example, a test case to check if user is able to add a new item to the grocery list. This unit test will tackle the requirement of adding new items to the list. More over, this case will occur very often in real life scenarios and a test that validates this functionality is a quality test case. 

### 1.4 Bug Tracking

* In order to ensure the quality of our program, there will be a ticketing system in place where all team members will be notified by QA engineer every time a new bug is found.
* When a developer adds new code to the codebase, all team members will be notified via the ticketing system. 
* All of the code will be tracked via git and GitHub. 
###### This will be done via a discord channel titled "bug-tickets"

### 1.5 Technology
The testing technology we will be using for this application is JUNIT. Since the code base will comprise of java code, as well as Android Studio providing built in support for Junit, it seems like the best option for the team. 

Discord server "bug-tickets" used to keep track of the occurrence of bugs as well as to notify all members of  updates to the code

## 2 Test Cases

| Test case                                           | Purpose                                                      | Steps                                                        | Expected Result                                              | Result                                                       | Additional Information                                       |
| --------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Creating a new list                                 | Seeing that a new list is created and saved                  | Create a new list.                                           | New list is created and saved                                | A new list is created and appears in the list holder.        | Due to how the lists are saved, there was a fear that an empty list would not be saved. |
| Deleting an existing list                           | Making sure that an existing list and all its entries are deleted. | Press the delete button on a list.                           | List and all its contents are deleted.                       | The list is deleted and never appears in the list holder again. | All the items in the list are also deleted from the database. |
| Renaming an existing list                           | Making sure that an existing list is renamed.                | Click on the edit button on the list card and enter a new name. | Specified list is renamed                                    | The list is renamed and all of the list items remain in the list. | There was a worry that the renaming of the list will disconnect the list items from the list. |
| Adding an item to the list by category.             | Making sure that picking a item type sends you to the right items and the items are sent to the list. | press add item, pick the correct item type, pick the item, enter desired quantity. | The item is added to the list with the correct quantity.     | The item that was selected is added to the list along with the quantity that was inputted. |                                                              |
| Adding an item to the list by text search           | Making sure that searching for an item returns similarly named items to pick. | Press add item, type in item name, press search button, pick item. | The correct item is available for picking and is added to the list. | The similarly named items appear in a list and the item can be added to the list. | Compared to the item type adding method, this method has a different way to send the item information, which was a concern. |
| Removing an Item from the list.                     | Making sure that an item on the list is removed.             | Click on the trashcan on the item that you want to remove.   | Item is completely removed from the list.                    | The item is gone from the list and never reappears.          | There was a concern that the removal was only visual and the item would reappear when reopening the app. The item is removed from the database entirely on deletion. |
| Editing the quantity of an item on the list         | Making sure that an item can have it's quantity changed      | Click on the pen on the item you want to change the quantity of and input a new quantity. | The item on the list displays the new quantity and the new quantity is saved. | The new quantity is saved and displayed on the list.         |                                                              |
| Checking off an item.                               | Verifying that items on a list can be checked off and that the check off is saved | Click on the item that you want to be checked off.           | A check is displayed next to the item                        | A check is displayed to the right of the name of the item. The check is saved and remains until removed. | The initial check off idea had no way to be saved but this new method does. |
| Clearing all of the check off marks                 | Being able to uncheck all items on a list. This makes reusing a list easy. | Press the clear all checks button on the bottom of the screen. | All existing checks are removed and none of the items have check marks. | All items on the list do not have checks and is saved to the database. | Previous check off method made it impossible to remove checks from items off screen but this new method fixes that. |
| Adding an item that does not exist in the database. | If an item cannot be found, it is added to a database so it appears in the add items list for the next time it is needed. | Press the add item button. Either press the category it would be in or search for the item name. If not appearing, press the button on the bottom right to add the item to the database. This will ask you to input the item name, item type, and the quantity you want. | The item will appear in the database and in your list.       | The new item will appear in your list and is saved in the database so that it can be accessed for the next time. | The assumption is made that if you are adding an item you cannot find to the database, you would also want it in your list. |
| Return button on list.                              | The button will return you to the list holder.               | Click on the return button on the bottom left of the list.   | The app will return you to the list holder.                  | The app returns you to the list holder and saves your list.  |                                                              |
| Home button on the item add.                        | This button will return you back to the list holder.         | Click on add item button, click on the home button on the bottom left. | The app will return you to the list holder.                  | The app returns you to the list holder.                      |                                                              |

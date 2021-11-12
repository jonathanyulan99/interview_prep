## DESIGN 1 - Mohammed Chowdhury
![Design1](https://i.imgur.com/3d3xP1U.png)

As a team, we decided that Design 1 reflects the concepts of the team design. However, it fails to convey the information in an easy to consume manner. Some of the points that raised a few questions were the naming conventions of the classes and their purpose. Particularly, It was unclear to the team what the purpose of ItemList when you have the GroceryList. Will it have lists within a list? This ambiguity caused the team to move forward with a team solution instead of moving on with Design 1. With that being said, It is clear that this design reflects the team design greatly. In Design 1, classes "Item" and "ItemType" serve the same purpose as the Team Design's  "GroceryItem" and "GroceryItemType" classes. The "ItemList" class in Design 1 serves the same purpose as "GroceryList" in the Team Design. Finally, the "ListHolder" class in the TeamDesign reflects the "GroceryList" in Design 1. All in all, Design 1 was designed with the correct vision however it was not selected as the team design due to its ambiguity and failure to convey the key ideas of the design thoroughly.




## DESIGN 2 - Carlos Romero
![Design2](https://i.imgur.com/YnHFE8p.png)
With this design, there a couple of obvious problems we found. To start off, the Item class and the GroceryEntry class can be combined into one. The need to have just an item so that it can work with the database is unnecessary. The database does not need to hold and most likely will not use a specific class for its lists. ItemType class being a parent to Item class was a good idea but it is missing the multiplicity. The design is missing a way to manage the lists, as it is specified that the app should allow the user to make several lists and allow them to create and delete them. As was stated before, the GroceryEntry class should be combined with the Item class. This new class should have an association with the GroceryList class, as the GroceryList will use several of this new class. Even with all these flaws, it still had a similar structure to the diagrams from the rest of the group.

## DESIGN 3 - Davron
![Design3](https://i.imgur.com/6Eb2kp2.png)

Design 3 showed a lot of features that are similar to the final design, such as the 'List Manager' and 'Grocery List' class. However, it lacks many important features. The List Manager and Grocery classes are well made but the design as a whole seems incomplete. 

## DESIGN 4 - Jonathan Yulan

![individualDesign](https://raw.githubusercontent.com/jonathanyulan99/Assignment5/main/370.PNG)

As a whole we felt that Design 4 followed more or less a similiar direction that the other designs before it had implemented. A few points were raised; in regards to the lack of the database methods/functionality going un-defined. The question of whether or not to display the database was a source of contention throughout our group's meeting. In addition, another class that some team members utilized and implemented was a 'user' class. Design 4 did not define a user class(which we later came to an agreement was unecessary). Team1 decided that the database and listManager classes would handle all the functionality that a user class would, making it not needed. In addition, Design 4 hit on all the necessary requirements, however our team felt that the itemTypeSet class was unecessary and that this function would be better implemented through a GroceryItem class that inherited from a GroceryItemType class. Both of these classes would have some interaction with a database, in order to add new GroceryItemTypes, as well as GroceryItems. The association created with the database and the groceryListView class was also unecessary. After discussing it as a team; the team decided that the design did not need the association between the database and groceryListView class. A proposed idea was to simply have the groceryListView class simply contain all the instantianted list that were created, in a sort of container/list. Design 4's itemType inherited from item which we later proposed should be vice versa. The structure presented in design 4 was clear and made intutive sense, yet design 4 seemed a bit complicated and overall we felt that a simplier, more concise design was the best way forward. 

## DESIGN 5 - Dean
![Design 5](https://i.imgur.com/f2PlCO7.png)
In my design, the user class was created to handle list management amongst users. While this was not required, 
I felt that this was necessary to manage the creation, deletion and renaming list functions. Our group agreed
to not have this function in our final design. The benefit of this is to remove unnecessary functions and to transfer functionality over to a class titled ListHolder. ListHolder will also hold the ability to automatically save the list which is very beneficial to the user experience.

Within the GroceryList class, my design involved the handling of editing the list, including adding, deleting and changing the quantity of items. The function for checking an item on the list was handled within the item class. After review by the group, it was decided that the checkmark  functionality to an item would be handled in the GroceryList instead. The benefit here is that implementation should be a lot easier as anything in a list should automatically have  the ability to check it on or off. We even included a groupItemByType function in GroceryList that will further enhance the functionality of the list more than I would've originally imagined.

## DESIGN 6 - Lin Shi

![Design 6](https://i.imgur.com/qYBxPPN.png)

Design 6: The main pro is this design gave us clear ideas of what our final team-design would look like. We keeps the majority methods in this design and put them into our final design. We used the same aggregation relationships as this design used. We have the similar classes including User (ListHolder), GroceryList, GroceryItem, ItemType (GroceryItemType). 

The mainly con is that GroceryDB Class made us confused. The reason is we think the methods inside this Class should be implemented in Database layer. Thus, we deleted GroceryDB Class and its methods in our final design. Instead, we added doesItemExist() in GroceryList, which accepts output from query as its input and return if the item the user searched exists in current database. If yes, addItem() and changeQty() method can help add that item to user's list. If no, database should be updated later. 

In addition, we made some changes on this design to make it better. For example, we changed the input type in function selectList() from String to GroceryList and changed input type in checkOffItem() from String to GroceryItem. We reviewed and considered the requirement that user can check the items without deleting them. We all agreed with that the aim of the method is to allow user to check if they pick up all items shown on their list when they are shopping, so the method shouldn't have return types. And we expends setChecked(boolean) method in GroceryItem Class into two different methods: isChecked(boolean) and setCheck(). The method isChecked(boolean) checks if an item is checked, if not, setCheck() is used to check unchecked items without conflicts.

## TEAM DESIGN :

![TeamDesign](https://i.imgur.com/fTU5y7Y.png)

Most of our individual assignments had a similar thought process; specifically, when it came to the overall hierarchical structure of the application we were designing. While many of our designs included a database representation, we ultimately decided that the database was something that should not be included in the UML diagram. In addition, we felt that the UML diagram’s main purpose was to capture the necessary entity classes and focus on the functional requirement of the application we were building and center our focus on what the application is supposed to do.  

Some members included a user class representation in their personal designs, which allowed for the support of multiple users. This was a requirement that was not implicitly stated, and as a team we decided that our final design should not have that included. Mostly for the same reason that the database representation did not happen to make it in on our final team design. We were able to address all of our concern’s by moving required methods from certain classes and found that we could simplify our design by re-arranging methods to different classes. A proposed itemTypeSet class was brought up, which would fulfill one of the requirements of having the <list> of item_types represented. We decided on scrapping that all together. 

All of our group member’s individual designs featured four (4) common classes, which were ultimately all the classes that we showcased on our final team-design. Every member had some sort of representation of a GroceryItem, GroceryItemType, GroceryList, and a ListManager/holder/view. For much of our team, the methods and class variables were more or less the same. Certain members had different variable names, and we decided on all the final class variable names and methods. Almost all of the individual design’s featured a ‘has’ relationship between the classes. Specifically, the GroceryItemType ‘has’ 0 or more GroceryItem(s); the Listholder class ‘has’ 0 or more GroceryList(s). Overall, much of our individual designs satisfied all the necessary requirements of the application. 

The highlighted differences between our final team-design and our individual designs; were the omission of the user and database classes and the overall simplification of our UML design to display only four classes. Ultimately our team agreed that many of our individual designs were overly complex or had functionality highlighted that was not needed, and thus we decided on a simpler design that we felt would be easier to implement and still fulfill all the requirements needed.



## SUMMARY :

This experience was a huge learning experience for everyone. For this phase of the project, we learned that constructive criticism allows the team to evolve and improve together. We were able to work together to get the best parts of our designs and combine them to produce the final product. We decided on having each member present their design so that the group could get an idea of their thought process. This allowed us to understand everyone's designs and point out any flaws in the individual designs. This helped narrow down what information should and should not go into our final team design. In summation, this group assignment was a success. 
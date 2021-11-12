### Requirement #1: Allow the app to add, delete and change the quanity.

Design Implementation: I added to the design a itemList class with attributes quantity,itemName and itemType. It includes addItem, removeItem and setQuantity() operations to meet the first requirement,

### Requirement #2: In a database have types of Food and put the food in the corresponding type.

Design Implementation: to meet this requrement, I created a database that creates unique tables based to type of food.
The contents of the table will include the differnet foods of that type.

### Requirement#3: User should be able to pick the food from a list. Top of the list is the type and the subsequesnt items are foods that belong in that type.

Design Implementation: an ItemType class was created with attribute "Type" with operations that get and set the type. This class is used by the ItemList class to identify each list as a particular type. 

### Requirement #4: be able to search for an item and if not found add it to the database.

Design Implementation: Database was created to perform CRUD operations. 

### Requirement #5 : after modifying the list, save it automatically and immediately

Design Implementation : Not considered because it does not affect the design directly

### Requirement #6 : users must be able to check off items in a list.

Design Implementation : item class was created where each item has a isChecked attribute to keep track of wether it is checked off

### Requirement # 7: users must be able to clear checked items

Design Implementation: itemList has a clearAllChecks operation that iterates through each item and sets its checked attribute to false. 

### Requirement #8 : check off marks for a list don't go away  (persistent)

Design Implementation: the databases CRUD operations will handle the storing of the state of each item,

### Requirement #9 : app lists items in a list grouped by type

Design Implementation : the UI will show ItemType before ItemList

### Requirement # 10: allow app to support multiple lists

Design Implementation: the GroceryList class with attributes listName, numOfLists , isSaved has the operation of addList() which creates a new separate list.

### Requirement # 11 : UI must be responsive and intuitive.

Design Implementation: ignored as it does not relate to design. 


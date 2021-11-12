package edu.qc.seclass.glm;

import androidx.room.Dao;
import androidx.room.Delete;
import androidx.room.Insert;
import androidx.room.Query;
import androidx.room.Update;

import java.util.List;

@Dao
public interface GroceryItemDao {
    @Query("SELECT * FROM GroceryItem")
    List<GroceryItem> getAll();

    @Query("SELECT DISTINCT list_name FROM GroceryItem")
    List<String> getLists();

    @Query("SELECT * FROM GroceryItem WHERE list_name == :lName AND item_name != :invalid ORDER BY item_type")
    List<GroceryItem> getListItems(String lName, String invalid);

    @Query("SELECT * FROM GroceryItem WHERE list_name == :lName")
    List<GroceryItem> getItemsToDelete(String lName);

    @Query("UPDATE GroceryItem SET item_qty = :quantity WHERE leID == :id")
    void updateQty(int quantity, int id);

    @Query("UPDATE GroceryItem SET list_name = :listNm WHERE list_name == :oldListNm")
    void updateListName(String listNm, String oldListNm);

    @Query("UPDATE GroceryItem SET checked_off = :newState WHERE leID == :id")
    void updateCheckedOff(boolean newState, int id);

    @Insert
    void insertAll(GroceryItem... groceryItems);

    @Delete
    void delete(GroceryItem groceryItem);
}

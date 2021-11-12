package edu.qc.seclass.glm;

import androidx.room.Dao;
import androidx.room.Delete;
import androidx.room.Insert;
import androidx.room.Query;

import java.util.List;

@Dao
public interface ItemsDao {
    @Query("SELECT * FROM Items")
    List<Items> getAll();

    @Query("SELECT DISTINCT item_type FROM Items")
    List<String> getTypes();

    @Query("SELECT item_name FROM Items WHERE item_type == :typeNm")
    List<String> getItemsOfType(String typeNm);

    @Query("SELECT item_name FROM Items WHERE item_name LIKE '%'||:likeNm||'%'")
    List<String> getItemsLike(String likeNm);

    @Query("SELECT max(item_type) FROM Items WHERE item_name == :input")
    String getTypeFromName(String input);

    @Insert
    void insertAll(Items... items);

    @Delete
    void delete(Items items);
}

package edu.qc.seclass.glm;

import androidx.appcompat.app.AppCompatActivity;
import androidx.room.ColumnInfo;
import androidx.room.Entity;
import androidx.room.PrimaryKey;

import android.os.Bundle;

@Entity
public class GroceryItem {
    @PrimaryKey(autoGenerate = true)
    public int leID;

    @ColumnInfo(name = "list_name")
    public String listName = "";

    @ColumnInfo(name = "item_name")
    public String itemName = "";

    @ColumnInfo(name = "item_type")
    public String itemType ;

    @ColumnInfo(name = "item_qty")
    public int itemQty = 0;

    @ColumnInfo(name = "checked_off")
    public boolean checkedOff = false;

}
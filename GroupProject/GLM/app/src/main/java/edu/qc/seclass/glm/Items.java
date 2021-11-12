package edu.qc.seclass.glm;

import androidx.room.ColumnInfo;
import androidx.room.Entity;
import androidx.room.PrimaryKey;

@Entity
public class Items {
    @PrimaryKey(autoGenerate = true)
    public int itemId;

    @ColumnInfo(name = "item_name")
    public String itemName;

    @ColumnInfo(name = "item_type")
    public String itemType;
}

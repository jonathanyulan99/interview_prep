package edu.qc.seclass.glm;

import android.content.Context;

import androidx.room.Database;
import androidx.room.Room;
import androidx.room.RoomDatabase;

@Database(entities = {GroceryItem.class}, version = 1)
public abstract class GroceryItemDatabase extends RoomDatabase {
    public abstract GroceryItemDao GroceryItemDao();

    private static GroceryItemDatabase INSTANCE;

    public static GroceryItemDatabase getDbInstance(Context context){
        if(INSTANCE == null){
            INSTANCE = Room.databaseBuilder(context.getApplicationContext(), GroceryItemDatabase.class, "DB_NAME").allowMainThreadQueries().build();
        }
        return INSTANCE;
    }
}

package edu.qc.seclass.glm;

import android.content.Context;

import androidx.room.Database;
import androidx.room.Room;
import androidx.room.RoomDatabase;

@Database(entities = {Items.class}, version = 1)
public abstract class ItemsDatabase extends RoomDatabase {
    public abstract ItemsDao itemsDao();

    private static ItemsDatabase INSTANCE_2;

    public static ItemsDatabase getDbInstance(Context context){
        if(INSTANCE_2 == null){
            INSTANCE_2 = Room.databaseBuilder(context.getApplicationContext(), ItemsDatabase.class, "DB_NAME2").allowMainThreadQueries().build();
        }
        return INSTANCE_2;
    }
}

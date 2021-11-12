package edu.qc.seclass.glm;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class NewList extends AppCompatActivity {

    Button confirmNewList;
    EditText enterListName;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_new_list);

        confirmNewList = findViewById(R.id.newListButton);
        enterListName = findViewById(R.id.newListET);


        confirmNewList.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                saveNewList(enterListName.getText().toString());
                Intent i = new Intent(NewList.this, ListHolder.class);
                startActivity(i);
                finish();
            }
        });
    }

    private void saveNewList(String listName){
        GroceryItemDatabase db = GroceryItemDatabase.getDbInstance(this.getApplicationContext());

        GroceryItem groceryItem = new GroceryItem();
        groceryItem.listName = listName;
        groceryItem.itemName = "invalid";
        groceryItem.itemType = "invalid";
        groceryItem.itemQty = -1;
        groceryItem.checkedOff = false;

        db.GroceryItemDao().insertAll(groceryItem);
    }
}
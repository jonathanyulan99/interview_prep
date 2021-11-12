package edu.qc.seclass.glm;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class NewItem extends AppCompatActivity {
    private Button addToDataBaseBTN;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_new_item);

        getSupportActionBar().setTitle("Add New Item to Data Base");
        addToDataBaseBTN = findViewById(R.id.addToDbBTN);
        EditText itemNameInput = findViewById(R.id.nameET);
        EditText itemTypeInput = findViewById(R.id.typeET);
        EditText quantityInput = findViewById(R.id.newItemQty);
        addToDataBaseBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                saveNewItem(itemNameInput.getText().toString(), itemTypeInput.getText().toString());

                Intent resultIntent = new Intent();
                resultIntent.putExtra("QUANTITY",quantityInput.getText().toString());
                resultIntent.putExtra("ITEM_NAME",itemNameInput.getText().toString());
                resultIntent.putExtra("ITEM_TYPE", itemTypeInput.getText().toString());

                setResult(RESULT_OK, resultIntent);
                finish();
            }
        });
    }

    private void saveNewItem(String itemNameIn, String itemTypeIn){
        ItemsDatabase db = ItemsDatabase.getDbInstance(this.getApplicationContext());

        Items items = new Items();
        items.itemName = itemNameIn;
        items.itemType = itemTypeIn;
        db.itemsDao().insertAll(items);
    }
}
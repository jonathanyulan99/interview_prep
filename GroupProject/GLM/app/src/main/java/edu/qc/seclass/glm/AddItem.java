package edu.qc.seclass.glm;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class AddItem extends AppCompatActivity {
    private Button addItemToList;
    private EditText quantity;
    private TextView itemTypeBeingAdded;
    private String typeName = "";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_item);
        addItemToList = findViewById(R.id.addItemToListBTN);
        quantity = findViewById(R.id.enterQuantityET);
        itemTypeBeingAdded = findViewById(R.id.addingItemTypeTV);
        //String itemNameFromItemList = getInfoFromItemList();


        Intent intent = getIntent();
        typeName = intent.getStringExtra("TYPE_NAME");
        String itemNameFromItemList = intent.getStringExtra("ITEM_NAME");
        itemTypeBeingAdded.setText("Adding "+ itemNameFromItemList);

        addItemToList.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                //Intent resultIntent = new Intent(AddItem.this, GroceryList.class);
                Intent resultIntent = new Intent();
                resultIntent.putExtra("QUANTITY",quantity.getText().toString());
                resultIntent.putExtra("ITEM_NAME",itemNameFromItemList);
                resultIntent.putExtra("ITEM_TYPE", typeName);
                //startActivity(resultIntent);
                setResult(RESULT_OK, resultIntent);
                finish();

            }
        });
    }

    private String getInfoFromItemList(){
        Intent intent = getIntent();
        String itemName  = intent.getStringExtra("ITEM_NAME");
        if(itemName == null){return "Item";}

        return itemName;
    }
}
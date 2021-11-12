package edu.qc.seclass.glm;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class EditListName extends AppCompatActivity {

    Button confirmNewListName;
    EditText enterListName;
    String oldListName = "";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_edit_list_name);

        confirmNewListName = findViewById(R.id.newListNameButton);
        enterListName = findViewById(R.id.newNameET);

        Intent intent = getIntent();
        oldListName = intent.getStringExtra("OLD_NAME");

        confirmNewListName.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                saveNewListName(enterListName.getText().toString());
                Intent i = new Intent(EditListName.this, ListHolder.class);
                startActivity(i);
                finish();
            }
        });
    }

    private void saveNewListName(String listName){
        GroceryItemDatabase db = GroceryItemDatabase.getDbInstance(this.getApplicationContext());

        db.GroceryItemDao().updateListName(listName, oldListName);
    }
}
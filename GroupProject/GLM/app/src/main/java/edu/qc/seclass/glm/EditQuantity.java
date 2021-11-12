package edu.qc.seclass.glm;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class EditQuantity extends AppCompatActivity {

    //private Button confirmQty;
    //private EditText enterQty;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_edit_quantity);

        Intent i = getIntent();
        Button confirmQty = findViewById(R.id.editQtybutton);
        EditText enterQty = findViewById(R.id.editQtyNumber);


        confirmQty.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent resultIntent = new Intent();
                resultIntent.putExtra("Qty", enterQty.getText().toString());

                setResult(RESULT_OK, resultIntent);
                finish();
            }
        });
    }
}
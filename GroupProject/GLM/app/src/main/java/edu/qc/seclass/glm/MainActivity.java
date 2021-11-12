package edu.qc.seclass.glm;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.MotionEvent;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {
    private Button goTolistBtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        goTolistBtn = findViewById(R.id.gotolistBTN);



        // the main activity will redirect app to ListHolder using an "Intent" (i think that's how you do it)
        //https://developer.android.com/reference/android/content/Intent

        Intent i = new Intent(MainActivity.this, ListHolder.class);
        startActivity(i);
        finish();
    }
}
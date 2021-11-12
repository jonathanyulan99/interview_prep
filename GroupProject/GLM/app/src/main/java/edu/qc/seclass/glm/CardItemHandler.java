package edu.qc.seclass.glm;

import android.graphics.Paint;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;


import java.io.Serializable;
public class CardItemHandler extends AppCompatActivity {


    private int firstImageResource;


    private int secondImageResource;


    private int thirdImageResource;


    private String itemText;


    private String quantityText;



    public CardItemHandler(String quantityText,String itemText,int firstImageResource, int secondImageResource,int thirdImageResource){
        this.firstImageResource = firstImageResource;
        this.secondImageResource = secondImageResource;
        this.thirdImageResource = thirdImageResource;
        this.itemText = itemText;
        this.quantityText = quantityText;
    }


    public CardItemHandler(String quantityText,String itemText, int secondImageResource,int thirdImageResource){
        this.secondImageResource = secondImageResource;
        this.thirdImageResource = thirdImageResource;
        this.itemText = itemText;
        this.quantityText = quantityText;
    }

    public CardItemHandler(String quantityText,String itemText, int secondImageResource){
        this.secondImageResource = secondImageResource;
        this.itemText = itemText;
        this.quantityText = quantityText;
    }


    public CardItemHandler(String quantityText,String itemText){
        this.itemText = itemText;
        this.quantityText = quantityText;
    }




    public int getFirstImageResource() {
        return firstImageResource;
    }

    public void setFirstImageResource(int i){this.firstImageResource = i;}

    public int getSecondImageResource() {
        return secondImageResource;
    }

    public int getThirdImageResource() {
        return thirdImageResource;
    }


    public String getItemText() {
        //ensures the characters are not so long that they flow out of screen
        //if(itemText == null){itemText = "Here is the problem";}
        if(itemText.length() > 21){
            itemText = itemText.substring(0,21);
        }
        return this.itemText;
    }

    public String getQuantityText() {
        //ensures the characters are not so long that they flow out of screen
        if(quantityText.length() > 6){
            quantityText = quantityText.substring(0,6);
        }
        return this.quantityText;
    }

    public void setQuantityText(String s){quantityText = s;}
}

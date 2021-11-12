package edu.qc.seclass.glm;


import androidx.annotation.Nullable;

import androidx.annotation.NonNull;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.content.Intent;
import android.graphics.Paint;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.material.floatingactionbutton.FloatingActionButton;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class GroceryList extends AppCompatActivity {
    private String listNm = "";
    private GroceryItem groceryItem;
    private FloatingActionButton addItemBTN;
    private Button clearChecksBTN;
    private Button returnBTN;

    private ArrayList<CardItemHandler> cardItemList = new ArrayList<>();


    //private ArrayList<CardItemHandler> cardItemListofItems;
    private RecyclerView recyclerView;
    private RecyclerAdapter adapter; //provides recycler-view with new views when needed
    private RecyclerView.LayoutManager layoutManager;


    private int tempPosition = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_grocery_list);
        getSupportActionBar().setTitle("Your Items");
        addItemBTN = findViewById(R.id.addItemBTN);
        clearChecksBTN = findViewById(R.id.clearChecksBTN);
        returnBTN = findViewById(R.id.returnBTN);

        cardItemList = new ArrayList<>();

        Intent intent = getIntent();
        listNm = intent.getStringExtra("NAME_OF_LIST");

        Toast.makeText(getApplicationContext(), listNm, Toast.LENGTH_SHORT).show();

        cardItemList = getDbItems();
        createRecyclerView(cardItemList);

        //clearAllChecks(clearChecksBTN);

        addItemBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i = new Intent(GroceryList.this, TypeList.class);
                startActivityForResult(i, 1);
            }
        });

        returnBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v2) {
                Intent i = new Intent(GroceryList.this, ListHolder.class);
                startActivity(i);
                finish();
            }
        });

        clearChecksBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                clearAllChecks();
            }
        });

    }

    private void createRecyclerView(ArrayList<CardItemHandler> cardItemList) {
        layoutManager = new LinearLayoutManager(this); //the layout of the recyclerView will be linear
        recyclerView = findViewById(R.id.recyclerViewListHolder);
        recyclerView.setHasFixedSize(true); //this means that the cards will not resize based on size of the texts and images of the card_item
        adapter = new RecyclerAdapter(cardItemList);//that adapter is set to adapt to cardItemList arrayList
        recyclerView.setAdapter(adapter);//Whats happening: adapter takes contents of cardItemList ArrayList and makes it readable to recyclerView
        recyclerView.setLayoutManager(layoutManager);//recyclerView will have a linear layout

        adapter.setOnItemClickListener(new RecyclerAdapter.OnItemClickListener() {
            @Override
            // clicking on the card will result on the name having a strike through.
            public void onItemClick(int position) {
                //RecyclerAdapter.RecyclerViewHolder clickedView = (RecyclerAdapter.RecyclerViewHolder) recyclerView.findViewHolderForAdapterPosition(position);
                //clickedView.strikeName();

                if ( cardItemList.get(position).getFirstImageResource() == R.drawable.checkgreen ) {
                    checkItem(position, false);
                    cardItemList.get(position).setFirstImageResource(R.drawable.checknone);
                }
                else{
                    checkItem(position, true);
                    cardItemList.get(position).setFirstImageResource(R.drawable.checkgreen);
                }
                adapter.notifyDataSetChanged();
            }

            // clicking the trash can will remove the card from the list
            @Override
            public void onThirdImageClick(int position) {
                removeItem(position);
            }

            @Override
            public void onSecondImageClick(int position) {
                tempPosition = position;
                Intent intent = new Intent(GroceryList.this, EditQuantity.class);
                startActivityForResult(intent, 2);
            }
        });
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if (resultCode == RESULT_CANCELED) {
            Toast.makeText(getApplicationContext(), "Cancelled.", Toast.LENGTH_SHORT).show();
        }
        if (resultCode == RESULT_OK) {
            if (requestCode == 1) {
                Toast.makeText(GroceryList.this, "Item added.", Toast.LENGTH_SHORT).show();
                //int result = data.getIntExtra("result", 0);
                String itemQuantity = data.getStringExtra("QUANTITY");
                String itemName = data.getStringExtra("ITEM_NAME");
                String typeName = data.getStringExtra("ITEM_TYPE");

                saveNewGroceryItem(listNm, itemName, typeName, Integer.parseInt(itemQuantity));

                createRecyclerView(getDbItems());
            }

            if (requestCode == 2) {
                Toast.makeText(GroceryList.this, "Item edited.", Toast.LENGTH_SHORT).show();
                String result = data.getStringExtra("Qty");

                GroceryItemDatabase db = GroceryItemDatabase.getDbInstance(this.getApplicationContext());// get instance of GroceryItem DB
                List<GroceryItem> removeList = db.GroceryItemDao().getListItems(listNm, "invalid");// get list of GroceryItems in current list
                GroceryItem temp = removeList.get(tempPosition); // get the GroceryItem of the list entry that wants to be edited
                db.GroceryItemDao().updateQty(Integer.parseInt(result), temp.leID); // update the entry with the
                createRecyclerView(getDbItems());
                //cardItemList.get(tempPosition).setQuantityText(result);
                //adapter.notifyItemChanged(tempPosition);
            }
        }

    }

    public void setListName(String name) {
        this.listNm = name;
    }

    public void addItem(GroceryItem item) {
    }

    public void removeItem(int position) {
        GroceryItemDatabase db = GroceryItemDatabase.getDbInstance(this.getApplicationContext());
        List<GroceryItem> removeList = db.GroceryItemDao().getListItems(listNm, "invalid");

        db.GroceryItemDao().delete(removeList.get(position));
        createRecyclerView(getDbItems());
    }


    //this method will most likely be a button onlick

    public void clearAllChecks() {
        GroceryItemDatabase db = GroceryItemDatabase.getDbInstance(this.getApplicationContext());
        List<GroceryItem> currentList = db.GroceryItemDao().getListItems(listNm, "invalid");

        for(int i = 0; i < currentList.size(); i++){
            if ( currentList.get(i).checkedOff ) {
                checkItem(i, false);
            }
        }
        createRecyclerView(getDbItems());
    }

    private void saveNewGroceryItem(String listName, String itemName, String itemType, int qty) {
        GroceryItemDatabase db = GroceryItemDatabase.getDbInstance(this.getApplicationContext());

        GroceryItem groceryItem = new GroceryItem();
        groceryItem.listName = listName;
        groceryItem.itemName = itemName;
        groceryItem.itemType = itemType;
        groceryItem.itemQty = qty;
        groceryItem.checkedOff = false;

        db.GroceryItemDao().insertAll(groceryItem);
    }

    private void checkItem(int position, boolean check){
        GroceryItemDatabase db = GroceryItemDatabase.getDbInstance(this.getApplicationContext());
        List<GroceryItem> currentList = db.GroceryItemDao().getListItems(listNm, "invalid");

        db.GroceryItemDao().updateCheckedOff(check, currentList.get(position).leID);
    }

    private ArrayList<CardItemHandler> getDbItems() {
        GroceryItemDatabase db = GroceryItemDatabase.getDbInstance(this.getApplicationContext());

        ArrayList<CardItemHandler> tempArrayList = new ArrayList<>();
        List<GroceryItem> tempList = db.GroceryItemDao().getListItems(listNm, "invalid");

        for (int i = 0; i < tempList.size(); i++) {
            GroceryItem tempItem = tempList.get(i);
            if ( tempItem.checkedOff )
                tempArrayList.add(new CardItemHandler(String.valueOf(tempItem.itemQty), tempItem.itemName, R.drawable.checkgreen,R.drawable.edit, R.drawable.trash));
            else
                tempArrayList.add(new CardItemHandler(String.valueOf(tempItem.itemQty), tempItem.itemName, R.drawable.checknone,R.drawable.edit, R.drawable.trash));
        }

        return tempArrayList;
    }
}
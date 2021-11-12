package edu.qc.seclass.glm;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import com.google.android.material.floatingactionbutton.FloatingActionButton;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TypeList extends AppCompatActivity {
    private RecyclerView recyclerView;
    private RecyclerAdapter adapter; //provides recycler-view with new views when needed
    private RecyclerView.LayoutManager layoutManager;
    private FloatingActionButton searchButton;
    private FloatingActionButton homeBtn;
    private EditText whatToSearch;
    private HashMap<String,ArrayList<CardItemHandler>> ItemTypeMapOfItems;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_type_list);
        getSupportActionBar().setTitle("Types of Items Available");

        searchButton = findViewById(R.id.itemTextSearchBtn);
        homeBtn = findViewById(R.id.homeBtn);
        whatToSearch = findViewById(R.id.itemSearchET);

        ItemTypeMapOfItems = new HashMap<>();
        populateDefaultItemsToHashMap(ItemTypeMapOfItems);



        ArrayList<CardItemHandler> cardItemListOfItemTypes = getDbItems();
        createRecyclerView(cardItemListOfItemTypes);

        searchButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i = new Intent(TypeList.this, ItemList.class);
                String itemToSearch = whatToSearch.getText().toString();
                i.setFlags(Intent.FLAG_ACTIVITY_FORWARD_RESULT);
                i.putExtra("ITEM_LIKE", itemToSearch);
                i.putExtra("IS_SEARCH", true);
                startActivity(i);
                finish();
            }
        });

        homeBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i = new Intent(TypeList.this, ListHolder.class);
                startActivity(i);
            }
        });
    }
    private void createRecyclerView(ArrayList<CardItemHandler> cardItemList){
        layoutManager = new LinearLayoutManager(this); //the layout of the recyclerView will be linear
        recyclerView = findViewById(R.id.recyclerViewListHolder);
        recyclerView.setHasFixedSize(true); //this means that the cards will not resize based on size of the texts and images of the card_item
        adapter = new RecyclerAdapter(cardItemList);//that adapter is set to adapt to cardItemList arrayList
        recyclerView.setAdapter(adapter);//Whats happening: adapter takes contents of cardItemList ArrayList and makes it readable to recyclerView
        recyclerView.setLayoutManager(layoutManager);//recylerView will have a linear layout

        adapter.setOnItemClickListener(new RecyclerAdapter.OnItemClickListener() {
            @Override
            public void onItemClick(int position) {
                Intent i = new Intent(TypeList.this, ItemList.class);
                String typeName = cardItemList.get(position).getItemText();
                i.setFlags(Intent.FLAG_ACTIVITY_FORWARD_RESULT);
                i.putExtra("TYPE_NAME", typeName);
                i.putExtra("IS_SEARCH", false);
                startActivity(i);
                finish();
            }

            @Override
            public void onThirdImageClick(int position) {

            }

            @Override
            public void onSecondImageClick(int position) {

            }
        });
    }

    //create a hashmap where key = item type (associated with each card), value = arrayList of type CardItemHandler
    //pass  proper arrayList to ItemList , based on the card selected.
    //iterate though the hashmap and add a new card to cardItemList via "cardItemList.add(new CardItemHandler("",entry.getKey()))"
    private void loadCardItemList(ArrayList<CardItemHandler> cardList){
        for(Map.Entry<String,ArrayList<CardItemHandler>> entry : ItemTypeMapOfItems.entrySet()){
            cardList.add(new CardItemHandler("",entry.getKey()));
        }
    }

    private void populateDefaultItemsToHashMap(HashMap<String,ArrayList<CardItemHandler>> map){
        map.put("Fruits",setDefaultFruits());
        map.put("Vegetables", setDefaultVegetables());

    }

    private ArrayList<CardItemHandler> setDefaultFruits(){
        ArrayList<CardItemHandler> items = new ArrayList<>();
        items.add(new CardItemHandler("","Apples"));
        items.add(new CardItemHandler("","Oranges"));
        items.add(new CardItemHandler("","Bananas"));
        items.add(new CardItemHandler("","Grapes"));
        return items;
    }

    private ArrayList<CardItemHandler> setDefaultVegetables(){
        ArrayList<CardItemHandler> items = new ArrayList<>();
        items.add(new CardItemHandler("","Broccoli"));
        items.add(new CardItemHandler("","Cabbage"));
        items.add(new CardItemHandler("","Lettuce"));
        items.add(new CardItemHandler("","Spinach"));
        return items;
    }

    private ArrayList<CardItemHandler> getDbItems(){
        ItemsDatabase db = ItemsDatabase.getDbInstance(this.getApplicationContext());

        ArrayList<CardItemHandler> tempArrayList = new ArrayList<>();
        List<String> tempList =  db.itemsDao().getTypes();

        for(int i = 0; i < tempList.size(); i++){
            tempArrayList.add(new CardItemHandler("",tempList.get(i)));
        }

        return tempArrayList;
    }
}
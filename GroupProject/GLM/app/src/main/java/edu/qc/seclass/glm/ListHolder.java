package edu.qc.seclass.glm;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

import com.google.android.material.floatingactionbutton.FloatingActionButton;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ListHolder extends AppCompatActivity {
    private GroceryList groceryList;

    private RecyclerView recyclerView;
    private RecyclerAdapter adapter; //provides recycler-view with new views when needed
    private RecyclerView.LayoutManager layoutManager;
    private ArrayList<CardItemHandler> cardItemListOfLists;
    private HashMap<String,ArrayList<CardItemHandler>> listMapOfGroceryList;

    private FloatingActionButton addListButton;
    private int tempPosition = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getSupportActionBar().setTitle("Your Lists");
        setContentView(R.layout.activity_list_holder);
        listMapOfGroceryList = new HashMap<>();
        //cardItemListofLists = new ArrayList<>();
        //populateDefaultItemsToHashMap(listMapOfGroceryList); //adds default items into the listMapOfGroceryList hashMap
        //loadCardList(cardItemListofLists); // loads the key's of the hash map into the cardItemList ArrayList.


        cardItemListOfLists =  getDbItems();
        createRecyclerView(cardItemListOfLists);

        addListButton = findViewById(R.id.addListButton);

        addListButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i = new Intent(ListHolder.this, NewList.class);
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
                Intent i = new Intent(ListHolder.this, GroceryList.class);
                //ArrayList<CardItemHandler> list = listMapOfGroceryList.get(cardItemList.get(position).getItemText().toString());
                String nameOfList = cardItemList.get(position).getItemText();
                i.putExtra("NAME_OF_LIST",nameOfList);
                startActivity(i);
                finish();
            }

            @Override
            public void onThirdImageClick(int position) {
                deleteList(position, cardItemList.get(position).getItemText());
            }

            @Override
            public void onSecondImageClick(int position) {
                tempPosition = position;
                Intent intent = new Intent(ListHolder.this, EditListName.class);
                intent.putExtra("OLD_NAME", cardItemList.get(position).getItemText());
                startActivity(intent);
                finish();
            }
        });
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if (resultCode == RESULT_CANCELED){
            Toast.makeText(getApplicationContext(),"Cancelled.",Toast.LENGTH_SHORT).show();
        }
        if (resultCode == RESULT_OK) {
            if (requestCode == 1) {
                Toast.makeText(ListHolder.this, "List created.", Toast.LENGTH_SHORT).show();
            }
            if (requestCode == 2) {

            }
        }
    }

    private void loadCardList(ArrayList<CardItemHandler> cardList){
        for(Map.Entry<String,ArrayList<CardItemHandler>> entry : listMapOfGroceryList.entrySet()){
            cardList.add(new CardItemHandler("",entry.getKey(),R.drawable.edit,R.drawable.trash));
        }
    }

    private void populateDefaultItemsToHashMap(HashMap<String,ArrayList<CardItemHandler>> map){
        map.put("Supermarket List",setDefaultSuperMarketList());
        map.put("Weekly List", setDefaultVegetables());
    }
    private ArrayList<CardItemHandler> setDefaultSuperMarketList(){
        ArrayList<CardItemHandler> items = new ArrayList<>();
        items.add(new CardItemHandler("10","Apples",R.drawable.edit,R.drawable.trash));
        items.add(new CardItemHandler("3","Oranges",R.drawable.edit,R.drawable.trash));
        items.add(new CardItemHandler("1","Dozen Eggs",R.drawable.edit,R.drawable.trash));
        items.add(new CardItemHandler("1","Mango Juice",R.drawable.edit,R.drawable.trash));
        items.add(new CardItemHandler("10","Apples",R.drawable.edit,R.drawable.trash));
        items.add(new CardItemHandler("3","Oranges",R.drawable.edit,R.drawable.trash));
        items.add(new CardItemHandler("1","Dozen Eggs",R.drawable.edit,R.drawable.trash));
        items.add(new CardItemHandler("1","Mango Juice",R.drawable.edit,R.drawable.trash));
        items.add(new CardItemHandler("3","Oranges",R.drawable.edit,R.drawable.trash));
        items.add(new CardItemHandler("1","Dozen Eggs",R.drawable.edit,R.drawable.trash));
        items.add(new CardItemHandler("1","Mango Juice",R.drawable.edit,R.drawable.trash));
        return items;
    }

    private ArrayList<CardItemHandler> setDefaultVegetables(){
        ArrayList<CardItemHandler> items = new ArrayList<>();
        items.add(new CardItemHandler("10","Green Eggs",R.drawable.edit,R.drawable.trash));
        items.add(new CardItemHandler("3","Ham",R.drawable.edit,R.drawable.trash));

        return items;
    }

    public void renameList(GroceryList list,String newName){
        list.setListName(newName);
    }

    public void deleteList(int position, String listNm){
        GroceryItemDatabase db = GroceryItemDatabase.getDbInstance(this.getApplicationContext());
        List<GroceryItem> removeList = db.GroceryItemDao().getItemsToDelete(listNm);

        for(int i = 0; i < removeList.size(); i++){
            db.GroceryItemDao().delete(removeList.get(i));
        }
        createRecyclerView(getDbItems());
    }

    private ArrayList<CardItemHandler> getDbItems(){
        GroceryItemDatabase db = GroceryItemDatabase.getDbInstance(this.getApplicationContext());

        ArrayList<CardItemHandler> tempArrayList = new ArrayList<>();
        List<String> tempList =  db.GroceryItemDao().getLists();

        for(int i = 0; i < tempList.size(); i++){
            tempArrayList.add(new CardItemHandler("",tempList.get(i),R.drawable.edit,R.drawable.trash));
        }

        return tempArrayList;
    }
}
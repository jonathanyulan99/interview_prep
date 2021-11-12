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
import java.util.List;

public class ItemList extends AppCompatActivity {
    private RecyclerView recyclerView;
    private RecyclerAdapter adapter; //provides recycler-view with new views when needed
    private RecyclerView.LayoutManager layoutManager;
    private FloatingActionButton editItemListBtn;
    private FloatingActionButton homeButton;
    private ArrayList<CardItemHandler> cardItemListOfPossibleItems ;
    private String typeName = "";
    private boolean isSearch;
    private String searchEntry = "";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_item_list);
        getSupportActionBar().setTitle("Items Available");
        editItemListBtn= findViewById(R.id.editItemListBtn);
        homeButton = findViewById(R.id.homeBtn2);

        Intent intent = getIntent();
        typeName = intent.getStringExtra("TYPE_NAME");
        isSearch = intent.getBooleanExtra("IS_SEARCH", false);

        if ( isSearch ){
            searchEntry = intent.getStringExtra("ITEM_LIKE");
            Toast.makeText(getApplicationContext(),searchEntry,Toast.LENGTH_SHORT).show();
            cardItemListOfPossibleItems = getDbLikeItems(searchEntry);
        }
        else{
            cardItemListOfPossibleItems = getDbItems(typeName);}
        createRecyclerView(cardItemListOfPossibleItems);

        editItemListBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i = new Intent(ItemList.this, NewItem.class);
                i.setFlags(Intent.FLAG_ACTIVITY_FORWARD_RESULT);
                startActivity(i);
                finish();
            }
        });

        homeButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i = new Intent(ItemList.this, ListHolder.class);
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
                Intent i = new Intent(ItemList.this, AddItem.class);
                i.setFlags(Intent.FLAG_ACTIVITY_FORWARD_RESULT);
                i.putExtra("ITEM_NAME",cardItemList.get(position).getItemText());
                if ( isSearch ){
                    i.putExtra("TYPE_NAME", getTypeIfSearch(cardItemList.get(position).getItemText()));
                }
                else
                    i.putExtra("TYPE_NAME", typeName);
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

    private ArrayList<CardItemHandler> getInfoFromTypeList(ArrayList<CardItemHandler> list){
        Intent intent = getIntent();
        ArrayList<CardItemHandler> listOfItems = (ArrayList<CardItemHandler>) intent.getSerializableExtra("ARRAYOFITEMS");

        if(listOfItems != null){
            list = listOfItems;
        }
        return list;
    }

    private String getTypeIfSearch(String n){
        ItemsDatabase db = ItemsDatabase.getDbInstance(this.getApplicationContext());

        return db.itemsDao().getTypeFromName(n);
    }

    private ArrayList<CardItemHandler> getDbLikeItems(String likeNm){
        ItemsDatabase db = ItemsDatabase.getDbInstance(this.getApplicationContext());

        ArrayList<CardItemHandler> tempArrayList = new ArrayList<>();
        List<String> tempList =  db.itemsDao().getItemsLike(likeNm);

        for(int i = 0; i < tempList.size(); i++){
            tempArrayList.add(new CardItemHandler("",tempList.get(i)));
        }

        return tempArrayList;
    }

    private ArrayList<CardItemHandler> getDbItems(String typeNm){
        ItemsDatabase db = ItemsDatabase.getDbInstance(this.getApplicationContext());

        ArrayList<CardItemHandler> tempArrayList = new ArrayList<>();
        List<String> tempList =  db.itemsDao().getItemsOfType(typeNm);

        for(int i = 0; i < tempList.size(); i++){
            tempArrayList.add(new CardItemHandler("",tempList.get(i)));
        }

        return tempArrayList;
    }

}
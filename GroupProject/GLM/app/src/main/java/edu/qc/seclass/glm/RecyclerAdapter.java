package edu.qc.seclass.glm;

import android.graphics.Paint;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;
//the RecyclerAdapters job is to connect the Object arrayList to the ViewHolder. The view holder then populates the content of the Object as a view on recycler view
//theory of recyclerView Explained : https://youtu.be/uh6lKnfp5hY
public class RecyclerAdapter extends RecyclerView.Adapter<RecyclerAdapter.RecyclerViewHolder> {

    private ArrayList<CardItemHandler> cardItemList;
    //must create OnItemClickListener must be made first  before making this variable  since there is a built in OnItemClickClick
    private OnItemClickListener itemClickListener;

    public interface OnItemClickListener{
        void onItemClick(int position); // this method will  forced to be  implemented when OnItemClickListener is called by a RecyclerAdapter object
        void onThirdImageClick(int position); // this will be used when there is a need for a button on the third ImageView
        void onSecondImageClick(int position); // for the edit buttons
    }

    //an OnItemClickListener created by a class that will use this recycler view will call this method
    public void setOnItemClickListener(OnItemClickListener listener){
        itemClickListener = listener;
    }

    public static class RecyclerViewHolder extends RecyclerView.ViewHolder {
        public ImageView firstImage;
        public ImageView secondImage;
        public ImageView thirdImage;
        public TextView  itemName;
        public TextView itemQuantity;

        //purpose of the view holder is to hold the view itself (the card in our case)
        public RecyclerViewHolder(@NonNull View itemView,OnItemClickListener listener) {
            super(itemView);
            firstImage = itemView.findViewById(R.id.firstImgIV);
            secondImage = itemView.findViewById(R.id.secondImgIV);
            thirdImage = itemView.findViewById(R.id.thirdImgIV);
            itemName = itemView.findViewById(R.id.itemTV);
            itemQuantity = itemView.findViewById(R.id.quantityTV);
            //when the user taps an view in the recyclerView
            itemView.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    if(listener != null){
                        int position = getAdapterPosition();
                        if(position != RecyclerView.NO_POSITION){
                            listener.onItemClick(position);
                        }
                    }
                }//end of onClick
            });

            // this is for delete buttons
            thirdImage.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    if(listener != null) {
                        int position = getAdapterPosition();
                        if (position != RecyclerView.NO_POSITION) {
                            listener.onThirdImageClick(position);
                        }
                    }
                }
            });

            // this is for edit buttons
            secondImage.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    if(listener != null) {
                        int position = getAdapterPosition();
                        if (position != RecyclerView.NO_POSITION) {
                            listener.onSecondImageClick(position);
                        }
                    }
                }
            });
        }
    }//end of RecyclerViewHolder class

    public RecyclerAdapter(ArrayList<CardItemHandler> itemList){
        this.cardItemList = itemList;
    }

    @NonNull
    @Override
    public RecyclerViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        //sends the card item information to the recycle adapter.
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.card_item, parent, false);
        RecyclerViewHolder rvh = new RecyclerViewHolder(view,itemClickListener);
        return rvh;
    }

    @Override
    public void onBindViewHolder(@NonNull RecyclerViewHolder holder, int position) {
        CardItemHandler currentItemHandler = cardItemList.get(position);
        //set firstImage, secondImage, ThirdImage to the value of the images in card_item.xml
        //the value of the images in card_item_xml can be retried by the CardItemHand.java class.
        holder.firstImage.setImageResource(currentItemHandler.getFirstImageResource());
        holder.secondImage.setImageResource(currentItemHandler.getSecondImageResource());
        holder.thirdImage.setImageResource(currentItemHandler.getThirdImageResource());

        //set the text of the itemQuantity and itemName as card_item.xml's textViews
        //the value of the texts in card_item_xml can be retrieved by the CardItemHand.java class.
        holder.itemQuantity.setText(currentItemHandler.getQuantityText());
        holder.itemName.setText(currentItemHandler.getItemText());
    }

    @Override
    public int getItemCount() {
        return cardItemList.size();
    }






}

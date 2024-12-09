import streamlit as st

# App Title
st.title("Meal Prep Menu")

# Categories and their items
menu = {
    "Vegetarian": [
        {"name": "Curry Butternut Squash & Fall Vegetables with Farro Pilaf", 
         "info": "836 Calories, 19g Protein, 154g Carbs, 20g Fat (V, Veg, GF, DF)"},
        {"name": "Mushroom Quinoa Stir Fry", 
         "info": "1076 Calories, 48g Protein, 185g Carbs, 17g Fat (V, Veg, GF, DF)"},
        {"name": "Vegetarian Shepherd’s Pie", 
         "info": "436 Calories, 20g Protein, 63g Carbs, 11g Fat (Veg, GF)"}
    ],
    "Poultry": [
        {"name": "Peruvian Chicken with Green Beans & Cauliflower Rice", 
         "info": "466 Calories, 33g Protein, 20g Carbs, 28g Fat (GF)"},
        {"name": "Teriyaki Chicken with Thai Basil Rice Noodles", 
         "info": "977 Calories, 42g Protein, 185g Carbs, 4g Fat (DF)"},
        {"name": "Tandoori Chicken with Yellow Rice & Curry Cauliflower", 
         "info": "930 Calories, 41g Protein, 161g Carbs, 51g Fat (GF)**"},
        {"name": "Jerk Chicken with Plantains & Vegetables", 
         "info": "817 Calories, 39g Protein, 68g Carbs, 51g Fat (GF, DF)**"},
        {"name": "Chicken Sausage with Peppers & Potatoes", 
         "info": "481 Calories, 27g Protein, 46g Carbs, 22g Fat**"}
    ],
    "Seafood": [
        {"name": "BBQ Atlantic Salmon with Squash & Potatoes", 
         "info": "580 Calories, 30g Protein, 80g Carbs, 30g Fat (GF, DF)"},
        {"name": "Simply Seared Salmon with Quinoa Pilaf & Mixed Vegetables", 
         "info": "580 Calories, 29g Protein, 30g Carbs, 38g Fat (GF, DF)"},
        {"name": "Pesto Salmon with Farro Pilaf & Brussels Sprouts", 
         "info": "715 Calories, 30g Protein, 45g Carbs, 46g Fat (GF, DF)"}
    ],
    "Meat": [
        {"name": "Mediterranean Turkey Meatballs with Lentils", 
         "info": "613 Calories, 60g Protein, 85g Carbs, 4g Fat (DF)"},
        {"name": "Beef Meatloaf with Mashed Potatoes & Green Beans", 
         "info": "526 Calories, 30g Protein, 61g Carbs, 14g Fat"}
    ],
    "Pasta": [
        {"name": "Rasta Pasta (Vegetarian, Chicken, Shrimp, or Salmon)", 
         "info": ("Veg: 563 Calories, 18g Protein, 88g Carbs, 16g Fat\n"
                  "Chicken: 692 Calories, 42g Protein, 88g Carbs, 18g Fat\n"
                  "Shrimp: 787 Calories, 58g Protein, 97g Carbs, 16g Fat\n"
                  "Salmon: 724 Calories, 40g Protein, 88g Carbs, 23g Fat")},
        {"name": "Lasagna with Garlic Bread & Broccoli", 
         "info": ("Chicken: 851 Calories, 57g Protein, 61g Carbs, 47g Fat\n"
                  "Beef: 1021 Calories, 48g Protein, 50g Carbs, 59g Fat")}
    ],
    "Bowls": [
        {"name": "Harvest Grain Bowl (Vegetarian, Chicken, Shrimp, or Beef)", 
         "info": ("Veg: 1367 Calories, 33g Protein, 150g Carbs, 75g Fat\n"
                  "Chicken: 1464 Calories, 57g Protein, 150g Carbs, 78g Fat")},
        {"name": "Taco Bowl (Vegetarian, Chicken, Shrimp, or Beef)", 
         "info": ("Veg: 1047 Calories, 30g Protein, 220g Carbs, 6g Fat\n"
                  "Chicken: 1137 Calories, 57g Protein, 205g Carbs, 10g Fat")}
    ],
    "Meal Prep Packages": [
        {"name": "1 Meal", "info": "$15.50"},
        {"name": "7 Meals", "info": "$15.02 each"},
        {"name": "10 Meals", "info": "$14.68 each"},
        {"name": "12 Meals", "info": "$14.18 each"},
        {"name": "14 Meals", "info": "$13.32 each"}
    ]
}

# Universal toggle for nutritional info
show_nutrition = st.checkbox("Show nutritional information")

# Display each category
for category, items in menu.items():
    with st.expander(category):
        for item in items:
            st.markdown(f"**{item['name']}**")
            if show_nutrition:
                st.write(item['info'])

# Footer
st.write("---")
st.write("Choose your meals and enjoy healthy, balanced options!")

# ============================================
# Ocean Plastic Pollution Mapping
# Data Analytics Project
# ============================================


# Import Libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium



# ============================================
# Creating Dataset
# ============================================

data = pd.DataFrame({

    "Location": [
        "Mumbai",
        "Chennai",
        "Goa",
        "Kochi",
        "Visakhapatnam",
        "Pune",
        "Kolkata"
    ],


    "Latitude": [
        19.0760,
        13.0827,
        15.2993,
        9.9312,
        17.6868,
        18.5204,
        22.5726
    ],


    "Longitude": [
        72.8777,
        80.2707,
        74.1240,
        76.2673,
        83.2185,
        73.8567,
        88.3639
    ],


    "Plastic_Tonnage": [
        250,
        180,
        120,
        90,
        150,
        70,
        210
    ],


    "Source": [
        "Citizen Science",
        "Survey",
        "Mapping Project",
        "Citizen Science",
        "Survey",
        "Research Data",
        "Cleaning Project"
    ]

})


# Display Dataset

print("Ocean Plastic Pollution Dataset")
print(data)



# ============================================
# Data Analysis
# ============================================


print("\nTotal Plastic Pollution:")

total = data["Plastic_Tonnage"].sum()

print(total,"Tonnes")



# Highest Pollution Area

highest = data.loc[
    data["Plastic_Tonnage"].idxmax()
]


print("\nHighest Pollution Location:")

print(highest["Location"])

print(
    highest["Plastic_Tonnage"],
    "Tonnes"
)



# ============================================
# Bar Chart
# ============================================


plt.figure(figsize=(10,5))


sns.barplot(
    x="Location",
    y="Plastic_Tonnage",
    data=data
)


plt.title(
    "Ocean Plastic Pollution by Location"
)


plt.xlabel(
    "Location"
)


plt.ylabel(
    "Plastic Waste (Tonnes)"
)


plt.xticks(rotation=45)


plt.show()



# ============================================
# Pie Chart
# ============================================


plt.figure(figsize=(7,7))


plt.pie(

    data["Plastic_Tonnage"],

    labels=data["Location"],

    autopct="%1.1f%%"

)


plt.title(
    "Plastic Pollution Distribution"
)


plt.show()



# ============================================
# Geographical Mapping
# ============================================


ocean_map = folium.Map(

    location=[20,78],

    zoom_start=5

)



for index,row in data.iterrows():


    folium.CircleMarker(


        location=[

            row["Latitude"],

            row["Longitude"]

        ],


        radius=row["Plastic_Tonnage"]/20,


        popup=(

            row["Location"]

            +"<br>Plastic: "

            +str(row["Plastic_Tonnage"])

            +" Tonnes"

        ),


        color="red",


        fill=True


    ).add_to(ocean_map)




# Save Map


ocean_map.save(
    "Ocean_Plastic_Pollution_Map.html"
)



print(
"\nMap Created Successfully!"
)


print(
"Open Ocean_Plastic_Pollution_Map.html file to see map"
)

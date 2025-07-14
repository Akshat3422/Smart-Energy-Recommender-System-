import streamlit as st
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset from pickle
with open("smart_home_energy_consumption_large.pkl", "rb") as file:
    dataset = pickle.load(file)

# Ensure Home ID is an integer column
if "Home ID" in dataset.columns:
    dataset["Home ID"] = dataset["Home ID"].astype(int)

st.title("💡 Smart Energy Consumption Recommender")

# User input
user_input = st.text_input("Enter Household ID", "1234")

def recommend_energy_saving(user_id):
    recommendations = []  # Initialize list

    try:
        user_id = int(user_id)  # Convert input to integer
        user_data = dataset[dataset["Home ID"] == user_id]

        if user_data.empty:
            return ["⚠️ Household ID not found."]
        
        category = user_data["consumption_category"].iloc[0]

        if category == "High":
            recommendations.append("⚡ Reduce peak hour usage (6-9 PM).")
            recommendations.append("🔄 Use energy-efficient appliances.")
            recommendations.append("🌞 Consider solar panel installation.")
        
        elif category == "Medium":
            recommendations.append("🔄 Optimize heavy appliance usage.")
            recommendations.append("⏳ Run appliances at off-peak hours.")
        
        else:
            recommendations.append("✅ You have efficient energy usage. Keep it up!")

    except ValueError:
        return ["⚠️ Please enter a valid numeric Household ID."]
    
    return recommendations

if st.button("Get Recommendations"):
    recommendations = recommend_energy_saving(user_input)
    st.subheader(f"Recommendations for Household {user_input}:")
    for rec in recommendations:
        st.write("✔️", rec)

# Show Clustering Visualization
st.subheader("Energy Consumption Clusters")

fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(x=dataset["Hour"], y=dataset["Energy Consumption (kWh)"], hue=dataset["consumption_category"], palette="viridis", ax=ax)
ax.set_xlabel("Hour of Day")
ax.set_ylabel("Energy Consumption (kWh)")
ax.set_title("Household Energy Consumption Clusters")

# Display plot in Streamlit
st.pyplot(fig)

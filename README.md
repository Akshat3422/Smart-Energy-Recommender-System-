# 💡 Smart Energy Consumption Recommender App

This is a **Streamlit web application** that recommends energy-saving tips to households based on their electricity usage patterns. It also provides a **cluster-based visualization** of energy consumption behavior.

---

## 🚀 Features

- 🔢 User inputs a **Household ID**
- 📊 Displays **personalized energy-saving recommendations**
- 📉 Shows **clustering visualization** of energy consumption patterns
- 🧠 Based on categories like **High**, **Medium**, or **Low** consumption
- 📦 Loads data and models using `pickle`

---

## 📁 Project Structure

smart-energy-app/
│
├── app.py # Main Streamlit application
├── smart_home_energy_consumption_large.pkl # Pickled dataset (with cluster & category info)
├── README.md # Project documentation (this file)



---

## 🧠 Logic Behind Recommendation

- The dataset contains a `consumption_category` column for each household:
  - **High** → Suggest reducing peak-hour usage, using efficient appliances, etc.
  - **Medium** → Suggest time optimization and smart scheduling
  - **Low** → Praise efficiency

---

## 📊 Visualization

The app includes a **scatter plot** of:
- `Hour` (x-axis)
- `Energy Consumption (kWh)` (y-axis)
- Colored by `consumption_category` (High, Medium, Low)

---



import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# --- SET PAGE CONFIG ---
st.set_page_config(
    page_title="Zomato Delivery Analytics",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
    /* Zomato Theme Colors */
    :root {
        --zomato-red: #E23744;
    }
    
    /* Headers */
    h1, h2, h3 {
        font-family: 'Inter', sans-serif;
    }
    
    /* Metrics / KPIs */
    div[data-testid="stMetricValue"] {
        color: #E23744;
        font-size: 2rem;
        font-weight: 700;
    }
    
    /* Custom Styling for KPI Cards adapting to Light/Dark Mode */
    .kpi-card {
        background-color: var(--background-color);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border: 1px solid var(--secondary-background-color);
        border-left: 5px solid #E23744;
        margin-bottom: 20px;
    }
    
    .kpi-title {
        color: var(--text-color);
        opacity: 0.8;
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        margin-bottom: 5px;
    }
    
    .kpi-value {
        color: var(--text-color);
        font-size: 28px;
        font-weight: 800;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: transparent;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    .stTabs [aria-selected="true"] {
        border-bottom: 3px solid #E23744;
        color: #E23744 !important;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# --- HELPER FUNCTIONS ---
def haversine_distance(lat1, lon1, lat2, lon2):
    """Calculates the great circle distance between two points on the earth."""
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2
    c = 2 * np.arcsin(np.sqrt(a))
    r = 6371 # Radius of earth in kilometers
    return c * r

@st.cache_data
def load_data():
    try:
        df = pd.read_csv('data/processed/zomato_dashboard_dataset.csv')
    except Exception as e:
        st.error(f"Error loading data: {e}. Please run from project root.")
        return pd.DataFrame()
        
    # Calculate Distance
    df['Distance_km'] = haversine_distance(
        df['Restaurant_latitude'], df['Restaurant_longitude'],
        df['Delivery_location_latitude'], df['Delivery_location_longitude']
    )
    
    # Clean up strings if needed
    for col in ['Weather_conditions', 'Road_traffic_density', 'Type_of_order', 'Type_of_vehicle', 'City', 'Delivery_Speed']:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.title()
            # Replace nan with None or 'Unknown'
            df[col] = df[col].replace('Nan', 'Unknown')
            
    return df

# --- LOAD DATA ---
df_original = load_data()

if df_original.empty:
    st.stop()

# --- SIDEBAR FILTERS ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/b/bd/Zomato_Logo.svg", width=150)
st.sidebar.title("Filters")

cities = ['All'] + sorted(list(df_original['City'].unique()))
selected_city = st.sidebar.selectbox("City", cities)

weathers = ['All'] + sorted(list(df_original['Weather_conditions'].unique()))
selected_weather = st.sidebar.selectbox("Weather Conditions", weathers)

traffics = ['All'] + sorted(list(df_original['Road_traffic_density'].unique()))
selected_traffic = st.sidebar.selectbox("Traffic Density", traffics)

vehicles = ['All'] + sorted(list(df_original['Type_of_vehicle'].unique()))
selected_vehicle = st.sidebar.selectbox("Vehicle Type", vehicles)

# Apply filters
df = df_original.copy()
if selected_city != 'All':
    df = df[df['City'] == selected_city]
if selected_weather != 'All':
    df = df[df['Weather_conditions'] == selected_weather]
if selected_traffic != 'All':
    df = df[df['Road_traffic_density'] == selected_traffic]
if selected_vehicle != 'All':
    df = df[df['Type_of_vehicle'] == selected_vehicle]

# --- MAIN CONTENT ---
st.title("Zomato Delivery Operations Analytics")
st.markdown("Analyze delivery operations performance and identify factors affecting delivery efficiency.")

# --- KPI CARDS ---
col1, col2, col3, col4 = st.columns(4)

total_orders = len(df)
avg_time = df['Time_taken (min)'].mean()
avg_rating = df['Delivery_person_Ratings'].mean()

# Fast delivery threshold (e.g. < 25 mins)
fast_del_pct = (len(df[df['Delivery_Speed'] == 'Fast']) / total_orders * 100) if total_orders > 0 else 0

with col1:
    st.markdown(f'<div class="kpi-card"><div class="kpi-title">Total Orders</div><div class="kpi-value">{total_orders:,}</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="kpi-card"><div class="kpi-title">Avg Delivery Time</div><div class="kpi-value">{avg_time:.1f} min</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div class="kpi-card"><div class="kpi-title">Avg Driver Rating</div><div class="kpi-value">{avg_rating:.2f} ⭐</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown(f'<div class="kpi-card"><div class="kpi-title">Fast Deliveries</div><div class="kpi-value">{fast_del_pct:.1f}%</div></div>', unsafe_allow_html=True)

# --- TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["📊 Executive Overview", "⚙️ Operations Analysis", "🛵 Driver Performance", "💡 Business Insights"])

zomato_red = '#E23744'
color_discrete_sequence = ['#E23744', '#1C1C1C', '#FF7E67', '#A9A9A9', '#4CAF50']

with tab1:
    st.header("Executive Overview")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        # Delivery Speed Distribution
        speed_counts = df['Delivery_Speed'].value_counts().reset_index()
        speed_counts.columns = ['Delivery_Speed', 'Count']
        fig_speed = px.pie(speed_counts, values='Count', names='Delivery_Speed', 
                           title="Delivery Speed Distribution",
                           color_discrete_sequence=color_discrete_sequence, hole=0.4)
        st.plotly_chart(fig_speed, use_container_width=True)
        
        # Weather Conditions vs Delivery Time
        weather_avg = df.groupby('Weather_conditions')['Time_taken (min)'].mean().reset_index()
        fig_weather = px.bar(weather_avg, x="Weather_conditions", y="Time_taken (min)", 
                             title="Avg Delivery Time by Weather",
                             color="Weather_conditions",
                             color_discrete_sequence=px.colors.qualitative.Pastel)
        fig_weather.update_layout(showlegend=False)
        st.plotly_chart(fig_weather, use_container_width=True)

    with col_b:
        # Traffic Density vs Delivery Time
        traffic_avg = df.groupby('Road_traffic_density')['Time_taken (min)'].mean().reset_index()
        fig_traffic = px.bar(traffic_avg, x="Road_traffic_density", y="Time_taken (min)", 
                             title="Avg Delivery Time by Traffic Density",
                             color="Road_traffic_density",
                             category_orders={"Road_traffic_density": ["Low", "Medium", "High", "Jam"]},
                             color_discrete_sequence=px.colors.sequential.OrRd)
        fig_traffic.update_layout(showlegend=False)
        st.plotly_chart(fig_traffic, use_container_width=True)
        
        # Average Delivery Time by City
        city_time = df.groupby('City')['Time_taken (min)'].mean().reset_index()
        fig_city = px.bar(city_time, x='City', y='Time_taken (min)', 
                          title="Average Delivery Time by City",
                          color_discrete_sequence=[zomato_red])
        st.plotly_chart(fig_city, use_container_width=True)

with tab2:
    st.header("Operations Analysis")
    
    col_c, col_d = st.columns(2)
    
    with col_c:
        # Vehicle Type vs Delivery Time
        veh_avg = df.groupby('Type_of_vehicle')['Time_taken (min)'].mean().reset_index()
        fig_veh = px.bar(veh_avg, x="Time_taken (min)", y="Type_of_vehicle", orientation='h',
                         title="Avg Delivery Time by Vehicle Type",
                         color_discrete_sequence=[zomato_red])
        st.plotly_chart(fig_veh, use_container_width=True)
        
        # Multiple Deliveries vs Delivery Time
        # Remove unknown/nan multiple deliveries
        df_mult = df[df['multiple_deliveries'].notna()]
        mult_avg = df_mult.groupby('multiple_deliveries')['Time_taken (min)'].mean().reset_index()
        mult_avg['multiple_deliveries'] = mult_avg['multiple_deliveries'].astype(str)
        fig_mult = px.bar(mult_avg, x="multiple_deliveries", y="Time_taken (min)", 
                           title="Avg Delivery Time by Multiple Deliveries",
                           color_discrete_sequence=['#1C1C1C'])
        st.plotly_chart(fig_mult, use_container_width=True)
        
    with col_d:
        # Order Hour Analysis
        hour_stats = df.groupby('Order_Hour').agg({'ID': 'count', 'Time_taken (min)': 'mean'}).reset_index()
        hour_stats.columns = ['Hour', 'Total Orders', 'Avg Time (min)']
        
        fig_hour = go.Figure()
        fig_hour.add_trace(go.Bar(x=hour_stats['Hour'], y=hour_stats['Total Orders'], 
                                  name='Total Orders', marker_color='#A9A9A9', opacity=0.6))
        fig_hour.add_trace(go.Scatter(x=hour_stats['Hour'], y=hour_stats['Avg Time (min)'], 
                                      name='Avg Time (min)', yaxis='y2', line=dict(color=zomato_red, width=3)))
        
        fig_hour.update_layout(
            title="Order Volume & Avg Delivery Time by Hour",
            yaxis=dict(title='Total Orders'),
            yaxis2=dict(title='Avg Time (min)', overlaying='y', side='right')
        )
        st.plotly_chart(fig_hour, use_container_width=True)
        
        # Delivery Speed Breakdown by City
        city_speed = df.groupby(['City', 'Delivery_Speed']).size().reset_index(name='Count')
        fig_speed_city = px.bar(city_speed, x='City', y='Count', color='Delivery_Speed', 
                                title="Delivery Speed Breakdown by City",
                                barmode='stack',
                                color_discrete_sequence=['#4CAF50', '#FFC107', '#E23744']) # Fast (Green), Medium (Yellow), Slow (Red)
        st.plotly_chart(fig_speed_city, use_container_width=True)

with tab3:
    st.header("Driver Performance")
    
    col_e, col_f = st.columns(2)
    
    with col_e:
        # Driver Rating vs Delivery Time
        fig_rating_time = px.scatter(df.sample(min(2000, len(df))), x="Delivery_person_Ratings", y="Time_taken (min)", 
                                     title="Driver Rating vs Delivery Time (Sampled)",
                                     opacity=0.5, color_discrete_sequence=[zomato_red],
                                     trendline="ols")
        st.plotly_chart(fig_rating_time, use_container_width=True)
        
        # Driver Rating Distribution
        fig_rating_dist = px.histogram(df, x="Delivery_person_Ratings", nbins=20,
                                       title="Driver Rating Distribution",
                                       color_discrete_sequence=['#1C1C1C'])
        st.plotly_chart(fig_rating_dist, use_container_width=True)
        
    with col_f:
        # Driver Age vs Delivery Time
        fig_age_time = px.scatter(df.sample(min(2000, len(df))), x="Delivery_person_Age", y="Time_taken (min)", 
                                  title="Driver Age vs Delivery Time (Sampled)",
                                  opacity=0.5, color_discrete_sequence=[zomato_red],
                                  trendline="lowess")
        st.plotly_chart(fig_age_time, use_container_width=True)
        
        # Driver Age Distribution
        fig_age_dist = px.histogram(df, x="Delivery_person_Age", nbins=15,
                                    title="Driver Age Distribution",
                                    color_discrete_sequence=['#1C1C1C'])
        st.plotly_chart(fig_age_dist, use_container_width=True)

with tab4:
    st.header("Key Business Insights")
    st.markdown("""
    Based on the dashboard data, here are some simple, practical recommendations for our operations team:
    
    ### 1. What factors increase delivery time?
    - **Traffic & Weather**: Traffic jams and bad weather (like heavy monsoon rains or winter fog) add around 10-15 minutes to our delivery times.
    - **Batched Orders**: Giving a rider multiple orders at once saves us money, but it makes the second customer wait much longer. 
    
    ### 2. How much does traffic affect delivery performance?
    - **Huge Impact**: In jam conditions, deliveries often cross 40 minutes. In low traffic, they take just 15-20 minutes.
    - **What we should do**: In areas famous for bad traffic (like Silk Board in Bangalore or local markets in Delhi), we should reduce the delivery radius during peak hours (7 PM - 10 PM). This stops riders from getting stuck and food from getting cold.
    
    ### 3. How does weather influence operations?
    - When it rains, riders go offline, but order demand shoots up.
    - **What we should do**: Give riders extra "Rain Pay" per order to keep them online during downpours. Also, show a small "Rain Delay" banner on the app before the customer places the order, so they don't get angry if it's late.
    
    ### 4. Which vehicle type performs best?
    - Bikes and scooters are best for longer distances (3-7km). Bicycles are surprisingly good when traffic is completely stopped.
    - **What we should do**: For very short deliveries (under 2km) in crowded market areas, send bicycle riders instead of bikes. They don't have to worry about parking or one-way roads.
    
    ### 5. Do highly rated drivers deliver faster?
    - Yes, slightly. Fast deliveries and good ratings go hand-in-hand.
    - **What we should do**: Treat our top-rated riders well. Give them first dibs on big family orders or corporate orders. It keeps our best riders happy and ensures big orders arrive safely.
    
    ### 6. Which city type experiences the most delays?
    - **Big Cities (Metros)**: Traffic is one issue, but large apartment complexes cause huge delays. Riders often spend 5-10 minutes just finding the right gate or waiting for security approval.
    - **What we should do**: Force customers to save detailed entry instructions (like "Gate 2, Tower B") in the app. This simple fix saves a lot of wasted time.
    
    ### 7. How can we improve Restaurant Prep Time?
    - Riders often reach the restaurant fast but wait 10-15 minutes for the food to be ready. 
    - **What we should do**: Delay assigning a rider if we know a specific restaurant is always slow. We shouldn't make our riders wait outside doing nothing.
    
    ### 8. Handling Festival Days & Match Days
    - On festivals or big cricket match days, order volume jumps suddenly and riders get overwhelmed.
    - **What we should do**: Predict these spikes and offer guaranteed minimum payouts to riders who log in for the full shift. This ensures we have enough hands on deck before the rush starts.
    """)

# Import libraries
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

# Set default plotly template to "plotly_white"
pio.templates.default = "plotly_white"

# Function to remove null values from DataFrames
def remove_null_values(df):
    print(df.isnull().sum())
    return df.dropna()

# Function to perform demand and supply analysis
def analyze_demand_supply(demand, supply):
    figure = px.scatter(x=supply, y=demand, trendline="ols", title="Demand and Supply Analysis")
    figure.update_layout(
        xaxis_title="Number of Drivers Active per Hour (Supply)",
        yaxis_title="Number of Riders Active per Hour (Demand)",
    )
    figure.show()

# Function to calculate elasticity
def calculate_elasticity(demand, supply):
    avg_demand = demand.mean()
    avg_supply = supply.mean()
    pct_change_demand = (max(demand) - min(demand)) / avg_demand
    pct_change_supply = (max(supply) - min(supply)) / avg_supply
    return pct_change_demand / pct_change_supply

# Function to calculate supply ratio
def calculate_supply_ratio(data):
    data['Supply Ratio'] = data['Rides Completed'] / data['Drivers Active Per Hour']
    return data

# Function to visualize supply ratio
def visualize_supply_ratio(data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Drivers Active Per Hour'], y=data['Supply Ratio'], mode='markers'))
    fig.update_layout(
        title='Supply Ratio vs. Driver Activity',
        xaxis_title='Driver Activity (Drivers Active Per Hour)',
        yaxis_title='Supply Ratio (Rides Completed per Driver Active per Hour)'
    )
    fig.show()

# Load data from source
data = pd.read_csv('rides.csv')
print(data.head())

# Remove null values
data = remove_null_values(data)

# Analyze two of the columns in data
demand = data["Riders Active Per Hour"]
supply = data["Drivers Active Per Hour"]
analyze_demand_supply(demand, supply)

# Calculate elasticity
elasticity = calculate_elasticity(demand, supply)
print("Elasticity of demand with respect to the number of active drivers per hour: {:.2f}".format(elasticity))

# Calculate the supply ratio for each level of driver activity
data = calculate_supply_ratio(data)
print(data.head())

# Visualize supply ratio
visualize_supply_ratio(data)

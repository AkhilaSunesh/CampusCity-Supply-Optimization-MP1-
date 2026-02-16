import pulp
import pandas as pd

# Warehouses
warehouses = {
    "WH_NORTH": {"capacity": 400, "construction": 300000, "operational": 800},
    "WH_SOUTH": {"capacity": 350, "construction": 280000, "operational": 700},
    "WH_EAST": {"capacity": 450, "construction": 320000, "operational": 900}
}

# Facilities
facilities = {
    "MED_CENTER": 80,
    "ENG_BUILDING": 30,
    "SCIENCE_HALL": 35,
    "DORM_A": 55,
    "DORM_B": 45,
    "LIBRARY": 25
}

days = 365
budget = 1500000

# Annualize demand
annual_demand = {f: d*days for f,d in facilities.items()}

# Annualize warehouse cost
annual_cost = {}
annual_capacity = {}

for w,data in warehouses.items():
    construction_annual = data["construction"]/10
    operational_annual = data["operational"]*days
    annual_cost[w] = construction_annual + operational_annual
    annual_capacity[w] = data["capacity"]*days

# Random transportation cost example
import random
transport_cost = {(w,f): random.uniform(3.8,4.8)
                  for w in warehouses
                  for f in facilities}

# Model
model = pulp.LpProblem("Campus_Distribution", pulp.LpMinimize)

x = pulp.LpVariable.dicts("ship",
                          (warehouses, facilities),
                          lowBound=0)

y = pulp.LpVariable.dicts("select",
                          warehouses,
                          cat="Binary")

# Objective
model += (
    pulp.lpSum(transport_cost[w,f]*x[w][f]
               for w in warehouses
               for f in facilities)
    +
    pulp.lpSum(annual_cost[w]*y[w]
               for w in warehouses)
)

# Demand constraints
for f in facilities:
    model += pulp.lpSum(x[w][f] for w in warehouses) == annual_demand[f]

# Capacity constraints
for w in warehouses:
    model += pulp.lpSum(x[w][f] for f in facilities) <= annual_capacity[w]*y[w]

# Select exactly 2 warehouses
model += pulp.lpSum(y[w] for w in warehouses) == 2

# Budget constraint
model += model.objective <= budget

# Solve
model.solve()

print("Status:", pulp.LpStatus[model.status])
print("Total Cost:", pulp.value(model.objective))

# Supply Chain Optimization Model

## 1. Parameters

### Annual Demand
To calculate the total demand for facility $f$:

$$
D_f^{\text{annual}} = D_f^{\text{daily}} \times 365
$$

**Example Calculation:**

270 x 365 = 98,550 


### Annual Capacity
To calculate the total capacity for warehouse $w$:

$$
Cap_w^{\text{annual}} = Cap_w^{\text{daily}} \times 365
$$

### Costs
**Construction Cost (Annualized over 10 years):**
$$
C_w^{\text{annual}} = \frac{\text{Construction Cost}_w}{10}
$$

**Operational Cost (Annual):**
$$
O_w^{\text{annual}} = \text{Operational Cost}_w \times 365
$$

---

## 2. Decision Variables

### Binary Variable (Location Selection)
$$
y_w =
\begin{cases}
1 & \text{if warehouse } w \text{ is selected} \\
0 & \text{otherwise}
\end{cases}
$$

### Continuous Variable (Flow)
$$
x_{wf} = \text{annual units shipped from warehouse } w \text{ to facility } f
$$

---

## 3. Objective Function

**Goal:** Minimize Total Annual Cost (Transportation + Facility Costs)

$$
\min Z = \sum_{w \in W} \sum_{f \in F} c_{wf} x_{wf} + \sum_{w \in W} \left( C_w^{\text{annual}} + O_w^{\text{annual}} \right) y_w
$$

## 4. Constraints

### 1. Demand Satisfaction
Each facility must receive its full annual demand:

$$
\sum_{w \in W} x_{wf} = D_f^{\text{annual}} \quad \forall f \in F
$$

### 2. Capacity Constraint
The total flow from a warehouse cannot exceed its capacity (and is zero if the warehouse is not open):

$$
\sum_{f \in F} x_{wf} \leq Cap_w^{\text{annual}} \cdot y_w \quad \forall w \in W
$$

### 3. Warehouse Selection Constraint
Exactly 2 warehouses must be selected:

$$
\sum_{w \in W} y_w = 2
$$

### 4. Budget Constraint
The total cost must be within the specified budget:

$$
\text{Total Annual Cost} \leq 1,500,000
$$

### 5. Non-Negativity & Integrality

$$
\begin{aligned}
x_{wf} &\geq 0 \\
y_w &\in \{0, 1\}
\end{aligned}
$$

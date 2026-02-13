# Campus City Emergency Supply Distribution Optimization

**Course:** 24MAT382 - Computational Optimization & Applications  
**Institution:** Saintgits College of Engineering (Autonomous)  
**Project Type:** Micro-Project (Real-Time Optimization)

### Student Details
**Name:** Akhila Sunesh <br> 
**Batch:** CS-A <br>
**Sem:** VI <br>
**Roll No.** 16

---

## 📌 Project Overview
This repository contains the computational implementation for the **Campus City Emergency Supply Distribution** problem.

The objective of this project is to design an optimal supply chain network for emergency resources across campus facilities. Using **Mixed-Integer Linear Programming (MILP)**, the model determines:
1. Which **two** warehouses to open (out of three candidates).
2. The optimal **shipment quantities** from warehouses to facilities.
3. A strategy that **minimizes total annual costs** (transportation + fixed operational costs) while satisfying demand, capacity, and budget constraints.

## 📂 Repository Structure
Per the Micro-Project guidelines, the repository is organized as follows:

```text
├── /src
│   └── main.py          # The complete executable Python source code
├── /data
│   ├── facilities.csv   # Dataset containing facility demands
│   └── warehouses.csv   # Dataset containing warehouse capacities and costs
├── Report.pdf           # Final Technical Report
└── README.md            # Project documentation (this file)

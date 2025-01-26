# TOPSIS Implementation in Python

## Overview

This project implements the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method, a multi-criteria decision-making technique. TOPSIS is used to rank alternatives based on their closeness to an ideal solution and a farthest solution. The steps in this implementation include data normalization, weighted normalization, distance calculation, and ranking.

---

## Steps in the Code

### 1. **Loading the Data**
The input data is loaded using `pd.read_csv()` from a CSV file containing alternatives and criteria.

### 2. **Normalization**
The values are normalized using the **Euclidean norm (L2 norm)** to make all columns comparable.

### 3. **Weighted Normalization**
The normalized matrix is multiplied by the weights of the criteria. By default, equal weights are assumed, but these can be customized.

### 4. **Ideal and Negative-Ideal Solutions**
- **Ideal Solution (Best):** Maximum values for beneficial criteria.
- **Negative-Ideal Solution (Worst):** Minimum values for beneficial criteria.

### 5. **Distance Calculation**
The Euclidean distance is calculated for each alternative from:
- The **Ideal Solution**.
- The **Negative-Ideal Solution**.

### 6. **TOPSIS Score**
The relative closeness to the ideal solution is computed using the formula:
\[
TOPSIS\_Score = \frac{D_{negative}}{D_{ideal} + D_{negative}}
\]
Where:
- \(D_{ideal}\): Distance to the ideal solution.
- \(D_{negative}\): Distance to the negative-ideal solution.

### 7. **Ranking**
Alternatives are ranked based on their TOPSIS scores. A higher score indicates a better alternative.

### 8. **Saving the Result**
The final results, including the TOPSIS scores and ranks, are saved to a new CSV file.

---

## How to Use

1. **Install Required Libraries**:
   Ensure you have Python installed along with the required libraries:
   ```bash
   pip install pandas numpy

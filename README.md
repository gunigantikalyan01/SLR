# Height vs. Weight Prediction — Simple Linear Regression

A machine learning project implementing **Simple Linear Regression** to model and predict human body weight (in kilograms) based on height (in meters) across **15 observations**.

---

## 📊 Dataset Overview
The dataset contains 15 clean, continuous records with zero missing values:

* **Independent Variable (X):** `Height` (in meters, ranging from `1.47` m to `1.83` m)
* **Dependent Variable (y):** `Weight` (in kilograms, ranging from `52.21` kg to `74.46` kg)

### Summary Statistics

| Metric | Height (m) | Weight (kg) |
| :--- | :---: | :---: |
| **Count** | 15 | 15 |
| **Mean** | 1.65 | 62.08 |
| **Std Dev** | 0.11 | 7.04 |
| **Min** | 1.47 | 52.21 |
| **Median (50%)** | 1.65 | 61.29 |
| **Max** | 1.83 | 74.46 |

---

## 📐 Mathematical Formulation & Results

Simple Linear Regression fits a straight line using Ordinary Least Squares (OLS) defined by:

\[ y = mX + c\]

Fitting the model to this dataset yields the following equation and performance metrics:

\[Weight = 61.2722 times {Height} - 39.0620\]

| Evaluation Metric | Value | Interpretation |
| :--- | :---: | :--- |
| **Slope (m)** | `61.2722` | Weight increases by ~61.27 kg per 1-meter increase in height |
| **Intercept (c)** | `-39.0620` | Theoretical baseline y-intercept |
| **R² Score** | `0.9892` | Height explains **98.92%** of the variance in weight |
| **Mean Squared Error (MSE)** | `0.4994` | Average squared prediction error |
| **Root Mean Squared Error (RMSE)** | `0.7067 kg` | Average prediction deviation in kilograms |
| **Mean Absolute Error (MAE)** | `0.5739 kg` | Average absolute error across all predictions |

## 👤 Author

**Guniganti Kalyan**  
Data Scientist  
* 📧 Email: [kalyanguniganti@gmail.com](mailto:kalyanguniganti@gmail.com)

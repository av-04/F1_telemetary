# 🏎️ F1 Telemetry Explorer

A Python-based telemetry analysis tool that allows users to compare Formula 1 driver performance in real-time. Built with **FastF1**, **Streamlit**, and **Matplotlib**.

## 🚀 Features
* **Dynamic Race Selection:** Automatically fetches the race calendar for any season (2020-2024).
* **Speed Trace Analysis:** Compare speed vs. distance for any two drivers.
* **Gap Analysis (Delta):** visualizes where one driver is gaining or losing time against another using linear interpolation.
* **Corner Visualization:** Highlights track sectors and braking zones.
* **Elo rating and Prediction of the next season:** Uses a Elo rating system named strat_score which uses the finishing position,overtaking and consistency
   $$\text{Strat\_Score} = \text{Base} + S_{\text{Finish}} + S_{\text{Overtake}} + S_{\text{Consistency}}$$
   By summing these three factors, the model can identify that a driver who started P20 and finished P8 might actually have performed better (higher score) than a driver who started P1 and finished P1, because       the recovery drive required more "Racecraft" and "Consistency.

## 🛠️ Tech Stack
* **Python 3.10+**
* **Streamlit** (Frontend/UI)
* **FastF1** (Data API & Processing)
* **Matplotlib & Seaborn** (Visualization)
* **Pandas & NumPy** (Data Manipulation)

## 🖼️ Screenshots
<img width="1919" height="935" alt="Screenshot 2025-12-07 031044" src="https://github.com/user-attachments/assets/7eca13ac-cb37-4a50-888c-509d950f68a6" />
<img width="1919" height="936" alt="Screenshot 2025-12-07 031053" src="https://github.com/user-attachments/assets/723ab731-03ba-4395-9da1-e6c190871555" />
<img width="1252" height="1318" alt="b1765bcdcb5f999d48a6c797863bbc22c1ae8da0c012126acd1e1271" src="https://github.com/user-attachments/assets/b6934903-550c-4a07-a43a-092ee48e7d79" />
<img width="1918" height="821" alt="image" src="https://github.com/user-attachments/assets/6a17a527-e509-4dcb-b785-4ec637c49a75" />



## 📦 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/f1-telemetry-app.git](https://github.com/YOUR_USERNAME/f1-telemetry-app.git)
   cd f1-telemetry-app






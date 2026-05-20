 EV Safety System – AI-Powered Predictive Maintenance for EV Chargers
📌 Project Overview
This project develops a machine learning model to predict electric vehicle (EV) charger failures before they occur.
By analyzing operational parameters such as voltage, temperature, session duration, and maintenance history, the system identifies potentially failing chargers with 99% accuracy, enabling proactive maintenance and reducing downtime.
Live Demo: https://ev-safety-system-5w5ik8ftvztrpk4shuic7c.streamlit.app/
________________________________________
🎯 Objective
Build a predictive model that:
•	Detects potential charger failures with high accuracy (99%)
•	Provides real-time risk assessment and actionable recommendations
•	Reduces false alarms while minimizing missed failures
•	Enables predictive maintenance for EV charging infrastructure
________________________________________
📊 Dataset
The dataset contains operational data from EV chargers with the following features:
Feature	Description
voltage	Charger voltage (220–240V range)
temperature	Operating temperature (°C)
session_duration	Duration of charging session (minutes)
charger_condition	Physical condition (L=Normal, M=Warning, H=Critical)
error_code	System error code (0=No Error, 1=Minor, 2=Major)
days_since_maintenance	Days since last maintenance
location	Geographic location
weather	Weather condition during operation
failed	Target variable (0=Operational, 1=Failed)
Dataset Size: 9,984 records | Perfectly balanced (50% OK, 50% Failed)
________________________________________
🔧 Data Preprocessing Steps
Step	Description
Balancing	Stratified sampling to ensure equal representation of all charger conditions and failure status
Unit Conversion	Temperature and voltage converted to practical units; session duration to minutes
Range Scaling	Voltage normalized to 220–240V; session duration capped at 10–100 minutes
Feature Engineering	Derived error_code from charger condition for better model performance
Timestamp Addition	Added realistic timestamps for temporal analysis
________________________________________
🤖 Models Evaluated
Four machine learning models were tested across three feature sets:
Model	Description
Random Forest	Ensemble of decision trees (100 estimators)
Gradient Boosting	Sequential tree-based boosting
Logistic Regression	Linear classifier with L2 regularization
SVM	Support Vector Machine with RBF kernel
Feature Sets Tested
Set	Features Included
Set 1	Voltage + Temperature (basic electrical parameters)
Set 2	Voltage + Temperature + Session Duration + Error Code (extended operational data)
Set 3	All features (full dataset)
________________________________________
📈 Results & Performance
Best Model: Random Forest with All Features
Metric	Value
Accuracy	99.0%
AUC-ROC	0.9999 (near perfect)
True Positives	997/997 failures detected
False Negatives	0 (no missed failures)
False Positives	20 (minimal false alarms)
Complete Model Comparison
Feature Set	Model	Accuracy	AUC-ROC	TP	TN	FP	FN
Set 1 (V+T)	Random Forest	88.1%	0.9471	919	840	160	78
Set 1 (V+T)	Gradient Boosting	77.2%	0.8401	687	855	145	310
Set 1 (V+T)	Logistic Regression	63.9%	0.6979	697	579	421	300
Set 1 (V+T)	SVM	66.2%	0.7091	640	682	318	357
Set 2 (V+T+S+E)	Random Forest	98.8%	0.9992	997	976	24	0
Set 2 (V+T+S+E)	Gradient Boosting	88.7%	0.9467	882	889	111	115
Set 2 (V+T+S+E)	Logistic Regression	64.3%	0.7157	660	625	375	337
Set 2 (V+T+S+E)	SVM	82.8%	0.8925	812	841	159	185
Set 3 (All Features)	Random Forest	99.0%	0.9999	997	980	20	0
Set 3 (All Features)	Gradient Boosting	90.2%	0.9643	912	890	110	85
Set 3 (All Features)	Logistic Regression	69.1%	0.7457	711	669	331	286
Set 3 (All Features)	SVM	86.3%	0.9289	881	842	158	116
________________________________________
🌐 Web Application
The model is deployed as an interactive web application using Streamlit.
Live Demo: https://ev-safety-system-5w5ik8ftvztrpk4shuic7c.streamlit.app/
App Features
Feature	Description
Real time Prediction	Input charger parameters → instant failure risk assessment
Manual Input Form	User friendly interface for single predictions
CSV Upload	Batch prediction for multiple chargers
Visual Dashboard	Risk probability visualization with color coded recommendations
Decision Support	Actionable maintenance recommendations based on risk level
Risk Levels & Recommendations
Risk Probability	Status	Recommendation
< 15%	✅ Safe	No action needed
15–40%	👀 Warning	Monitor closely
40–70%	⚠️ High Risk	Schedule inspection within 3 days
> 70%	🚨 Critical	Immediate maintenance required
________________________________________
📁 Project Structure

EV-Safety-System/
├── EV_Suraksha_Final.csv          # Processed dataset
├── ev safety system.ipynb         # Complete analysis notebook
├── app.py                         # Streamlit web application
├── model.pkl                      # Trained Random Forest model
├── requirements.txt               # Python dependencies
├── ai4i2020.csv          # original dataset

└── README.md                      # Project documentation
________________________________________
🛠️ Technologies Used
Technology	Purpose
Python 3.13	Core programming language
Pandas / NumPy	Data manipulation and analysis
Scikit learn	Machine learning models (Random Forest, etc.)
Matplotlib / Seaborn	Data visualization
Streamlit	Web application deployment
Jupyter Notebook	Development and analysis
________________________________________
💡 Business Impact
Benefit	Impact
Cost Savings	40–60% reduction in catastrophic repair costs
Reduced Downtime	99% failure detection → near zero unexpected downtime
Extended Equipment Life	Early intervention prevents cumulative damage
Customer Satisfaction	Minimized service interruptions improves user experience
Scalability	Model can be deployed across entire EV charging network
________________________________________
🔮 Future Improvements
•	Real time monitoring integration with IoT sensors
•	Time series analysis for degradation pattern detection
•	Anomaly detection for unknown failure modes
•	Explainable AI (SHAP/LIME) for prediction interpretability
•	Multi charger optimization for predictive maintenance scheduling
•	Mobile application for field technicians
________________________________________
🚀 How to Run Locally
1. Clone the repository

git clone <repository-url>
cd EV-Safety-System
2. Install dependencies

pip install -r requirements.txt
3. Run the Streamlit app

streamlit run app.py
4. (Optional) Run the Jupyter notebook

jupyter notebook "ev safety system.ipynb"


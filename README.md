# PhishGuard AI: Enterprise Data Pipeline for Phishing Detection

PhishGuard is an end-to-end AI-driven data engineering pipeline designed to identify and analyze malicious URLs. By combining Python-based Machine Learning with Enterprise Data Engineering principles, the system provides real-time threat intelligence and business-centric security insights.

# 🚀 Project Overview

This project satisfies the 6th-semester Data Science specialization requirements by implementing a complete life-cycle of data: from raw ingestion to predictive analytics and visualization.

# 🛠️ Mandatory Components (7/7 Implemented)

#	Component	Implementation Detail
1	**Data Ingestion:**	Automated ingestion of raw URL metadata via Python/Pandas.
2	**Data Storage:**	Medallion architecture: Raw (CSV) and Processed (Data Warehouse) storage.
3	**ELT Process:**	Automated cleaning, null-handling, and feature engineering.
4	**Data Modeling:**	Star Schema design with Fact (Scans) and Dimension (Result) tables.
5	**Visualization:**	Interactive Power BI Dashboard for threat monitoring.
6	**Business Insights:**	Correlation analysis between URL structure and phishing probability.
7	**End-to-End Pipeline:**	Fully automated workflow from raw input to dashboard refresh.

# 🤖 Machine Learning Features

    Model: Random Forest Classifier

    Input: 30+ structural features (URL length, SSL state, special characters).

    Target: Binary Classification (Safe vs. Phishing).

    Accuracy: ~95-97% (Dataset-dependent).

# 📁 Project Structure
Plaintext

PhishGuard_Project/
├── 01_Raw_Data/          # Original Kaggle CSV (phishing_raw.csv)
├── 02_Processed_Data/    # Modeled Star Schema (Fact_Scans.csv, Dim_Result.csv)
├── 03_Scripts/           # Python Pipeline (pipeline.py) and Flask API (app.py)
├── 04_Dashboard/         # Power BI File (.pbix)
└── README.md

# ⚙️ Setup & Installation

**1. Prerequisites**

    Python 3.10+

    Power BI Desktop (Windows)

    Git

**2. Installation**
Bash

# Clone the repository
git clone https://github.com/unreasonablecoder/PhisGuardAI.git

# Install dependencies
pip install pandas scikit-learn flask flask-cors joblib

**3. Running the Pipeline**
Bash

cd 03_Scripts
python pipeline.py

This will process the raw data, train the AI model, and generate the Fact/Dimension tables for Power BI.

# 📊 Business Insights

    Domain Red-Flags: 85% of phishing attempts utilize a prefix-suffix dash (-) in the domain.

    Structural Anomalies: URLs exceeding 75 characters show a high correlation with malicious intent.

    Security Recommendation: Implement automated flagging for external communications containing these specific structural markers.

# 👨‍💻 Author

**B. Navnit Kumar**
**B.Tech CSE (Data Science) | 6th Semester**
**Rungta College of Engineering and Technology (RCET Bhilai)**
**Chhattisgarh Swami Vivekanand Technical University**
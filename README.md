# ConfidenceIntervalVisualizer# 📊 Confidence Interval Visualizer

## 🎯 Project Overview  
This interactive dashboard helps visualize confidence intervals for population proportions by simulating random samples from a real-world dataset. The tool allows users to adjust the **sample size** and **number of samples**, displaying how the confidence interval changes with different sampling conditions.

## 🏗️ Features  
- ✅ **Interactive Visualization**: Adjustable sliders for sample size and number of samples  
- 📈 **Statistical Insights**: View confidence intervals dynamically  
- 🔗 **Kaggle Data Integration**: Automatically retrieves poll data using environment variables  

## 🔄 Workflow  
1. **Retrieve Dataset from Kaggle**  
   - Uses environment variables (`KAGGLE_USERNAME`, `KAGGLE_KEY`) to authenticate  
   - Downloads dataset automatically via the Kaggle API  

2. **Process the Data**  
   - Loads relevant columns for population proportions  
   - Draws random samples and calculates confidence intervals  

3. **Visualization with Dash**  
   - Stacked line plot of min, max, and point estimates  
   - Interactive UI for adjusting parameters  

## 🚀 Setup & Run  
```bash
pip install -r requirements.txt
python app.py
```

## 🛠️ CI/CD Integration  
- GitHub Actions pipeline for automated testing and environment setup  
- Ensures continuous deployment and correctness of the visualization  

## 📂 File Structure  
```
.
├── data/                   # Raw and processed datasets  
├── notebooks/              # Exploratory analysis in Jupyter Notebooks  
├── src/                    # Source code (data loading, visualization)  
├── tests/                  # Unit tests for sampling and visualization  
├── .github/workflows/ci.yml # GitHub Actions workflow  
├── app.py                  # Main dashboard application  
├── requirements.txt        # Python dependencies  
└── README.md               # Project documentation  
```

## 📌 Next Steps  
- Expand support for other statistical confidence intervals  
- Add bootstrap resampling methods  

---

💡 **Want to learn more?** Check out the source code and run it in your own environment! 🚀  

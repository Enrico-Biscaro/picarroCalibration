# Calibration of raw measurements from Picarro L2130-i and L2140-i Cavity Ring-Down Spectrometers (CRDS)

This repository contains the tools and workflow used to calibrate raw isotope measurements produced by Picarro L2130-i and L2140-i analyzers.

## 📁 1. Contents

#### 📝 Main calibration Jupyter Notebook  

 > 📓 `picarroCalibrationv01.ipynb`
The main Jupyter Notebook demonstrating the full calibration workflow:
> - **Import raw CRDS measurements** from Picarro **L2130-i** or **L2140-i** analyzers;  
> - **Detect and remove outliers** using either the **Median Absolute Deviation (MAD)**  or **Standard Deviation (SD)** method;
> - **Perform Simple Linear Regression** to generate calibration relationships; 
> - **Produce** a complete and detailed **final report of the run**. 


#### 🧰 Python utility modules

> - **📏 `calculateStandard.py`**  
  Function for computing standard values used during calibration.
> - **🔍 `detectOutliersMAD.py`**  
  Function to detect all the outliers of the run using the Median Absolute Deviation (MAD) method.
> - **📊 `outliersPlot.py`**  
  Tools for visualizing outliers and quality-control diagnostics.
> - **⚙️ `outliersRule.py`**  
  Function to select and remove specific injections from the run.
> - **📈 `regression.py`**  
    Functions for performing Simple Linear Regression and generating calibration relationships between raw measurements and known standards.

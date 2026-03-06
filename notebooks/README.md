# Research Notebooks
* **01_vix_spike_analysis.ipynb**: Analyzes the 60.72 VKOSPI record high.
* **02_hormuz_regime_modeling.ipynb**: Initial Parametric VaR testing.
## Create VIX Spike Analysis Notebook

### Subtask:
Create a new Jupyter notebook file named `01_vix_spike_analysis.ipynb` in the `notebooks/` directory. This notebook will be dedicated to analyzing the 60.72 VKOSPI record high.
%%writefile notebooks/01_vix_spike_analysis.ipynb
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# VIX Spike Analysis: Understanding the 60.72 VKOSPI Record High\n\nThis notebook is dedicated to analyzing the historical VKOSPI (Korea VIX) spike to 60.72, a record high. We will explore the context, implications, and potential correlations of this event."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.18"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}%%writefile notebooks/02_hormuz_regime_modeling.ipynb
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Hormuz Regime Modeling\n",
    "\n",
    "This notebook focuses on initial Parametric Value at Risk (VaR) testing related to the Hormuz regime and its impact on oil prices."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.18"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4import os

# Define paths to the notebooks
vix_notebook_path = 'notebooks/01_vix_spike_analysis.ipynb'
hormuz_notebook_path = 'notebooks/02_hormuz_regime_modeling.ipynb'

# Confirm the creation of the notebooks
print(f"Checking for {vix_notebook_path}: {os.path.exists(vix_notebook_path)}")
print(f"Checking for {hormuz_notebook_path}: {os.path.exists(hormuz_notebook_path)}")

# List contents of the notebooks directory to visually confirm
print("\nContents of 'notebooks/' directory:")
!ls -l notebooks/
}

## Summary:

### Q&A
Yes, both `01_vix_spike_analysis.ipynb` and `02_hormuz_regime_modeling.ipynb` files were successfully created in the `notebooks/` directory.

### Data Analysis Key Findings
*   The `01_vix_spike_analysis.ipynb` file, intended for analyzing the 60.72 VKOSPI record high, was successfully created in the `notebooks/` directory.
*   The `02_hormuz_regime_modeling.ipynb` file, focusing on Parametric Value at Risk (VaR) testing related to the Hormuz regime, was also successfully created in the `notebooks/` directory.
*   Verification using `os.path.exists()` returned `True` for both notebook paths, confirming their existence.
*   The `ls -l notebooks/` command further confirmed the presence of both `01_vix_spike_analysis.ipynb` and `02_hormuz_regime_modeling.ipynb` in the directory.

### Insights or Next Steps
*   The foundational Jupyter notebook files are in place, providing the structure for subsequent analytical tasks on VIX spike analysis and Hormuz regime modeling.
*   The next logical step is to populate these newly created notebooks with relevant code and data for the specified analyses.







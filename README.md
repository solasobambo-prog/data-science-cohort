# TS Academy — Data Science Cohort Coursework

Repository containing completed assignments, hands-on drills, and capstone notebooks for the **TS Academy Data Science Track**.

## Repository Structure

```text
data-science-cohort/
├── module-01-python-fundamentals/     # Core Python syntax, data structures, and control flow
├── module-02-data-manipulation/       # Pandas Series, DataFrames, filtering, and aggregation
├── module-03-cleaning-and-stats/      # Missingness audits, outlier detection, and descriptive statistics
└── README.md
```

*(Note: New module folders will be added sequentially as coursework progresses.)*

## Engineering & Notebook Standards

All notebooks in this repository adhere to the following reproducibility and analytical standards:

* **Restart-and-Run-All Discipline:** Every notebook executes cleanly top-to-bottom on a fresh kernel without hidden state or out-of-order dependencies.
* **Raw Data Preservation:** An untouched `raw_copy` snapshot is captured immediately upon loading so diagnostic reports always reflect initial dataset states.
* **Predict-Then-Verify Workflow:** Hypotheses regarding missingness, skewness, and outlier counts are documented prior to code execution and verified against live outputs.
* **Flag-Before-Fill:** Informative and structural missingness patterns are captured via boolean indicator columns before applying median, mode, or domain-driven imputations.
* **Honest Statistical Reporting:** Skewed distributions are summarized using `n`, median, and IQR alongside explicit caveats rather than relying solely on outlier-sensitive means.

## Tools & Environment

* **Languages & Libraries:** Python 3.x, `pandas`, `numpy`, `kagglehub`
* **Environments:** Google Colab & VS Code (Jupyter Notebooks)

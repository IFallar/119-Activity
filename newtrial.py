# Descriptive Analytics on file 'Plant Experiment.xlsx' 
# Work on Variable: Weight
# Load necessary packages
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
import researchpy as rp

df = pd.read_excel('PlantExperiment.xlsx')
df.isnull().values.any()
df.info()

# Exploratory Data Analysis
# Conduct Normality testing
# Null Hypothesis: The distribution is approximately normal

Wtx = df[(df['Group'] == 'Treatment')].Weight
Wcon = df[(df['Group'] == 'Control')].Weight
stats.anderson(Wtx, dist='norm')
stats.anderson(Wcon, dist='norm')
# Data Visualization - Boxplot

# %matplotlib inline

sns.set(style="whitegrid")
plt.figure(figsize=(10, 8))
ax = sns.boxplot(x='Group', y='Weight', data=df, orient="v")

# Data Visualization - Distribution plot
sns.set(style="whitegrid")
plt.figure(figsize=(10, 8))
bx = sns.distplot(df[df["Group"] == "Control"].Weight)
cx = sns.distplot(df[df["Group"] == "Treatment"].Weight)
# Conduct Test for Homogeneity
stats.levene(Wtx, Wcon, center='mean')

# Descriptive Analysis
Desc = df['Weight'].groupby(df['Group']).describe()
Desc.to_csv("DescRes1.csv")

# Inferential Analysis
# Condition: Distributions Approximately Normal | Variance is Homogenous

rp.ttest(Wtx, Wcon, equal_variances=True, paired=False)

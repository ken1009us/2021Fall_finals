# Data analysis of Bike Sharing - Big Data Systems

## Introduction

Bike sharing has become more popular in recent days. It not only serves as a new way to transit, but also a hobby for many people who prefer a more convenient way to ride.

The dataset includes the data of stations, trips, and weather in 3 cities: Montreal, Toronto, and Washington DC.

Our goal is to improve one data analysis of bike sharing on kaggle and to explore more details by adding two hypotheses in this project to make it more comprehensive.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install some modules.

```bash
pip install scipy
pip install seaborn
pip install numpy
pip import pandas
pip install matplotlib
```

## Preparation

Import scipy, seaborn, numpy, pandas, matplotlib, datetime.

```python
from scipy import stats

import seaborn as sns
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
```

## Data

Trip Dataframe

![image](https://github.com/ken1009us/2021Fall_finals/blob/main/image/trip.png "Trip Dataframe")

Station Dataframe

![image](https://github.com/ken1009us/2021Fall_finals/blob/main/image/station.png "Station Dataframe")

Weather Dataframe

![image](https://github.com/ken1009us/2021Fall_finals/blob/main/image/weather.png "Weather Dataframe")

## Output

Weather conditions:

prectot: Precipitation (mm day-1)\
qv2m : Specific Humidity at 2 Meters (g/kg)\
rh2m: Relative Humidity at 2 Meters (%)\
ps: Surface Pressure (kPa)\
t2m_range: Temperature Range at 2 Meters (C)\
ts: Earth Skin Temperature (C)\
t2mdew:  Dew/Frost Point at 2 Meters (C)\
t2mwet: Wet Bulb Temperature at 2 Meters (C)\
t2m_max: Maximum Temperature at 2 Meters (C)\
t2m_min: Minimum Temperature at 2 Meters (C)\
t2m: Temperature at 2 Meters (C)\
ws50m_range: Wind Speed Range at 50 Meters (m/s)\
ws10m_range: Wind Speed Range at 10 Meters (m/s)\
ws50m_min: Minimum Wind Speed at 50 Meters (m/s)\
ws10m_min: Minimum Wind Speed at 10 Meters (m/s)\
ws50m_max: Maximum Wind Speed at 50 Meters (m/s)\
ws10m_max: Maximum Wind Speed at 10 Meters (m/s)\
ws50m: Wind Speed at 50 Meters (m/s)\
ws10m: Wind Speed at 10 Meters (m/s)\

Hypothesis #1 - Total daily trips duration depends on weather conditions (Take Montreal for example)

Here are some scatter plots, they show us the correlation between weather conditions and total daily trips duration. I used the for loop to draw the scatter plot and set titles for each factor.

![image](https://github.com/ken1009us/2021Fall_finals/blob/main/image/hypo1-1.png "hypo1-1")

If we want to go through the correlation between each factor and total daily trips duration, we can use some statistical methods. We chose the Pearson correlation coefficient which is a measure of linear correlation between two sets of data. We got two numbers from the method. The first number is Pearson's r, which means a numerical summary of the strength of the linear association between the variables, and the second number is the probability that the true value of r is zero. We can find out that there is a linear relationship between the maximum temperature and total daily trips duration. By contrast, the maximum wind speed at 50 meters and total daily trips duration have the largest negative correlation.

![image](https://github.com/ken1009us/2021Fall_finals/blob/main/image/hypo1-2.png "Station Dataframe")

Here is a correlation matrix and every correlation matrix is symmetrical.

![image](https://github.com/ken1009us/2021Fall_finals/blob/main/image/correlation_matrix.png "correlation_matrix")

This is a heat map. We can clearly spot linear relationships between variables through the heat map.

![image](https://github.com/ken1009us/2021Fall_finals/blob/main/image/hypo1-3.png "Station Dataframe")


Hypothesis #2 - Club members ride longer in a trip

We aimed to verify if club members ride longer in a trip.

You can see that in Montreal, casual riders have a longer duration in a trip compared to the member riders.
The difference is about an average of 400 to 600 seconds. Six minutes to 10 minutes.

![image](https://github.com/ken1009us/2021Fall_finals/blob/main/image/hypo2-m.png "Station Dataframe")

For the Toronto area, this visualization couldn’t provide much information because the data of the member riders in the dataset is incomplete, so we couldn’t explore more for this area based on this hypothesis.

![image](https://github.com/ken1009us/2021Fall_finals/blob/main/image/hypo2-t.png "Station Dataframe")

As for the Washington region, the casual riders also ride longer than the member riders in a trip. Moreover, compared to the result of Montreal, the duration difference between member riders and casual riders is bigger. It’s about an average of 8 minutes to 20 minutes.

![image](https://github.com/ken1009us/2021Fall_finals/blob/main/image/hypo2-w.png "Station Dataframe")


Hypothesis #3 - Compared to casual riders, member riders have a higher possibility to take bikes

Calculate the percentage of members riding bikes.

In conclusion about Montreal, we found out that there are some missing data in the dataset. However, if there is sufficient data for the whole year, then you can find out compared to casual riders, member riders have a higher possibility to take bikes in 2014.

![image](https://github.com/ken1009us/2021Fall_finals/blob/main/image/hypo3-m.png "Station Dataframe")

In Toronto, the dataset only records casual riders. So, in this dataset, we can only find out when the casual riders ride bikes. We cannot come to the conclusion of this hypothesis due to the fact that the dataset did not provide sufficient data for us to explore.

![image](https://github.com/ken1009us/2021Fall_finals/blob/main/image/hypo3-t.png "Station Dataframe")

In Washington, you can see that the proportion of casual riders is quite low just like in Montreal. It fits the hypothesis compared to casual riders, member riders have a higher possibility to take bikes.

![image](https://github.com/ken1009us/2021Fall_finals/blob/main/image/hypo3-w.png "Station Dataframe")

## Data Sources

1. Capital Bikeshare trip history data (Capital Bikeshare is a bike-sharing company in Washington)\
https://s3.amazonaws.com/capitalbikeshare-data/index.html

2. Novel Corona Virus 2019 Dataset\
https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset/tasks?taskId=508

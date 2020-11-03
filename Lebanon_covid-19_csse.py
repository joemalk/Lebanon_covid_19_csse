#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import datetime

# In the following, change 'Country/Region' to your desired choice. I wrote the Python file for the Country/Region Lebanon.

# Change the following to the location of the CSSE file "time_series_covid19_confirmed_global.csv"
with open('covid-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv', mode='r')   as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if row['Country/Region']=='Lebanon':
            Lebanon_confirmed = row

# Change the following to the location of the CSSE file "time_series_covid19_deaths_global.csv"
with open('covid-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv', mode='r')   as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if row['Country/Region']=='Lebanon':
            Lebanon_deaths = row

# Change the following to the location of the CSSE file "time_series_covid19_recovered_global.csv"
with open('covid-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv', mode='r')   as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if row['Country/Region']=='Lebanon':
            Lebanon_recovered = row

Lebanon_confirmed.pop('Province/State')
Lebanon_confirmed.pop('Country/Region','Lat')
Lebanon_confirmed.pop('Lat')
Lebanon_confirmed.pop('Long')

Lebanon_deaths.pop('Province/State')
Lebanon_deaths.pop('Country/Region','Lat')
Lebanon_deaths.pop('Lat')
Lebanon_deaths.pop('Long')

Lebanon_recovered.pop('Province/State')
Lebanon_recovered.pop('Country/Region','Lat')
Lebanon_recovered.pop('Lat')
Lebanon_recovered.pop('Long')

confirmed = np.array(np.array(list(Lebanon_confirmed.items()))[:,1].reshape(-1,1),                     dtype = np.int32)

deaths = np.array(np.array(list(Lebanon_deaths.items()))[:,1].reshape(-1,1),                  dtype = np.int32)

recovered = np.array(np.array(list(Lebanon_recovered.items()))[:,1].reshape(-1,1),                     dtype = np.int32)

Lebanon_cdr = np.concatenate([confirmed,deaths,recovered], axis = 1)

dates = pd.date_range('20200122', periods=Lebanon_cdr.shape[0])

Lebanon_cdr_data = pd.DataFrame(Lebanon_cdr, index=dates, columns=['confirmed',                                                            'deaths','recovered'])

plt.figure()

Lebanon_cdr_data
data_daily_changes = Lebanon_cdr_data.diff()
data_daily_changes.plot()
march_description = data_daily_changes.loc['2020-03-01':'2020-03-31'].describe()
april_description = data_daily_changes.loc['2020-04-01':'2020-04-30'].describe()
may_description = data_daily_changes.loc['2020-05-01':'2020-05-31'].describe()
june_description = data_daily_changes.loc['2020-06-01':'2020-06-30'].describe()

march_description.loc[['mean','std']]
april_description.loc[['mean','std']]
may_description.loc[['mean','std']]
june_description.loc[['mean','std']]
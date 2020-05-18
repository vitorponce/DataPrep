import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from functools import reduce
from scipy import stats
df = pd.read_csv('data_set.csv', sep=';', encoding='ISO-8859-1')


### Primeiro passo, tratamento dos dados
############################
###### Data Wrangling ######
############################
df.shape
# Quais e quantos valores são nulos?
df.isnull().sum()
# Nome de todas as colunas
df.columns

### Renomeando colunas
df = df.rename(columns={"Q210A": "Q21A"})
df = df.rename(columns={"Q210B": "Q21B"})
df = df.rename(columns={"Q210C": "Q21C"})
df = df.rename(columns={"Q210OUTRO": "Q21OUTRO"})
df = df.rename(columns={"Q43A.1": "Q43A1"})

### Preenchendo valores nulos como "Nenhum"
df['Q21B'] = df['Q21B'].fillna('Nenhum')
df['Q21B'].describe()
df['Q21C'] = df['Q21C'].fillna('Nenhum')
df['Q21C'].describe()
df['Q24B'] = df['Q24B'].fillna('Nenhum')
df['Q24B'].describe()
df['Q24OUTRO'] = df['Q24OUTRO'].fillna('Nenhum')
df['Q24OUTRO'].describe()
df['Q24C'] = df['Q24C'].fillna('Nenhum')
df['Q24C'].describe()
df['Q43B'] = df['Q43B'].fillna('Nenhum')
df['Q43B'].describe()
df['Q43C'] = df['Q43C'].fillna('Nenhum')
df['Q43C'].describe()
df['Q43A1'] = df['Q43A1'].fillna('Nenhum')
df['Q43A1'].describe()
print(df)

##Dropando colunas

df = df.drop("Q21OUTRO",axis=1)
df.shape

##Setando a coluna ID
df.set_index('ID', inplace = True)
df['Q24A'].head(12)

############################
###### Data Wrangling ######
############################

sns.boxplot(x=df['Q21'])
sns.boxplot(x=df['Q11'])


#create the dataframe
z = np.abs(stats.zscore(df['Q11']))
print(z)

threshold = 3
print(np.where(z > 3))
print(z[25][1])

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)


print(df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))

df_o = df_o[(z < 3).all(axis=1)]

df['Q11'].describe()



#############################
######## Detecting Outliers #
anomalies = []

# multiply and add by random numbers to get some real values
# data = np.random.randn(50000)  * 20 + 20

# Function to Detection Outlier on one-dimentional datasets.
def find_anomalies(random_data):
    # Set upper and lower limit to 3 standard deviation
    random_data_std = std(random_data)
    random_data_mean = mean(random_data)
    anomaly_cut_off = random_data_std * 3
    
    lower_limit  = random_data_mean - anomaly_cut_off 
    upper_limit = random_data_mean + anomaly_cut_off
    print(lower_limit)
    # Generate outliers
    for outlier in random_data:
        if outlier > upper_limit or outlier < lower_limit:
            anomalies.append(outlier)
    return anomalies

find_anomalies(df)















###Data Cleaning

# Cleaning columns using the .apply function

    # unwanted_characters = ['[', ',', '-']

    # def clean_dates(item):
    #     dop= str(item.loc['Date of Publication'])
        
    #     if dop == 'nan' or dop[0] == '[':
    #         return np.NaN
        
    #     for character in unwanted_characters:
    #         if character in dop:
    #             character_index = dop.find(character)
    #             dop = dop[:character_index]
        
    #     return dop

    # df['Date of Publication'] = df.apply(clean_dates, axis = 1)



# ALTERNATIVE to 
# def clean_dates(dop):
#     dop = str(dop)
#     if dop.startswith('[') or dop == 'nan':
#         return 'NaN'
#     for character in unwanted_characters:
#         if character in dop:
#             character_index = dop.find(character)
#             dop = dop[:character_index]
#     return dop

# df['Date of Publication'] = df['Date of Publication'].apply(clean_dates)
# df.head()




###Setando a visualizacao de dados###
# sns.set()

# covid_data_2020MAR29 = (covid_data
#                         .query("date == datetime.date(2020, 3, 29)")
#                         .filter(['country','confirmed','dead','recovered'])
#                         .groupby('country')
#                         .agg('sum')
#                         .sort_values('confirmed', ascending = False)
#                         .reset_index()
# )
# print(covid_data_2020MAR29)

# ###ScatterPlot###
# sns.scatterplot(data = covid_data_2020MAR29
#                 ,x = 'confirmed'
#                 ,y = 'dead'
#                 )
# ###ScatterPlot###

# ###LineChart###
# confimed_by_date_xchina = (covid_data
#                            .query('country != "China"')
#                            .filter(['date','confirmed'])
#                            .groupby('date')
#                            .agg('sum')
#                            .reset_index()
#                            )
# print(confimed_by_date_xchina)

# ###LineChart###

# ###Plotting aggregate data###
# sns.lineplot(data = confimed_by_date_xchina
#              ,x = 'date'
#              ,y = 'confirmed'
#              )
# ###Plotting aggregate data###



# # Here, we’re still going to group our data and aggregate it to sum up the total number of confirmed cases by date.#
# confirmed_by_date_china_xchina = (covid_data
#                            .assign(china_flg = np.where(covid_data.country == 'China', 'China', 'Not China'))
#                            .filter(['date','confirmed','china_flg'])
#                            .groupby(['date','china_flg'])
#                            .agg('sum')
#                            .reset_index()
#                            )
# # Here, we’re still going to group our data and aggregate it to sum up the total number of confirmed cases by date.#

# ###Plot the data###

# sns.lineplot(data = confirmed_by_date_china_xchina
#              ,x = 'date'
#              ,y = 'confirmed'
#              ,hue = 'china_flg'
#              )
# ###Plot the data###

# # We have the country name, and the total number of confirmed cases for the top 15 countries.
# confirmed_by_country_top15 = (covid_data
#                         .query('date == datetime.date(2020, 3, 29)')
#                         .filter(['country','confirmed'])
#                         .groupby('country')
#                         .agg('sum')
#                         .sort_values('confirmed', ascending = False)
#                         .reset_index()
#                         .iloc[0:15,:]
#                         )
# print(confirmed_by_country_top15)

# ###Barplot###

# sns.barplot(data = confirmed_by_country_top15
#             ,x = 'country'
#             ,y = 'confirmed'
#         )
# ###Barplot###

# ###Horizontal barplot

# sns.barplot(data = confirmed_by_country_top15
#             ,y = 'country'
#             ,x = 'confirmed'
#             ,color = 'darkred'
#         )
# ###Horizontal barplot


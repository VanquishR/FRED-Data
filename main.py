from fredapi import Fred
import pandas as pd
import openpyxl


# Replace 'your_api_key' with your actual FRED API key
api_key = '421802436b543bd414221d27079314e8'
fred = Fred(api_key=api_key)

# Specify the series you want to pull
series_codes = [
    'UNRATE', 'PSAVERT', 'PI', 'PCE', 'DRCCLACBS', 'HOUST', 'PERMIT', 'HSN1F', 'EXHOSLUSM495S',
    'ACTLISCOUUS', 'ETOTALUSQ176N', 'FIXHAI', 'M2SL'
   , 'CES0500000003', 'INDPRO', 'DGORDER',
    'ATCGNO', 'ISRATIO', 'TTLCONS', 'TCU', 'TOTALSLAR',
    'TOTALSA', 'RRVRUSQ156N'
]

# I removed  as these were daily: 'T10YIE', 'T5YIE' ,
#     'T10Y2Y'
# Create a dictionary to store data for each series
data_dict = {}

# Retrieve and store the data for each series
for series_code in series_codes:
    data = fred.get_series(series_code)
    data_dict[series_code] = data

# Create a DataFrame from the dictionary
df = pd.DataFrame(data_dict)

# Save the DataFrame to an Excel file
df.to_excel('FRED_data.xlsx', index_label='Date')
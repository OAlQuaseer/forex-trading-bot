# service

# this is where our data science application code is located

from models import Company, Index, Configuration
import pandas as pd

def get_nasdaq_100_index_companies(url):
    companies = []
    table_list = pd.read_html('https://en.wikipedia.org/wiki/Nasdaq-100')
    ndx_100_index_constituents_df  = table_list[4]

    for index, series in ndx_100_index_constituents_df.iterrows():
        company = Company(series['Ticker'])
        company.name = series['Company']
        company.sector = series['GICS Sector']
        company.industry = series['GICS Sub-Industry']
        companies.append(company)
    
    return companies

def get_snp_500_companies(url):
    companies = []
    table = pd.read_html(url)[0]
    for index, row in table.iterrows():
        company = Company(row['Symbol'])
        company.name = row['Security']
        company.sector = row['GICS Sector']
        company.industry = row['GICS Sub-Industry']
        companies.append(company)
    return companies

def get_ftse_companies(url):
    companies = []
    table = pd.read_html(url)[3]
    for index, row in table.iterrows():
        company = Company(row['EPIC'])
        company.name = row['Company']
        company.sector = row['FTSE Industry Classification Benchmark sector[12]']
        companies.append(company)
    return companies


async def run (config: Configuration):
    companies_map = {
        Index.SNP500: get_snp_500_companies,
        Index.FTSE100: get_ftse_companies,
        Index.NDX100: get_nasdaq_100_index_companies
    }

    url = config.get_url()

    func_to_get_data = companies_map.get(config.index, None)
    
    if func_to_get_data is None:
        raise KeyError(f'{input.index} is not supported')
    
    companies = func_to_get_data(url)

    return [c.name for c in companies]



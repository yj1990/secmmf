# secmmf - SEC Money Market Fund Data Scraper

- Author: Yangjue Han
- Date: May 2020

## Introduction
This repository contains code that enables the user to parse and download money market fund holdings information in N-MFP2 filings from SEC EDGAR system. At the end of every month, all U.S. money market funds are required to report their securities holdings to SEC, including identification, maturity, market value, yield to maturity, issuer information, and other features. For repurchase agreement contracts, money market funds also have to report information on collateral securities. The granularity of this dataset provides an unparallel opportunity for financial economists to study questions related to the shadow banking system.

## Installation

```
pip install secmmf
```

## Usage

### Initial setup
The module `secmmf` contains a set of functions that parse and download the information in N-MFP2 filings. The user should first specify the path of a directory to store the downloaded data to `data_dir` and the storage of `data_dir` should be at least 20GBs. Note that the package can only be used to download N-MFP2 filings, but could be extended to download other filings with a similar format. The package does not provide any data cleaning function.

```python
>>> import secmmf

>>> data_dir = ## YOUR DIRECTORY HERE ##
>>> pathfile = 'xmlpath.csv' # no need to change this
```

### Build index of filings 
First we download and extract the paths of filings from SEC EDGAR system using method `download_sec_index()`. 
- By specifying `start_date` and `end_date`, the user will limit the time range to [`start_date`,`end_date`]. The default start date is 2016-10 and end date is the current month. 
- The method will output a csv file named `index_file.csv` in `data_dir`. We then use `generate_index()` to create a file of urls linked to XML files that can be easily parsed, named `pathfile`.

```python
>>> secmmf.download_sec_index(data_dir, form_name = 'N-MFP2', start_date = '2016-10', end_date = '2020-05')
>>> generate_index(data_dir, pathfile)
```

### Download raw files
Next, we download XML files from `pathfile` and parse them into un-modified csv files using `scrape()`. 
- Depending on the number of files to download and internet connection, this step might take up to 4 hours. 
- Paths contained in `pathfile` are divided into 20 blocks and the corresponding csv files will be saved into 20 different subfolders. 
- If the program is interrupted at any block, the user can specify `start_block` or `end_block` to modify the exact portion of files to download.

```python
>>> scrape(data_dir, pathfile, N_blocks=20, start_block=1, end_block=20)
```

### Generate fund-level and holdings-level tables
Raw csv files contain unstructure data that combine both fund-level information and asset holdings. We can use `gen_table_fund()` and `gen_table_holdings()` to generate tables with ready-to-use data on fund-level information and asset holdings. Finally, `wrap()` method combines all formatted tables into a single table for each level of information and clean up the data folder. 

```python
gen_table_fund(data_dir, pathfile)
gen_table_holdings(data_dir, pathfile)
wrap(data_dir)
# Done!
```

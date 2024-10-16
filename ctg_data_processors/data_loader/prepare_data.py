# Authors: 
#   Name: Prajwal Goudar
#   Student ID: 202304088
#   Email: x2023dvk@stfx.ca

#   Name: Rahul Rudragoudar
#   Student ID: 202304297
#   Email: x2023dvl@stfx.ca


import pandas as pd

def prepare_nsp_data(path_to_xls_file):
    """
    This function reads the data from the excel file and prepares it for NSP analysis.
    Basically, it removes the columns that are not useful for NSP analysis and exports the modified dataset as required by df-analyze package to a csv file.

    This function uses pandas library to read and modify the dataset.
    @software{
        reback2020pandas,
        author       = {The pandas development team},
        title        = {pandas-dev/pandas: Pandas},
        month        = feb,
        year         = 2020,
        publisher    = {Zenodo},
        version      = {latest},
        doi          = {10.5281/zenodo.3509134},
        url          = {https://doi.org/10.5281/zenodo.3509134}
    }

    This function uses xlrd library to read the excel file which is installed as a dependency of pandas library.
    @software{
        xlrd,
        author       = {Chris Withers and the xlrd development team},
        title        = {xlrd},
        version      = {latest},
        url          = {https://xlrd.readthedocs.io/en/latest/#xlrd}
        copyright    = Copyright 2005-2019 Stephen John Machin, Lingfo Pty Ltd. 2019-2021 Chris Withers Revision 0c4e80b3.
    }

    Args:
    path_to_xls_file: Path to the excel file containing the raw data downloaded from (Campos, D. & Bernardes, J. (2000). Cardiotocography [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C51S4N.)

    Returns:
    data: The modified dataset in pandas dataframe format
    """


    # Load the data from the excel file
    data = pd.read_excel(path_to_xls_file, sheet_name='Raw Data')
    
    # Remove columns that are not useful for NSP analysis
    columns_to_drop = ['FileName', 'Date', 'SegFile', 'b', 'e', 'SUSP', 'LBE', 'DR', 'A', 'B', 'C', 'D', 'E', 'AD', 'DE', 'LD', 'FS', 'SUSP', 'CLASS']
    data = data.drop(columns=columns_to_drop)

    # Remove the first row from raw data as it doesn't have any values
    data = data.drop(index=0)

    # Print the head of the modified dataset. this will print first few rows
    print(data.head())

    # Export the modified dataset to a csv file
    # TODO: Improvise the below line to use dynamic path instead of a static path
    data.to_csv('data/output/processed_data_ctg_nsp.csv', index=False)
    
    return data
# Authors: 
#   Name: Prajwal Goudar
#   Student ID: 202304088
#   Email: x2023dvk@stfx.ca

#   Name: Rahul Rudragoudar
#   Student ID: 202304297
#   Email: x2023dvl@stfx.ca

import pandas as pd

def read_data(input_path, sheet_name):
    """
    This function reads the data for analysis.
    Basically, it removes the columns that are not useful for different kind of analysis and exports the modified dataset as required by df-analyze package to a csv file.

    This function uses xlrd library which is installed as the dependecy for pandas library to extract the content from xls file.
    @software{
        xlrd,
        author       = {Chris Withers and the xlrd development team},
        title        = {xlrd},
        version      = {latest},
        url          = {https://xlrd.readthedocs.io/en/latest/#xlrd}
        copyright    = Copyright 2005-2019 Stephen John Machin, Lingfo Pty Ltd. 2019-2021 Chris Withers Revision 0c4e80b3.
    }

    This function uses pandas library to read the dataset.
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

    Args:
    input_path: Input path for the xls file.
    sheet_name: Name of the sheet in the xls file.

    Returns:
    data: The data read from the xls file in pandas dataframe format
    """
    
    data = pd.read_excel(input_path, sheet_name=sheet_name)
    return data


def prepare_data(raw_data, output_path, columns_to_drop):
    """
    This function prepares the data for analysis.
    Basically, it removes the columns that are not useful for different kind of analysis and exports the modified dataset as required by df-analyze package to a csv file.

    This function uses pandas library to modify the dataset.
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

    Args:
    raw_data: The raw data downloaded from (Campos, D. & Bernardes, J. (2000). Cardiotocography [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C51S4N.)
    output_path: The path where the csv file will be stored.
    columns_to_drop: Unwanted columns that will be removed from dataframe

    Returns:
    data: The modified dataset in pandas dataframe format
    """
    
    # Remove columns that are not useful for analysis
    data = raw_data.drop(columns=columns_to_drop)

    # Remove the first row from raw data as it doesn't have any values
    data = data.drop(index=0)

    # Print the head of the modified dataset. this will print first few rows
    print(data.head())

    # Export the modified dataset to a csv file
    data.to_csv(output_path, index=False)
    
    return data
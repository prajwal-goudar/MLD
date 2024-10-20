# Authors: 
#   Name: Prajwal Goudar
#   Student ID: 202304088
#   Email: x2023dvk@stfx.ca

#   Name: Rahul Rudragoudar
#   Student ID: 202304297
#   Email: x2023dvl@stfx.ca

from data_loader.prepare_data import prepare_data, read_data

# Load the data from the excel file, this uses pandas and xlrd packages to read excel file and store it as pandas data frame
raw_data = read_data('data/input/ctg.xls', 'Raw Data')

# These are the columns/attributes which are not required by any of the following analysis
unwanted_columns = ['FileName', 'Date', 'SegFile', 'b', 'e', 'SUSP', 'LBE', 'DR', 'A', 'B', 'C', 'D', 'E', 'AD', 'DE', 'LD', 'FS', 'SUSP']

# NSP DATA FOR ALL INPUT VARIABLES

# Remove CLASS column as it will not be requied in NSP Analysis
columns_to_drop_for_nsp_data = unwanted_columns + ['CLASS']

# Prepare the data for analysis and store it in the output path provided as second parameter.
nsp__all_data = prepare_data(raw_data, 'data/output/processed_data_ctg_nsp_all.csv', columns_to_drop_for_nsp_data)

# FHR DATA FOR ALL INPUT VARIABLES

# Remove NSP column as it will not be requied in FHR Analysis
columns_to_drop_for_fhr_data = unwanted_columns + ['NSP']

# Prepare the data for analysis and store it in the output path provided as second parameter.
fhr_all_data = prepare_data(raw_data, 'data/output/processed_data_ctg_fhr_all.csv', columns_to_drop_for_fhr_data)

# NSP DATA CONSIDERING HEART RATE OF FETUS

# Along with CLASS (this is not needed as we are analysing the model for NSP and not FHR) we are also removing FM - movement of fetus per second and UC - which is mothers uterus contracts per second.

columns_to_drop_for_nsp_heart_rate_data = unwanted_columns + ['CLASS', 'FM', 'UC']

# Prepare the data for analysis and store it in the output path provided as second parameter.
nsp_heart_data = prepare_data(raw_data, 'data/output/processed_data_ctg_nsp_heart.csv', columns_to_drop_for_nsp_heart_rate_data)

# FHR DATA CONSIDERING HEART RATE OF FETUS

# Along with NSP (this is not needed as we are analysing the model for FHR and not NSP) we are also removing FM - movement of fetus per second and UC - which is mothers uterus contracts per second.

columns_to_drop_for_fhr_heart_rate_data = unwanted_columns + ['NSP', 'FM', 'UC']

# Prepare the data for analysis and store it in the output path provided as second parameter.
nsp_heart_data = prepare_data(raw_data, 'data/output/processed_data_ctg_fhr_heart.csv', columns_to_drop_for_fhr_heart_rate_data)

# NSP data when we do not consider histogram measurements
	
# Along with CLASS (this is not needed as we are analysing the model for NSP and not FHR) we are also removing FM - movement of fetus per second and Max - the number of peaks in the histogram of fetal heart rates and NMAX - the number of peaks in the histogram of fetal heart rates.

columns_to_drop_for_nsp_no_histogram_data = unwanted_columns + ['CLASS', 'FM', 'Max', 'Nmax']

# Prepare the data for analysis and store it in the output path provided as second parameter.
nsp_no_histogram_data = prepare_data(raw_data, 'data/output/processed_data_ctg_nsp_no_histogram.csv', columns_to_drop_for_nsp_no_histogram_data)

# FHR data when we do not consider histogram measurements

# Along with NSP (this is not needed as we are analysing the model for FHR and not NSP) we are also removing FM - movement of fetus per second and Max - the number of peaks in the histogram of fetal heart rates and NMAX - the number of peaks in the histogram of fetal heart rates.

columns_to_drop_for_fhr_no_histogram_data = unwanted_columns + ['NSP', 'FM', 'Max', 'Nmax']

# Prepare the data for analysis and store it in the output path provided as second parameter.
fhr_no_histogram_data = prepare_data(raw_data, 'data/output/processed_data_ctg_fhr_no_histogram.csv', columns_to_drop_for_fhr_no_histogram_data)

# NSP data when we do not consider any long-term fluctuations and abnormality attributes

# Along with CLASS (this is not needed as we are analysing the model for NSP and not FHR) we are also removing below columns
# DP - The number of times the fetal heart rate decreases for a prolonged period per second.
# MLTV - The average fluctuation of the fetal heart rate in the long term.
# ALTV - The percentage of time during which the fetal heart rate fluctuates abnormally in the long term.
# ASTV - The percentage of time during which the fetal heart rate fluctuates abnormally in the short term.

columns_to_drop_for_nsp_no_long_term_fluctuations_and_abnorm = unwanted_columns + ['CLASS', 'DP', 'MLTV', 'ALTV', 'ASTV']

# Prepare the data for analysis and store it in the output path provided as second parameter.
nsp_no_long_term_fluctuations_and_abnorm_data = prepare_data(raw_data, 'data/output/processed_data_ctg_nsp_no_fluc.csv', columns_to_drop_for_nsp_no_long_term_fluctuations_and_abnorm)

# FHR data when we do not consider any long-term fluctuations and abnormality attributes

# Along with NSP (this is not needed as we are analysing the model for FHR and not NSP) we are also removing the following:
# DP - The number of times the fetal heart rate decreases for a prolonged period per second.
# MLTV - The average fluctuation of the fetal heart rate in the long term.
# ALTV - The percentage of time during which the fetal heart rate fluctuates abnormally in the long term.
# ASTV - The percentage of time during which the fetal heart rate fluctuates abnormally in the short term.

columns_to_drop_for_fhr_no_long_term_fluctuations_and_abnorm = unwanted_columns + ['NSP', 'DP', 'MLTV', 'ALTV', 'ASTV']

# Prepare the data for analysis and store it in the output path provided as second parameter.
fhr_no_long_term_fluctuations_and_abnorm_data = prepare_data(raw_data, 'data/output/processed_data_ctg_fhr_no_fluc.csv', columns_to_drop_for_fhr_no_long_term_fluctuations_and_abnorm)
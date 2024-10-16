This project uses df-analyze (https://github.com/stfxecutables/df-analyze/blob/master/README.md) package to compare different machine learning alrgoithms and generate results on a cardiotocography dataset downloaded from UCI Machine Learning Repository (Campos, D. & Bernardes, J. (2000). Cardiotocography [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C51S4N.)

To execute, provide right permissions to the initiate_nsp_mld_analysis.sh script and run the script using ./initiate_nsp_mld_analysis.sh (assuming the command line is pointed to the parent directory of this project)

The script modifies the data as per the requirement of df-analyze package, clones and installs df-analyze package and produces the results using df-analyze package.

PLEASE NOTE: This project is tested using python version 3.12.6 on environment mentioned below, we will try to add a dockerfile during next phase of this project. 


Below details are generated using uname and lsb commands
Distributor ID: Ubuntu
Description:    Ubuntu 22.04.4 LTS
Release:        22.04
Codename:       jammy
Architecture:   x86_64

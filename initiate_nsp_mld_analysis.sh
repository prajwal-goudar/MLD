# Authors: 
#   Name: Prajwal Goudar
#   Student ID: 202304088
#   Email: x2023dvk@stfx.ca

#   Name: Rahul Rudragoudar
#   Student ID: 202304297
#   Email: x2023dvl@stfx.ca

# A shell script which helps to execute the data processing and analysis of the machine learning algorithms on the CTG dataset using NSP as target variable using the df-analyze package

# Navigate to the ctg_data_processors folder
cd ctg_data_processors

# Install requied packages mentioned in requirements file
pip install -r requirements.txt

# Execute the __init__.py which loads the data and stores the data in right format as required by df-analyze package in the data/output folder
python3 __init__.py

# Navigate to the previous folder
cd ..

# Clone df-analyze repo
git clone https://github.com/stfxecutables/df-analyze.git

# Navigate back to the parent folder and initialize the virtual environment by installing required packages for df-analyze (https://github.com/stfxecutables/df-analyze/blob/master/local_install.sh shows required packages)
cd df-analyze && python -m venv .venv --clear && source .venv/bin/activate &&  python -m pip install --upgrade pip setuptools wheel --no-cache-dir && python -m pip install \
    cli-test-helpers \
    joblib \
    jsonpickle \
    lightgbm \
    llvmlite \
    matplotlib \
    numba \
    numpy \
    openpyxl \
    optuna \
    pandas \
    pyarrow \
    pytest \
    "pytest-xdist[psutil]" \
    python-dateutil \
    scikit-image \
    scikit-learn \
    scipy \
    seaborn \
    statsmodels \
    tabulate \
    torch \
    torchaudio \
    torchvision \
    tqdm \
    typing_extensions \
    skorch \
    "transformers[torch]" \
    accelerate \
    "datasets[vision]" \
    protobuf \
    sentencepiece \
    pytorch_tabular

# Execute the df-analyze package to analyze the nsp data considering all input variables and store the results in its respective directory
python df-analyze.py --df ../ctg_data_processors/data/output/processed_data_ctg_nsp_all.csv --target NSP --mode classify --classifiers knn lgbm rf lr sgd dummy gandalf --regressors knn lgbm rf elastic sgd dummy gandalf --feat-select filter embed wrap --redundant-wrapper-selection --embed-select lgbm linear --wrapper-select step-up --wrapper-model linear --norm robust --nan median --filter-method assoc pred --filter-assoc-cont-classify mut_info --filter-assoc-cat-classify mut_info --filter-assoc-cont-regress mut_info --filter-assoc-cat-regress mut_info --filter-pred-regress mae --filter-pred-classify acc --htune-trials 50 --htune-cls-metric acc --htune-reg-metric mae --test-val-size 0.4 --outdir ./df_analyze_all_nsp_results_gandalf

# Execute the df-analyze package to analyze the class fhr data considering all input variables and store the results in its respective directory
python df-analyze.py --df ../ctg_data_processors/data/output/processed_data_ctg_fhr_all.csv --target CLASS --mode classify --classifiers knn lgbm rf lr sgd dummy gandalf --regressors knn lgbm rf elastic sgd dummy gandalf --feat-select filter embed wrap --redundant-wrapper-selection --embed-select lgbm linear --wrapper-select step-up --wrapper-model linear --norm robust --nan median --filter-method assoc pred --filter-assoc-cont-classify mut_info --filter-assoc-cat-classify mut_info --filter-assoc-cont-regress mut_info --filter-assoc-cat-regress mut_info --filter-pred-regress mae --filter-pred-classify acc --htune-trials 50 --htune-cls-metric acc --htune-reg-metric mae --test-val-size 0.4 --outdir ./df_analyze_all_fhr_results_gandalf

# Execute the df-analyze package to analyze the nsp data when considering only heart rate measurements of fetus and store the results in its respective directory
python df-analyze.py --df ../ctg_data_processors/data/output/processed_data_ctg_nsp_heart.csv --target NSP --mode classify --classifiers knn lgbm rf lr sgd dummy gandalf --regressors knn lgbm rf elastic sgd dummy gandalf --feat-select filter embed wrap --redundant-wrapper-selection --embed-select lgbm linear --wrapper-select step-up --wrapper-model linear --norm robust --nan median --filter-method assoc pred --filter-assoc-cont-classify mut_info --filter-assoc-cat-classify mut_info --filter-assoc-cont-regress mut_info --filter-assoc-cat-regress mut_info --filter-pred-regress mae --filter-pred-classify acc --htune-trials 50 --htune-cls-metric acc --htune-reg-metric mae --test-val-size 0.4 --outdir ./df_analyze_nsp_heart_rate_results_gandalf

# Execute the df-analyze package to analyze the class fhr data when considering only heart rate measurements of fetus and store the results in its respective directory
python df-analyze.py --df ../ctg_data_processors/data/output/processed_data_ctg_fhr_heart.csv --target CLASS --mode classify --classifiers knn lgbm rf lr sgd dummy gandalf --regressors knn lgbm rf elastic sgd dummy gandalf --feat-select filter embed wrap --redundant-wrapper-selection --embed-select lgbm linear --wrapper-select step-up --wrapper-model linear --norm robust --nan median --filter-method assoc pred --filter-assoc-cont-classify mut_info --filter-assoc-cat-classify mut_info --filter-assoc-cont-regress mut_info --filter-assoc-cat-regress mut_info --filter-pred-regress mae --filter-pred-classify acc --htune-trials 50 --htune-cls-metric acc --htune-reg-metric mae --test-val-size 0.4 --outdir ./df_analyze_fhr_heart_rate_results_gandalf

# Execute the df-analyze package to analyze the nsp data when we do not consider histogram measurements and store the results in its respective directory
python df-analyze.py --df ../ctg_data_processors/data/output/processed_data_ctg_nsp_no_histogram.csv --target NSP --mode classify --classifiers knn lgbm rf lr sgd dummy gandalf --regressors knn lgbm rf elastic sgd dummy gandalf --feat-select filter embed wrap --redundant-wrapper-selection --embed-select lgbm linear --wrapper-select step-up --wrapper-model linear --norm robust --nan median --filter-method assoc pred --filter-assoc-cont-classify mut_info --filter-assoc-cat-classify mut_info --filter-assoc-cont-regress mut_info --filter-assoc-cat-regress mut_info --filter-pred-regress mae --filter-pred-classify acc --htune-trials 50 --htune-cls-metric acc --htune-reg-metric mae --test-val-size 0.4 --outdir ./df_analyze_nsp_no_histogram_results_gandalf

# Execute the df-analyze package to analyze the class fhr data when we do not consider histogram measurement and store the results in its respective directory
python df-analyze.py --df ../ctg_data_processors/data/output/processed_data_ctg_fhr_no_histogram.csv --target CLASS --mode classify --classifiers knn lgbm rf lr sgd dummy gandalf --regressors knn lgbm rf elastic sgd dummy gandalf --feat-select filter embed wrap --redundant-wrapper-selection --embed-select lgbm linear --wrapper-select step-up --wrapper-model linear --norm robust --nan median --filter-method assoc pred --filter-assoc-cont-classify mut_info --filter-assoc-cat-classify mut_info --filter-assoc-cont-regress mut_info --filter-assoc-cat-regress mut_info --filter-pred-regress mae --filter-pred-classify acc --htune-trials 50 --htune-cls-metric acc --htune-reg-metric mae --test-val-size 0.4 --outdir ./df_analyze_fhr_no_histogram_results_gandalf

# Execute the df-analyze package to analyze the nsp data when we do not consider any long-term fluctuations and abnormality attributes and store the results in its respective directory
python df-analyze.py --df ../ctg_data_processors/data/output/processed_data_ctg_nsp_no_fluc.csv --target NSP --mode classify --classifiers knn lgbm rf lr sgd dummy gandalf --regressors knn lgbm rf elastic sgd dummy gandalf --feat-select filter embed wrap --redundant-wrapper-selection --embed-select lgbm linear --wrapper-select step-up --wrapper-model linear --norm robust --nan median --filter-method assoc pred --filter-assoc-cont-classify mut_info --filter-assoc-cat-classify mut_info --filter-assoc-cont-regress mut_info --filter-assoc-cat-regress mut_info --filter-pred-regress mae --filter-pred-classify acc --htune-trials 50 --htune-cls-metric acc --htune-reg-metric mae --test-val-size 0.4 --outdir ./df_analyze_nsp_no_fluc_results_gandalf

# Execute the df-analyze package to analyze the class fhr data when we do not consider any long-term fluctuations and abnormality attributes and store the results in its respective directory
python df-analyze.py --df ../ctg_data_processors/data/output/processed_data_ctg_fhr_no_fluc.csv --target CLASS --mode classify --classifiers knn lgbm rf lr sgd dummy gandalf --regressors knn lgbm rf elastic sgd dummy gandalf --feat-select filter embed wrap --redundant-wrapper-selection --embed-select lgbm linear --wrapper-select step-up --wrapper-model linear --norm robust --nan median --filter-method assoc pred --filter-assoc-cont-classify mut_info --filter-assoc-cat-classify mut_info --filter-assoc-cont-regress mut_info --filter-assoc-cat-regress mut_info --filter-pred-regress mae --filter-pred-classify acc --htune-trials 50 --htune-cls-metric acc --htune-reg-metric mae --test-val-size 0.4 --outdir ./df_analyze_fhr_no_fluc_results_gandalf
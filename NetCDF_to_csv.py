#-------------------------------------------------------------------------------
# Purpose: NetCDF to csv file conversion

# Created:     07/10/2022
#-------------------------------------------------------------------------------

#Import library
import xarray as xr

# to convert whole dataset
Dataset = xr.open_dataset("direction\\to\\your\\file.nc")

Dataset.to_dataframe().to_csv("direction\\to\\save.csv")

#to export only one variable

Dataset["variable_name"].to_dataframe().to_csv("direction\\to\\save.csv")
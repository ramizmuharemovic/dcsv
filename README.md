# dcsv
### Convert parquet to csv

# Linux
sudo curl -L --output /usr/local/bin/dcsv https://raw.githubusercontent.com/ramizmuharemovic/dcsv/main/linux/dcsv

sudo chmod +x /usr/local/bin/dcsv


## Test
curl -O https://raw.githubusercontent.com/ramizmuharemovic/dcsv/main/test/test.parquet

dcsv test.parquet


# Mac
sudo curl -L --output /usr/local/bin/dcsv https://raw.githubusercontent.com/ramizmuharemovic/dcsv/main/mac/dcsv

sudo chmod +x /usr/local/bin/dcsv

## Test
curl -O https://raw.githubusercontent.com/ramizmuharemovic/dcsv/main/test/test.parquet

dcsv test.parquet
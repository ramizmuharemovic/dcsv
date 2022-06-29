# dcsv
### Convert parquet to csv

# Linux
curl -O https://raw.githubusercontent.com/ramizmuharemovic/dcsv/main/linux/dcsv

sudo mv dcsv /usr/local/bin

sudo chmod +x /usr/local/bin/dcsv


## Test
curl -O https://raw.githubusercontent.com/ramizmuharemovic/dcsv/main/test/test.parquet

dcsv test.parquet


# Mac
sudo curl -L --output /usr/local/bin 

sudo chmod +x /usr/local/bin/dcsv https://raw.githubusercontent.com/ramizmuharemovic/dcsv/main/mac/dcsv

## Test
curl -O https://raw.githubusercontent.com/ramizmuharemovic/dcsv/main/test/test.parquet

dcsv test.parquet
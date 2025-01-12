#!/bin/sh

# Government API
export API="https://www.data.gouv.fr/api/1/"

# Creating necessary directories
mkdir -p "ANFR Dataset"
mkdir -p "Pre-processed data"
mkdir -p "Graphs"

cd "ANFR Dataset"

# Downloading and unzipping data
urls=$(curl -sS $API'datasets/551d4ff3c751df55da0cd89f/' | jq -r '.resources[].url')

# Calculate total number of URLs
total_urls=$(echo "$urls" | wc -l | tr -d ' ')

# Initialize progress counter
progress=0

# Loop through each URL and download the item
for url in $urls; do
  # Download the item using curl
  filename=$(basename "$url")
  # Renaming the file for certain urls
  if [ "$url" = "https://static.data.gouv.fr/resources/donnees-sur-les-installations-radioelectriques-de-plus-de-5-watts-1/20160502-155515/20160402_Tables_de_reference.zip" ]; then
    filename="20160430_Tables_de_reference.zip"
  fi
  if [ "$url" = "https://static.data.gouv.fr/resources/donnees-sur-les-installations-radioelectrique-de-plus-de-5-watts/20150402-162907/Tables_de_Reference.zip" ]; then
    filename="20150402_Tables_de_Reference.zip"
  fi
  if [ "$url" = "https://static.data.gouv.fr/resources/donnees-sur-les-installations-radioelectrique-de-plus-de-5-watts/20150402-163118/Tables_supports_antennes_emetteurs_bandes.zip" ]; then
    filename="20150402_Tables_supports_antennes_emetteurs_bandes.zip"
  fi
  if [ "$url" = "https://static.data.gouv.fr/resources/donnees-sur-les-installations-radioelectriques-de-plus-de-5-watts-1/20150506-094926/Tables_de_Reference.zip" ]; then
    filename="20150506_Tables_de_Reference.zip"
  fi
  if [ "$url" = "https://static.data.gouv.fr/resources/donnees-sur-les-installations-radioelectriques-de-plus-de-5-watts-1/20150506-094419/Tables_supports_antennes_emetteurs_bandes.zip" ]; then
    filename="20150506_Tables_supports_antennes_emetteurs_bandes.zip"
  fi
  foldername="${filename%.zip}"  # Extracting folder name without ".zip" extension
  
  # Download the file
  curl -sS "$url" -o "$filename"
  
  if [ ! "$url" = "https://static.data.gouv.fr/resources/donnees-sur-les-installations-radioelectriques-de-plus-de-5-watts-1/20190904-044845/2019-08-description-des-tables.pdf" ]; then
    # Extract the downloaded zip file
    unzip -qo "$filename" -d "$foldername"
    
    # Removed the downloaded zip file
    rm "$filename"
  fi

  
  # Increment progress counter
  progress=$((progress + 1))
  
  # Print progress bar
  printf "Progress: ["
  i=0
  while [ $i -lt $((progress * 10 / total_urls)) ]; do
    printf "#"
    i=$((i + 1))
  done
  while [ $i -lt 10 ]; do
    printf " "
    i=$((i + 1))
  done
  printf "] $progress/$total_urls\r"
done

printf "\nAll items downloaded and extracted successfully!\n"

# Fixing remaining missnamed data
mv "20230331-export-etalab-data" "20220331-export-etalab-data"
mv "31052018_Export_Etalab_Data" "20180531_Export_Etalab_Data"
mv "31052018_Export_Etalab_Ref" "20180531_Export_Etalab_Ref"
mv "20180228_Export_Etalab_Ref" "20180228_Export_Etalab_Data"
mv "Export_Etalab_Ref" "20180228_Export_Etalab_Data"
mv "Export_Etalab_Ref_22122017" "20171222_Export_Etalab_Ref"
mv "Export_Etalab_Data_22122017" "20171222_Export_Etalab_Data"
mv "20240428-export-etalab-data" "20230428-export-etalab-data"
cp -R "20161126_Tables_de_reference" "20161224_Tables_de_reference"
mv "20160730_DATA2/20160730_DATA" .
rm -r "20160730_DATA2"

mv "table-de-reference-mars-2020" "20200305-export-etalab-ref"
mv "tables-supports-antennes-emetteurs-bandes-mars-2020" "20200305-export-etalab-data"

mv "tables-de-reference-avril-2020" "20200402-export-etalab-ref"
mv "tables-supports-antennes-emetteurs-bandes-avril-2020" "20200402-export-etalab-data"

mv "tables-de-reference-janvier-2020" "20200106-export-etalab-ref"
mv "tables-supports-antennes-emetteurs-bandes-janvier-2020" "20200106-export-etalab-data"

mv "tables-de-references-fevrier-2023" "20230203-export-etalab-ref"
mv "tables-supports-antennes-emetteurs-bandes-fevrier-2023" "20230203-export-etalab-data"

mv "20180228_Export_Etalab_Data" "20180228_Export_Etalab_Ref"
mv "20180228_Export_Etalab_Ref/20180228_Export_Etalab_Data.zip" .
unzip -qo "20180228_Export_Etalab_Data.zip" -d "20180228_Export_Etalab_Data"

mv 20150402_Tables_de_Reference/Tables_de_Reference/* "20150402_Tables_de_Reference/"
mv 20150402_Tables_supports_antennes_emetteurs_bandes/Tables_supports_antennes_emetteurs_bandes/* "20150402_Tables_supports_antennes_emetteurs_bandes/"

printf "Malformed items renamed successfully!\n"

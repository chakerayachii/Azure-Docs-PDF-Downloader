!/bin/bash


# Define directory names
download_dir="azure-docs"
clean_dir="docs-clean"

# Create the directory for downloaded PDFs
if [ ! -d "$download_dir" ]; then
    mkdir "$download_dir"
fi

alias urldecode='python3 -c "import sys, urllib.parse as ul; print(ul.unquote_plus(sys.argv[1]))"'
alias urlencode='python3 -c "import sys, urllib.parse as ul;  print (ul.quote_plus(sys.argv[1]))"'
### example
# https://learn.microsoft.com/pdf\?url\=https://learn.microsoft.com/en-us/azure/app-service/toc.json
startUrl='https://learn.microsoft.com/pdf?url='
for row in $(curl https://api.github.com/repos/MicrosoftDocs/azure-docs/contents/articles | jq -c -r '.[] | select(.type | contains("dir")) | "\(.name)"'); do
    enc=$(urlencode https://learn.microsoft.com/en-us/azure/${row}/toc.json)
    wget -O "${download_dir}/${row}.pdf" "${startUrl}${enc}"
done

# Run Python script to clean up downloaded PDFs
python3 cleanDocs.py

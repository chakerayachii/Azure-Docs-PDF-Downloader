# Azure Docs PDF Downloader

This script downloads PDFs from the Microsoft Azure documentation and organizes them into a folder.

## Instructions

### Prerequisites

Before running the script, ensure you have the following installed:

- `jq`: Command-line JSON processor (install via your package manager or from https://stedolan.github.io/jq/download/)
- `wget`: Command-line utility for downloading files (usually pre-installed on most systems)
- `Python 3`: Required for running the `cleanDocs.py` script
- `PyPDF2`: Required for PDF processing in the `cleanDocs.py` script (install via pip: `pip install PyPDF2`)

### Running the Script

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/azure-docs-pdf-downloader.git
   ```

2. Navigate to the downloaded directory:

   ```bash
   cd azure-docs-pdf-downloader
   ```

3. Make the shell script executable:

   ```bash
   chmod +x download_and_clean.sh

   ```

4. Run the shell script:

```bash
./download_and_clean.sh
```

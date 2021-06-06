
from azure_sync.src.azure_sync.creds import load_credentials
from azure_sync.src.azure_sync.uploadclient import AzureUpload


credentials = load_credentials("/home/dthole/.creds/azure-blob-sync.creds")
print(f"Credentials loaded? {len(credentials) > 0}")

azUpload = AzureUpload(credentials, "blob-tutorial")
azUpload.upload_files("/home/dthole/temp/blob-tutorial/*", overwrite=True)
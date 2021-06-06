import os
import glob
import os.path
from azure.storage.blob import BlobServiceClient


class AzureUpload:
    def __init__(self, credentials, container_name=None):
        self.credentials = credentials
        self.service_client = None
        self.service_container = None
        self.container_name = container_name

    def create_service_client(self):
        self.service_client = BlobServiceClient.from_connection_string(self.connectionString)

    def get_service_container(self):
        if self.container_name is None:
            container = list(self.service_client.list_containers())[0]
        else:
            container = list(self.service_client.list_containers(name_starts_with=self.container_name))[0]
        self.service_container = self.service_client.get_container_client(container)

    def upload_file(self, filename, overwrite=False):
        basename = os.path.basename(filename)
        with open(filename, "rb") as data:
            self.service_container.upload_blob(name=basename, data=data, overwrite=overwrite)

    def upload_files(self, directoryPath, overwrite=False):
        for filename in glob.glob(directoryPath):
            print(f"Currently processing, {filename}")
            self.upload_file(filename, overwrite=overwrite)
            print(f"Finished processing, {filename}")
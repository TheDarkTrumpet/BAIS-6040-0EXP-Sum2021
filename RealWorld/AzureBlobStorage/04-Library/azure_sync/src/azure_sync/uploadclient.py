import os
import glob
import os.path
from azure.storage.blob import BlobServiceClient


class AzureUpload:
    """
    A class used to encapsulate uploads of files/directories to Microsoft Azure

    Attributes
    ----------
    credentials : str
       A formatted string for the connection string, provided by Azure, for a particular storage account
    container_name : str
       The container that we should store the resulting files in.

    Methods
    -------
    upload_file(filename, overwrite=False)
       Given a specific file name (absolute path), upload the file to Azure
    upload_files(directoryPath, overwrite=False)
       Given a specific directory name (absolute path), upload the files in the directory to Azure
    """
    def __init__(self, credentials, container_name=None):
        self.credentials = credentials
        self.container_name = container_name
        self.service_client = self.__create_service_client()
        self.service_container = self.__get_service_container()

    def upload_file(self, filename, overwrite=False):
        """
        Given a specific file name (absolute path), upload the file to Azure

        Parameters
        ----------
        filename : str
            The filename (absolute path), uploaded to Azure
        overwrite : bool
            Flag to allow for files to be overwritten in the storage container
        """
        basename = os.path.basename(filename)
        with open(filename, "rb") as data:
            self.service_container.upload_blob(name=basename, data=data, overwrite=overwrite)

    def upload_files(self, directoryPath, overwrite=False):
        """
        Given a directory path (absolute path), upload the files in the directory to Azure

        Parameters
        ----------
        directoryPath : str
            The directory (absolute path), uploaded to Azure
        overwrite : bool
            Flag to overwrite the contents within the container
        """
        for filename in glob.glob(directoryPath):
            print(f"Currently processing, {filename}")
            self.upload_file(filename, overwrite=overwrite)
            print(f"Finished processing, {filename}")

    def __create_service_client(self):
        return BlobServiceClient.from_connection_string(self.credentials)

    def __get_service_container(self):
        if self.container_name is None:
            container = list(self.service_client.list_containers())[0]
        else:
            container = list(self.service_client.list_containers(name_starts_with=self.container_name))[0]
        return self.service_client.get_container_client(container)
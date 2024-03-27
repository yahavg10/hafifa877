from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import base64

CONNECTION_STRING = """DefaultEndpointsProtocol=https;
EndpointSuffix=core.windows.net;
AccountName=onboardingpractice;
AccountKey=2qAbr+yOWtOTrtZ50YLRRDsqp8eLL/zgOXl4pdeiWyanhZ4VkFMqXwd6PMAUBRqy0oTo1QcX2F79+AStaFSy9g==;
BlobEndpoint=https://onboardingpractice.blob.core.windows.net/;
FileEndpoint=https://onboardingpractice.file.core.windows.net/;
QueueEndpoint=https://onboardingpractice.queue.core.windows.net/;
TableEndpoint=https://onboardingpractice.table.core.windows.net/"""


def process_files():
    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)

    container_client = blob_service_client.get_container_client("python")

    for blob in container_client.list_blobs():

        blob_client = container_client.get_blob_client(blob.name)
        blob_data = blob_client.download_blob().readall()

        decoded_data = base64.b64decode(blob_data).decode('utf-8')

        new_blob_client = container_client.get_blob_client(blob.name)
        new_blob_client.upload_blob(decoded_data, overwrite=True)


process_files()




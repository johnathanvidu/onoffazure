from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
import os


credential = DefaultAzureCredential()
resource_client = ResourceManagementClient(credential, "24aae708-4612-497c-a91e-7ec5c657f9db")

# Retrieve the list of resource groups
group_list = resource_client.resource_groups.list()

# Show the groups in formatted output
column_width = 40

print("Resource Group".ljust(column_width) + "Location")
print("-" * (column_width * 2))

for group in list(group_list):
    print(f"{group.name:<{column_width}}{group.location}")

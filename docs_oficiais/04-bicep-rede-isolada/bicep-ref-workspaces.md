# Microsoft.MachineLearningServices workspaces

- [Latest](workspaces)
- [2026-09-01](2026-09-01/workspaces)
- [2026-07-15-preview](2026-07-15-preview/workspaces)
- [2026-07-01](2026-07-01/workspaces)
- [2026-05-15-preview](2026-05-15-preview/workspaces)
- [2026-05-01](2026-05-01/workspaces)
- [2026-03-15-preview](2026-03-15-preview/workspaces)
- [2026-03-01](2026-03-01/workspaces)
- [2026-01-15-preview](2026-01-15-preview/workspaces)
- [2025-12-01](2025-12-01/workspaces)
- [2025-10-01-preview](2025-10-01-preview/workspaces)
- [2025-09-01](2025-09-01/workspaces)
- [2025-07-01-preview](2025-07-01-preview/workspaces)
- [2025-06-01](2025-06-01/workspaces)
- [2025-04-01](2025-04-01/workspaces)
- [2025-04-01-preview](2025-04-01-preview/workspaces)
- [2025-01-01-preview](2025-01-01-preview/workspaces)
- [2024-10-01](2024-10-01/workspaces)
- [2024-10-01-preview](2024-10-01-preview/workspaces)
- [2024-07-01-preview](2024-07-01-preview/workspaces)
- [2024-04-01](2024-04-01/workspaces)
- [2024-04-01-preview](2024-04-01-preview/workspaces)
- [2024-01-01-preview](2024-01-01-preview/workspaces)
- [2023-10-01](2023-10-01/workspaces)
- [2023-08-01-preview](2023-08-01-preview/workspaces)
- [2023-06-01-preview](2023-06-01-preview/workspaces)
- [2023-04-01](2023-04-01/workspaces)
- [2023-04-01-preview](2023-04-01-preview/workspaces)
- [2023-02-01-preview](2023-02-01-preview/workspaces)
- [2022-12-01-preview](2022-12-01-preview/workspaces)
- [2022-10-01](2022-10-01/workspaces)
- [2022-10-01-preview](2022-10-01-preview/workspaces)
- [2022-06-01-preview](2022-06-01-preview/workspaces)
- [2022-05-01](2022-05-01/workspaces)
- [2022-02-01-preview](2022-02-01-preview/workspaces)
- [2022-01-01-preview](2022-01-01-preview/workspaces)
- [2021-07-01](2021-07-01/workspaces)
- [2021-04-01](2021-04-01/workspaces)
- [2021-03-01-preview](2021-03-01-preview/workspaces)
- [2021-01-01](2021-01-01/workspaces)
- [2020-09-01-preview](2020-09-01-preview/workspaces)
- [2020-08-01](2020-08-01/workspaces)
- [2020-06-01](2020-06-01/workspaces)
- [2020-05-15-preview](2020-05-15-preview/workspaces)
- [2020-05-01-preview](2020-05-01-preview/workspaces)
- [2020-04-01](2020-04-01/workspaces)
- [2020-04-01-preview](2020-04-01-preview/workspaces)
- [2020-03-01](2020-03-01/workspaces)
- [2020-02-18-preview](2020-02-18-preview/workspaces)
- [2020-01-01](2020-01-01/workspaces)
- [2019-11-01](2019-11-01/workspaces)
- [2019-06-01](2019-06-01/workspaces)
- [2019-05-01](2019-05-01/workspaces)
- [2018-11-19](2018-11-19/workspaces)
- [2018-03-01-preview](2018-03-01-preview/workspaces)

::: zone pivot="deployment-language-bicep"

## Bicep resource definition

The workspaces resource type can be deployed with operations that target:

- **Resource groups** - See [resource group deployment commands](/en-us/azure/azure-resource-manager/bicep/deploy-to-resource-group)

For a list of changed properties in each API version, see [change log](change-log/workspaces).

## Usage Examples

### Bicep Samples

A basic example of deploying Azure Machine Learning Workspace.

```bicep
param resourceName string = 'acctest0001'
param location string = 'westeurope'

resource storageAccount 'Microsoft.Storage/storageAccounts@2021-09-01' = {
  name: resourceName
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    accessTier: 'Hot'
    allowBlobPublicAccess: true
    allowCrossTenantReplication: true
    allowSharedKeyAccess: true
    defaultToOAuthAuthentication: false
    encryption: {
      keySource: 'Microsoft.Storage'
      services: {
        queue: {
          keyType: 'Service'
        }
        table: {
          keyType: 'Service'
        }
      }
    }
    isHnsEnabled: false
    isNfsV3Enabled: false
    isSftpEnabled: false
    minimumTlsVersion: 'TLS1_2'
    networkAcls: {
      defaultAction: 'Allow'
    }
    publicNetworkAccess: 'Enabled'
    supportsHttpsTrafficOnly: true
  }
}

resource vault 'Microsoft.KeyVault/vaults@2021-10-01' = {
  name: resourceName
  location: location
  properties: {
    accessPolicies: [
      {
        objectId: '45a2d1ea-488a-44b0-bb2e-3cd8e485ebef'
        permissions: {
          certificates: [
            'all'
          ]
          keys: [
            'all'
          ]
          secrets: [
            'all'
          ]
          storage: []
        }
        tenantId: tenant().tenantId
      }
    ]
    createMode: 'default'
    enablePurgeProtection: true
    enableRbacAuthorization: false
    enableSoftDelete: true
    enabledForDeployment: false
    enabledForDiskEncryption: false
    enabledForTemplateDeployment: false
    publicNetworkAccess: 'Enabled'
    sku: {
      family: 'A'
      name: 'standard'
    }
    tenantId: tenant().tenantId
  }
}

resource workspace 'Microsoft.MachineLearningServices/workspaces@2022-05-01' = {
  name: resourceName
  location: location
  sku: {
    name: 'Basic'
    tier: 'Basic'
  }
  properties: {
    applicationInsights: component.id
    keyVault: vault.id
    publicNetworkAccess: 'Disabled'
    storageAccount: storageAccount.id
    v1LegacyMode: false
  }
}

resource component 'Microsoft.Insights/components@2020-02-02' = {
  name: resourceName
  location: location
  kind: 'web'
  properties: {
    Application_Type: 'web'
    DisableIpMasking: false
    DisableLocalAuth: false
    ForceCustomerStorageForProfiler: false
    RetentionInDays: 90
    SamplingPercentage: 100
    publicNetworkAccessForIngestion: 'Enabled'
    publicNetworkAccessForQuery: 'Enabled'
  }
}
```

### Azure Verified Modules

The following [Azure Verified Modules](https://aka.ms/avm) can be used to deploy this resource type.

| Module | Description |
| --- | --- |
| [Machine Learning Services Workspace](https://github.com/Azure/bicep-registry-modules/tree/main/avm/res/machine-learning-services/workspace) | AVM Resource Module for Machine Learning Services Workspace |

### Azure Quickstart Samples

The following [Azure Quickstart templates](https://aka.ms/azqst) contain Bicep samples for deploying this resource type.

| Bicep File | Description |
| --- | --- |
| [Azure AI Foundry basic setup](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/aifoundry-basics/main.bicep) | This set of templates demonstrates how to set up Azure AI Foundry with the basic setup, meaning with public internet access enabled, Microsoft-managed keys for encryption and Microsoft-managed identity configuration for the AI resource. |
| [Azure AI Foundry basic setup](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/aifoundry-cmk/main.bicep) | This set of templates demonstrates how to set up Azure AI Foundry with the basic setup, meaning with public internet access enabled, Microsoft-managed keys for encryption and Microsoft-managed identity configuration for the AI resource. |
| [Azure AI Foundry Network Restricted](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/aifoundry-network-restricted/main.bicep) | This set of templates demonstrates how to set up Azure AI Foundry with private link and egress disabled, using Microsoft-managed keys for encryption and Microsoft-managed identity configuration for the AI resource. |
| [Azure AI Foundry with Microsoft Entra ID Authentication](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/aifoundry-entraid-passthrough/main.bicep) | This set of templates demonstrates how to set up Azure AI Foundry with Microsoft Entra ID authentication for dependent resources, such as Azure AI Services and Azure Storage. |
| [Azure AI Studio basic setup](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/aistudio-cmk-service-side-encryption/main.bicep) | This set of templates demonstrates how to set up Azure AI Studio with the basic setup, meaning with public internet access enabled, Microsoft-managed keys for encryption and Microsoft-managed identity configuration for the AI resource. |
| [Azure AI Studio Network Restricted](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-network-restricted/main.bicep) | This set of templates demonstrates how to set up Azure AI Studio with private link and egress disabled, using Microsoft-managed keys for encryption and Microsoft-managed identity configuration for the AI resource. |
| [Azure Machine Learning end-to-end secure setup](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-end-to-end-secure/main.bicep) | This set of Bicep templates demonstrates how to set up Azure Machine Learning end-to-end in a secure set up. This reference implementation includes the Workspace, a compute cluster, compute instance and attached private AKS cluster. |
| [Azure Machine Learning end-to-end secure setup (legacy)](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-end-to-end-secure-v1-legacy-mode/main.bicep) | This set of Bicep templates demonstrates how to set up Azure Machine Learning end-to-end in a secure set up. This reference implementation includes the Workspace, a compute cluster, compute instance and attached private AKS cluster. |
| [Basic Agent Setup API Keys](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.azure-ai-agent-service/basic-agent-keys/main.bicep) | This set of templates demonstrates how to set up Azure AI Agent Service with the basic setup using API keys authetication for the AI Service/AOAI connection. Agents use multi-tenant search and storage resources fully managed by Microsoft. You won’t have visibility or control over these underlying Azure resources. |
| [Basic Agent Setup Identity](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.azure-ai-agent-service/basic-agent-identity/main.bicep) | This set of templates demonstrates how to set up Azure AI Agent Service with the basic setup using managed identity authetication for the AI Service/AOAI connection. Agents use multi-tenant search and storage resources fully managed by Microsoft. You won’t have visibility or control over these underlying Azure resources. |
| [Create an AKS compute target with a Private IP address](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-private-ip/main.bicep) | This template creates an AKS compute target in given Azure Machine Learning service workspace with a private IP address. |
| [Create an Azure Machine Learning service workspace](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-workspace/main.bicep) | This deployment template specifies an Azure Machine Learning workspace, and its associated resources including Azure Key Vault, Azure Storage, Azure Application Insights and Azure Container Registry. This configuration describes the minimal set of resources you require to get started with Azure Machine Learning. |
| [Create an Azure Machine Learning service workspace (CMK)](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-workspace-cmk-service-side-encryption/main.bicep) | This deployment template specifies how to create an Azure Machine Learning workspace with service-side encryption using your encryption keys. |
| [Create an Azure Machine Learning service workspace (CMK)](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-workspace-cmk/main.bicep) | This deployment template specifies an Azure Machine Learning workspace, and its associated resources including Azure Key Vault, Azure Storage, Azure Application Insights and Azure Container Registry. The example shows how to configure Azure Machine Learning for encryption with a customer-managed encryption key. |
| [Create an Azure Machine Learning service workspace (legacy)](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-workspace-vnet-v1-legacy-mode/main.bicep) | This deployment template specifies an Azure Machine Learning workspace, and its associated resources including Azure Key Vault, Azure Storage, Azure Application Insights and Azure Container Registry. This configuration describes the set of resources you require to get started with Azure Machine Learning in a network isolated set up. |
| [Create an Azure Machine Learning service workspace (vnet)](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-workspace-vnet/main.bicep) | This deployment template specifies an Azure Machine Learning workspace, and its associated resources including Azure Key Vault, Azure Storage, Azure Application Insights and Azure Container Registry. This configuration describes the set of resources you require to get started with Azure Machine Learning in a network isolated set up. |
| [Deploy Secure AI Foundry with a managed virtual network](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/aifoundry-networking-aoao/main.bicep) | This template creates a secure Azure AI Foundry environment with robust network and identity security restrictions. |
| [Network Secured Agent with User Managed Identity](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.azure-ai-agent-service/network-secured-agent/main.bicep) | This set of templates demonstrates how to set up Azure AI Agent Service with virtual network isolation using User Managed Identity authetication for the AI Service/AOAI connection and private network links to connect the agent to your secure data. |
| [Standard Agent Setup](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.azure-ai-agent-service/standard-agent/main.bicep) | This set of templates demonstrates how to set up Azure AI Agent Service with the standard setup, meaning with managed identity authentication for project/hub connections and public internet access enabled. Agents use customer-owned, single-tenant search and storage resources. With this setup, you have full control and visibility over these resources, but you will incur costs based on your usage. |

## Resource format

To create a Microsoft.MachineLearningServices/workspaces resource, add the following Bicep to your template.

```bicep
resource symbolicname 'Microsoft.MachineLearningServices/workspaces@2026-09-01' = {
  identity: {
    type: 'string'
    userAssignedIdentities: {
      {customized property}: {}
    }
  }
  kind: 'string'
  location: 'string'
  name: 'string'
  properties: {
    allowPublicAccessWhenBehindVnet: bool
    applicationInsights: 'string'
    associatedWorkspaces: [
      'string'
    ]
    containerRegistry: 'string'
    description: 'string'
    discoveryUrl: 'string'
    enableDataIsolation: bool
    enableServiceSideCMKEncryption: bool
    encryption: {
      cosmosDbResourceId: 'string'
      identity: {
        userAssignedIdentity: 'string'
      }
      keyVaultProperties: {
        identityClientId: 'string'
        keyIdentifier: 'string'
        keyVaultArmId: 'string'
      }
      searchAccountResourceId: 'string'
      status: 'string'
      storageAccountResourceId: 'string'
    }
    featureStoreSettings: {
      computeRuntime: {
        sparkRuntimeVersion: 'string'
      }
      offlineStoreConnectionName: 'string'
      onlineStoreConnectionName: 'string'
    }
    friendlyName: 'string'
    hbiWorkspace: bool
    hubResourceId: 'string'
    imageBuildCompute: 'string'
    keyVault: 'string'
    managedNetwork: {
      enableNetworkMonitor: bool
      firewallSku: 'string'
      isolationMode: 'string'
      managedNetworkKind: 'string'
      outboundRules: {
        {customized property}: {
          category: 'string'
          status: 'string'
          type: 'string'
          // For remaining properties, see OutboundRule objects
        }
      }
      status: {
        sparkReady: bool
        status: 'string'
      }
    }
    primaryUserAssignedIdentity: 'string'
    provisionNetworkNow: bool
    publicNetworkAccess: 'string'
    serverlessComputeSettings: {
      serverlessComputeCustomSubnet: 'string'
      serverlessComputeNoPublicIP: bool
    }
    serviceManagedResourcesSettings: {
      cosmosDb: {
        collectionsThroughput: int
      }
    }
    sharedPrivateLinkResources: [
      {
        name: 'string'
        properties: {
          groupId: 'string'
          privateLinkResourceId: 'string'
          requestMessage: 'string'
          status: 'string'
        }
      }
    ]
    storageAccount: 'string'
    systemDatastoresAuthMode: 'string'
    v1LegacyMode: bool
    workspaceHubConfig: {
      additionalWorkspaceStorageAccounts: [
        'string'
      ]
      defaultWorkspaceResourceGroup: 'string'
    }
  }
  sku: {
    capacity: int
    family: 'string'
    name: 'string'
    size: 'string'
    tier: 'string'
  }
  tags: {
    {customized property}: 'string'
  }
}
```

### OutboundRule objects

Set the **type** property to specify the type of object.

For **FQDN**, use:

```bicep
{
  destination: 'string'
  type: 'FQDN'
}
```

For **PrivateEndpoint**, use:

```bicep
{
  destination: {
    serviceResourceId: 'string'
    sparkEnabled: bool
    sparkStatus: 'string'
    subresourceTarget: 'string'
  }
  fqdns: [
    'string'
  ]
  type: 'PrivateEndpoint'
}
```

For **ServiceTag**, use:

```bicep
{
  destination: {
    action: 'string'
    addressPrefixes: [
      'string'
    ]
    portRanges: 'string'
    protocol: 'string'
    serviceTag: 'string'
  }
  type: 'ServiceTag'
}
```

## Property Values

### Microsoft.MachineLearningServices/workspaces

| Name | Description | Value |
| --- | --- | --- |
| identity | The managed service identities assigned to this resource. | ManagedServiceIdentity |
| kind |  | string |
| location |  | string |
| name | The resource name | string Constraints:Pattern = `^[a-zA-Z0-9][a-zA-Z0-9_-]{2,32}$` (required) |
| properties | Additional attributes of the entity. | WorkspaceProperties (required) |
| sku | Optional. This field is required to be implemented by the RP because AML is supporting more than one tier | Sku |
| tags | Resource tags | Dictionary of tag names and values. See [Tags in templates](/en-us/azure/azure-resource-manager/management/tag-resources#arm-templates) |

### ComputeRuntimeDto

| Name | Description | Value |
| --- | --- | --- |
| sparkRuntimeVersion |  | string |

### CosmosDbSettings

| Name | Description | Value |
| --- | --- | --- |
| collectionsThroughput |  | int |

### EncryptionProperty

| Name | Description | Value |
| --- | --- | --- |
| cosmosDbResourceId | The byok cosmosdb account that customer brings to store customer's datawith encryption | string |
| identity | Identity to be used with the keyVault | IdentityForCmk |
| keyVaultProperties | KeyVault details to do the encryption | KeyVaultProperties (required) |
| searchAccountResourceId | The byok search account that customer brings to store customer's datawith encryption | string |
| status | Indicates whether or not the encryption is enabled for the workspace. | 'Disabled''Enabled' (required) |
| storageAccountResourceId | The byok storage account that customer brings to store customer's datawith encryption | string |

### FeatureStoreSettings

| Name | Description | Value |
| --- | --- | --- |
| computeRuntime |  | ComputeRuntimeDto |
| offlineStoreConnectionName |  | string |
| onlineStoreConnectionName |  | string |

### FqdnOutboundRule

| Name | Description | Value |
| --- | --- | --- |
| destination |  | string |
| type | Type of a managed network Outbound Rule of a machine learning workspace. | 'FQDN' (required) |

### IdentityForCmk

| Name | Description | Value |
| --- | --- | --- |
| userAssignedIdentity | UserAssignedIdentity to be used to fetch the encryption key from keyVault | string |

### KeyVaultProperties

| Name | Description | Value |
| --- | --- | --- |
| identityClientId | Currently, we support only SystemAssigned MSI.We need this when we support UserAssignedIdentities | string |
| keyIdentifier | KeyVault key identifier to encrypt the data | string Constraints:Min length = 1Pattern = `[a-zA-Z0-9_]` (required) |
| keyVaultArmId | KeyVault Arm Id that contains the data encryption key | string Constraints:Min length = 1Pattern = `[a-zA-Z0-9_]` (required) |

### ManagedNetworkProvisionStatus

| Name | Description | Value |
| --- | --- | --- |
| sparkReady |  | bool |
| status | Status for the managed network of a machine learning workspace. | 'Active''Inactive' |

### ManagedNetworkSettings

| Name | Description | Value |
| --- | --- | --- |
| enableNetworkMonitor | A flag to indicate if monitoring needs to be enabled for the managed network. | bool |
| firewallSku | Firewall Sku used for FQDN Rules | 'Basic''Standard' |
| isolationMode | Isolation mode for the managed network of a machine learning workspace. | 'AllowInternetOutbound''AllowOnlyApprovedOutbound''Disabled' |
| managedNetworkKind | The Kind of the managed network. Users can switch from V1 to V2 for granular access controls, but cannot switch back to V1 once V2 is enabled. | 'V1''V2' |
| outboundRules | Dictionary of &lt;OutboundRule&gt; | ManagedNetworkSettingsOutboundRules |
| status | Status of the Provisioning for the managed network of a machine learning workspace. | ManagedNetworkProvisionStatus |

### ManagedNetworkSettingsOutboundRules

| Name | Description | Value |
| --- | --- | --- |

### ManagedServiceIdentity

| Name | Description | Value |
| --- | --- | --- |
| type | Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed). | 'None''SystemAssigned''SystemAssigned,UserAssigned''UserAssigned' (required) |
| userAssignedIdentities | The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests. | UserAssignedIdentities |

### OutboundRule

| Name | Description | Value |
| --- | --- | --- |
| category | Category of a managed network Outbound Rule of a machine learning workspace. | 'Dependency''Recommended''Required''UserDefined' |
| status | Type of a managed network Outbound Rule of a machine learning workspace. | 'Active''Deleting''Failed''Inactive''Provisioning' |
| type | Set to 'FQDN' for type FqdnOutboundRule. Set to 'PrivateEndpoint' for type PrivateEndpointOutboundRule. Set to 'ServiceTag' for type ServiceTagOutboundRule. | 'FQDN''PrivateEndpoint''ServiceTag' (required) |

### PrivateEndpointDestination

| Name | Description | Value |
| --- | --- | --- |
| serviceResourceId | A type definition that refers the id to an Azure Resource Manager resource. | string |
| sparkEnabled |  | bool |
| sparkStatus | Type of a managed network Outbound Rule of a machine learning workspace. | 'Active''Deleting''Failed''Inactive''Provisioning' |
| subresourceTarget |  | string |

### PrivateEndpointOutboundRule

| Name | Description | Value |
| --- | --- | --- |
| destination | Private Endpoint destination for a Private Endpoint Outbound Rule for the managed network of a machine learning workspace. | PrivateEndpointDestination |
| fqdns |  | string[] |
| type | Type of a managed network Outbound Rule of a machine learning workspace. | 'PrivateEndpoint' (required) |

### ServerlessComputeSettings

| Name | Description | Value |
| --- | --- | --- |
| serverlessComputeCustomSubnet | The resource ID of an existing virtual network subnet in which serverless compute nodes should be deployed | string |
| serverlessComputeNoPublicIP | The flag to signal if serverless compute nodes deployed in custom vNet would have no public IP addresses for a workspace with private endpoint | bool |

### ServiceManagedResourcesSettings

| Name | Description | Value |
| --- | --- | --- |
| cosmosDb |  | CosmosDbSettings |

### ServiceTagDestination

| Name | Description | Value |
| --- | --- | --- |
| action | The action enum for networking rule. | 'Allow''Deny' |
| addressPrefixes | Optional, if provided, the ServiceTag property will be ignored. | string[] |
| portRanges |  | string |
| protocol |  | string |
| serviceTag |  | string |

### ServiceTagOutboundRule

| Name | Description | Value |
| --- | --- | --- |
| destination | Service Tag destination for a Service Tag Outbound Rule for the managed network of a machine learning workspace. | ServiceTagDestination |
| type | Type of a managed network Outbound Rule of a machine learning workspace. | 'ServiceTag' (required) |

### SharedPrivateLinkResource

| Name | Description | Value |
| --- | --- | --- |
| name | Unique name of the private link | string |
| properties | Properties of a shared private link resource. | SharedPrivateLinkResourceProperty |

### SharedPrivateLinkResourceProperty

| Name | Description | Value |
| --- | --- | --- |
| groupId | group id of the private link | string |
| privateLinkResourceId | the resource id that private link links to | string |
| requestMessage | Request message | string |
| status | Connection status of the service consumer with the service provider\r\nPossible state transitions\r\nPending -&gt; Approved (Service provider approves the connection request)\r\nPending -&gt; Rejected (Service provider rejects the connection request)\r\nPending -&gt; Disconnected (Service provider deletes the connection)\r\nApproved -&gt; Rejected (Service provider rejects the approved connection)\r\nApproved -&gt; Disconnected (Service provider deletes the connection)\r\nRejected -&gt; Pending (Service consumer re-initiates the connection request that was rejected)\r\nRejected -&gt; Disconnected (Service provider deletes the connection) | 'Approved''Disconnected''Pending''Rejected''Timeout' |

### Sku

| Name | Description | Value |
| --- | --- | --- |
| capacity | If the SKU supports scale out/in then the capacity integer should be included. If scale out/in is not possible for the resource this may be omitted. | int |
| family | If the service has different generations of hardware, for the same SKU, then that can be captured here. | string |
| name | The name of the SKU. Ex - P3. It is typically a letter+number code | string (required) |
| size | The SKU size. When the name field is the combination of tier and some other value, this would be the standalone code. | string |
| tier | This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT. | 'Basic''Free''Premium''Standard' |

### UserAssignedIdentities

| Name | Description | Value |
| --- | --- | --- |

### UserAssignedIdentity

| Name | Description | Value |
| --- | --- | --- |

### WorkspaceHubConfig

| Name | Description | Value |
| --- | --- | --- |
| additionalWorkspaceStorageAccounts |  | string[] |
| defaultWorkspaceResourceGroup |  | string |

### WorkspaceProperties

| Name | Description | Value |
| --- | --- | --- |
| allowPublicAccessWhenBehindVnet | The flag to indicate whether to allow public access when behind VNet. | bool |
| applicationInsights | ARM id of the application insights associated with this workspace. | string |
| associatedWorkspaces |  | string[] |
| containerRegistry | ARM id of the container registry associated with this workspace. | string |
| description | The description of this workspace. | string |
| discoveryUrl | Url for the discovery service to identify regional endpoints for machine learning experimentation services | string |
| enableDataIsolation |  | bool |
| enableServiceSideCMKEncryption |  | bool |
| encryption |  | EncryptionProperty |
| featureStoreSettings | Settings for feature store type workspace. | FeatureStoreSettings |
| friendlyName | The friendly name for this workspace. This name in mutable | string |
| hbiWorkspace | The flag to signal HBI data in the workspace and reduce diagnostic data collected by the service | bool |
| hubResourceId |  | string |
| imageBuildCompute | The compute name for image build | string |
| keyVault | ARM id of the key vault associated with this workspace. This cannot be changed once the workspace has been created | string |
| managedNetwork | Managed Network settings for a machine learning workspace. | ManagedNetworkSettings |
| primaryUserAssignedIdentity | The user assigned identity resource id that represents the workspace identity. | string |
| provisionNetworkNow | Set to trigger the provisioning of the managed VNet with the default Options when creating a Workspace with the managed VNet enabled, or else it does nothing. | bool |
| publicNetworkAccess | Whether requests from Public Network are allowed. | 'Disabled''Enabled' |
| serverlessComputeSettings | Settings for serverless compute in a workspace | ServerlessComputeSettings |
| serviceManagedResourcesSettings | The service managed resource settings. | ServiceManagedResourcesSettings |
| sharedPrivateLinkResources | The list of shared private link resources in this workspace. | SharedPrivateLinkResource[] |
| storageAccount | ARM id of the storage account associated with this workspace. This cannot be changed once the workspace has been created | string |
| systemDatastoresAuthMode | The auth mode used for accessing the system datastores of the workspace. | 'AccessKey''Identity''UserDelegationSAS' |
| v1LegacyMode | Enabling v1\_legacy\_mode may prevent you from using features provided by the v2 API. | bool |
| workspaceHubConfig | WorkspaceHub's configuration object. | WorkspaceHubConfig |

### WorkspaceTags

| Name | Description | Value |
| --- | --- | --- |

::: zone-end

::: zone pivot="deployment-language-arm-template"

## ARM template resource definition

The workspaces resource type can be deployed with operations that target:

- **Resource groups** - See [resource group deployment commands](/en-us/azure/azure-resource-manager/templates/deploy-to-resource-group) For a list of changed properties in each API version, see [change log](change-log/workspaces).

## Usage Examples

### Azure Quickstart Templates

The following [Azure Quickstart templates](https://aka.ms/azqst) deploy this resource type.

| Template | Description |
| --- | --- |
| [Azure AI Foundry basic setup](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/aifoundry-basics)[![Deploy to Azure](../media/deploy-to-azure.svg)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.machinelearningservices%2Faifoundry-basics%2Fazuredeploy.json) | This set of templates demonstrates how to set up Azure AI Foundry with the basic setup, meaning with public internet access enabled, Microsoft-managed keys for encryption and Microsoft-managed identity configuration for the AI resource. |
| [Azure AI Foundry basic setup](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/aifoundry-cmk)[![Deploy to Azure](../media/deploy-to-azure.svg)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.machinelearningservices%2Faifoundry-cmk%2Fazuredeploy.json) | This set of templates demonstrates how to set up Azure AI Foundry with the basic setup, meaning with public internet access enabled, Microsoft-managed keys for encryption and Microsoft-managed identity configuration for the AI resource. |
| [Azure AI Foundry Network Restricted](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/aifoundry-network-restricted)[![Deploy to Azure](../media/deploy-to-azure.svg)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.machinelearningservices%2Faifoundry-network-restricted%2Fazuredeploy.json) | This set of templates demonstrates how to set up Azure AI Foundry with private link and egress disabled, using Microsoft-managed keys for encryption and Microsoft-managed identity configuration for the AI resource. |
| [Azure AI Foundry with Microsoft Entra ID Authentication](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/aifoundry-entraid-passthrough)[![Deploy to Azure](../media/deploy-to-azure.svg)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.machinelearningservices%2Faifoundry-entraid-passthrough%2Fazuredeploy.json) | This set of templates demonstrates how to set up Azure AI Foundry with Microsoft Entra ID authentication for dependent resources, such as Azure AI Services and Azure Storage. |
| [Azure AI Studio basic setup](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/aistudio-cmk-service-side-encryption)[![Deploy to Azure](../media/deploy-to-azure.svg)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.machinelearningservices%2Faistudio-cmk-service-side-encryption%2Fazuredeploy.json) | This set of templates demonstrates how to set up Azure AI Studio with the basic setup, meaning with public internet access enabled, Microsoft-managed keys for encryption and Microsoft-managed identity configuration for the AI resource. |
| [Azure AI Studio Network Restricted](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-network-restricted)[![Deploy to Azure](../media/deploy-to-azure.svg)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.machinelearningservices%2Fmachine-learning-network-restricted%2Fazuredeploy.json) | This set of templates demonstrates how to set up Azure AI Studio with private link and egress disabled, using Microsoft-managed keys for encryption and Microsoft-managed identity configuration for the AI resource. |
| [Azure Machine Learning end-to-end secure setup](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-end-to-end-secure)[![Deploy to Azure](../media/deploy-to-azure.svg)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.machinelearningservices%2Fmachine-learning-end-to-end-secure%2Fazuredeploy.json) | This set of Bicep templates demonstrates how to set up Azure Machine Learning end-to-end in a secure set up. This reference implementation includes the Workspace, a compute cluster, compute instance and attached private AKS cluster. |
| [Azure Machine Learning end-to-end secure setup (legacy)](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-end-to-end-secure-v1-legacy-mode)[![Deploy to Azure](../media/deploy-to-azure.svg)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.machinelearningservices%2Fmachine-learning-end-to-end-secure-v1-legacy-mode%2Fazuredeploy.json) | This set of Bicep templates demonstrates how to set up Azure Machine Learning end-to-end in a secure set up. This reference implementation includes the Workspace, a compute cluster, compute instance and attached private AKS cluster. |
| [Azure Machine Learning Workspace](https://github.com/Azure/azure-quickstart-templates/tree/master/modules/machine-learning-workspace/0.9)[![Deploy to Azure](../media/deploy-to-azure.svg)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fmodules%2Fmachine-learning-workspace%2F0.9%2Fazuredeploy.json) | This template creates a new Azure Machine Learning Workspace, along with an encrypted Storage Account, KeyVault and Applications Insights Logging |
| [Basic Agent Setup API Keys](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.azure-ai-agent-service/basic-agent-keys)[![Deploy to Azure](../media/deploy-to-azure.svg)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.azure-ai-agent-service%2Fbasic-agent-keys%2Fazuredeploy.json) | This set of templates demonstrates how to set up Azure AI Agent Service with the basic setup using API keys authetication for the AI Service/AOAI connection. Agents use multi-tenant search and storage resources fully managed by Microsoft. You won’t have visibility or control over these underlying Azure resources. |
| [Basic Agent Setup Identity](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.azure-ai-agent-service/basic-agent-identity)[![Deploy to Azure](../media/deploy-to-azure.svg)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.azure-ai-agent-service%2Fbasic-agent-identity%2Fazuredeploy.json) | This set of templates demonstrates how to set up Azure AI Agent Service with the basic setup using managed identity authetication for the AI Service/AOAI connection. Agents use multi-tenant search and storage resources fully managed by Microsoft. You won’t have visibility or control over these underlying Azure resources. |
| [Create AML workspace with multiple Datasets & Datastores](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-dataset-create-workspace-multiple-dataset-datastore)[![Deploy to Azure](../media/deploy-to-azure.svg)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.machinelearningservices%2Fmachine-learning-dataset-create-workspace-multiple-dataset-datastore%2Fazuredeploy.json) | This template creates Azure Machine Learning workspace with multiple datasets & datastores. |
| [Create an AKS compute target with a Private IP address](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-private-ip)[![Deploy to Azure](../media/deploy-to-azure.svg)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.machinelearningservices%2Fmachine-learning-private-ip%2Fazuredeploy.json) | This template creates an AKS compute target in given Azure Machine Learning service workspace with a private IP address. |
| [Create an Azure Machine Learning service workspace](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-workspace)[![Deploy to Azure](../media/deploy-to-azure.svg)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.machinelearningservices%2Fmachine-learning-workspace%2Fazuredeploy.json) | This deployment template specifies an Azure Machine Learning workspace, and its associated resources including Azure Key Vault, Azure Storage, Azure Application Insights and Azure Container Registry. This configuration describes the minimal set of resources you require to get started with Azure Machine Learning. |
| [Create an Azure Machine Learning service workspace (CMK)](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-workspace-cmk-service-side-encryption)[![Deploy to Azure](../media/deploy-to-azure.svg)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.machinelearningservices%2Fmachine-learning-workspace-cmk-service-side-encryption%2Fazuredeploy.json) | This deployment template specifies how to create an Azure Machine Learning workspace with service-side encryption using your encryption keys. |
| [Create an Azure Machine Learning service workspace (CMK)](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-workspace-cmk)[![Deploy to Azure](../media/deploy-to-azure.svg)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.machinelearningservices%2Fmachine-learning-workspace-cmk%2Fazuredeploy.json) | This deployment template specifies an Azure Machine Learning workspace, and its associated resources including Azure Key Vault, Azure Storage, Azure Application Insights and Azure Container Registry. The example shows how to configure Azure Machine Learning for encryption with a customer-managed encryption key. |
| [Create an Azure Machine Learning service workspace (legacy)](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-workspace-vnet-v1-legacy-mode)[![Deploy to Azure](../media/deploy-to-azure.svg)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.machinelearningservices%2Fmachine-learning-workspace-vnet-v1-legacy-mode%2Fazuredeploy.json) | This deployment template specifies an Azure Machine Learning workspace, and its associated resources including Azure Key Vault, Azure Storage, Azure Application Insights and Azure Container Registry. This configuration describes the set of resources you require to get started with Azure Machine Learning in a network isolated set up. |
| [Create an Azure Machine Learning service workspace (vnet)](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-workspace-vnet)[![Deploy to Azure](../media/deploy-to-azure.svg)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.machinelearningservices%2Fmachine-learning-workspace-vnet%2Fazuredeploy.json) | This deployment template specifies an Azure Machine Learning workspace, and its associated resources including Azure Key Vault, Azure Storage, Azure Application Insights and Azure Container Registry. This configuration describes the set of resources you require to get started with Azure Machine Learning in a network isolated set up. |
| [Deploy Secure AI Foundry with a managed virtual network](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/aifoundry-networking-aoao)[![Deploy to Azure](../media/deploy-to-azure.svg)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.machinelearningservices%2Faifoundry-networking-aoao%2Fazuredeploy.json) | This template creates a secure Azure AI Foundry environment with robust network and identity security restrictions. |
| [Network Secured Agent with User Managed Identity](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.azure-ai-agent-service/network-secured-agent)[![Deploy to Azure](../media/deploy-to-azure.svg)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.azure-ai-agent-service%2Fnetwork-secured-agent%2Fazuredeploy.json) | This set of templates demonstrates how to set up Azure AI Agent Service with virtual network isolation using User Managed Identity authetication for the AI Service/AOAI connection and private network links to connect the agent to your secure data. |
| [Standard Agent Setup](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.azure-ai-agent-service/standard-agent)[![Deploy to Azure](../media/deploy-to-azure.svg)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.azure-ai-agent-service%2Fstandard-agent%2Fazuredeploy.json) | This set of templates demonstrates how to set up Azure AI Agent Service with the standard setup, meaning with managed identity authentication for project/hub connections and public internet access enabled. Agents use customer-owned, single-tenant search and storage resources. With this setup, you have full control and visibility over these resources, but you will incur costs based on your usage. |

## Resource format

To create a Microsoft.MachineLearningServices/workspaces resource, add the following JSON to your template.

```json
{
  "type": "Microsoft.MachineLearningServices/workspaces",
  "apiVersion": "2026-09-01",
  "name": "string",
  "identity": {
    "type": "string",
    "userAssignedIdentities": {
      "{customized property}": {
      }
    }
  },
  "kind": "string",
  "location": "string",
  "properties": {
    "allowPublicAccessWhenBehindVnet": "bool",
    "applicationInsights": "string",
    "associatedWorkspaces": [ "string" ],
    "containerRegistry": "string",
    "description": "string",
    "discoveryUrl": "string",
    "enableDataIsolation": "bool",
    "enableServiceSideCMKEncryption": "bool",
    "encryption": {
      "cosmosDbResourceId": "string",
      "identity": {
        "userAssignedIdentity": "string"
      },
      "keyVaultProperties": {
        "identityClientId": "string",
        "keyIdentifier": "string",
        "keyVaultArmId": "string"
      },
      "searchAccountResourceId": "string",
      "status": "string",
      "storageAccountResourceId": "string"
    },
    "featureStoreSettings": {
      "computeRuntime": {
        "sparkRuntimeVersion": "string"
      },
      "offlineStoreConnectionName": "string",
      "onlineStoreConnectionName": "string"
    },
    "friendlyName": "string",
    "hbiWorkspace": "bool",
    "hubResourceId": "string",
    "imageBuildCompute": "string",
    "keyVault": "string",
    "managedNetwork": {
      "enableNetworkMonitor": "bool",
      "firewallSku": "string",
      "isolationMode": "string",
      "managedNetworkKind": "string",
      "outboundRules": {
        "{customized property}": {
          "category": "string",
          "status": "string",
          "type": "string"
          // For remaining properties, see OutboundRule objects
        }
      },
      "status": {
        "sparkReady": "bool",
        "status": "string"
      }
    },
    "primaryUserAssignedIdentity": "string",
    "provisionNetworkNow": "bool",
    "publicNetworkAccess": "string",
    "serverlessComputeSettings": {
      "serverlessComputeCustomSubnet": "string",
      "serverlessComputeNoPublicIP": "bool"
    },
    "serviceManagedResourcesSettings": {
      "cosmosDb": {
        "collectionsThroughput": "int"
      }
    },
    "sharedPrivateLinkResources": [
      {
        "name": "string",
        "properties": {
          "groupId": "string",
          "privateLinkResourceId": "string",
          "requestMessage": "string",
          "status": "string"
        }
      }
    ],
    "storageAccount": "string",
    "systemDatastoresAuthMode": "string",
    "v1LegacyMode": "bool",
    "workspaceHubConfig": {
      "additionalWorkspaceStorageAccounts": [ "string" ],
      "defaultWorkspaceResourceGroup": "string"
    }
  },
  "sku": {
    "capacity": "int",
    "family": "string",
    "name": "string",
    "size": "string",
    "tier": "string"
  },
  "tags": {
    "{customized property}": "string"
  }
}
```

### OutboundRule objects

Set the **type** property to specify the type of object.

For **FQDN**, use:

```json
{
  "destination": "string",
  "type": "FQDN"
}
```

For **PrivateEndpoint**, use:

```json
{
  "destination": {
    "serviceResourceId": "string",
    "sparkEnabled": "bool",
    "sparkStatus": "string",
    "subresourceTarget": "string"
  },
  "fqdns": [ "string" ],
  "type": "PrivateEndpoint"
}
```

For **ServiceTag**, use:

```json
{
  "destination": {
    "action": "string",
    "addressPrefixes": [ "string" ],
    "portRanges": "string",
    "protocol": "string",
    "serviceTag": "string"
  },
  "type": "ServiceTag"
}
```

## Property Values

### Microsoft.MachineLearningServices/workspaces

| Name | Description | Value |
| --- | --- | --- |
| apiVersion | The api version | '2026-09-01' |
| identity | The managed service identities assigned to this resource. | ManagedServiceIdentity |
| kind |  | string |
| location |  | string |
| name | The resource name | string Constraints:Pattern = `^[a-zA-Z0-9][a-zA-Z0-9_-]{2,32}$` (required) |
| properties | Additional attributes of the entity. | WorkspaceProperties (required) |
| sku | Optional. This field is required to be implemented by the RP because AML is supporting more than one tier | Sku |
| tags | Resource tags | Dictionary of tag names and values. See [Tags in templates](/en-us/azure/azure-resource-manager/management/tag-resources#arm-templates) |
| type | The resource type | 'Microsoft.MachineLearningServices/workspaces' |

### ComputeRuntimeDto

| Name | Description | Value |
| --- | --- | --- |
| sparkRuntimeVersion |  | string |

### CosmosDbSettings

| Name | Description | Value |
| --- | --- | --- |
| collectionsThroughput |  | int |

### EncryptionProperty

| Name | Description | Value |
| --- | --- | --- |
| cosmosDbResourceId | The byok cosmosdb account that customer brings to store customer's datawith encryption | string |
| identity | Identity to be used with the keyVault | IdentityForCmk |
| keyVaultProperties | KeyVault details to do the encryption | KeyVaultProperties (required) |
| searchAccountResourceId | The byok search account that customer brings to store customer's datawith encryption | string |
| status | Indicates whether or not the encryption is enabled for the workspace. | 'Disabled''Enabled' (required) |
| storageAccountResourceId | The byok storage account that customer brings to store customer's datawith encryption | string |

### FeatureStoreSettings

| Name | Description | Value |
| --- | --- | --- |
| computeRuntime |  | ComputeRuntimeDto |
| offlineStoreConnectionName |  | string |
| onlineStoreConnectionName |  | string |

### FqdnOutboundRule

| Name | Description | Value |
| --- | --- | --- |
| destination |  | string |
| type | Type of a managed network Outbound Rule of a machine learning workspace. | 'FQDN' (required) |

### IdentityForCmk

| Name | Description | Value |
| --- | --- | --- |
| userAssignedIdentity | UserAssignedIdentity to be used to fetch the encryption key from keyVault | string |

### KeyVaultProperties

| Name | Description | Value |
| --- | --- | --- |
| identityClientId | Currently, we support only SystemAssigned MSI.We need this when we support UserAssignedIdentities | string |
| keyIdentifier | KeyVault key identifier to encrypt the data | string Constraints:Min length = 1Pattern = `[a-zA-Z0-9_]` (required) |
| keyVaultArmId | KeyVault Arm Id that contains the data encryption key | string Constraints:Min length = 1Pattern = `[a-zA-Z0-9_]` (required) |

### ManagedNetworkProvisionStatus

| Name | Description | Value |
| --- | --- | --- |
| sparkReady |  | bool |
| status | Status for the managed network of a machine learning workspace. | 'Active''Inactive' |

### ManagedNetworkSettings

| Name | Description | Value |
| --- | --- | --- |
| enableNetworkMonitor | A flag to indicate if monitoring needs to be enabled for the managed network. | bool |
| firewallSku | Firewall Sku used for FQDN Rules | 'Basic''Standard' |
| isolationMode | Isolation mode for the managed network of a machine learning workspace. | 'AllowInternetOutbound''AllowOnlyApprovedOutbound''Disabled' |
| managedNetworkKind | The Kind of the managed network. Users can switch from V1 to V2 for granular access controls, but cannot switch back to V1 once V2 is enabled. | 'V1''V2' |
| outboundRules | Dictionary of &lt;OutboundRule&gt; | ManagedNetworkSettingsOutboundRules |
| status | Status of the Provisioning for the managed network of a machine learning workspace. | ManagedNetworkProvisionStatus |

### ManagedNetworkSettingsOutboundRules

| Name | Description | Value |
| --- | --- | --- |

### ManagedServiceIdentity

| Name | Description | Value |
| --- | --- | --- |
| type | Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed). | 'None''SystemAssigned''SystemAssigned,UserAssigned''UserAssigned' (required) |
| userAssignedIdentities | The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests. | UserAssignedIdentities |

### OutboundRule

| Name | Description | Value |
| --- | --- | --- |
| category | Category of a managed network Outbound Rule of a machine learning workspace. | 'Dependency''Recommended''Required''UserDefined' |
| status | Type of a managed network Outbound Rule of a machine learning workspace. | 'Active''Deleting''Failed''Inactive''Provisioning' |
| type | Set to 'FQDN' for type FqdnOutboundRule. Set to 'PrivateEndpoint' for type PrivateEndpointOutboundRule. Set to 'ServiceTag' for type ServiceTagOutboundRule. | 'FQDN''PrivateEndpoint''ServiceTag' (required) |

### PrivateEndpointDestination

| Name | Description | Value |
| --- | --- | --- |
| serviceResourceId | A type definition that refers the id to an Azure Resource Manager resource. | string |
| sparkEnabled |  | bool |
| sparkStatus | Type of a managed network Outbound Rule of a machine learning workspace. | 'Active''Deleting''Failed''Inactive''Provisioning' |
| subresourceTarget |  | string |

### PrivateEndpointOutboundRule

| Name | Description | Value |
| --- | --- | --- |
| destination | Private Endpoint destination for a Private Endpoint Outbound Rule for the managed network of a machine learning workspace. | PrivateEndpointDestination |
| fqdns |  | string[] |
| type | Type of a managed network Outbound Rule of a machine learning workspace. | 'PrivateEndpoint' (required) |

### ServerlessComputeSettings

| Name | Description | Value |
| --- | --- | --- |
| serverlessComputeCustomSubnet | The resource ID of an existing virtual network subnet in which serverless compute nodes should be deployed | string |
| serverlessComputeNoPublicIP | The flag to signal if serverless compute nodes deployed in custom vNet would have no public IP addresses for a workspace with private endpoint | bool |

### ServiceManagedResourcesSettings

| Name | Description | Value |
| --- | --- | --- |
| cosmosDb |  | CosmosDbSettings |

### ServiceTagDestination

| Name | Description | Value |
| --- | --- | --- |
| action | The action enum for networking rule. | 'Allow''Deny' |
| addressPrefixes | Optional, if provided, the ServiceTag property will be ignored. | string[] |
| portRanges |  | string |
| protocol |  | string |
| serviceTag |  | string |

### ServiceTagOutboundRule

| Name | Description | Value |
| --- | --- | --- |
| destination | Service Tag destination for a Service Tag Outbound Rule for the managed network of a machine learning workspace. | ServiceTagDestination |
| type | Type of a managed network Outbound Rule of a machine learning workspace. | 'ServiceTag' (required) |

### SharedPrivateLinkResource

| Name | Description | Value |
| --- | --- | --- |
| name | Unique name of the private link | string |
| properties | Properties of a shared private link resource. | SharedPrivateLinkResourceProperty |

### SharedPrivateLinkResourceProperty

| Name | Description | Value |
| --- | --- | --- |
| groupId | group id of the private link | string |
| privateLinkResourceId | the resource id that private link links to | string |
| requestMessage | Request message | string |
| status | Connection status of the service consumer with the service provider\r\nPossible state transitions\r\nPending -&gt; Approved (Service provider approves the connection request)\r\nPending -&gt; Rejected (Service provider rejects the connection request)\r\nPending -&gt; Disconnected (Service provider deletes the connection)\r\nApproved -&gt; Rejected (Service provider rejects the approved connection)\r\nApproved -&gt; Disconnected (Service provider deletes the connection)\r\nRejected -&gt; Pending (Service consumer re-initiates the connection request that was rejected)\r\nRejected -&gt; Disconnected (Service provider deletes the connection) | 'Approved''Disconnected''Pending''Rejected''Timeout' |

### Sku

| Name | Description | Value |
| --- | --- | --- |
| capacity | If the SKU supports scale out/in then the capacity integer should be included. If scale out/in is not possible for the resource this may be omitted. | int |
| family | If the service has different generations of hardware, for the same SKU, then that can be captured here. | string |
| name | The name of the SKU. Ex - P3. It is typically a letter+number code | string (required) |
| size | The SKU size. When the name field is the combination of tier and some other value, this would be the standalone code. | string |
| tier | This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT. | 'Basic''Free''Premium''Standard' |

### UserAssignedIdentities

| Name | Description | Value |
| --- | --- | --- |

### UserAssignedIdentity

| Name | Description | Value |
| --- | --- | --- |

### WorkspaceHubConfig

| Name | Description | Value |
| --- | --- | --- |
| additionalWorkspaceStorageAccounts |  | string[] |
| defaultWorkspaceResourceGroup |  | string |

### WorkspaceProperties

| Name | Description | Value |
| --- | --- | --- |
| allowPublicAccessWhenBehindVnet | The flag to indicate whether to allow public access when behind VNet. | bool |
| applicationInsights | ARM id of the application insights associated with this workspace. | string |
| associatedWorkspaces |  | string[] |
| containerRegistry | ARM id of the container registry associated with this workspace. | string |
| description | The description of this workspace. | string |
| discoveryUrl | Url for the discovery service to identify regional endpoints for machine learning experimentation services | string |
| enableDataIsolation |  | bool |
| enableServiceSideCMKEncryption |  | bool |
| encryption |  | EncryptionProperty |
| featureStoreSettings | Settings for feature store type workspace. | FeatureStoreSettings |
| friendlyName | The friendly name for this workspace. This name in mutable | string |
| hbiWorkspace | The flag to signal HBI data in the workspace and reduce diagnostic data collected by the service | bool |
| hubResourceId |  | string |
| imageBuildCompute | The compute name for image build | string |
| keyVault | ARM id of the key vault associated with this workspace. This cannot be changed once the workspace has been created | string |
| managedNetwork | Managed Network settings for a machine learning workspace. | ManagedNetworkSettings |
| primaryUserAssignedIdentity | The user assigned identity resource id that represents the workspace identity. | string |
| provisionNetworkNow | Set to trigger the provisioning of the managed VNet with the default Options when creating a Workspace with the managed VNet enabled, or else it does nothing. | bool |
| publicNetworkAccess | Whether requests from Public Network are allowed. | 'Disabled''Enabled' |
| serverlessComputeSettings | Settings for serverless compute in a workspace | ServerlessComputeSettings |
| serviceManagedResourcesSettings | The service managed resource settings. | ServiceManagedResourcesSettings |
| sharedPrivateLinkResources | The list of shared private link resources in this workspace. | SharedPrivateLinkResource[] |
| storageAccount | ARM id of the storage account associated with this workspace. This cannot be changed once the workspace has been created | string |
| systemDatastoresAuthMode | The auth mode used for accessing the system datastores of the workspace. | 'AccessKey''Identity''UserDelegationSAS' |
| v1LegacyMode | Enabling v1\_legacy\_mode may prevent you from using features provided by the v2 API. | bool |
| workspaceHubConfig | WorkspaceHub's configuration object. | WorkspaceHubConfig |

### WorkspaceTags

| Name | Description | Value |
| --- | --- | --- |

::: zone-end

::: zone pivot="deployment-language-terraform"

## Terraform (AzAPI provider) resource definition

The workspaces resource type can be deployed with operations that target:

- **Resource groups** For a list of changed properties in each API version, see [change log](change-log/workspaces).

## Usage Examples

### Terraform Samples

A basic example of deploying Azure Machine Learning Workspace.

```terraform
terraform {
  required_providers {
    azapi = {
      source = "Azure/azapi"
    }
    azurerm = {
      source = "hashicorp/azurerm"
    }
  }
}

provider "azurerm" {
  features {
  }
}

provider "azapi" {
  skip_provider_registration = false
}

variable "resource_name" {
  type    = string
  default = "acctest0001"
}

variable "location" {
  type    = string
  default = "westeurope"
}

data "azurerm_client_config" "current" {
}

resource "azapi_resource" "resourceGroup" {
  type     = "Microsoft.Resources/resourceGroups@2020-06-01"
  name     = var.resource_name
  location = var.location
  body = {
    tags = {
      stage = "test"
    }
  }
  schema_validation_enabled = false
  response_export_values    = ["*"]
}

resource "azapi_resource" "storageAccount" {
  type      = "Microsoft.Storage/storageAccounts@2021-09-01"
  parent_id = azapi_resource.resourceGroup.id
  name      = var.resource_name
  location  = var.location
  body = {
    kind = "StorageV2"
    properties = {
      accessTier                   = "Hot"
      allowBlobPublicAccess        = true
      allowCrossTenantReplication  = true
      allowSharedKeyAccess         = true
      defaultToOAuthAuthentication = false
      encryption = {
        keySource = "Microsoft.Storage"
        services = {
          queue = {
            keyType = "Service"
          }
          table = {
            keyType = "Service"
          }
        }
      }
      isHnsEnabled      = false
      isNfsV3Enabled    = false
      isSftpEnabled     = false
      minimumTlsVersion = "TLS1_2"
      networkAcls = {
        defaultAction = "Allow"
      }
      publicNetworkAccess      = "Enabled"
      supportsHttpsTrafficOnly = true
    }
    sku = {
      name = "Standard_LRS"
    }
  }
  schema_validation_enabled = false
  response_export_values    = ["*"]
}

resource "azapi_resource" "component" {
  type      = "Microsoft.Insights/components@2020-02-02"
  parent_id = azapi_resource.resourceGroup.id
  name      = var.resource_name
  location  = var.location
  body = {
    kind = "web"
    properties = {
      Application_Type                = "web"
      DisableIpMasking                = false
      DisableLocalAuth                = false
      ForceCustomerStorageForProfiler = false
      RetentionInDays                 = 90
      SamplingPercentage              = 100
      publicNetworkAccessForIngestion = "Enabled"
      publicNetworkAccessForQuery     = "Enabled"
    }
  }
  schema_validation_enabled = false
  response_export_values    = ["*"]
}

resource "azapi_resource" "vault" {
  type      = "Microsoft.KeyVault/vaults@2021-10-01"
  parent_id = azapi_resource.resourceGroup.id
  name      = var.resource_name
  location  = var.location
  body = {
    properties = {
      accessPolicies = [
        {
          objectId = "45a2d1ea-488a-44b0-bb2e-3cd8e485ebef"
          permissions = {
            certificates = [
              "all",
            ]
            keys = [
              "all",
            ]
            secrets = [
              "all",
            ]
            storage = []
          }
          tenantId = data.azurerm_client_config.current.tenant_id
        }
      ]
      createMode                   = "default"
      enablePurgeProtection        = true
      enableRbacAuthorization      = false
      enableSoftDelete             = true
      enabledForDeployment         = false
      enabledForDiskEncryption     = false
      enabledForTemplateDeployment = false
      publicNetworkAccess          = "Enabled"
      sku = {
        family = "A"
        name   = "standard"
      }
      tenantId = data.azurerm_client_config.current.tenant_id
    }
  }
  schema_validation_enabled = false
  response_export_values    = ["*"]
}

resource "azapi_resource" "workspace" {
  type      = "Microsoft.MachineLearningServices/workspaces@2022-05-01"
  parent_id = azapi_resource.resourceGroup.id
  name      = var.resource_name
  location  = var.location
  identity {
    type         = "SystemAssigned"
    identity_ids = []
  }
  body = {
    properties = {
      applicationInsights = azapi_resource.component.id
      keyVault            = azapi_resource.vault.id
      publicNetworkAccess = "Disabled"
      storageAccount      = azapi_resource.storageAccount.id
      v1LegacyMode        = false
    }
    sku = {
      name = "Basic"
      tier = "Basic"
    }
  }
  ignore_casing             = true
  schema_validation_enabled = false
  response_export_values    = ["*"]
}
```

### Azure Verified Modules

The following [Azure Verified Modules](https://aka.ms/avm) can be used to deploy this resource type.

| Module | Description |
| --- | --- |
| [Machine Learning Services Workspace](https://github.com/Azure/terraform-azurerm-avm-res-machinelearningservices-workspace) | AVM Resource Module for Machine Learning Services Workspace |

## Resource format

To create a Microsoft.MachineLearningServices/workspaces resource, add the following Terraform to your template.

```terraform
resource "azapi_resource" "symbolicname" {
  type = "Microsoft.MachineLearningServices/workspaces@2026-09-01"
  name = "string"
  parent_id = "string"
  identity {
    type = "string"
    identity_ids = [
      "string"
    ]
  }
  location = "string"
  tags = {
    {customized property} = "string"
  }
  body = {
    kind = "string"
    properties = {
      allowPublicAccessWhenBehindVnet = bool
      applicationInsights = "string"
      associatedWorkspaces = [
        "string"
      ]
      containerRegistry = "string"
      description = "string"
      discoveryUrl = "string"
      enableDataIsolation = bool
      enableServiceSideCMKEncryption = bool
      encryption = {
        cosmosDbResourceId = "string"
        identity = {
          userAssignedIdentity = "string"
        }
        keyVaultProperties = {
          identityClientId = "string"
          keyIdentifier = "string"
          keyVaultArmId = "string"
        }
        searchAccountResourceId = "string"
        status = "string"
        storageAccountResourceId = "string"
      }
      featureStoreSettings = {
        computeRuntime = {
          sparkRuntimeVersion = "string"
        }
        offlineStoreConnectionName = "string"
        onlineStoreConnectionName = "string"
      }
      friendlyName = "string"
      hbiWorkspace = bool
      hubResourceId = "string"
      imageBuildCompute = "string"
      keyVault = "string"
      managedNetwork = {
        enableNetworkMonitor = bool
        firewallSku = "string"
        isolationMode = "string"
        managedNetworkKind = "string"
        outboundRules = {
          {customized property} = {
            category = "string"
            status = "string"
            type = "string"
            // For remaining properties, see OutboundRule objects
          }
        }
        status = {
          sparkReady = bool
          status = "string"
        }
      }
      primaryUserAssignedIdentity = "string"
      provisionNetworkNow = bool
      publicNetworkAccess = "string"
      serverlessComputeSettings = {
        serverlessComputeCustomSubnet = "string"
        serverlessComputeNoPublicIP = bool
      }
      serviceManagedResourcesSettings = {
        cosmosDb = {
          collectionsThroughput = int
        }
      }
      sharedPrivateLinkResources = [
        {
          name = "string"
          properties = {
            groupId = "string"
            privateLinkResourceId = "string"
            requestMessage = "string"
            status = "string"
          }
        }
      ]
      storageAccount = "string"
      systemDatastoresAuthMode = "string"
      v1LegacyMode = bool
      workspaceHubConfig = {
        additionalWorkspaceStorageAccounts = [
          "string"
        ]
        defaultWorkspaceResourceGroup = "string"
      }
    }
    sku = {
      capacity = int
      family = "string"
      name = "string"
      size = "string"
      tier = "string"
    }
  }
}
```

### OutboundRule objects

Set the **type** property to specify the type of object.

For **FQDN**, use:

```terraform
{
  destination = "string"
  type = "FQDN"
}
```

For **PrivateEndpoint**, use:

```terraform
{
  destination = {
    serviceResourceId = "string"
    sparkEnabled = bool
    sparkStatus = "string"
    subresourceTarget = "string"
  }
  fqdns = [
    "string"
  ]
  type = "PrivateEndpoint"
}
```

For **ServiceTag**, use:

```terraform
{
  destination = {
    action = "string"
    addressPrefixes = [
      "string"
    ]
    portRanges = "string"
    protocol = "string"
    serviceTag = "string"
  }
  type = "ServiceTag"
}
```

## Property Values

### Microsoft.MachineLearningServices/workspaces

| Name | Description | Value |
| --- | --- | --- |
| identity | The managed service identities assigned to this resource. | ManagedServiceIdentity |
| kind |  | string |
| location |  | string |
| name | The resource name | string Constraints:Pattern = `^[a-zA-Z0-9][a-zA-Z0-9_-]{2,32}$` (required) |
| properties | Additional attributes of the entity. | WorkspaceProperties (required) |
| sku | Optional. This field is required to be implemented by the RP because AML is supporting more than one tier | Sku |
| tags | Resource tags | Dictionary of tag names and values. |
| type | The resource type | "Microsoft.MachineLearningServices/workspaces@2026-09-01" |

### ComputeRuntimeDto

| Name | Description | Value |
| --- | --- | --- |
| sparkRuntimeVersion |  | string |

### CosmosDbSettings

| Name | Description | Value |
| --- | --- | --- |
| collectionsThroughput |  | int |

### EncryptionProperty

| Name | Description | Value |
| --- | --- | --- |
| cosmosDbResourceId | The byok cosmosdb account that customer brings to store customer's datawith encryption | string |
| identity | Identity to be used with the keyVault | IdentityForCmk |
| keyVaultProperties | KeyVault details to do the encryption | KeyVaultProperties (required) |
| searchAccountResourceId | The byok search account that customer brings to store customer's datawith encryption | string |
| status | Indicates whether or not the encryption is enabled for the workspace. | 'Disabled''Enabled' (required) |
| storageAccountResourceId | The byok storage account that customer brings to store customer's datawith encryption | string |

### FeatureStoreSettings

| Name | Description | Value |
| --- | --- | --- |
| computeRuntime |  | ComputeRuntimeDto |
| offlineStoreConnectionName |  | string |
| onlineStoreConnectionName |  | string |

### FqdnOutboundRule

| Name | Description | Value |
| --- | --- | --- |
| destination |  | string |
| type | Type of a managed network Outbound Rule of a machine learning workspace. | 'FQDN' (required) |

### IdentityForCmk

| Name | Description | Value |
| --- | --- | --- |
| userAssignedIdentity | UserAssignedIdentity to be used to fetch the encryption key from keyVault | string |

### KeyVaultProperties

| Name | Description | Value |
| --- | --- | --- |
| identityClientId | Currently, we support only SystemAssigned MSI.We need this when we support UserAssignedIdentities | string |
| keyIdentifier | KeyVault key identifier to encrypt the data | string Constraints:Min length = 1Pattern = `[a-zA-Z0-9_]` (required) |
| keyVaultArmId | KeyVault Arm Id that contains the data encryption key | string Constraints:Min length = 1Pattern = `[a-zA-Z0-9_]` (required) |

### ManagedNetworkProvisionStatus

| Name | Description | Value |
| --- | --- | --- |
| sparkReady |  | bool |
| status | Status for the managed network of a machine learning workspace. | 'Active''Inactive' |

### ManagedNetworkSettings

| Name | Description | Value |
| --- | --- | --- |
| enableNetworkMonitor | A flag to indicate if monitoring needs to be enabled for the managed network. | bool |
| firewallSku | Firewall Sku used for FQDN Rules | 'Basic''Standard' |
| isolationMode | Isolation mode for the managed network of a machine learning workspace. | 'AllowInternetOutbound''AllowOnlyApprovedOutbound''Disabled' |
| managedNetworkKind | The Kind of the managed network. Users can switch from V1 to V2 for granular access controls, but cannot switch back to V1 once V2 is enabled. | 'V1''V2' |
| outboundRules | Dictionary of &lt;OutboundRule&gt; | ManagedNetworkSettingsOutboundRules |
| status | Status of the Provisioning for the managed network of a machine learning workspace. | ManagedNetworkProvisionStatus |

### ManagedNetworkSettingsOutboundRules

| Name | Description | Value |
| --- | --- | --- |

### ManagedServiceIdentity

| Name | Description | Value |
| --- | --- | --- |
| type | Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed). | 'None''SystemAssigned''SystemAssigned,UserAssigned''UserAssigned' (required) |
| userAssignedIdentities | The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests. | UserAssignedIdentities |

### OutboundRule

| Name | Description | Value |
| --- | --- | --- |
| category | Category of a managed network Outbound Rule of a machine learning workspace. | 'Dependency''Recommended''Required''UserDefined' |
| status | Type of a managed network Outbound Rule of a machine learning workspace. | 'Active''Deleting''Failed''Inactive''Provisioning' |
| type | Set to 'FQDN' for type FqdnOutboundRule. Set to 'PrivateEndpoint' for type PrivateEndpointOutboundRule. Set to 'ServiceTag' for type ServiceTagOutboundRule. | 'FQDN''PrivateEndpoint''ServiceTag' (required) |

### PrivateEndpointDestination

| Name | Description | Value |
| --- | --- | --- |
| serviceResourceId | A type definition that refers the id to an Azure Resource Manager resource. | string |
| sparkEnabled |  | bool |
| sparkStatus | Type of a managed network Outbound Rule of a machine learning workspace. | 'Active''Deleting''Failed''Inactive''Provisioning' |
| subresourceTarget |  | string |

### PrivateEndpointOutboundRule

| Name | Description | Value |
| --- | --- | --- |
| destination | Private Endpoint destination for a Private Endpoint Outbound Rule for the managed network of a machine learning workspace. | PrivateEndpointDestination |
| fqdns |  | string[] |
| type | Type of a managed network Outbound Rule of a machine learning workspace. | 'PrivateEndpoint' (required) |

### ServerlessComputeSettings

| Name | Description | Value |
| --- | --- | --- |
| serverlessComputeCustomSubnet | The resource ID of an existing virtual network subnet in which serverless compute nodes should be deployed | string |
| serverlessComputeNoPublicIP | The flag to signal if serverless compute nodes deployed in custom vNet would have no public IP addresses for a workspace with private endpoint | bool |

### ServiceManagedResourcesSettings

| Name | Description | Value |
| --- | --- | --- |
| cosmosDb |  | CosmosDbSettings |

### ServiceTagDestination

| Name | Description | Value |
| --- | --- | --- |
| action | The action enum for networking rule. | 'Allow''Deny' |
| addressPrefixes | Optional, if provided, the ServiceTag property will be ignored. | string[] |
| portRanges |  | string |
| protocol |  | string |
| serviceTag |  | string |

### ServiceTagOutboundRule

| Name | Description | Value |
| --- | --- | --- |
| destination | Service Tag destination for a Service Tag Outbound Rule for the managed network of a machine learning workspace. | ServiceTagDestination |
| type | Type of a managed network Outbound Rule of a machine learning workspace. | 'ServiceTag' (required) |

### SharedPrivateLinkResource

| Name | Description | Value |
| --- | --- | --- |
| name | Unique name of the private link | string |
| properties | Properties of a shared private link resource. | SharedPrivateLinkResourceProperty |

### SharedPrivateLinkResourceProperty

| Name | Description | Value |
| --- | --- | --- |
| groupId | group id of the private link | string |
| privateLinkResourceId | the resource id that private link links to | string |
| requestMessage | Request message | string |
| status | Connection status of the service consumer with the service provider\r\nPossible state transitions\r\nPending -&gt; Approved (Service provider approves the connection request)\r\nPending -&gt; Rejected (Service provider rejects the connection request)\r\nPending -&gt; Disconnected (Service provider deletes the connection)\r\nApproved -&gt; Rejected (Service provider rejects the approved connection)\r\nApproved -&gt; Disconnected (Service provider deletes the connection)\r\nRejected -&gt; Pending (Service consumer re-initiates the connection request that was rejected)\r\nRejected -&gt; Disconnected (Service provider deletes the connection) | 'Approved''Disconnected''Pending''Rejected''Timeout' |

### Sku

| Name | Description | Value |
| --- | --- | --- |
| capacity | If the SKU supports scale out/in then the capacity integer should be included. If scale out/in is not possible for the resource this may be omitted. | int |
| family | If the service has different generations of hardware, for the same SKU, then that can be captured here. | string |
| name | The name of the SKU. Ex - P3. It is typically a letter+number code | string (required) |
| size | The SKU size. When the name field is the combination of tier and some other value, this would be the standalone code. | string |
| tier | This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT. | 'Basic''Free''Premium''Standard' |

### UserAssignedIdentities

| Name | Description | Value |
| --- | --- | --- |

### UserAssignedIdentity

| Name | Description | Value |
| --- | --- | --- |

### WorkspaceHubConfig

| Name | Description | Value |
| --- | --- | --- |
| additionalWorkspaceStorageAccounts |  | string[] |
| defaultWorkspaceResourceGroup |  | string |

### WorkspaceProperties

| Name | Description | Value |
| --- | --- | --- |
| allowPublicAccessWhenBehindVnet | The flag to indicate whether to allow public access when behind VNet. | bool |
| applicationInsights | ARM id of the application insights associated with this workspace. | string |
| associatedWorkspaces |  | string[] |
| containerRegistry | ARM id of the container registry associated with this workspace. | string |
| description | The description of this workspace. | string |
| discoveryUrl | Url for the discovery service to identify regional endpoints for machine learning experimentation services | string |
| enableDataIsolation |  | bool |
| enableServiceSideCMKEncryption |  | bool |
| encryption |  | EncryptionProperty |
| featureStoreSettings | Settings for feature store type workspace. | FeatureStoreSettings |
| friendlyName | The friendly name for this workspace. This name in mutable | string |
| hbiWorkspace | The flag to signal HBI data in the workspace and reduce diagnostic data collected by the service | bool |
| hubResourceId |  | string |
| imageBuildCompute | The compute name for image build | string |
| keyVault | ARM id of the key vault associated with this workspace. This cannot be changed once the workspace has been created | string |
| managedNetwork | Managed Network settings for a machine learning workspace. | ManagedNetworkSettings |
| primaryUserAssignedIdentity | The user assigned identity resource id that represents the workspace identity. | string |
| provisionNetworkNow | Set to trigger the provisioning of the managed VNet with the default Options when creating a Workspace with the managed VNet enabled, or else it does nothing. | bool |
| publicNetworkAccess | Whether requests from Public Network are allowed. | 'Disabled''Enabled' |
| serverlessComputeSettings | Settings for serverless compute in a workspace | ServerlessComputeSettings |
| serviceManagedResourcesSettings | The service managed resource settings. | ServiceManagedResourcesSettings |
| sharedPrivateLinkResources | The list of shared private link resources in this workspace. | SharedPrivateLinkResource[] |
| storageAccount | ARM id of the storage account associated with this workspace. This cannot be changed once the workspace has been created | string |
| systemDatastoresAuthMode | The auth mode used for accessing the system datastores of the workspace. | 'AccessKey''Identity''UserDelegationSAS' |
| v1LegacyMode | Enabling v1\_legacy\_mode may prevent you from using features provided by the v2 API. | bool |
| workspaceHubConfig | WorkspaceHub's configuration object. | WorkspaceHubConfig |

### WorkspaceTags

| Name | Description | Value |
| --- | --- | --- |

::: zone-end
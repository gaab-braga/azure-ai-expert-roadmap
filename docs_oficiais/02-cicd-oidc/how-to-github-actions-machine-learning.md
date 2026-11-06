# Use GitHub Actions with Azure Machine Learning

**APPLIES TO:**![](media/yes.png?view=azureml-api-2)[Azure CLI ml extension v2 (current)](how-to-configure-cli?view=azureml-api-2)![](media/yes.png?view=azureml-api-2)[Python SDK azure-ai-ml v2 (current)](https://aka.ms/sdk-v2-install)

Get started with [GitHub Actions](https://docs.github.com/en/actions) to train a model on Azure Machine Learning.

This article teaches you how to create a GitHub Actions workflow that builds and deploys a machine learning model to [Azure Machine Learning](overview-what-is-azure-machine-learning?view=azureml-api-2). You train a [scikit-learn](https://scikit-learn.org/) linear regression model on the NYC Taxi dataset.

GitHub Actions use a workflow YAML (.yml) file in the `/.github/workflows/` path in your repository. This definition contains the various steps and parameters that make up the workflow.

## Prerequisites

- An Azure Machine Learning workspace. For steps for creating a workspace, see [Create the workspace](quickstart-create-resources?view=azureml-api-2#create-the-workspace).
- The Azure Machine Learning SDK for Python v2. To install the SDK, use the following command:

    ```bash
    pip install azure-ai-ml azure-identity
    ```

    To update an existing installation of the SDK to the latest version, use the following command:

    ```bash
    pip install --upgrade azure-ai-ml azure-identity
    ```

    For more information, see [Azure Machine Learning Package client library for Python](/en-us/python/api/overview/azure/ai-ml-readme).

- A GitHub account. If you don't have one, [create a free account](https://github.com/join).

## Step 1: Get the code

Fork the following repo at GitHub:

```
https://github.com/azure/azureml-examples
```

Clone your forked repo locally.

```
git clone https://github.com/YOUR-USERNAME/azureml-examples
```

## Step 2: Authenticate with Azure

First, define how to authenticate with Azure. The recommended, more secure option is to [sign in by using OpenID Connect with a Microsoft Entra application or a user-assigned managed identity](/en-us/azure/developer/github/connect-from-azure-openid-connect). If necessary, you can also use [sign in by using a service principal and secret](/en-us/azure/developer/github/connect-from-azure-secret). This approach is less secure and not recommended.

### Generate deployment credentials

# [OpenID Connect](#tab/openid)
To use [Azure Login action](https://github.com/marketplace/actions/azure-login) with OIDC, you need to configure a federated identity credential on a Microsoft Entra application or a user-assigned managed identity.

**Option 1: Microsoft Entra application**

- Create a Microsoft Entra application with a service principal by [Azure portal](/en-us/entra/identity-platform/howto-create-service-principal-portal#register-an-application-with-microsoft-entra-id-and-create-a-service-principal), [Azure CLI](/en-us/cli/azure/azure-cli-sp-tutorial-1#create-a-service-principal), or [Azure PowerShell](/en-us/powershell/azure/create-azure-service-principal-azureps#create-a-service-principal).
- Copy the values for **Client ID**, **Subscription ID**, and **Directory (tenant) ID** to use later in your GitHub Actions workflow.
- Assign an appropriate role to your service principal by [Azure portal](/en-us/entra/identity-platform/howto-create-service-principal-portal#assign-a-role-to-the-application), [Azure CLI](/en-us/cli/azure/azure-cli-sp-tutorial-5#create-or-remove-a-role-assignment), or [Azure PowerShell](/en-us/powershell/azure/create-azure-service-principal-azureps#manage-service-principal-roles).
- [Configure a federated identity credential on a Microsoft Entra application](/en-us/entra/workload-id/workload-identity-federation-create-trust) to trust tokens issued by GitHub Actions to your GitHub repository.

**Option 2: User-assigned managed identity**

- [Create a user-assigned managed identity](/en-us/entra/identity/managed-identities-azure-resources/how-manage-user-assigned-managed-identities#create-a-user-assigned-managed-identity).
- Copy the values for **Client ID**, **Subscription ID**, and **Directory (tenant) ID** to use later in your GitHub Actions workflow.
- [Assign an appropriate role to your user-assigned managed identity](/en-us/entra/identity/managed-identities-azure-resources/how-manage-user-assigned-managed-identities#manage-access-to-user-assigned-managed-identities).
- [Configure a federated identity credential on a user-assigned managed identity](/en-us/entra/workload-id/workload-identity-federation-create-trust-user-assigned-managed-identity) to trust tokens issued by GitHub Actions to your GitHub repository.

# [Service principal](#tab/userlevel)
- Create a Microsoft Entra application with a service principal by [Azure portal](/en-us/entra/identity-platform/howto-create-service-principal-portal#register-an-application-with-microsoft-entra-id-and-create-a-service-principal), [Azure CLI](/en-us/cli/azure/azure-cli-sp-tutorial-1#create-a-service-principal), or [Azure PowerShell](/en-us/powershell/azure/create-azure-service-principal-azureps#create-a-service-principal).
- Create a client secret for your service principal by [Azure portal](/en-us/entra/identity-platform/howto-create-service-principal-portal#option-3-create-a-new-client-secret), [Azure CLI](/en-us/cli/azure/azure-cli-sp-tutorial-2?branch=main#create-a-service-principal-containing-a-password), or [Azure PowerShell](/en-us/powershell/azure/create-azure-service-principal-azureps?#password-based-authentication).
- Copy the values for **Client ID**, **Client Secret**, **Subscription ID**, and **Directory (tenant) ID** to use later in your GitHub Actions workflow.
- Assign an appropriate role to your service principal by [Azure portal](/en-us/entra/identity-platform/howto-create-service-principal-portal#assign-a-role-to-the-application), [Azure CLI](/en-us/cli/azure/azure-cli-sp-tutorial-5#create-or-remove-a-role-assignment), or [Azure PowerShell](/en-us/powershell/azure/create-azure-service-principal-azureps#manage-service-principal-roles).

---

### Create secrets

# [OpenID Connect](#tab/openid)
You need to provide your application's **Client ID**, **Directory (tenant) ID**, and **Subscription ID** to the login action. These values can either be provided directly in the workflow or can be stored in GitHub secrets and referenced in your workflow. Saving the values as GitHub secrets is the more secure option.

1. In [GitHub](https://github.com/), go to your repository.
2. Select **Security &gt; Secrets and variables &gt; Actions**.

    ![Screenshot of adding a secret](../reusable-content/media/github-select-actions.png?view=azureml-api-2)
3. Select **New repository secret**.

    Note

    To enhance workflow security in public repositories, use [environment secrets](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment#environment-secrets) instead of repository secrets. If the environment requires approval, a job cannot access environment secrets until one of the required reviewers approves it.
4. Create secrets for `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, and `AZURE_SUBSCRIPTION_ID`. Copy these values from your Microsoft Entra application or user-assigned managed identity for your GitHub secrets:

    | GitHub secret | Microsoft Entra application or user-assigned managed identity |
    | --- | --- |
    | AZURE\_CLIENT\_ID | Client ID |
    | AZURE\_SUBSCRIPTION\_ID | Subscription ID |
    | AZURE\_TENANT\_ID | Directory (tenant) ID |

    Note

    For security reasons, we recommend using GitHub Secrets rather than passing values directly to the workflow.

# [Service principal](#tab/userlevel)
1. In [GitHub](https://github.com/), go to your repository.
2. Go to **Settings** in the navigation menu.
3. Select **Security &gt; Secrets and variables &gt; Actions**.

    ![Screenshot of adding a secret](../reusable-content/media/github-select-actions.png?view=azureml-api-2)
4. Select **New repository secret**.
5. Paste the entire JSON output from the Azure CLI command into the secret's value field. Give the secret the name `AZURE_CREDENTIALS`.
6. Select **Add secret**.

---

## Step 3: Update `setup.sh` to connect to your Azure Machine Learning workspace

Update the CLI setup file variables to match your workspace.

1. In your forked repository, go to `azureml-examples/cli/`.
2. Edit `setup.sh` and update these variables in the file.

    | Variable | Description |
    | --- | --- |
    | `GROUP` | Name of resource group |
    | `LOCATION` | Location of your workspace (example: `eastus2`) |
    | `WORKSPACE` | Name of Azure Machine Learning workspace |

## Step 4: Update `pipeline.yml` with your compute cluster name

Use a `pipeline.yml` file to deploy your Azure Machine Learning pipeline. The pipeline is a machine learning pipeline and not a DevOps pipeline. You only need to make this update if you're using a name other than `cpu-cluster` for your compute cluster name.

1. In your forked repository, go to `azureml-examples/cli/jobs/pipelines/nyc-taxi/pipeline.yml`.
2. Each time you see `compute: azureml:cpu-cluster`, update the value of `cpu-cluster` with your compute cluster name. For example, if your cluster is named `my-cluster`, your new value would be `azureml:my-cluster`. There are five updates.

## Step 5: Run your GitHub Actions workflow

Your workflow authenticates with Azure, sets up the Azure Machine Learning CLI, and uses the CLI to train a model in Azure Machine Learning.

# [OpenID Connect](#tab/openid)
Your workflow file is made up of a trigger section and jobs:

- A trigger starts the workflow in the `on` section. The workflow runs by default on a cron schedule and when a pull request is made from matching branches and paths. Learn more about [events that trigger workflows](https://docs.github.com/actions/using-workflows/events-that-trigger-workflows).
- In the jobs section of the workflow, you check out code and sign in to Azure with the Azure login action using OpenID Connect.
- The jobs section also includes a setup action that installs and sets up the [Machine Learning CLI (v2)](how-to-configure-cli?view=azureml-api-2). Once the CLI is installed, the run job action runs your Azure Machine Learning `pipeline.yml` file to train a model with NYC taxi data.

### Enable your workflow

1. In your forked repository, open `.github/workflows/cli-jobs-pipelines-nyc-taxi-pipeline.yml` and verify that your workflow looks similar to this.

    Note

    The workflow file in the repo may include additional steps (such as bootstrapping and validation) not shown here. The following example shows the core steps.

    ```yaml
    name: cli-jobs-pipelines-nyc-taxi-pipeline
    on:
      workflow_dispatch:
      schedule:
        - cron: "0 0/4 * * *"
      pull_request:
        branches:
          - main
        paths:
          - cli/jobs/pipelines/nyc-taxi/**
          - .github/workflows/cli-jobs-pipelines-nyc-taxi-pipeline.yml
          - cli/run-pipeline-jobs.sh
          - cli/setup.sh
    permissions:
      id-token: write
    jobs:
      build:
        runs-on: ubuntu-latest
        steps:
        - name: check out repo
          uses: actions/checkout@v4
        - name: azure login
          uses: azure/login@v2
          with:
              client-id: ${{ secrets.AZURE_CLIENT_ID }}
              tenant-id: ${{ secrets.AZURE_TENANT_ID }}
              subscription-id: ${{ secrets.AZURE_SUBSCRIPTION_ID }}
        - name: setup
          run: bash setup.sh
          working-directory: cli
          continue-on-error: true
        - name: run job
          run: bash -x ../../../run-job.sh pipeline.yml
          working-directory: cli/jobs/pipelines/nyc-taxi
    ```
2. Select **View runs**.
3. Enable workflows by selecting **I understand my workflows, go ahead and enable them**.
4. Select the **cli-jobs-pipelines-nyc-taxi-pipeline workflow** and choose to **Enable workflow**.

    ![Screenshot of enable GitHub Actions workflow.](media/how-to-github-actions-machine-learning/enable-github-actions-ml-workflow.png?view=azureml-api-2)
5. Select **Run workflow** and choose the option to **Run workflow** now.

    ![Screenshot of run GitHub Actions workflow.](media/how-to-github-actions-machine-learning/github-actions-run-workflow.png?view=azureml-api-2)

# [Service principal](#tab/userlevel)
Your workflow file is made up of a trigger section and jobs:

- A trigger starts the workflow in the `on` section. The workflow runs by default on a cron schedule and when a pull request is made from matching branches and paths. Learn more about [events that trigger workflows](https://docs.github.com/actions/using-workflows/events-that-trigger-workflows).
- In the jobs section of the workflow, you check out code and sign in to Azure with your service principal secret.
- The jobs section also includes a setup action that installs and sets up the [Machine Learning CLI (v2)](how-to-configure-cli?view=azureml-api-2). Once the CLI is installed, the run job action runs your Azure Machine Learning `pipeline.yml` file to train a model with NYC taxi data.

### Enable your workflow

1. In your forked repository, open `.github/workflows/cli-jobs-pipelines-nyc-taxi-pipeline.yml` and verify that your workflow looks similar to this.

    Note

    The workflow file in the repo may include additional steps not shown here. The following example shows the core steps.

    ```yaml
    name: cli-jobs-pipelines-nyc-taxi-pipeline
    on:
      workflow_dispatch:
      schedule:
        - cron: "0 0/4 * * *"
      pull_request:
        branches:
          - main
        paths:
          - cli/jobs/pipelines/nyc-taxi/**
          - .github/workflows/cli-jobs-pipelines-nyc-taxi-pipeline.yml
          - cli/run-pipeline-jobs.sh
          - cli/setup.sh
    jobs:
      build:
        runs-on: ubuntu-latest
        steps:
        - name: check out repo
          uses: actions/checkout@v4
        - name: azure login
          uses: azure/login@v2
          with:
            creds: ${{secrets.AZURE_CREDENTIALS}}
        - name: setup
          run: bash setup.sh
          working-directory: cli
          continue-on-error: true
        - name: run job
          run: bash -x ../../../run-job.sh pipeline.yml
          working-directory: cli/jobs/pipelines/nyc-taxi
    ```
2. Select **View runs**.
3. Enable workflows by selecting **I understand my workflows, go ahead and enable them**.
4. Select the **cli-jobs-pipelines-nyc-taxi-pipeline workflow** and choose to **Enable workflow**. ![Screenshot of enable GitHub Actions workflow.](media/how-to-github-actions-machine-learning/enable-github-actions-ml-workflow.png?view=azureml-api-2)
5. Select **Run workflow** and choose the option to **Run workflow** now. ![Screenshot of run GitHub Actions workflow.](media/how-to-github-actions-machine-learning/github-actions-run-workflow.png?view=azureml-api-2)

---

## Step 6: Verify your workflow run

1. Open your completed workflow run and verify that the build job ran successfully. You see a green checkmark next to the job.
2. Open Azure Machine Learning studio and go to **nyc-taxi-pipeline-example**. Verify that each part of your job (prep, transform, train, predict, score) completed and that you see a green checkmark.

    ![Screenshot of successful Machine Learning Studio run.](media/how-to-github-actions-machine-learning/github-actions-machine-learning-nyc-taxi-complete.png?view=azureml-api-2)

## Clean up resources

When you no longer need your resource group and repository, clean up the resources you deployed by deleting the resource group and your GitHub repository.
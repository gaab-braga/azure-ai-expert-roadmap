---
layout: Conceptual
title: 'Study guide for Exam AI-300: Operationalizing Machine Learning and Generative AI Solutions | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-300
breadcrumb_path: /breadcrumb/toc.json
feedback_system: None
uhfHeaderId: MSDocsHeader-Certifications
description: 'Study guide for Exam AI-300: Operationalizing Machine Learning and Generative AI Solutions | Microsoft Docs'
documentationcenter: NA
author: Micsullivan
ms.topic: article
ms.tgt_pltfrm: NA
ms.workload: NA
ms.date: 2026-02-18T00:00:00.0000000Z
ms.author: msulliv
ms.service: learn
locale: en-us
document_id: 4e7c2cc7-a7b2-d33c-d731-7931f3ce4029
document_version_independent_id: 4e7c2cc7-a7b2-d33c-d731-7931f3ce4029
updated_at: 2026-10-15T23:49:00.0000000Z
original_content_git_url: https://github.com/MicrosoftDocs/learn-certs-pr/blob/live/learn-certs-pr/certifications/resources/study-guides/ai-300.md
gitcommit: https://github.com/MicrosoftDocs/learn-certs-pr/blob/3ef953ce3dc226404276adda39f75159a4cf2983/learn-certs-pr/certifications/resources/study-guides/ai-300.md
git_commit_id: 3ef953ce3dc226404276adda39f75159a4cf2983
site_name: Docs
depot_name: MSDN.learn-certs-pr
page_type: conceptual
toc_rel: ../../../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
word_count: 1243
asset_id: certifications/resources/study-guides/ai-300
moniker_range_name: 
monikers: []
item_type: Content
source_path: learn-certs-pr/certifications/resources/study-guides/ai-300.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d6f38669-3d05-40f2-afd8-e49f7dd20884
- https://authoring-docs-microsoft.poolparty.biz/devrel/a3955c7b-f5ee-420d-aff5-d7119738f38b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/55265cca-de9b-48dc-a77a-9047cc39a575
- https://authoring-docs-microsoft.poolparty.biz/devrel/b31948f4-2f38-404b-ac93-c3c8c5b3ae33
platformId: 6fa0e5b6-a7f3-9a86-1127-deb6454fcb3a
---

# Study guide for Exam AI-300: Operationalizing Machine Learning and Generative AI Solutions | Microsoft Learn

Tip

The Practice Assessment is available on AI Skills Navigator, with a new upgraded experience. Please navigate to [AI Skills Navigator | Microsoft Certified: Machine Learning Operations Engineer Associate](https://aiskillsnavigator.microsoft.com/credentials/cert-6e7fcf9954d1620318e5d199346ace3b7bd84edc8be79e735bcdc09ada8437bf) certification page to take the practice assessment.

NOTE: You must be signed in to AI Skills Navigator to be able to launch the Practice Assessment.

## Purpose of this document

This study guide should help you understand what to expect on the exam and includes a summary of the topics the exam might cover and links to additional resources. The information and materials in this document should help you focus your studies as you prepare for the exam.

| Useful links | Description |
| --- | --- |
| [How to earn the certification](/en-us/credentials/certifications/operationalizing-machine-learning-and-generative-ai-solutions/) | Some certifications only require passing one exam, while others require passing multiple exams. |
| [Certification renewal](/en-us/credentials/certifications/renew-your-microsoft-certification) | Microsoft associate, expert, and specialty certifications expire annually. You can renew by passing a **free** online assessment on Microsoft Learn. |
| [Your Microsoft Learn profile](/en-us/users/) | Connecting your certification profile to Microsoft Learn allows you to schedule and renew exams and share and print certificates. |
| [Exam scoring and score reports](/en-us/credentials/certifications/exam-scoring-reports) | A score of 700 or greater is required to pass. |
| [Exam sandbox](https://aka.ms/examdemo) | You can explore the exam environment by visiting our exam sandbox. |
| [Request accommodations](/en-us/credentials/certifications/request-accommodations) | If you use assistive devices, require extra time, or need modification to any part of the exam experience, you can request an accommodation. |

## About the exam

Some exams are localized into other languages, and those are updated approximately eight weeks after the English version is updated. If the exam isn't available in your preferred language, you can request an additional 30 minutes to complete the exam.

#### Note

The bullets that follow each of the skills measured are intended to illustrate how we are assessing that skill. Related topics may be covered in the exam.

#### Note

Most questions cover features that are general availability (GA). The exam may contain questions on Preview features if those features are commonly used.

## Skills measured

### Audience profile

As a candidate for this Microsoft Certification, you should have subject matter expertise in setting up infrastructure for machine learning operations (MLOps) and generative AI operations (GenAIOps) solutions on Azure, together referred to as *AI operations* (AIOps). You need experience training, optimizing, deploying, and maintaining traditional machine learning models by using Azure Machine Learning, in addition to experience deploying, evaluating, monitoring, and optimizing generative AI applications and agents by using Microsoft Foundry.

You should have a data science background with experience in Python programming and an entry-level understanding of DevOps practices, including using tools like GitHub Actions and working with command-line interfaces (CLIs).

Additionally, you need knowledge and experience in MLOps by using:

- Machine Learning.
- Foundry.
- GitHub Actions.
- Infrastructure as code (IaC) practices with Bicep and Azure CLI.

Your responsibilities for this role include:

- Designing and implementing MLOps infrastructure.
- Implementing machine learning model lifecycle and operations.
- Designing and implementing GenAIOps infrastructure.
- Implementing generative AI quality assurance and observability.
- Optimizing generative AI systems and model performance.

You work with data scientists, DevOps teams, and stakeholders to deliver scalable AI solutions with comprehensive automation and monitoring.

### Skills at a glance

- Design and implement an MLOps infrastructure (15–20%)
- Implement machine learning model lifecycle and operations (25–30%)
- Design and implement a GenAIOps infrastructure (20–25%)
- Implement generative AI quality assurance and observability (10–15%)
- Optimize generative AI systems and model performance (10–15%)

### Design and implement an MLOps infrastructure (15–20%)

#### Create and manage resources in a Machine Learning workspace

- Create and manage a workspace
- Create and manage datastores
- Create and manage compute targets
- Configure identity and access management for workspaces

#### Create and manage assets in a Machine Learning workspace

- Create and manage data assets
- Create and manage environments
- Create and manage components
- Share assets across workspaces by using registries

#### Implement IaC for Machine Learning

- Configure GitHub integration with Machine Learning to enable secure access
- Deploy Machine Learning workspaces and resources by using Bicep and Azure CLI
- Automate resource provisioning by using GitHub Actions workflows
- Restrict network access to Machine Learning workspaces
- Manage source control for machine learning projects by using Git

### Implement machine learning model lifecycle and operations (25–30%)

#### Orchestrate model training

- Configure experiment tracking with MLflow
- Use automated machine learning to explore optimal models
- Use notebooks for experimentation and exploration
- Automate hyperparameter tuning
- Run model training scripts
- Manage distributed training for large and deep learning models
- Implement training pipelines
- Compare model performance across jobs

#### Implement model registration and versioning

- Package a feature retrieval specification with the model artifact
- Register an MLflow model
- Evaluate a model by using responsible AI principles
- Manage model lifecycle, including archiving models

#### Deploy machine learning models for production environments

- Deploy models as real-time or batch endpoints with managed inference options
- Test and troubleshoot model endpoints
- Implement progressive rollout and safe rollback strategies

#### Monitor and maintain machine learning models in production

- Detect and analyze data drift
- Monitor performance metrics of models deployed to production
- Configure retraining or alert triggers when thresholds are exceeded

### Design and implement a GenAIOps infrastructure (20–25%)

#### Implement Foundry environments and platform configuration

- Create and configure Foundry resources and project environments
- Configure identity and access management with managed identities and role-based access control (RBAC)
- Implement network security and private networking configurations
- Deploy infrastructure using Bicep templates and Azure CLI

#### Deploy and manage foundation models for production workloads

- Deploy foundation models by using serverless API endpoints and managed compute options
- Select appropriate models for specific use cases
- Implement model versioning and production deployment strategies
- Configure provisioned throughput units for high-volume workloads

#### Implement prompt versioning and management with source control

- Design and develop prompts
- Create prompt variants and compare performance across different prompts
- Implement version control for prompts by using Git repositories

### Implement generative AI quality assurance and observability (10–15%)

#### Configure evaluation and validation for generative AI applications and agents

- Create test datasets and data mapping for comprehensive model evaluation
- Implement AI quality metrics, including groundedness, relevance, coherence, and fluency
- Configure risk and safety evaluations for harmful content detection
- Set up automated evaluation workflows by using built-in and custom evaluation metrics

#### Implement observability for generative AI applications and agents

- Examine continuous monitoring in Foundry
- Monitor performance metrics, including latency, throughput, and response times
- Track and optimize cost metrics, including token consumption and resource usage
- Configure detailed logging, tracing, and debugging capabilities for production troubleshooting

### Optimize generative AI systems and model performance (10–15%)

#### Optimize retrieval-augmented generation (RAG) performance and accuracy

- Optimize retrieval performance by tuning similarity thresholds, chunk sizes, and retrieval strategies
- Select and fine-tune embedding models for domain-specific use cases and accuracy improvements
- Implement and optimize hybrid search approaches combining semantic and keyword-based retrieval
- Evaluate and improve RAG system performance by using relevance metrics and A/B testing frameworks

#### Implement advanced fine-tuning and model customization

- Design and implement advanced fine-tuning methods
- Create and manage synthetic data for fine-tuning
- Monitor and optimize fine-tuned model performance
- Manage a fine-tuned model from development through production deployment

## Study resources

We recommend that you train and get hands-on experience before you take the exam. We offer self-study options and classroom training as well as links to documentation, community sites, and videos.

| Study resources | Links to learning and documentation |
| --- | --- |
| Get trained | [Choose from self-paced learning paths and modules or take an instructor-led course](/en-us/credentials/certifications/exams/AI-300#two-ways-to-prepare) |
| Find documentation | [Artificial Intelligence overview](/en-us/compliance/assurance/assurance-artificial-intelligence#what-is-copilot-and-how-does-it-work)[Generative AI documentation](/en-us/ai/playbook/technology-guidance/generative-ai/#enterprise-generative-ai-application)[Microsoft 365 Copilot documentation](/en-us/office365/servicedescriptions/office-365-platform-service-description/microsoft-365-copilot)[Microsoft 365 documentation](/en-us/microsoft-365/) |
| Ask a question | [Microsoft Q&A | Microsoft Docs](/en-us/answers/products/) |
| Get community support | [Microsoft 365 Copilot community hub](https://techcommunity.microsoft.com/category/microsoft365copilot)[Microsoft 365 community hub](https://techcommunity.microsoft.com/category/microsoft365) |
| Follow Microsoft Learn | [Microsoft Learn - Microsoft Tech Community](https://techcommunity.microsoft.com/t5/microsoft-learn/ct-p/MicrosoftLearn) |
| Find a video | [Exam Readiness Zone](/en-us/shows/exam-readiness-zone/)[Browse other Microsoft Learn shows](/en-us/shows/browse) |
---
description: Deploy Azure Bicep templates with proper validation, monitoring, and rollback capabilities
mode: 'agent'  
tools: ['codebase', 'terminal', 'azureCli', 'azureBicepSchemas']
---

# Bicep Template Deployment

Your goal is to deploy Azure Bicep templates safely with proper validation, monitoring, and rollback capabilities.

## Pre-Deployment Validation

### 1. **Template Validation**
- [ ] Bicep linting passes without errors
- [ ] Template compiles to valid ARM JSON
- [ ] Parameter files validated against schema
- [ ] What-if deployment shows expected changes

### 2. **Environment Readiness**
- [ ] Target subscription and resource group exist
- [ ] Required permissions validated
- [ ] Dependencies available and accessible
- [ ] Naming conflicts checked

### 3. **Safety Measures**
- [ ] Backup of existing resources (if applicable)
- [ ] Rollback plan documented
- [ ] Deployment notifications configured
- [ ] Impact assessment completed

## Deployment Process

### 1. **Staged Deployment**
```bash
# 1. Validate template
az deployment group validate \
  --resource-group $RESOURCE_GROUP \
  --template-file main.bicep \
  --parameters @parameters.json

# 2. Preview changes
az deployment group what-if \
  --resource-group $RESOURCE_GROUP \
  --template-file main.bicep \
  --parameters @parameters.json

# 3. Deploy with monitoring
az deployment group create \
  --resource-group $RESOURCE_GROUP \
  --template-file main.bicep \
  --parameters @parameters.json \
  --confirm-with-what-if
```

### 2. **Deployment Monitoring**
- Monitor deployment progress in real-time
- Watch for error conditions and warnings
- Validate resource health post-deployment
- Verify connectivity and functionality

### 3. **Post-Deployment Validation**
- [ ] All resources created successfully
- [ ] Configuration matches template specifications
- [ ] Health checks passing
- [ ] Monitoring and alerting active

## Rollback Procedures

In case of deployment issues:
1. **Immediate Actions**: Stop deployment, assess impact
2. **Rollback Options**: Previous template version, manual fixes
3. **Communication**: Notify stakeholders of issues and resolution
4. **Post-Mortem**: Document lessons learned

Always provide detailed deployment logs and validation results.

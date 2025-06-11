---
description: Review Azure Bicep templates for best practices, security, and compliance
mode: 'agent'
tools: ['codebase', 'search', 'azureBicepSchemas', 'azureCli']
---

# Bicep Template Review

Your goal is to perform a comprehensive review of Azure Bicep templates to ensure they follow best practices, security guidelines, and compliance requirements.

## Review Criteria

### 1. **Code Quality**
- [ ] Proper parameter naming and descriptions
- [ ] Appropriate use of variables and functions
- [ ] Consistent resource naming conventions
- [ ] Proper module organization and structure

### 2. **Security Best Practices**
- [ ] Managed identities used instead of service principals
- [ ] Secrets stored in Key Vault, not hardcoded
- [ ] Network security groups properly configured
- [ ] RBAC assignments follow least privilege
- [ ] Storage accounts use private endpoints

### 3. **Reliability & Resilience**
- [ ] Availability zones configured where applicable
- [ ] Backup and disaster recovery considered
- [ ] Health checks and monitoring implemented
- [ ] Proper dependency management

### 4. **Performance & Cost**
- [ ] Appropriate SKU selections
- [ ] Auto-scaling configured correctly
- [ ] Reserved capacity considered for predictable workloads
- [ ] Cost optimization recommendations

### 5. **Compliance & Governance**
- [ ] Required tags applied consistently
- [ ] Policy compliance validated
- [ ] Resource naming follows conventions
- [ ] Documentation and comments adequate

## Review Process

1. **Static Analysis**: Check syntax, structure, and patterns
2. **Security Scan**: Identify security vulnerabilities
3. **Best Practice Validation**: Compare against Azure Well-Architected Framework
4. **Cost Analysis**: Estimate and optimize costs

## Review Report

Provide detailed findings with:
- **Critical Issues**: Security vulnerabilities requiring immediate attention
- **Recommendations**: Specific improvements with code examples
- **Compliance Status**: Adherence to organizational policies
- **Optimization Opportunities**: Performance and cost improvements

Always include specific code snippets showing before/after improvements.

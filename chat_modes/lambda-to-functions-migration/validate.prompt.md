---
description: Validate migrated Azure Functions to ensure they match original Lambda function behavior
mode: 'agent'
tools: ['codebase', 'search', 'terminal', 'azureCli']
---

# Lambda to Functions Migration Validation

Your goal is to validate that migrated Azure Functions maintain the same behavior as the original AWS Lambda functions.

## Validation Checklist

### 1. **Functional Validation**
- [ ] Input/output behavior matches exactly
- [ ] Error handling preserves original behavior
- [ ] Response formats are identical
- [ ] Logging maintains same information level

### 2. **Performance Validation**
- [ ] Execution time within acceptable range
- [ ] Memory usage optimized for Azure Functions
- [ ] Cold start times meet requirements
- [ ] Scaling behavior validated under load

### 3. **Integration Validation**
- [ ] All external service integrations working
- [ ] Authentication mechanisms properly migrated
- [ ] Event triggers functioning correctly
- [ ] Environment variables properly configured

### 4. **Security Validation**
- [ ] Managed identity replacing IAM roles correctly
- [ ] Secrets properly stored in Key Vault
- [ ] Network security rules applied
- [ ] Compliance requirements met

## Testing Approach

1. **Unit Tests**: Migrate and adapt existing Lambda unit tests
2. **Integration Tests**: Test with real Azure services
3. **Load Tests**: Validate performance under expected load
4. **Security Tests**: Verify security posture improvements

## Validation Report

Generate a comprehensive validation report with:
- **Test Results**: Pass/fail status for each validation criteria
- **Performance Comparison**: Before/after metrics
- **Issue Log**: Any discrepancies found and resolutions
- **Recommendations**: Post-migration optimization suggestions

Always provide specific test cases and verification scripts.

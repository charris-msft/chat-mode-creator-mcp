---
description: Evaluate AWS Lambda functions for Azure Functions migration readiness and provide detailed assessment
mode: 'agent'
tools: ['codebase', 'search', 'githubRepo', 'terminal']
---

# Lambda Migration Evaluation

Your goal is to evaluate AWS Lambda functions for migration to Azure Functions and provide a comprehensive assessment.

## Evaluation Criteria

### 1. **Runtime Compatibility**
- Assess current Lambda runtime vs Azure Functions support
- Identify any runtime-specific dependencies
- Check for custom runtimes or layers

### 2. **Code Analysis**
- Review function code for AWS-specific services
- Identify hardcoded AWS resource references
- Assess third-party dependencies compatibility

### 3. **Triggers and Events**
- Map Lambda triggers to Azure Functions equivalents
- Identify unsupported trigger types
- Assess event payload differences

### 4. **Infrastructure Dependencies**
- Review VPC configurations
- Assess IAM roles and permissions
- Check environment variables and secrets

### 5. **Performance Characteristics**
- Evaluate memory and timeout requirements
- Assess cold start implications
- Review scaling patterns

## Assessment Output

Provide a structured report including:
- **Migration Complexity**: Low/Medium/High with rationale
- **Required Changes**: Detailed list of code modifications needed
- **Azure Equivalents**: Mapping of AWS services to Azure services
- **Risk Assessment**: Potential challenges and mitigation strategies
- **Effort Estimation**: Time and resource requirements

Always include specific code examples and actionable recommendations.

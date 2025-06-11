---
description: Validate specifications for completeness, consistency, and readiness for code generation
mode: 'agent'
tools: ['codebase', 'search', 'semanticSearch']
---

# Specification Validation

Your goal is to validate specifications (PRDs, implementation plans) for completeness and consistency before code generation begins.

## Validation Framework

### 1. **Completeness Check**
- [ ] All domain concepts clearly defined
- [ ] System invariants explicitly stated
- [ ] User stories cover all required functionality
- [ ] Acceptance scenarios in Given/When/Then format
- [ ] Technical decisions documented with rationale

### 2. **Consistency Analysis**
- [ ] Terminology used consistently throughout
- [ ] No contradictory requirements
- [ ] Technical choices align with requirements
- [ ] Dependencies properly documented
- [ ] Cross-references are accurate

### 3. **Implementation Readiness**
- [ ] Database schema matches domain concepts
- [ ] API structure supports user stories
- [ ] Business rules can be validated
- [ ] Error handling scenarios covered
- [ ] Performance requirements quantified

### 4. **Checklist Integration**
- [ ] Pre-generation checklists included
- [ ] Cross-layer alignment verified
- [ ] Security requirements addressed
- [ ] Testing strategy defined

## Validation Process

### Step 1: Automated Analysis
Run consistency checks to identify:
- Undefined terms and concepts
- Contradictory statements
- Missing technical details
- Incomplete user stories

### Step 2: Manual Review
Focus on areas requiring human judgment:
- Business logic complexity
- User experience decisions
- Technical trade-offs
- Integration patterns

### Step 3: Gap Resolution
For each identified issue:
1. **Categorize**: Critical, Important, or Nice-to-have
2. **Research**: Gather additional context if needed
3. **Decide**: Make explicit decisions for ambiguous areas
4. **Document**: Update specifications with decisions

## Validation Report

Generate comprehensive validation results:
- **Readiness Score**: 0-100% based on completeness
- **Critical Issues**: Blockers preventing code generation
- **Recommendations**: Specific improvements needed
- **Checklist Status**: Pre-generation requirements met

Always provide specific examples and actionable next steps.

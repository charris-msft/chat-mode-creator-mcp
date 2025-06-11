---
description: Generate comprehensive test suites from acceptance scenarios and specifications
mode: 'agent'
tools: ['codebase', 'search', 'findTestFiles', 'semanticSearch']
---

# Test Generation from Specifications

Your goal is to generate comprehensive test suites based on acceptance scenarios and specifications, ensuring complete coverage of requirements.

## Test Generation Strategy

### 1. **Requirements Traceability**
- Map each acceptance scenario to test cases
- Ensure every user story has corresponding tests
- Cover all system invariants with validation tests
- Test business rules and constraints

### 2. **Test Types**

#### **Unit Tests**
- Test individual domain concepts
- Validate business rule implementation
- Test data model constraints
- Cover edge cases and error conditions

#### **Integration Tests**
- Test API endpoints against user stories
- Validate database schema with business logic
- Test external service integrations
- Verify end-to-end workflows

#### **Acceptance Tests**
- Direct translation of Given/When/Then scenarios
- User journey validation
- Cross-browser/platform testing
- Performance and load testing

### 3. **Test Data Strategy**
- Generate test data matching domain concepts
- Create boundary condition test cases
- Set up realistic test scenarios
- Maintain test data consistency

## Generation Process

### Step 1: Scenario Analysis
For each acceptance scenario:
```gherkin
Given [initial state]
When [action performed]
Then [expected outcome]
```

Generate corresponding test structure:
```javascript
describe('User Story: [title]', () => {
  beforeEach(() => {
    // Set up initial state
  });
  
  it('should [expected behavior]', async () => {
    // Perform action
    // Assert expected outcome
  });
});
```

### Step 2: Coverage Analysis
- Identify uncovered requirements
- Generate additional test cases for edge cases
- Ensure error handling is tested
- Validate security requirements

### Step 3: Test Implementation
- Generate test code in appropriate framework
- Include setup and teardown procedures
- Add meaningful assertions
- Provide clear test documentation

## Quality Assurance

### Test Quality Criteria
- [ ] Tests are independent and repeatable
- [ ] Clear, descriptive test names
- [ ] Meaningful error messages
- [ ] Appropriate test data and mocking
- [ ] Performance test thresholds defined

### Coverage Validation
- [ ] All user stories covered
- [ ] Edge cases included
- [ ] Error conditions tested
- [ ] Integration points validated
- [ ] Security requirements verified

Always generate production-ready test code with proper documentation and maintenance considerations.

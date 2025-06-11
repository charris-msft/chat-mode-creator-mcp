# 🤝 Contributing to Chat Mode Creator MCP Server

Thank you for your interest in contributing to the Chat Mode Creator MCP Server! We welcome contributions from everyone. 🎉

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- Git
- VS Code (for testing chat modes)
- GitHub CLI (optional, but recommended)

### Setup Development Environment
1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/chat-mode-creator-mcp.git
   cd chat-mode-creator-mcp
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1  # Windows
   # source .venv/bin/activate    # Linux/Mac
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Test the server**:
   ```bash
   python mcp_chatmode_server.py
   ```

## 🎯 Types of Contributions

### 🐛 Bug Reports
- Use the [Bug Report template](.github/ISSUE_TEMPLATE/bug_report.yml)
- Include detailed reproduction steps
- Provide environment information
- Add relevant logs if available

### ✨ Feature Requests
- Use the [Feature Request template](.github/ISSUE_TEMPLATE/feature_request.yml)
- Describe the problem you're solving
- Explain your proposed solution
- Consider alternatives and edge cases

### 🔧 Code Contributions
- **New Chat Modes**: Add specialized development workflows
- **Custom Prompts**: Enhance existing chat modes with new prompts
- **MCP Server Improvements**: Core functionality enhancements
- **Documentation**: README, guides, examples
- **Tests**: Unit tests, integration tests, validation scripts

## 📋 Development Guidelines

### Adding New Chat Modes
1. **Create the chat mode directory**:
   ```
   chat_modes/your-new-mode/
   ├── your-new-mode.chatmode.md
   ├── prompt1.prompt.md
   └── prompt2.prompt.md
   ```

2. **Follow the template structure**:
   ```markdown
   ---
   description: Brief description of the chat mode
   tools: ['relevant', 'tools', 'list']
   ---
   
   # Your Chat Mode Name
   
   ## Purpose
   What this mode helps with...
   
   ## Usage Guidelines
   How to use this mode effectively...
   
   ## Related Prompts
   - `/prompt1` - Description
   - `/prompt2` - Description
   ```

3. **Update the server code**:
   - Add your mode to `AVAILABLE_MODES` in `mcp_chatmode_server.py`
   - Add prompt templates to `AVAILABLE_PROMPT_TEMPLATES`

4. **Create example usage**:
   - Add examples to `example_usage.py`
   - Update documentation

### Code Style
- **Python**: Follow PEP 8 style guidelines
- **Markdown**: Use consistent formatting and emoji usage
- **Comments**: Write clear, concise comments for complex logic
- **Docstrings**: Use Google-style docstrings for functions and classes

### Testing
- **Manual Testing**: Ensure the MCP server starts without errors
- **Chat Mode Testing**: Verify chat modes create correctly in VS Code
- **Prompt Testing**: Test custom prompts work as expected
- **Example Testing**: Run `example_usage.py` to verify functionality

## 🔄 Pull Request Process

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**:
   - Follow the development guidelines
   - Write tests for new functionality
   - Update documentation as needed

3. **Test your changes**:
   ```bash
   python mcp_chatmode_server.py
   python example_usage.py
   ```

4. **Commit with descriptive messages**:
   ```bash
   git commit -m "feat: Add new Azure DevOps chat mode with pipeline prompts"
   ```

5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**:
   - Use the [PR template](.github/pull_request_template.md)
   - Provide clear description of changes
   - Link related issues
   - Include screenshots if applicable

## 🎨 Chat Mode Ideas

Looking for inspiration? Here are some chat mode ideas we'd love to see:

### 🔧 Development Workflows
- **Kubernetes Development**: YAML generation, troubleshooting, best practices
- **Docker Optimization**: Multi-stage builds, security scanning, performance
- **API Design**: OpenAPI specs, REST best practices, GraphQL schemas
- **Database Migration**: Schema changes, data migration strategies

### ☁️ Cloud Platforms
- **AWS to Azure**: Service mapping, migration patterns
- **GCP to Azure**: Resource conversion, architecture translation
- **Multi-Cloud**: Cross-platform compatibility, disaster recovery

### 🏗️ Infrastructure as Code
- **Terraform**: Module development, state management, best practices
- **Pulumi**: Modern IaC patterns, type safety, testing
- **ARM Templates**: Azure-specific templating, parameter optimization

### 🧪 Testing & Quality
- **Test-Driven Development**: TDD workflows, test patterns
- **Security Testing**: SAST/DAST integration, vulnerability management
- **Performance Testing**: Load testing strategies, monitoring setup

## 📊 Project Structure

```
chat-mode-creator-mcp/
├── .github/                    # GitHub configuration
│   ├── ISSUE_TEMPLATE/         # Issue templates
│   ├── workflows/              # CI/CD workflows
│   └── pull_request_template.md
├── chat_modes/                 # Chat mode templates
│   ├── azure-bicep-development/
│   ├── lambda-to-functions-migration/
│   └── spec-driven-development/
├── mcp_chatmode_server.py      # Main MCP server
├── example_usage.py            # Usage examples
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── CONTRIBUTING.md             # This file
└── .venv/                      # Virtual environment (local)
```

## 🎯 Code Review Process

### For Reviewers
- **Functionality**: Does the code work as intended?
- **Style**: Does it follow our coding guidelines?
- **Documentation**: Are changes properly documented?
- **Testing**: Are there adequate tests?
- **Performance**: Are there any performance implications?

### For Contributors
- **Be Responsive**: Address feedback promptly and professionally
- **Ask Questions**: If feedback is unclear, ask for clarification
- **Learn and Improve**: Use feedback as a learning opportunity
- **Test Thoroughly**: Ensure your changes work in different scenarios

## 🏆 Recognition

Contributors are recognized in several ways:
- **GitHub Contributors**: Automatically listed in the repository
- **Release Notes**: Major contributions mentioned in release notes
- **Documentation**: Contributor acknowledgments in README
- **Community**: Shout-outs in discussions and social media

## 📞 Getting Help

### 💬 Discussions
- Use [GitHub Discussions](https://github.com/charris-msft/chat-mode-creator-mcp/discussions) for questions
- Search existing discussions before creating new ones
- Tag your discussions with relevant labels

### 🐛 Issues
- Check [existing issues](https://github.com/charris-msft/chat-mode-creator-mcp/issues) first
- Use appropriate issue templates
- Provide detailed information for faster resolution

### 📧 Direct Contact
- For security issues, please email the maintainers directly
- For urgent matters, mention maintainers in issues or PRs

## 📜 Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). By participating, you are expected to uphold this code.

### Key Points
- **Be Respectful**: Treat everyone with respect and kindness
- **Be Inclusive**: Welcome contributors from all backgrounds
- **Be Constructive**: Provide helpful feedback and suggestions
- **Be Professional**: Maintain professional conduct in all interactions

## 🎉 Thank You!

Thank you for contributing to the Chat Mode Creator MCP Server! Your contributions help make VS Code development workflows more efficient and enjoyable for developers worldwide. 

Every contribution, no matter how small, makes a difference. We appreciate your time and effort! 🙏

---

**Happy Contributing!** 🚀✨

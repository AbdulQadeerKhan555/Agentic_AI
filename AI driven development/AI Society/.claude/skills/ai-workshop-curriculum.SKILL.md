# AI Workshop Curriculum Design

A skill for designing comprehensive AI workshop curricula tailored to university students, with a code-first approach and portfolio-ready projects.

## Description

This skill generates complete workshop curricula for AI topics (Computer Vision, NLP, Agents, etc.) following a structured 5-step design process. It creates both curriculum documentation and starter code files, prioritizing hands-on learning and practical portfolio projects.

## Usage

When invoked, ask the user for:
1. **Target Audience**: Juniors, Seniors, or Mixed (specify year/experience level)
2. **AI Topic**: The specific AI domain (e.g., Computer Vision, NLP, Reinforcement Learning, AI Agents, Generative AI, etc.)
3. **Workshop Duration**: Total time available (e.g., 2 hours, 3 hours, full day)

Then generate the complete curriculum following the procedure below.

## Procedure

### Step 1: Define Target Audience & Topic
- Clearly identify the audience's background (programming experience, AI knowledge)
- Specify the exact AI topic and scope
- Determine appropriate complexity level

### Step 2: Outline 3 Key Learning Objectives
Create 3 concrete learning objectives that answer: "What will they build by the end?"
- Each objective should be actionable and measurable
- Focus on portfolio-ready deliverables
- Ensure objectives are achievable within the workshop timeframe

### Step 3: Create Session Timeline
Allocate time following the 40% theory / 60% hands-on split:
- **Theory (40%)**: Concepts, explanations, live demos
- **Hands-on (60%)**: Coding exercises, project building, debugging

Break down the timeline into specific segments with time allocations.

### Step 4: Generate Prerequisites & Starter Code
- List all required libraries, software, and tools
- Provide installation instructions
- Create a starter code snippet that attendees will build upon
- Include comments explaining the structure

### Step 5: Draft 3 Discussion Questions
Create engaging questions to:
- Stimulate critical thinking
- Connect theory to real-world applications
- Encourage peer interaction

## Distinctive Features

Your curriculum design MUST incorporate these elements:

### 1. Portfolio-Ready Projects
- The final deliverable should be something students can showcase
- Include guidance on how to document/present the project
- Suggest extensions or improvements for their portfolio

### 2. Code-First Teaching
- Minimize slides (max 5-10 slides for entire workshop)
- Prioritize live coding and IDE usage
- Use interactive notebooks (Jupyter/Colab) when appropriate
- Show code examples before explaining theory

### 3. Resource Fallback Plan
Include contingency plans for technical issues:
- **If internet is slow**: Pre-downloaded datasets, local model files
- **If Colab fails**: Local Jupyter setup instructions
- **If libraries fail to install**: Docker container or pre-configured environment
- **Backup activities**: Offline exercises, code review sessions, architecture discussions

## Output Format

Generate TWO deliverables:

### 1. CURRICULUM.md
A complete curriculum document with the following structure:

```markdown
# [Workshop Title]: [AI Topic] for [Audience]

## Workshop Overview
- **Duration**: [X hours]
- **Target Audience**: [Description]
- **Difficulty Level**: [Beginner/Intermediate/Advanced]

## Learning Objectives
By the end of this workshop, students will be able to:
1. [Objective 1 - what they'll build]
2. [Objective 2 - what they'll build]
3. [Objective 3 - what they'll build]

## Prerequisites
### Required Knowledge
- [List prerequisite concepts]

### Required Software & Libraries
- [Detailed installation instructions]
- [Version specifications]

### Pre-Workshop Setup
- [Step-by-step setup guide]

## Session Timeline

### Part 1: [Title] (Theory - X minutes)
- [Subtopic 1]
- [Subtopic 2]
- **Teaching Approach**: [How to teach this - live coding, demo, etc.]

### Part 2: [Title] (Hands-on - X minutes)
- [Activity description]
- **What students will code**: [Specific tasks]

[Continue for all parts, maintaining 40/60 split]

## Hands-On Project: [Project Name]

### Project Description
[What students will build - be specific]

### Implementation Steps
1. [Step 1]
2. [Step 2]
[...]

### Portfolio Enhancement Tips
- [How to showcase this project]
- [Suggested extensions]
- [Documentation guidelines]

## Discussion Questions
1. [Question 1 - connecting to real-world]
2. [Question 2 - critical thinking]
3. [Question 3 - future applications]

## Resource Fallback Plan

### Scenario 1: Internet Connectivity Issues
- [Specific fallback actions]
- [Pre-downloaded resources needed]

### Scenario 2: Colab/Cloud Platform Failure
- [Local setup instructions]
- [Alternative platforms]

### Scenario 3: Library Installation Problems
- [Docker container option]
- [Pre-configured environment]

### Scenario 4: Time Constraints
- [Shortened version of workshop]
- [Which sections to prioritize]

## Additional Resources
- [Links to documentation]
- [Further reading]
- [Practice datasets]

## Instructor Notes
- [Common pitfalls to watch for]
- [Timing tips]
- [Engagement strategies]
```

### 2. Starter Code File(s)
Create appropriately named starter code file(s) based on the topic:
- For Python workshops: `workshop_starter.py` or `workshop_starter.ipynb`
- Include comprehensive comments
- Provide TODO sections for students to complete
- Include example outputs/expected results

The starter code should:
- Be immediately runnable (with proper setup)
- Have clear structure and organization
- Include helpful comments explaining each section
- Have designated areas for students to add their code
- Include basic error handling examples

## Guidelines

1. **Be Specific**: Avoid generic advice. Provide exact library versions, specific datasets, concrete code examples.

2. **Time Management**: Ensure the timeline is realistic. Include buffer time for questions and debugging.

3. **Accessibility**: Consider students with different learning speeds. Provide "stretch goals" for fast learners and "minimum viable" checkpoints for others.

4. **Real-World Relevance**: Connect every concept to practical applications or industry use cases.

5. **Engagement**: Design interactive moments throughout - polls, pair programming, live debugging sessions.

6. **Documentation**: Teach students to document their code as they build (comments, README, etc.).

## Example Invocation

User: "Create a workshop curriculum for Computer Vision - Image Classification for Junior students"

You should:
1. Ask for workshop duration if not specified
2. Generate complete CURRICULUM.md with all sections
3. Create starter code file (e.g., `image_classification_starter.ipynb`)
4. Ensure 40/60 theory/hands-on split
5. Include portfolio-ready project (e.g., "Custom Image Classifier Web App")
6. Provide resource fallback plans
7. Use code-first approach throughout

## Notes

- Always prioritize practical, hands-on learning over theoretical depth
- The goal is for students to leave with a working project they can show employers
- Assume students have basic Python knowledge but may be new to AI/ML
- Include diversity in examples and datasets when possible
- Consider computational constraints (not everyone has GPUs)

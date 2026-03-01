#!/bin/bash

# Template Generator for Notes
# Generates blank note templates following Bloom's Taxonomy structure

set -e

# Color codes for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Default values
NOTES_DIR="/home/abdul-qadeer-khan/Documents/study_system/notes"
DATE=$(date +%Y-%m-%d)
DATE_FILE=$(date +%Y%m%d)

# Function to display usage
usage() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Generate a blank note template following Bloom's Taxonomy structure"
    echo ""
    echo "Options:"
    echo "  -t, --topic TOPIC       Topic title (required)"
    echo "  -s, --subject SUBJECT   Subject domain (e.g., Computer Science, Biology)"
    echo "  -o, --output FILE       Output file path (default: notes/topic-name-YYYYMMDD.md)"
    echo "  -h, --help              Display this help message"
    echo ""
    echo "Examples:"
    echo "  $0 -t \"Binary Search\" -s \"Computer Science\""
    echo "  $0 --topic \"Photosynthesis\" --subject \"Biology\" --output custom-notes.md"
    exit 1
}

# Function to convert topic to kebab-case
to_kebab_case() {
    echo "$1" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-//' | sed 's/-$//'
}

# Parse command line arguments
TOPIC=""
SUBJECT=""
OUTPUT=""

while [[ $# -gt 0 ]]; do
    case $1 in
        -t|--topic)
            TOPIC="$2"
            shift 2
            ;;
        -s|--subject)
            SUBJECT="$2"
            shift 2
            ;;
        -o|--output)
            OUTPUT="$2"
            shift 2
            ;;
        -h|--help)
            usage
            ;;
        *)
            echo "Unknown option: $1"
            usage
            ;;
    esac
done

# Validate required arguments
if [ -z "$TOPIC" ]; then
    echo -e "${YELLOW}Error: Topic is required${NC}"
    usage
fi

# Set default subject if not provided
if [ -z "$SUBJECT" ]; then
    SUBJECT="General"
fi

# Set default output path if not provided
if [ -z "$OUTPUT" ]; then
    TOPIC_KEBAB=$(to_kebab_case "$TOPIC")
    OUTPUT="${NOTES_DIR}/${TOPIC_KEBAB}-${DATE_FILE}.md"
fi

# Create notes directory if it doesn't exist
mkdir -p "$(dirname "$OUTPUT")"

# Generate the template
cat > "$OUTPUT" << 'EOF'
# {{TOPIC}}

**Subject**: {{SUBJECT}}
**Date Created**: {{DATE}}
**Taxonomy Level**: All Six Levels
**Reference Materials**: None

---

## Remember: Foundational Knowledge

### Key Terms

- **Term 1**: Definition
- **Term 2**: Definition
- **Term 3**: Definition

### Essential Facts

- Fact 1
- Fact 2
- Fact 3

### Core Concepts

[Brief explanation of fundamental concepts and principles]

---

## Understand: Conceptual Comprehension

### Concept Explanations

[Detailed explanations of how things work and why they matter]

### Comparisons

[Compare and contrast related concepts]

**Concept A vs. Concept B:**
- Similarity 1
- Difference 1
- Difference 2

### Interpretations

[What the information means in context]

---

## Apply: Practical Application

### Worked Examples

**Example 1: [Title]**

[Step-by-step demonstration]

**Example 2: [Title]**

[Step-by-step demonstration]

### Application Scenarios

[Real-world contexts where concepts apply]

### Practice Exercises

1. Exercise 1
2. Exercise 2
3. Exercise 3

---

## Analyze: Critical Examination

### Component Analysis

[Breaking down complex systems into parts]

**Components:**
1. Component 1: Description
2. Component 2: Description
3. Component 3: Description

### Patterns and Relationships

[Connections between ideas and concepts]

### Comparative Analysis

[Detailed comparisons revealing insights]

---

## Evaluate: Critical Assessment

### Strengths and Weaknesses

**Strengths:**
- Strength 1
- Strength 2
- Strength 3

**Weaknesses:**
- Weakness 1
- Weakness 2
- Weakness 3

### Justifications

[Reasoning behind conclusions and assessments]

### Critical Perspectives

[Different viewpoints and their validity]

---

## Create: Synthesis and Innovation

### Integrated Understanding

[How concepts combine into larger frameworks]

### Novel Applications

[New ways to apply knowledge]

### Original Insights

[Unique perspectives or solutions developed]

---

## Additional Resources

### Related Topics
- Topic 1
- Topic 2
- Topic 3

### Further Study
- Resource 1
- Resource 2
- Resource 3

### Practice Resources
- Practice resource 1
- Practice resource 2

---

## Review Schedule

- **Initial review**: {{REVIEW_1}}
- **First reinforcement**: {{REVIEW_2}} (1 day)
- **Second reinforcement**: {{REVIEW_3}} (3 days)
- **Third reinforcement**: {{REVIEW_4}} (7 days)
- **Fourth reinforcement**: {{REVIEW_5}} (21 days)
EOF

# Replace placeholders
sed -i "s/{{TOPIC}}/$TOPIC/g" "$OUTPUT"
sed -i "s/{{SUBJECT}}/$SUBJECT/g" "$OUTPUT"
sed -i "s/{{DATE}}/$DATE/g" "$OUTPUT"

# Calculate review dates
REVIEW_1=$(date -d "$DATE + 1 day" +%Y-%m-%d)
REVIEW_2=$(date -d "$DATE + 2 days" +%Y-%m-%d)
REVIEW_3=$(date -d "$DATE + 4 days" +%Y-%m-%d)
REVIEW_4=$(date -d "$DATE + 8 days" +%Y-%m-%d)
REVIEW_5=$(date -d "$DATE + 22 days" +%Y-%m-%d)

sed -i "s/{{REVIEW_1}}/$REVIEW_1/g" "$OUTPUT"
sed -i "s/{{REVIEW_2}}/$REVIEW_2/g" "$OUTPUT"
sed -i "s/{{REVIEW_3}}/$REVIEW_3/g" "$OUTPUT"
sed -i "s/{{REVIEW_4}}/$REVIEW_4/g" "$OUTPUT"
sed -i "s/{{REVIEW_5}}/$REVIEW_5/g" "$OUTPUT"

# Success message
echo -e "${GREEN}✓ Template generated successfully${NC}"
echo -e "${BLUE}Topic:${NC} $TOPIC"
echo -e "${BLUE}Subject:${NC} $SUBJECT"
echo -e "${BLUE}Output:${NC} $OUTPUT"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "1. Open the template file: $OUTPUT"
echo "2. Fill in content for each Bloom's Taxonomy level"
echo "3. Replace placeholder text with actual information"
echo "4. Save and review according to the schedule"

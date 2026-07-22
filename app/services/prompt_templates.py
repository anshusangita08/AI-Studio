"""
Prompt templates used across the application.
"""

# Reusable prompt template string with placeholders
PROMPT_TEMPLATE = (
    "# Prompt for {{scene_title}}\n"
    "\n"
    "## Task Description\n"
    "Generate content based on the following scene description:\n"
    "\n"
    "{{scene_content}}\n"
    "\n"
    "## Instructions\n"
    "- Follow the structure and key elements from the scene description\n"
    "- Maintain consistency with the overall story tone and style\n"
    "- Focus on the specific elements mentioned in this scene\n"
    "- Ensure the generated content aligns with the project's narrative direction\n"
    "\n"
    "## Output Format\n"
    "Provide your response in markdown format.\n"
)

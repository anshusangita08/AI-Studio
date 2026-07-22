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

# Additional reusable prompt templates for future expansion

IMAGE_PROMPT_TEMPLATE = (
    "# Image Prompt for {{scene_title}}\n"
    "\n"
    "## Description\n"
    "{{scene_content}}\n"
    "\n"
    "## Instructions\n"
    "- Generate an image that captures the key visual elements described.\n"
    "- Use a consistent style with the overall story tone.\n"
    "- Ensure clarity and detail suitable for illustration.\n"
)

NARRATION_PROMPT_TEMPLATE = (
    "# Narration Prompt for {{scene_title}}\n"
    "\n"
    "## Scene Description\n"
    "{{scene_content}}\n"
    "\n"
    "## Instructions\n"
    "- Write a short narration that conveys the mood and actions of the scene.\n"
    "- Keep the tone consistent with the story's voice.\n"
    "- Use descriptive language to bring the scene to life.\n"
)

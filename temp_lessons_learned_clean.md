Story Engine

Never bypass StoryService.

Project APIs

Always inspect existing ProjectService before adding methods.

Routes

Pages must return TemplateResponse.

Tests

Run launcher before pytest when validating manually.

Git

Merge develop to main only after milestone completion.

## Separating Story and Expanded Story

When implementing separate story functionality, create distinct files for each:

- story.md (original story)
- expanded_story.md (generated content)

This separation allows users to:
- Keep original story unchanged
- Generate new content without overwriting the original
- Edit generated content freely

Use different form handlers for saving each type of content.
"""Mock story generator for expanding user stories without overwriting originals."""

def generate_mock_story(original_story: str) -> str:
    """
    Generate an expanded version of a story based on original content.
    
    Args:
        original_story (str): The original user-written story
        
    Returns:
        str: An expanded version that builds upon the original story
    """
    # Simple mock expansion - in real implementation this would use LLM or other logic
    if not original_story.strip():
        return "This is an expanded version of your story.\n\nIt provides more detail and context."
    
    # Create a simple expansion based on the content
    lines = original_story.split('\n')
    expanded_lines = []
    
    for line in lines:
        if line.strip():
            expanded_lines.append(f"Expanded: {line}")
        else:
            expanded_lines.append(line)
            
    expanded_content = '\n'.join(expanded_lines)
    
    # Add some additional context
    additional_context = f"\n\nThis expanded story builds upon the original:\n{original_story}\n\n"
    return expanded_content + additional_context
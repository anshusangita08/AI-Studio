"""
PromptTemplateEngine – a lightweight, pure‑Python template renderer.
"""

from __future__ import annotations

import re
from typing import Dict


class PromptTemplateEngine:
    """
    Render simple templates containing placeholders of the form {{placeholder}}.

    The engine does **not** read files, cache templates, or use any external libraries.
    It simply performs a single pass replacement using regular expressions.
    """

    _PLACEHOLDER_RE = re.compile(r"\{\{([^}]+)\}\}")

    def render(self, template: str, context: Dict[str, str]) -> str:
        """
        Render the given template string with values from *context*.

        Unknown placeholders are left unchanged.  Empty or missing values
        result in an empty string being inserted.

        Args:
            template (str): The template text containing {{placeholders}}.
            context (Dict[str, str]): Mapping of placeholder names to values.

        Returns:
            str: The rendered template.
        """

        def _replace(match: re.Match) -> str:
            # Strip whitespace around the key
            key = match.group(1).strip()
            if key in context:
                return str(context[key])
            # Unknown placeholder – keep original text
            return match.group(0)

        return self._PLACEHOLDER_RE.sub(_replace, template)

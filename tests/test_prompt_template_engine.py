import pytest

from app.services.prompt_template_engine import PromptTemplateEngine


@pytest.fixture
def engine() -> PromptTemplateEngine:
    return PromptTemplateEngine()


def test_single_placeholder(engine):
    tmpl = "Story\n\n{{story}}\n"
    ctx = {"story": "A hero arrives."}
    assert engine.render(tmpl, ctx) == "Story\n\nA hero arrives.\n"


def test_multiple_placeholders(engine):
    tmpl = "Scene\n\n{{scene_description}}\n"
    ctx = {"scene_description": "Walking through the forest."}
    assert (
        engine.render(tmpl, ctx)
        == "Scene\n\nWalking through the forest.\n"
    )


def test_repeated_placeholder(engine):
    tmpl = "{{greeting}}, {{name}}! {{greeting}} again."
    ctx = {"greeting": "Hi", "name": "Alice"}
    assert engine.render(tmpl, ctx) == "Hi, Alice! Hi again."


def test_unknown_placeholder(engine):
    tmpl = "Unknown: {{camera}}"
    ctx = {}
    # Unknown placeholder should remain unchanged
    assert engine.render(tmpl, ctx) == "Unknown: {{camera}}"


def test_empty_value(engine):
    tmpl = "Empty: {{empty}}."
    ctx = {"empty": ""}
    assert engine.render(tmpl, ctx) == "Empty: ."


def test_empty_template(engine):
    tmpl = ""
    ctx = {"any": "value"}
    assert engine.render(tmpl, ctx) == ""


def test_no_placeholders(engine):
    tmpl = "Just plain text."
    ctx = {}
    assert engine.render(tmpl, ctx) == "Just plain text."


def test_whitespace_inside_placeholder(engine):
    tmpl = "{{   story   }}"
    ctx = {"story": "A hero arrives."}
    assert engine.render(tmpl, ctx) == "A hero arrives."

from llm_dataclass import parse_response


def test_parse_response():
    xml = """<root>
    <child>Content</child>
    </root>"""
    result = parse_response(xml, "root")
    expected = {"root": {"child": "Content"}}
    assert result == expected


def test_parse_response_in_text():
    xml = """
    This is your document:
    <root>
    <child>Content</child>
    </root>

    Let me know if you need anything else.
    """
    result = parse_response(xml, "root")
    expected = {"root": {"child": "Content"}}
    assert result == expected


def test_parse_response_with_attributes():
    xml = """<root attr="value">
    <child attr="value">Content</child>
    </root>"""
    result = parse_response(xml, "root")
    expected = {
        "root": {"@attr": "value", "child": {"@attr": "value", "#text": "Content"}}
    }
    assert result == expected

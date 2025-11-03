from llm_dataclass import find_document
import re
import pytest

def test_find_document():

    xml = """<root>
    <child>Content</child>
    </root>"""
    result = find_document(xml, "root")
    re_expected = re.compile(r"<root[^>]*>.*?</root>", re.DOTALL)
    assert re_expected.fullmatch(result)

def test_find_document_in_text():

    xml = """
    This is your document:
    <root>
    <child>Content</child>
    </root>
    
    Let me know if you need anything else.
    """
    result = find_document(xml, "root")
    re_expected = re.compile(r"<root[^>]*>.*?</root>", re.DOTALL)
    assert re_expected.fullmatch(result)

def test_find_document_not_found():

    xml = """<root>
    <child>Content</child>
    </root>"""
    try:
        find_document(xml, "nonexistent")
    except ValueError as e:
        assert str(e) == "Tag <nonexistent> not found in the provided XML."
    else:
        assert False, "Expected ValueError was not raised."

def test_find_document_with_attributes():

    xml = """<root attr="value">
    <child>Content</child>
    </root>"""
    result = find_document(xml, "root")
    re_expected = re.compile(r'<root[^>]*>.*?</root>', re.DOTALL)
    assert re_expected.fullmatch(result)

def test_find_document_multiple_tags():

    xml = """<root>
    <child>Content</child>
    </root>
    <root>
    <child>Another Content</child>
    </root>"""
    with pytest.raises(ValueError) as excinfo:
        find_document(xml, "root")
    assert str(excinfo.value) == "Multiple <root> tags found in the provided XML."
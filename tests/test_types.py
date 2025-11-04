from dataclasses import dataclass


def test_str_load() -> None:
    import llm_dataclass

    @dataclass
    class StrWrapper:
        value: str

    schema = llm_dataclass.Schema(StrWrapper, root="str")

    xml_input = "<str><value>Hello, World!</value></str>"

    result = schema.loads(xml_input)
    assert result == StrWrapper(value="Hello, World!")

def test_str_dump() -> None:
    import llm_dataclass

    @dataclass
    class StrWrapper:
        value: str

    schema = llm_dataclass.Schema(StrWrapper, root="str")

    str_instance = StrWrapper(value="Hello, World!")
    xml_output = schema.dumps(str_instance)

    expected_xml = "<str>\n  <value>Hello, World!</value>\n</str>"
    assert xml_output == expected_xml

def test_int_load() -> None:
    import llm_dataclass

    @dataclass
    class IntWrapper:
        value: int

    schema = llm_dataclass.Schema(IntWrapper, root="int")

    xml_input = "<int><value>42</value></int>"

    result = schema.loads(xml_input)
    assert result == IntWrapper(value=42)

def test_int_dump() -> None:
    import llm_dataclass

    @dataclass
    class IntWrapper:
        value: int

    schema = llm_dataclass.Schema(IntWrapper, root="int")

    int_instance = IntWrapper(value=42)
    xml_output = schema.dumps(int_instance)

    expected_xml = "<int>\n  <value>42</value>\n</int>"
    assert xml_output == expected_xml

def test_float_load() -> None:
    import llm_dataclass

    @dataclass
    class FloatWrapper:
        value: float

    schema = llm_dataclass.Schema(FloatWrapper, root="float")

    xml_input = "<float><value>3.14</value></float>"

    result = schema.loads(xml_input)
    assert result == FloatWrapper(value=3.14)

def test_float_dump() -> None:
    import llm_dataclass

    @dataclass
    class FloatWrapper:
        value: float

    schema = llm_dataclass.Schema(FloatWrapper, root="float")

    float_instance = FloatWrapper(value=3.14)
    xml_output = schema.dumps(float_instance)

    expected_xml = "<float>\n  <value>3.14</value>\n</float>"
    assert xml_output == expected_xml

def test_bool_load() -> None:
    import llm_dataclass

    @dataclass
    class BoolWrapper:
        value: bool

    schema = llm_dataclass.Schema(BoolWrapper, root="bool")

    xml_input = "<bool><value>true</value></bool>"

    result = schema.loads(xml_input)
    assert result == BoolWrapper(value=True)

def test_bool_dump() -> None:
    import llm_dataclass

    @dataclass
    class BoolWrapper:
        value: bool

    schema = llm_dataclass.Schema(BoolWrapper, root="bool")

    bool_instance = BoolWrapper(value=True)
    xml_output = schema.dumps(bool_instance)

    expected_xml = "<bool>\n  <value>true</value>\n</bool>"
    assert xml_output == expected_xml

def test_load_bool_variants() -> None:
    import llm_dataclass

    @dataclass
    class BoolWrapper:
        value: bool

    schema = llm_dataclass.Schema(BoolWrapper, root="bool")

    true_variants = ["true", "True", "TRUE", "yes", "Yes", "YES", "on", "On", "ON", "1"]
    false_variants = ["false", "False", "FALSE", "no", "No", "NO", "off", "Off", "OFF", "0"]

    for variant in true_variants:
        xml_input = f"<bool><value>{variant}</value></bool>"
        result = schema.loads(xml_input)
        assert result == BoolWrapper(value=True), f"Failed for true variant: {variant}"

    for variant in false_variants:
        xml_input = f"<bool><value>{variant}</value></bool>"
        result = schema.loads(xml_input)
        assert result == BoolWrapper(value=False), f"Failed for false variant: {variant}"

def test_dataclass_simple_loads():

    from dataclasses import dataclass
    import llm_dataclass

    @dataclass
    class Person:
        name: str
        age: int

    schema = llm_dataclass.Schema(Person)

    xml_input = """<Person>
  <name>John Doe</name>
  <age>30</age>
</Person>"""

    person_instance = schema.loads(xml_input)
    assert person_instance == Person(name="John Doe", age=30)

def test_dataclass_array_loads():

    from dataclasses import dataclass, field
    import llm_dataclass

    @dataclass
    class Person:
        name: str
        pets: list[str] = field(default_factory=list, metadata={"xml": {"name": "pet"}})

    schema = llm_dataclass.Schema(Person)

    xml_input = """<Person>
  <name>Jane Doe</name>
  <pet>Fluffy</pet>
  <pet>Spot</pet>
</Person>"""

    person_instance = schema.loads(xml_input)
    assert person_instance == Person(name="Jane Doe", pets=["Fluffy", "Spot"])

def test_dataclass_nested_loads():

    from dataclasses import dataclass
    import llm_dataclass

    @dataclass
    class Address:
        street: str
        city: str

    @dataclass
    class Person:
        name: str
        age: int
        address: Address

    schema = llm_dataclass.Schema(Person)

    xml_input = """<Person>
  <name>John Doe</name>
  <age>30</age>
  <address>
    <street>123 Main St</street>
    <city>Anytown</city>
  </address>
</Person>"""

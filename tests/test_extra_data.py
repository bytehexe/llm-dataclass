from dataclasses import dataclass

import llm_dataclass


def test_extra_data_handling():
    @dataclass
    class Person:
        name: str
        age: int

    schema = llm_dataclass.Schema(Person, root="person")

    xml_input = """<person>
  <name>John Doe</name>
  <age>30</age>
  <nickname>Johnny</nickname>
  <hobby>Hiking</hobby>
</person>"""
    person = schema.loads(xml_input)
    assert person == Person(name="John Doe", age=30)

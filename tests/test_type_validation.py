#!/usr/bin/env python3

import dataclasses
import pytest
import sys
from typing import List, Optional

from llm_dataclass import Schema

# Test cases for forbidden type constructions

@dataclasses.dataclass
class ValidSimple:
    name: str
    age: int

@dataclasses.dataclass
class ValidOptional:
    name: Optional[str]
    age: int

@dataclasses.dataclass  
class ValidList:
    names: List[str]
    age: int

@dataclasses.dataclass
class InvalidOptionalList:
    # This should be forbidden: Optional[List[T]]
    names: Optional[List[str]]

@dataclasses.dataclass
class InvalidListOptional:
    # This should be forbidden: List[Optional[T]]
    names: List[Optional[str]]

@dataclasses.dataclass
class InvalidNestedList:
    # This should be forbidden: List[List[T]]
    matrix: List[List[str]]

def test_valid_constructions():
    """Test that valid type constructions work."""
    print("Testing valid constructions...")
    
    # These should all work
    schema1 = Schema(ValidSimple)
    print("✓ ValidSimple passed")
    
    schema2 = Schema(ValidOptional)
    print("✓ ValidOptional passed")
    
    schema3 = Schema(ValidList)
    print("✓ ValidList passed")

def test_invalid_constructions():
    """Test that invalid type constructions are rejected."""
    
    # Test Optional[List[T]] - should fail
    with pytest.raises(ValueError, match="Optional\\[List\\[T\\]\\]"):
        Schema(InvalidOptionalList)
    
    # Test List[Optional[T]] - should fail
    with pytest.raises(ValueError, match="List\\[Optional\\[T\\]\\]"):
        Schema(InvalidListOptional)
    
    # Test List[List[T]] - should fail
    with pytest.raises(ValueError, match="List\\[List\\[T\\]\\]"):
        Schema(InvalidNestedList)


if __name__ == "__main__":
    test_valid_constructions()
    test_invalid_constructions()
    print("\n🎉 All tests passed!")
import pytest
import os

class TestForm:
    def test_index_exists(self):
        assert os.path.exists("index.html")
    
    def test_has_form(self):
        with open("index.html", "r", encoding="utf-8") as f:
            content = f.read()
        assert "form" in content.lower()
    
    def test_has_inputs(self):
        with open("index.html", "r", encoding="utf-8") as f:
            content = f.read()
        assert "input" in content.lower()
    
    def test_has_button(self):
        with open("index.html", "r", encoding="utf-8") as f:
            content = f.read()
        assert "button" in content.lower() or "submit" in content.lower()
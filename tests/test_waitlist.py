from src.waitlist import Waitlist

def test_join_and_to_list():
    wl = Waitlist()
    wl.join("Alice")
    wl.join("Bob")
    assert wl.to_list() == ["Alice", "Bob"]

def test_find():
    wl = Waitlist()
    wl.join("Alice")
    assert wl.find("Alice")
    assert not wl.find("Charlie")

def test_cancel():
    wl = Waitlist()
    wl.join("Alice")
    wl.join("Bob")
    assert wl.cancel("Alice")
    assert wl.to_list() == ["Bob"]
    assert not wl.cancel("Charlie")

def test_bump():
    wl = Waitlist()
    wl.join("Alice")
    wl.join("Bob")
    wl.join("Charlie")
    assert wl.bump("Charlie")
    assert wl.to_list() == ["Charlie", "Alice", "Bob"]
    assert not wl.bump("Zara")

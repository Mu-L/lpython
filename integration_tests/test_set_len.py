from lpython import i32

def test_set():
    s: set[i32]
    s = {1, 2, 22, 2, -1, 1}
    assert len(s) == 4

test_set()
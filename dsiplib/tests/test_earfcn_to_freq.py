from dsiplib import earfcn_to_freq

def test_earfcn_valid():
    # Test valid EARFCN values within known ranges
    assert earfcn_to_freq(100) == 2110.0 + 0.1 * (100 - 0)  # Band 1
    assert earfcn_to_freq(700) == 1930.0 + 0.1 * (700 - 600)  # Band 2
    assert earfcn_to_freq(39650) == 2570.0  # Band 41

def test_earfcn_nan():
    # Test for "NaN" input
    assert earfcn_to_freq("NaN") == "N/A"

def test_earfcn_out_of_range():
    # Test for EARFCN values outside the predefined ranges
    assert earfcn_to_freq(-1) == 0.0  # Below range
    assert earfcn_to_freq(999999) == 0.0  # Above range

def test_earfcn_edge_cases():
    # Test edge values
    assert earfcn_to_freq(599) == 2110.0 + 0.1 * (599 - 0)  # Upper edge of Band 1
    assert earfcn_to_freq(600) == 1930.0  # Lower edge of Band 2

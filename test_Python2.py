import Lab2.Python2 as Lab2

def test_find_min_max():
    assert Lab2.find_min_max([1, 2, 3, 4, 5]) == [1, 5]

# Test cases for calc_average()
def test_calc_average():
    assert Lab2.calc_average([2, 4, 6, 8]) == 5.0

def test_calc_median_odd():
    assert Lab2.calc_median_temperature([3, 1, 2]) == 2

def test_calc_median_even():
    assert Lab2.calc_median_temperature([4, 2, 1, 3]) == 2.5


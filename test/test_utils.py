from common.utils import is_validate_chinese_city


def test_validate_chinese_city():
    assert is_validate_chinese_city("北京市") is True


def test_not_validate_chinese_city_1():
    assert is_validate_chinese_city("北京市1") is False


def test_not_validate_chinese_city_2():
    assert is_validate_chinese_city("beijingshi") is False
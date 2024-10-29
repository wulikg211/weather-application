def is_validate_chinese_city(city):
    return all('\u4e00' <= char <= '\u9fff' for char in city) and city.endswith("市")

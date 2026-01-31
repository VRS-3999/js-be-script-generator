def _normalize_list(value):
    if not value:
        return []
    if isinstance(value, list):
        return value
    return [value]
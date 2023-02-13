def compare_version(ver_a: str, ver_b: str) -> int:

    def get_diff(diff: int) -> int:
        '''
        return number representing the result
        of version comparison
        '''
        if diff > 0:
            return 1
        elif diff < 0:
            return -1
        return 0

    [major_a, minor_a] = ver_a.split('.')
    [major_b, minor_b] = ver_b.split('.')

    major: int = get_diff(int(major_a) - int(major_b))
    minor: int = get_diff(int(minor_a) - int(minor_b))

    return major if major != 0 else minor

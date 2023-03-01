def comp_ver(ver_a: str, ver_b: str) -> int:
    a = ver_a.split(".")
    b = ver_b.split(".")

    a_len = len(a)
    b_len = len(b)

    for num in range(max(a_len, b_len)):
        num1 = 0 if num >= a_len else int(a[num])
        num2 = 0 if num >= b_len else int(b[num])

        if num1 > num2:
            return 1
        elif num1 < num2:
            return -1
    
    return 0


assert comp_ver('1', '2') == -1
assert comp_ver('2', '1') == 1
assert comp_ver('1', '1') == 0
assert comp_ver('1.0', '1') == 0
assert comp_ver('1', '1.000') == 0
assert comp_ver('12.01', '12.1') == 0
assert comp_ver('13.0.1', '13.00.02') == -1
assert comp_ver('1.1.1.1', '1.1.1.1') == 0
assert comp_ver('1.1.1.2', '1.1.1.1') == 1
assert comp_ver('1.1.3', '1.1.3.000') == 0
assert comp_ver('3.1.1.0', '3.1.2.10') == -1
assert comp_ver('1.1', '1.10') == -1
assert comp_ver("0.1", "1.1") == -1
assert comp_ver("1.0.1", "1") == 1
assert comp_ver("7.5.2.4", "7.5.3") == -1
assert comp_ver("1.01", "1.001") == 0
assert comp_ver("1.0", "1.0.0") == 0
assert comp_ver("2", "2.0.0") == 0
assert comp_ver("1.01", "1.101") == -1

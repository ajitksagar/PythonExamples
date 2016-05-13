def is_prime(num):
        if abs(num) == 0 or abs(num) == 1:
            return False
        elif abs(num) == 2:
            return True
        else:
            i = 2
            while i <= abs(num):
                if abs(num) % i == 0:
                    break
                i += 1
        return True if i == abs(num) else False

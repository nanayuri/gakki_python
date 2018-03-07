class FileObject:
    def __del__(self):
        self.close()


class C2F(float):
    def __new__(cls, arg=0.0):
        return float.__new__(cls, arg * 1.8 + 32)



class Nint(int):
    def __new__(cls, integer):
        if str(integer).find('.') == -1:
            if str(integer).isalpha():
                integer1 = 0
                for each in integer:
                    integer1 += ord(each)
                    integer = integer1

        elif str(integer).find('.') != -1:
            integer = math.floor(integer)
        return int.__new__(cls, integer)

class Nint(int):
    def __new__(cls, arg=0):
        if isinstance(arg, str):
            total = 0
            for each in arg:
                total += ord(each)
            arg = total
        return int.__new__(cls, arg)

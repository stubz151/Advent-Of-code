class CommonLogic:

    @staticmethod
    def get_input_as_int_arr():
        with open('input', 'r') as f:
            data = f.read()
        res = [int(i) for i in data.split()]
        return res

    @staticmethod
    def get_input_as_str_arr():
        with open('input', 'r') as f:
            data = f.read()
        res = [str(i) for i in data.splitlines()]
        return res

    @staticmethod
    def get_input_as_batches():
        with open('input', 'r') as f:
            data = f.read()
        concat_arr = ''
        res = []
        for x in data.split("\n"):
            if x == '':
                concat_arr = concat_arr[:len(concat_arr)-1]
                res.append(concat_arr)
                concat_arr = ''
            else:
                concat_arr += x + ' '
        return res



class Burrows:
    def __init__(self,t):
        '''
        t: input string
        index_dict: Dictionary holding indexes of the strings generated while performing cyclic rotations.
                    This will be usefull while working on substring.
                    {
                        'AWJIUFHA$': 0
                    },
                    ...
        '''
        self.template_string = str(t) + '$'
        self.index_dict = {}

    def generate_cyclic_rotations(self):
        '''
        Convert the string to list.
        Pop the last element.
        Insert the popped element to first position.
        Join the list to form a string.
        Repeat.
        '''
        result = []
        temp_str_list = list(self.template_string)
        for i in range(len(temp_str_list)-1,-1,-1):
            temp_str_list.insert(0,temp_str_list.pop())
            temp_str = ''.join(temp_str_list)
            # print(temp_str,i)
            result.append(temp_str)
            self.index_dict[temp_str] = i
        self.rotations = result

    def lexi_sorting(self):
        self.rotations.sort()
        # print(self.rotations)
        # print(self.index_dict)
        # print(self.index_dict[self.rotations[6]])

    def bwt(self):
        '''
        Performing all operations required for finding bwt.
        '''
        b.generate_cyclic_rotations()
        b.lexi_sorting()
        bwt_str = ''
        for i in range(0,len(self.rotations)):
            bwt_str = bwt_str + self.rotations[i][-1]
        self.bwt_str = bwt_str
        return bwt_str

if __name__ == '__main__':
    b = Burrows('abracadabra')
    bwt_str = b.bwt()
    print(bwt_str)



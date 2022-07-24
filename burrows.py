

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

    def find_next_alphabet(self,matrix,req_alphabet,count,j):
        current_count = 1
        req_count = 1
        index = 0
        # print(req_alphabet,'search')
        for i in range(0,j):
            if matrix[i][0] == req_alphabet:
                if current_count == count:
                    req_alphabet = matrix[i][1]
                    index = i
                    # print(req_alphabet,'found at index',index)
                    break
                else:
                    current_count += 1

        for i in range(0,index):
            # print('searching',req_alphabet)
            if matrix[i][1] == req_alphabet:
                req_count += 1
        # print(req_alphabet,'search ends',req_count)
        return req_alphabet, req_count

    def inverse_bwt(self):
        result = ['$']
        matrix = []
        bwt_str = self.bwt_str
        sort_bwt_str_list = list(bwt_str)
        sort_bwt_str_list.sort()
        bwt_str_list = list(bwt_str)
        for i in range(0,len(bwt_str_list)):
            matrix.append([sort_bwt_str_list[i],bwt_str_list[i]])
        # print(matrix)

        count = 1 # stores index of occurance of the alphabet in the second column.
        while len(result) < len(matrix):
            for i in range(0,len(matrix)):
            # For first element after $.
                if matrix[i][0] == '$' and result == ['$']:
                    req_alphabet = matrix[i][1]
                    result.insert(0,req_alphabet)
                    # print("1 ->",req_alphabet,count)
                else: 
                    # print('Here',req_alphabet)
                    if matrix[i][0] == req_alphabet:
                        req_alphabet, count = Burrows.find_next_alphabet(self,matrix,req_alphabet,count,len(matrix))
                        # print("2 ->",req_alphabet,count)
                        result.insert(0,req_alphabet)
        if result[0] == '$':
            result = result[1:]
        print(result)


if __name__ == '__main__':
    b = Burrows('jannabanana')
    bwt_str = b.bwt()
    print(bwt_str)
    b.inverse_bwt()



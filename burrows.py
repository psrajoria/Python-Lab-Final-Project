import sys

class Burrows:
    def __init__(self,t):
        '''
        t: input string
        index_list: List holding indexes of the strings generated while performing cyclic rotations.
                    This will be usefull while working on substring.
                    [
                        ['A',1],
                        ['B',2],
                        ...
                    ]
        '''
        self.template_string = str(t) + '$'
        self.index_dict = []

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
            result.append(temp_str)
            self.index_dict.append([temp_str[-1],i])
        self.rotations = result
        # print(self.index_dict)
        self.index_dict.sort()
        # print(self.index_dict)

    def lexi_sorting(self):
        self.rotations.sort()
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

    def find_next_alphabet(self,matrix,req_alphabet,required_count,j):
        '''
        This is used to find the alphabet from the 2nd column by using the alphabet last fetched.
        Searches the 1st column, finds the appropriate alphabet in 2nd column and returns it along with the count of it in 2nd column.
        '''
        current_count = 1
        req_count = 1
        index = 0
        # print(req_alphabet,'search')

        for i in range(0,j):
            if matrix[i][0] == req_alphabet:
                if current_count == required_count:
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
        '''
        result: List for storing the inverse of the BWT string provided.
        matrix: 2D List for storing the 2 columns required for creating the inverse BWT.
        '''
        result = ['$']
        matrix = []

        # fetching the bwt string generated. Creating list from the string and sorting it
        # lexicographically for creating the 2 columns required for inverse bwt.
        bwt_str = self.bwt_str
        sort_bwt_str_list = list(bwt_str)
        sort_bwt_str_list.sort()
        bwt_str_list = list(bwt_str)

        # Creating the 2 columns in the form of 2D list.
        for i in range(0,len(bwt_str_list)):
            matrix.append([sort_bwt_str_list[i],bwt_str_list[i]])
        print(matrix)

        count = 1 # stores index of occurance of the alphabet in the second column.

        # keep iterating till the whole string is formed.
        while len(result) < len(matrix):
            for i in range(0,len(matrix)):
            # For first element after $.
                if matrix[i][0] == '$' and result == ['$']:
                    req_alphabet = matrix[i][1]
                    result.insert(0,req_alphabet)
                    # print("1 ->",req_alphabet,count)
                else:
                    # For all the elements after fetching the first.
                    # print('Here',req_alphabet)
                    if matrix[i][0] == req_alphabet:
                        req_alphabet, count = Burrows.find_next_alphabet(self,matrix,req_alphabet,count,len(matrix))
                        # print("2 ->",req_alphabet,count)
                        result.insert(0,req_alphabet)
        
        # discarding the $ from the first position(if present)
        if result[0] == '$':
            result = result[1:]

        print(''.join(result))
        return ''.join(result)

    def search_substring(self,substr):
        substr_len = len(substr)
        for i in range(0,len(self.template_string)-substr_len): 
            if self.template_string[i:i+substr_len] == substr:
                print(i)

if __name__ == '__main__':
    genome = sys.argv[1]
    b = Burrows(genome)
    bwt_str = b.bwt()
    print(bwt_str)
    b.inverse_bwt()
    b.search_substring('ANA')
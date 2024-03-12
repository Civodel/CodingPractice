class Solution:
    def isPalindrome(self, num: int) -> bool:
        # trabajar con el entero que se nos da
        # convertirlo a str
        # invertirlo
        # validar
        if num < 0:
            return False
        else:

            is_palindrome = False
            str_num = str(num)
            reverse_int = []
            int_length=len(str_num)
            for char in range(int_length):

                reverse_int.append(str_num[int_length-1])
                int_length=int_length-1

            new_str="".join(reverse_int)
            if new_str == str_num:
                is_palindrome = True

            return is_palindrome

if __name__ == '__main__':
    num=-1
print(Solution().isPalindrome(num))

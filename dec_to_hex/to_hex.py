class Solution(object):
    
    first = True

    # Lets make a dictionary to represent the alpha-num
    hex_dict = {
        10 : "a",
        11 : "b",
        12 : "c",
        13 : "d",
        14 : "e",
        15 : "f",
    }
    
    # A running list of our math results
    hex_result = []
    bin_result = []

    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0:
            return str(num)
        
        elif num == 1 and self.first or num == 2 and self.first:
            self.first = False
            return str(num)

        elif num >= 1:

            self.first = False

            # Get two results, one remainder & divisor of 16
            mod_res = self.__mod_sixteen__(num)
            div_res = self.__div_sixteen__(num)

            # Insert the remainder to the front of our List
            self.hex_result.insert(0, mod_res)

            # If we haven't reached zero, do it again
            if div_res > 0:
                self.toHex(div_res)

            # Once the quotient is 0, lets format our result
            return self.__format_hex_result__(self.hex_result)

        else:

            # Check -1 case first and return right away
            if num == -1:
                self.bin_result = "ffffffff"
                return str(self.bin_result)
            
            # Otherwise, lets calculate
            def twos_comp(num):
            
                def mod_two(num):
                    """ returns the remainder of a given num divided by 2
                    Args:
                        num (int): number to be divided
                    Returns:
                        num % 2 (int): remainder of num%16
                    """
                    return num % 2

                def div_two(num):
                    """ returns the quotient of given num and 2, no decimals
                    Args:
                        num (int): number to be divided
                    Returns:
                        num / 2: quotient of num and 2
                    """
                    return math.trunc(num/2)

                # Get two results, one remainder & divisor of 16
                mod_res = mod_two(abs(num))
                div_res = div_two(abs(num))

                # Insert the remainder to the front of our list
                self.bin_result.insert(0, mod_res)

                # If we haven't reached zero, start over
                if div_res > 0:

                    twos_comp(div_res)
            
            # Get the binary of the given negative num
            twos_comp(num)

            def add_one(s1):
                
                # Validate
                if not s1:
                    return ''

                # Determine the length
                maxlen = len(s1)

                # Instantiate
                result  = ''
                carry   = 0

                # Iterate over our 10 digits
                i = maxlen - 1
                
                first = True

                while(i >= 0):

                    # Add the given amount to the first (last) digit
                    if first:
                        s = int(s1[i]) + 1
                        first = False
                    # Then add 0's for the rest
                    else:
                        s = int(s1[i]) + 0
                    
                    # If it's a 1
                    if s == 2:
                        # Carry the 1 over
                        if carry == 0:
                            carry = 1
                            result = "%s%s" % (result, '0')
                        else:
                            result = "%s%s" % (result, '1')

                    # If it's a 1
                    elif s == 1:
                        if carry == 1:
                            result = "%s%s" % (result, '0')
                        else:
                            result = "%s%s" % (result, '1')
                    
                    # If it's a 0
                    else:
                        if carry == 1:
                            result = "%s%s" % (result, '1')
                            carry = 0   
                        else:
                            result = "%s%s" % (result, '0')
                    
                    # Decrement
                    i = i - 1;

                # If we have carried our 1 over, calculate
                if carry>0:
                    result = "%s%s" % (result, '1')

                # Otherwise, add it as is
                return result[::-1]
                        
            # Pad to 8 hex digits
            while len(self.bin_result) < 32:
                self.bin_result.insert(0, 0)

            # Flip it
            for index in range(len(self.bin_result)):
                if self.bin_result[index] == 0:
                    self.bin_result[index] = 1
                else:
                    self.bin_result[index] = 0

            # String to build
            bin_str = ""

            # Convert to string
            for item in self.bin_result:
                bin_str += str(item)
            
            # Add one to the binary result
            self.bin_result = add_one(bin_str)
            
            # Convert the binary to a base 10 integer
            new_int = int(self.bin_result, 2)
            
            # Use our handy function to get the Hex
            self.bin_result = self.toHex(new_int)
            
            # Return it
            return str(self.bin_result)
            
            
    def __mod_sixteen__(self, num):
        """ returns the remainder of a given num divided by 16
        Args:
            num (int): number to be divided
        Returns:
            num % 16 (int): remainder of num%16
        """
        return num % 16
    
    def __div_sixteen__(self, num):
        """ returns the quotient of given num and 16, no decimals
        Args:
            num (int): number to be divided
        Returns:
            num / 16: quotient of num and 16
        """
        return math.trunc(num/16)
    
    def __format_hex_result__(self, result):
        """ given a list, returns the hex formatted string
        Args:
            result (List): given list of toHex result
        Returns:
            formatted_result (str): a string representing the hex of given dec
        """
        # Instantiate return string
        formatted_result = ""

        # Iterate over the given List
        for item in result:
            # If our number is less than 10, concat it's string equiv
            if item < 10:
                formatted_result += str(item)
            # If it's more than 10 we know it's def less than 16, so refer to our dict
            else:
                formatted_result += str(self.hex_dict[item])
        
        return formatted_result

#!/usr/bin/python

import unittest

class StringCalculator(unittest.TestCase):
    """One possible solution for the StringCalculator kata. Tests are also included here"""

    def add(self, input):
        if (input == ""):
            return 0
        else:
            numberlist = self._get_list_of_numbers_from_input(input)
            self._check_negatives_not_allowed(numberlist)
            numberlist = self._ignore_numbers_above_1000(numberlist)
            return self._sum_numbers(numberlist)
    
    def _check_negatives_not_allowed(self, numberlist):
        neg_nums = self._extract_negative_numbers(numberlist)
        if (neg_nums != []):
            neg_nums_rep = self._make_list_of_numbers(neg_nums)
            raise ValueError("Negatives not allowed: {0}".format(neg_nums_rep))

    def _extract_negative_numbers(self, numberlist):
        return [i for i in numberlist if i < 0]

    def _make_list_of_numbers(self, numbers):
            return ",".join([str(i) for i in numbers])

    def _sum_numbers(self, numberlist):
        return sum(numberlist)

    def _get_list_of_numbers_from_input(self, input):
        input = self._normalize_delimiter(input)
        return [int(i) for i in input.split(",")]

    def _ignore_numbers_above_1000(self, numbers):
        return [i for i in numbers if i < 1001]

    def _normalize_delimiter(self, input):
        if self._has_delimiter(input):
            return self._normalize_custom_delimiter(input)
        else:
            return input.replace("\n", ",")

    def _has_delimiter(self, input):
        return input.startswith("//")

    def _normalize_custom_delimiter(self, input):
        delims = self._extract_delimiters(input)
        input = self._strip_delimiter_from_input(input)
        for delim in delims:
            input = input.replace(delim, ",")
        return input

    def _extract_delimiters(self, input):
        if self._has_enclosed_custom_delimiters(input):
            return self._extract_enclosed_delimiters(input) 
        else:
            return self._extract_simple_delimiter(input)

    def _extract_delimiters_part(self, input):
        return input.partition("\n")[0]

    def _extract_simple_delimiter(self, input):
        return input[2:3]

    def _extract_enclosed_delimiters(self, input):
        delimsinput = self._extract_delimiters_part(input)
        delimsinput = delimsinput[3:len(delimsinput)-1]
        return delimsinput.split("][")

    def _strip_delimiter_from_input(self, input):
        return input.partition("\n")[2]

    def _has_enclosed_custom_delimiters(self, input):
        return input[2] == '['




    def test_empty_add(self):
       self.assertEquals(0, self.add(""))

    def test_single_number_add(self):
        self.assertEquals(4, self.add("4"))

    def test_two_numbers_add(self):
        self.assertEquals(5, self.add("4,1"))

    def test_indef_numbers_add(self):
        self.assertEquals(6, self.add("1,1,1,2,1"))

    def test_allow_newline_as_separator(self):
        self.assertEquals(8, self.add("1\n2,5"))

    def test_allow_custom_separator(self):
        self.assertEquals(3, self.add("//;\n1;2"))
        
    def test_expect_error_using_negative_numbers(self):
        with self.assertRaisesRegexp(ValueError, "-1,-5,-3"):
            self.add("-1,2,4,-5,-3")

    def test_ignore_numbers_above_1000(self):
        self.assertEquals(5, self.add("1,1,1001,1003,3"))

    def test_allow_custom_delimiters_any_length(self):
        self.assertEquals(5, self.add("//[***]\n1***2***2"))

    def test_allow_multiple_delimiters(self):
        self.assertEquals(10, self.add("//[*][%]\n1*2%5*2"))
        

if __name__ == "__main__":
	unittest.main()

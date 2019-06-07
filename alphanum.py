# Alphanum algorithm: http://www.davekoelle.com/alphanum.html
# this program is modified from http://www.davekoelle.com/files/alphanum.py_v2.4
# Author: dyhe83 <https://github.com/dyhe83>

#
# Released under the MIT License - https://opensource.org/licenses/MIT
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
# USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import functools
import re


def cmp(a, b):
    return (a > b) - (a < b)


def get_chunk(item):
    re_chunk = re.compile(r'([\D]+|[\d]+)')
    item_chunk = re_chunk.match(item)

    # Subtract the matched portion from the original string
    # if there was a match, otherwise set it to ""
    item = (item[item_chunk.end():] if item_chunk else "")

    # Don't return the match object, just the text
    item_chunk = (item_chunk.group() if item_chunk else "")

    return item_chunk, item


def alphanum(a, b):
    re_letters = re.compile(r'\D+')
    re_numbers = re.compile(r'\d+')

    n = 0

    while n == 0:
        # Get a chunk and the original string with the chunk subtracted
        ac, a = get_chunk(a)
        bc, b = get_chunk(b)

        # Both items contain only letters
        if re_letters.match(ac) and re_letters.match(bc):
            n = cmp(ac, bc)
        else:
            # Both items contain only numbers
            if re_numbers.match(ac) and re_numbers.match(bc):
                n = cmp(int(ac), int(bc))
            else:
                # One item has letters and one item has numbers, or one item is empty
                n = cmp(ac, bc)

                # Prevent deadlocks
                if n == 0:
                    n = 1

    return n


def main():
    test_strings = ["1000X Radonius Maximus", "10X Radonius", "200X Radonius", "20X Radonius",
                    "20X Radonius Prime", "30X Radonius", "40X Radonius", "Allegia 50 Clasteron",
                    "Allegia 500 Clasteron", "Allegia 51 Clasteron", "Allegia 51B Clasteron", "Allegia 52 Clasteron",
                    "Allegia 60 Clasteron", "Alpha 100", "Alpha 2", "Alpha 200", "Alpha 2A", "Alpha 2A-8000",
                    "Alpha 2A-900", "Callisto Morphamax", "Callisto Morphamax 500", "Callisto Morphamax 5000",
                    "Callisto Morphamax 600", "Callisto Morphamax 700", "Callisto Morphamax 7000",
                    "Callisto Morphamax 7000 SE", "Callisto Morphamax 7000 SE2", "QRS-60 Intrinsia Machine",
                    "QRS-60F Intrinsia Machine", "QRS-62 Intrinsia Machine", "QRS-62F Intrinsia Machine",
                    "Xiph Xlater 10000", "Xiph Xlater 2000", "Xiph Xlater 300", "Xiph Xlater 40", "Xiph Xlater 5",
                    "Xiph Xlater 50", "Xiph Xlater 500", "Xiph Xlater 5000", "Xiph Xlater 58"]

    test_strings.sort(key=functools.cmp_to_key(alphanum))

    for string in test_strings:
        print(string)


if __name__ == '__main__':
    main()

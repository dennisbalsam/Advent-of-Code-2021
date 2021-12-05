# --- Part Two ---
# Next, you should verify the life support rating, which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating.

# Both the oxygen generator rating and the CO2 scrubber rating are values that can be found in your diagnostic report - finding them is the tricky part. Both values are located using a similar process that involves filtering out values until only one remains. Before searching for either rating value, start with the full list of binary numbers from your diagnostic report and consider just the first bit of those numbers. Then:

# Keep only numbers selected by the bit criteria for the type of rating value for which you are searching. Discard numbers which do not match the bit criteria.
# If you only have one number left, stop; this is the rating value for which you are searching.
# Otherwise, repeat the process, considering the next bit to the right.
# The bit criteria depends on which type of rating value you want to find:

# To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.
# To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered.
# For example, to determine the oxygen generator rating value using the same example diagnostic report from above:

# Start with all 12 numbers and consider only the first bit of each number. There are more 1 bits (7) than 0 bits (5), so keep only the 7 numbers with a 1 in the first position: 11110, 10110, 10111, 10101, 11100, 10000, and 11001.
# Then, consider the second bit of the 7 remaining numbers: there are more 0 bits (4) than 1 bits (3), so keep only the 4 numbers with a 0 in the second position: 10110, 10111, 10101, and 10000.
# In the third position, three of the four numbers have a 1, so keep those three: 10110, 10111, and 10101.
# In the fourth position, two of the three numbers have a 1, so keep those two: 10110 and 10111.
# In the fifth position, there are an equal number of 0 bits and 1 bits (one each). So, to find the oxygen generator rating, keep the number with a 1 in that position: 10111.
# As there is only one number left, stop; the oxygen generator rating is 10111, or 23 in decimal.
# Then, to determine the CO2 scrubber rating value from the same example above:

# Start again with all 12 numbers and consider only the first bit of each number. There are fewer 0 bits (5) than 1 bits (7), so keep only the 5 numbers with a 0 in the first position: 00100, 01111, 00111, 00010, and 01010.
# Then, consider the second bit of the 5 remaining numbers: there are fewer 1 bits (2) than 0 bits (3), so keep only the 2 numbers with a 1 in the second position: 01111 and 01010.
# In the third position, there are an equal number of 0 bits and 1 bits (one each). So, to find the CO2 scrubber rating, keep the number with a 0 in that position: 01010.
# As there is only one number left, stop; the CO2 scrubber rating is 01010, or 10 in decimal.
# Finally, to find the life support rating, multiply the oxygen generator rating (23) by the CO2 scrubber rating (10) to get 230.

# Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating, then multiply them together. What is the life support rating of the submarine? (Be sure to represent your answer in decimal, not binary.)

gamma_rate=''
epsilon_rate=''

with open('input.txt', 'r') as f:
    values = [value for value in f.read().splitlines()]
    for i in range(0,len(values[0])):
        v={'0':0,'1':0}
        elements = [value[i] for value in values[0:]]
        for num in elements:
            v[str(num)]+=1
        if v['0'] > v['1']:
            gamma_rate += '0'
            epsilon_rate += '1'
        else:
            gamma_rate += '1'
            epsilon_rate += '0'
    
    oxygen_rating, co2_rating = values, values
    for i in range(0,len(values[0])):
        v={'0':0,'1':0}
        u={'0':0,'1':0}
        elements_A = [value[i] for value in oxygen_rating[0:]]
        elements_B = [value[i] for value in co2_rating[0:]]
        for num in elements_A:
            v[str(num)]+=1
        for num in elements_B:
            u[str(num)]+=1

        if len(oxygen_rating) > 1:
            if (v['1'] > v['0'] or v['1'] == v['0']):
                oxygen_rating = [value for value in oxygen_rating if value[i] == '1']
            else:
                oxygen_rating = [value for value in oxygen_rating if value[i] == '0']
        if len(co2_rating) > 1:
            if u['0'] < u['1'] or u['0'] == u['1']:
                co2_rating = [value for value in co2_rating if value[i] == '0']
            else:
                co2_rating = [value for value in co2_rating if value[i] == '1']
    
    print(int(oxygen_rating[0],2)*int(co2_rating[0],2))
    print(int(gamma_rate,2)*int(epsilon_rate,2))
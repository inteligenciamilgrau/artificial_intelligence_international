# this scrap was maded with the intention to detect
# the next item of a list when a linear sequence is detected
# The input is a list with some numbers
# return if its a linear sequence and the next number

# its just some thinking exercises that try to find a solution
# and at the same time try to explore different ways to do the same thing

#list = [3,6, 9 ,12,15, 18]
list = [27,21,15,9, 3]

def discover_pattern(list):
    results = []
    for index, actual_number in enumerate(list):
        if not index == 0:
            results.append(list[index]- list[index-1])
    return results

print("results", discover_pattern(list))

a = list
r = [a[i]-a[i-1] for i in range(1, len(a))]
print("r", r)

####################

def calculate_pattern_sum(result):
    return sum(result) == result[0] * len(result)

def calculate_pattern_all(result):
    return all([i == result[0] for i in result])

def calculate_pattern_set(result):
    return len(result) != len(set(result))

def calculate_pattern_count(result):
    return result.count(result[0]) == len(result)

def pattern_is_linear(result):

    fisrt_element = result[0]
    #pattern = True
    #for element in result:
    #    if not element == fisrt_element:
    #        pattern = False

    #pattern = calculate_pattern_sum(result)
    #pattern = calculate_pattern_all(result)
    #pattern = calculate_pattern_set(result)
    pattern = calculate_pattern_count(result)

    if pattern == True:
        pattern_number = fisrt_element
        return pattern_number
    elif pattern == False:
        return None
patt = pattern_is_linear(r)
print("pattern is", patt)

#########################

def predict_next_number(patt, list):
    return list[-1] + patt

if not patt is None:
    print("predict", predict_next_number(patt, list))


######
result = r

print("pre-result", result.count(result[0]))
print("ret1", result.count(result[0]) == len(result))# Count the 0'th element


print("set", set(result))
print("set2", len(result) != len(set(result))) # Remove duplicates and compare length.


print("all1", [i == result[0] for i in result])
print("all2", all([i == result[0] for i in result])) # List comprehension and all statement


print("sum1", sum(result))
print("sum2", sum(result) == result[0] * len(result)) # using math, this one might not work 100%

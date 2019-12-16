courses = ['history', 'math', 'physics', 'compsci']
courses_2 = ['art', 'education']

# courses.insert(0, courses_2)
#append just adds the list
# courses.append(courses_2)
#extend adds the values from the list
# courses.remove('math')
#pop returns courses it pops
# courses.pop('math')
# courses.extend(courses_2)
#reverses the list
# courses.reverse()
#sorts in alphabetical/numerical order
# courses.sort()
#sorts in reverse order
# courses.sort(reverse=True)

#sorted function returns a sorted version of the list
#without altering original list
# sorted_courses = sorted(courses)

#return min and max values
# min(lyst)
# max(lyst)

#sum of numbers
# sum(lyst)

#index finds the index of a value
# print(courses.index('compsci'))

#check to see if a value is in the list
# print('art' in courses)

# for item in courses:
#     print(item)

#returns two values - index and value
# can set start = 1
# for index, course in enumerate(courses):
#     print(index, course)

# Turns these into CSV (or whatever)
# course_str = ', '.join(courses)

print(course_str)
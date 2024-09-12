names = ["Jim", "Jane", "Joe", "Jill"]
nums = [2,3,5,7,9,10]


def linear_search(search_term, search_list):
    for x in range(len(search_list)):
        if search_list[x]== search_term:
            print(search_term, x)

linear_search(7, nums)
linear_search("Joe", names)

# create a set, use a loop to add everything to the set, and create a list tha equal to the set

# def uniqueList(accountID):
#   uniqueSet = set()
#   for i in accountID:
#     uniqueSet.add(i)
#   return uniqueSet

# accountID = [123,456,789,123,567,456]
# # accountSet = {123,456,789,567}
# # newlist = list(accountSet)

# print(list(uniqueList(accountID)))
# # print(newlist)


def solution(id_list):
  # initiate unique id
  unique_id = 0
  # XOR every id in id list
  for i in id_list:
    # XOR operation
    unique_id ^= i
  return unique_id

print(solution([1,2,3,2,1]))
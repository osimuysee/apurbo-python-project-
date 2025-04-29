list = ["bangladesh", "india", "nepal"]
list.append("afganistan")
print("after sorts: ", list)
#adds one element on the end like [ b, a, c, d] 
list.sort()
print("after list: ", list)
#sorts in ascending order like [ a, b, c ] it's one kind of sequencing
list.sort(reverse = True)
print("after sort reverse: ", list)
# sorts in descending order like [ c, b, a] itr's reverse sequnce
list.reverse()
print("after reverse: ", list)
#reverse list totally 180 degree 
list.insert( 1, "china")
print("after insert: ", list)
#insert elemnt at index
list.remove("bangladesh")
print("after remove: ", list)
#remove first occurence of the element like [ b, c]
list.pop(2)
print("after remove the index: ", list)
#remove element of index
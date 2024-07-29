# Tuples
s3_buckets_lists = ("abhi_demo_bucket", "mani_demo_bucket", "raju_demo_bucket", "rani_demo_bucket", "amit_demo_bucket")

# 1)creating_tuple
print(s3_buckets_lists)

# 2) type_of_tuple(or)list
print(type(s3_buckets_lists))




# 2) tuple_indexing
print(s3_buckets_lists[0])
print(s3_buckets_lists[1])
print(s3_buckets_lists[2])
print(s3_buckets_lists[3])
print(s3_buckets_lists[4])




# 3) list_length
print(len(s3_buckets_lists))




#### 4) append_element_on_list(add-on-list but in tuple concept it is immutable it cannot add or remove obejects)
#### s3_buckets_lists.append("sruti_demo_bucket")
#### print(s3_buckets_lists)




#### 5) remove_element_from_list(remove-from-list but in tuple concept it is immutable it cannot add or remove obejects)
#### s3_buckets_lists.remove("sruti_demo_bucket")
#### print(s3_buckets_lists)




# 6) slicing_element_on_list ---> Creates a new list with elements at index 1, 2, and 3(UPPERBOUND IS NOT EXHICUTED)
new_list = s3_buckets_lists[1:4]
print(new_list)




# 7) concatination_tuple --->  You can combine two or more listing to create a new list
print(s3_buckets_lists[1] + "--" + s3_buckets_lists[2])




#### 8) sorting a list ---> (sort has no attribute it cannot perform on tuple)
#### numbers = (2000, 20, 2, 200)
#### numbers.sort()
#### print(numbers)



# 9) combination_of_different_elements ---> (tuple takes all elements weather its a integer, float, string nomatters)
random_list = (1.4, "surya", 500, "chandra", 300.501456, 5000)
print(random_list)

# anonymous function --> unNamed function anamika
# ei anonymous function user define function guloke choto kore dey
# print use kora jay ne 
# se only return kore
import functools
def square(x):
    return x*x
print(square(5))
# ei same jinish ta amra jokhon lambda_function diye korbo

#lambda arguments : expression
square = lambda x: x*x # ekhane lambda x holo lambda arguments : x*x holo expression
print(square(4))
# lambda function code ke choto kore fele

add = lambda a,b : a+b
print(add(1,2))

#  Python-এর একটি গুরুত্বপূর্ণ কনসেপ্ট নিয়ে কাজ করছে — সেটি হলো list of tuples কে sort করা। 

students = [('Rahim', 60) , ('Karim', 49), ('Fahim', 100)]
sorted_students = sorted(students, key = lambda x : x [1])
print(sorted_students)
# এখানে students একটি list of tuples।
# প্রতিটি tuple-এ দুটো উপাদান আছে:
# ছাত্রের নাম (string)
# তার নাম্বার বা স্কোর (integer)
# 🔹 sorted() ফাংশন একটা নতুন sorted লিস্ট রিটার্ন করে, যেটি মূল লিস্টকে পরিবর্তন করে না।

# 🔹 এখানে key = lambda x: x[1] এর মানে হল:
# প্রতিটি tuple-র x হিসেবে ধরা হচ্ছে।
# x[1] মানে আমরা প্রতি tuple-র index 1  উপাদান অর্থাৎ নাম্বার কে ধরে sort করছি।

# উদাহরণ:
# 'Rahim' → 60
# 'Karim' → 49
# 'Fahim' → 100
# এই স্কোর অনুযায়ী sort করলে সবচেয়ে কম স্কোর আগে আসবে।

#map(), filter(), reduce()
#map() function protiti elements traverse kore ekta ekta new list or tuples return kore
# map() ব্যবহার করে তুমি লিস্টের প্রতিটি উপাদানে একই কাজ করতে পারো।
# 🧠 মনে রাখো:
# সবগুলোর ওপর এক কাজ → map()

# numbers = [1, 2, 3, 4]
#result = list(map(square korte chacchi, kar upor apply korte chacchi))

# result = list(map(lambda x: x * 2, numbers))
# print(result)# otuput [2, 4, 6, 8]





# filter() ব্যবহার করে তুমি একটা লিস্ট থেকে কিছু আইটেম বাছাই করতে পারো — যেগুলো কোনো শর্ত পূরণ করে।
# 🧠 মনে রাখো:
# শর্ত অনুযায়ী কিছু বাছাই → filter()
numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)# output:[2, 4, 6]


# reduce() সবগুলো উপাদান নিয়ে একটার পর একটা মিলিয়ে একটা রেজাল্ট দেয়।

# তবে reduce() ব্যবহারের জন্য functools pakage থেকে import করতে হয়।
# 🧠 মনে রাখো:
# সব মিলিয়ে একটা রেজাল্ট → reduce()
# from functools import reduce
# numbers = [1, 2, 3, 4]
#result =functools.reduce(lambda x, y: x + y, numbers)
# print(result) #1+2 = 3, 3+3 = 6, 6+4 = 10 output hobe 10

#reduce
numbers = [1, 2, 3, 4]
sum =functools.reduce(lambda x,y : x+y, numbers)# ekhane functools use korte hobe
print(sum)

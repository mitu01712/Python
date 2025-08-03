# Python Dictionary হচ্ছে এমন এক ধরনের ডেটা স্ট্রাকচার, যেখানে ডেটা key-value pair আকারে সংরক্ষণ করা হয়।

# student = {
#     "name": "Rahim",
#     "age": 22,
#     "department": "CSE"
# }
# এখানে:
# name, age, department — এগুলো হলো key
# "Rahim", 22, "CSE" — এগুলো হলো value

#{}
#key value pair
#indexing er shujog nai
#kay gula obossoi immutable //value chaie change korte parbo

a = {'Rahim': 12, 'Karim': 14,'Fahim': 78, 1:[1, 2, 3, 4], 2: {3, 4, 5}}

print(type(a))

for i in a:
    print(i)# by default loop chalale amder key gula dibe
print("-----------------------------")
#amra jodi value gula ke print korte chai tahole values() method ke use korte hobe 
for i in a.values():
    print(i)

# ekhon jodi amra dictionary keys and values print korte chai sei khetre amra keys() and values() methods use korbo

print(a.keys(), a.values())

print("***********************************")
# dectionary er key values pair eksathe pete chaile 
for k,v in a.items():
    print(f"key Name : {k}, Values {v}")

#items() method ব্যবহার করলে একটি dictionary-এর সব key এবং তাদের corresponding value গুলোকে একসাথে tuple আকারে return করে।

#🧠 তাহলে for k, v in a.items() মানে কী?
# তুমি প্রতিবার লুপে k তে key আর v তে value রাখছো।

# dict.items()	key-value pair tuple আকারে দেয়
# dict.keys()	শুধু key গুলো দেয়
# dict.values()	শুধু value গুলো দেয়

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

a = [1, 2, 3]
b =["Mango", "Banana", "Apple"]

#{1 : "Mango", 2 : "Banana", 3 : "Apple"} eta korte chaschi
print(list(zip(a,b)))

# 🔍 zip(a, b) এর কাজ কী?
# zip(a, b) দুটি list বা iterable (যেমন: string, tuple) কে একসাথে জোড়া লাগিয়ে tuple বানায়।

# 🔸 প্রতিটি element হবে একটি tuple — যেখানে প্রথমটা a থেকে, দ্বিতীয়টা b থেকে নেওয়া।
c = dict(zip(b,a))# ekhan e ekhon b kay a holo value
print(dict(zip(a,b)))
print(c["Apple"])
#print(c[3]) error asle 3 nam e kono key nei


# ➡️ এই কোডটি দুটি list a এবং b কে zip() দিয়ে pair করে তারপর dict() দিয়ে dictionary বানায়।
  
import pathlib
import os

# # ami chacchi python ke use kore name.txt file ke read korte
# file = open('name.txt', 'r')# ekhane open()function holo build in function jetar vitore open('file_name','r')
# contant = file.read()
# print(contant)
# #file close korte// file er kaj sesh kore amra close kore dibo
# file.close()

# ekhane bar bar open kora close kora onek jhamela ei problem theke ber hoye aste chaile 
# with open('name.txt','r') as f: # as f means file take amra f variable er moddhe rakhbo
#     contant = f.read()
#     print(contant)

# 🔷 ধাপে ধাপে ব্যাখ্যা:
# 🟩 ১. with open('name.txt', 'r') as f:
# 🔸 open() ফাংশন দিয়ে ফাইল খোলা হয়।
# 🔸 'name.txt' → ফাইলের নাম (একই ফোল্ডারে থাকতে হবে)
# 🔸 'r' → অর্থ read mode — মানে আমরা শুধু ফাইলের লেখা পড়ব, কোনো লেখা যোগ বা পরিবর্তন করব না।
# 🔸 with ... as ... → এটা একটা safe system ফাইল খোলার জন্য।
# ফাইল খোলা এবং কাজ শেষে নিজে নিজেই বন্ধ হয়ে যায়।

    
# 🔷 f কেবল একটি variable name (নাম)
# 🔸 এখানে f মানে file object — মানে open() যেই ফাইলটা খুলেছে, সেটার একটা "রেফারেন্স" আমরা f নাম দিয়ে ধরে রেখেছি। ekhane amra je kono name object hisebe use korte parbo


# python code use kore amra kivabe ekta file e amra write korte pari

# with open('name.txt', 'w') as f:
#     # f.write("Hello world\n")
#     # f.write("I am writing in a file\n")
#       f.write("This is for testing")
    # # ei code ta run korle 
    # name.txt file e ja age likha chilo tai output dekhabe
# Mitu Rani Ghosh
# jashore, khulna, Dhaka, Bangladesh
# Ghatail Cantonment College, Ghatail, Tangail

# ekhon jodi amra name.txt file open kori tahole
# Hello world
# I am writing in a file // eta dekhabe ekhane ager likha gulo over write hoye ei likha bosay diche

# ekhon run korle Hello world I am writing in a file eta output asbe and 
# name.txt file e overwrite hoye this is for testing er sentence ta dekhabe

# at the end of the discasion we can say that write() function always previous contant fully over write kore currect text show korbe

# fully clean korar dorkar naw hoite pare
# ekhon amra chacchi ei porjonto joto gula text write korechi se gula por por show korbe //etar jonno amra jei method ke use kori seta holo append() method  // append() er kaj last er dike push koro

# with open('name.txt', 'a') as f:
#     f.write("\nHello world\n")
#     f.write("I am writing in a file\n")
#     f.write("This is for testing")

# # ekhon dhoro amder ekta list ache ekhon list er line add korte cachcci
# lines = ['\nI love Python\n', 'I am new to python\n']
# # ekhon jodi amra ei line take write korte chai
# with open('name.txt', 'a') as f:
#     f.writelines(lines)# kono line ke append korte chaile amrader object.writelines() take use korte hobe


#file exist kore kina eta check korte chai// etar jonno amder ekta build in packge dorkar porbe import os ekhane os mane opareting system 
# r opareting system mane eije amara ekta software chalaschi, file toiri kortechi,er sob e opareting system help kore  linax, windos, mac , (opareting system)jegulo hard ware er sathe directy involpment kare

if os.path.exists('name.txt'):
    print("File_exists")
else:
    print("File not found")

if os.path.exists('test.txt'):
    print("File_exists")
else:
    print("File not found")

# same kaj ta amra import pathlib build in packge use kore korte pari 
file_path = pathlib.Path('name.txt') # ekhane Path er P must capital letter hobe

if file_path.exists():
    print("File exists")
print(os.path.abspath('name.txt')) # full path dekhte chaile
print(os.path.getsize('name.txt')) # size jante chaile bytes e result dibe

with open('name.txt', 'r') as f:
    print(f.tell())
    print(f.read(10)) 

#     🔍 f.read(10) এর মানে:
# 👉 এটি ফাইল থেকে ১০টি বাইট (বা অক্ষর) পড়ে এবং সেই অংশটি প্রিন্ট করে।

# 🔍 tell() ফাংশনের কাজ কী?
# 👉 f.tell() ফাইলের কার্সার (file pointer) বর্তমানে কোথায় আছে — সেটার অবস্থান (position) বাইট (byte) হিসেবে দেখায়।

# 🎯 সহজভাবে বুঝি:
# ধরো, তুমি একটা বই পড়ছো, আর জানতে চাচ্ছো—তুমি এখন ঠিক কোন পেজ বা জায়গায় আছো।
# তেমনি, যখন তুমি Python দিয়ে কোনো ফাইল পড়ো বা লেখো, তখন ফাইলের pointer বা cursor কোন জায়গায় আছে, সেটা জানতে tell() ব্যবহার করা হয়।

# 🔹 pathlib এবং os মডিউল দুইটি Python-এর বিল্ট-ইন (built-in) লাইব্রেরি।
# 🔹 pathlib ফাইল পাথ (file path) ও ফাইল সংক্রান্ত কাজ সহজভাবে করার জন্য ব্যবহৃত হয়।
# 🔹 os মডিউল দিয়ে অপারেটিং সিস্টেম সংক্রান্ত কাজ (যেমন ফাইলের ঠিকানা, ডিরেক্টরি পাওয়া ইত্যাদি) করা যায়।

#🔹 এই লাইনে os.path.abspath() ফাংশনের মাধ্যমে 'name.txt' ফাইলটির সম্পূর্ণ ঠিকানা (absolute path) বের করা হচ্ছে।
# অর্থাৎ আপনার কম্পিউটারে এই ফাইলটি ঠিক কোন লোকেশনে আছে, সেই পথ 
# দেখাবে।

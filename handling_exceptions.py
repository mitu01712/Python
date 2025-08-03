# what is the diferent between errors vs exceptions

# compile time , run Time 
"""
Python-এ compile time এবং run time দুটি গুরুত্বপূর্ণ ধাপ, যেগুলো প্রোগ্রাম চালানোর সময় ভিন্ন ভিন্নভাবে কাজ করে। Compile time হলো সেই সময় যখন Python প্রোগ্রামটি রান করার আগেই কোডটি চেক করে নেয়, যাতে কোনো syntax error (মানে বানান বা গঠনগত ভুল) আছে কিনা। যদি কোডে কোন ভুল থাকে, যেমন ভুল বানানে ফাংশন লেখা হয় (printt("Hello")), তাহলে Python আগে থেকেই সেই ভুলটি ধরিয়ে দেয় এবং প্রোগ্রামটি চলতে দেয় না। এ ধরণের ভুলকে বলা হয় compile time error।

অন্যদিকে, run time হলো সেই সময় যখন কোডটি আসলেই চালানো হয় এবং তার কার্যকারিতা দেখা যায়। এ সময় দেখা যায় প্রোগ্রাম চলার সময় কোনো সমস্যা তৈরি হচ্ছে কিনা। যেমন, যদি কোডে লেখা থাকে a = 10; b = 0; print(a / b), তাহলে কোডটি দেখতে একেবারেই ঠিকঠাক মনে হবে এবং compile time-এ কোনো ভুল ধরা পড়বে না। কিন্তু যখন কোডটি চলবে, তখন ZeroDivisionError দেখাবে কারণ 0 দিয়ে ভাগ করা যায় না। এ ধরনের ভুলকে বলা হয় run time error।

আরও একটি গুরুত্বপূর্ণ run time ভুল হলো logic error। ধরো, তুমি দুটি সংখ্যার যোগফল বের করার জন্য add(x, y) নামের একটি ফাংশন বানালে, কিন্তু ভুল করে সেখানে return x - y লিখে ফেললে — syntax-এ কোনো ভুল হবে না, কোড চলবেও, কিন্তু যা চাইছো তা হবে না। এই ভুলটা কোড চালানোর সময়ই বোঝা যায়, তাই এটাও run time-এ ধরা পড়ে।

সংক্ষেপে বললে, compile time হচ্ছে কোড লেখার সময় গঠনগত ভুল চেক করার ধাপ, আর run time হচ্ছে প্রোগ্রাম চালানোর সময় চলমান ভুল বা অপ্রত্যাশিত আচরণ বোঝার ধাপ। এই দুইটি ভালোভাবে বোঝা গেলে প্রোগ্রামিং অনেক সহজ হয়ে যায়।
"""
"""
errors ---> errors gula amra compile time er error
example: syntax error, Indentation error

exceptions --> Run time error
example: Indexing, key, value, zero division error
"""

# with open("rahim.txt", 'r') as f:
#     print(f.read()) # ei folder e rahim.txt name kono file nei eta ekta exception error or run time error

# ekhon ei error ta ke ami handle korbo kivabe?
# try: # je code e exception thakte pare
#     with open("rahim.txt", 'r') as f:
#         print(f.read()) 
# except FileNotFoundError:
#     print("File not Found")
"""
🔍 সহজভাবে বললে:
try: তুমি যে কোড অংশে ভুল হওয়ার সম্ভাবনা আছে, সেটা এখানে রাখো।

except: যদি try ব্লকের কোডে ভুল হয়, তাহলে Python এখানকার কোড চালিয়ে error হ্যান্ডেল করে।

 উদাহরণ ১: ZeroDivisionError হ্যান্ডেল করা

try:
    result = 10 / 0
except ZeroDivisionError:
    print("ভুল: শূন্য দিয়ে ভাগ করা যায় না।")
Output:
ভুল: শূন্য দিয়ে ভাগ করা যায় না।
ব্যাখ্যা: এখানে 10 / 0 করলে সাধারণত ZeroDivisionError হয়, কিন্তু আমরা সেই error কে except দিয়ে ধরেছি, তাই প্রোগ্রাম ভাঙেনি।
"""


# 0 division error
"""
try:
    # with open("rahim.txt", 'r') as f:
    #     print(f.read())
    # print(10/0)
    # x = int("abc")
    # a= [1, 2, 3]
    # print(a[100])
    x = abc # jodi amra emon kono error kori jetar kono nam nei tokhon amra boli except Exception as e:
except ZeroDivisionError:
    print("Error: Division by Zero is not possible")
except FileNotFoundError:
    print("File not fount")
except ValueError:
    print("Invalid Value")
except IndexError:
    print("Invalid Index")
except Exception as e:
    print("some error occurred!!", e)
    
    ekhane jokhon first block e dekhe error file name exists kore na tokhon se filenotfounderror except e jay baki gula kaj kore na
    but jokhon file exists kore tokhon next line check kore error pay zerodivisionerror except e duke and error handle kore

    # ekhon jodi kono error e na thake tahole ekta smg asbe your code successfully run
"""
try:
        with open("name.txt", 'r') as f:
           print(f.read())
        print(10/0)
        x = int("12")
        a= [1, 2, 3]
        print(a[1])
        x = 10
except ZeroDivisionError:
    print("Error: Division by Zero is not possible")
except FileNotFoundError:
    print("File not fount")
except ValueError:
    print("Invalid Value")
except IndexError:
    print("Invalid Index")
except Exception as e:
    print("some error occurred!!", e)
else:
    print("Code executed successfully Run!!")

# r ekta key word ache seti holo finally keyword code er moddhe error thakuk ar na thakuk eta print korbe
finally:
    print("Error thak r na thak eta print korbei")

# ekhon ami user ke bollam apni ekta  png file upload koren but user vule pdf file upload kore diche

# # custom error baniyechi amra 
# def check_file(filename):
#     if not filename.endswith('.txt'):
#         raise ValueError("Only .txt files are allowed")
#     print("Valid File")

#check_file('data.csv')
# ekhane error dibe karon .txt file allowed not .csv file
# check_file('data.txt') # output asbe Valid file

"""
👉 এখানে কী হচ্ছে?
if not filename.endswith('.txt'):
যদি ফাইলের শেষে .txt না থাকে, তাহলে...
raise ValueError(...):
Python নিজে থেকে error ছুঁড়ে ফেলে (manually)। একে বলে raising an exception।
print("Valid File"):
যদি ফাইলটি .txt হয়, তাহলে এটা valid বলে মেসেজ দেবে।
"""
# amra ekhon ei custom error ke handle korbo

def check_file(filename):
    if not filename.endswith('.txt'):
        raise ValueError("Only .txt files are allowed")
    print("Valid File")

try:
    check_file('data.csv')
except Exception as e:
    print(e)
"""
এখানে তুমি try করে যাচ্ছো:
"আচ্ছা দেখি, ফাইলটা ঠিক আছে কিনা..."
যদি ঠিক .txt হয়, তাহলে বলবে: Valid File
যদি ভুল হয়, মানে .csv, তখন তুমিই বলবে: "Only .txt files are allowed"

🎨 একদম দৈনন্দিন উদাহরণ:
ধরো, তুমি একটা বাসে উঠতে যাচ্ছো, কিন্তু সেখানে লেখা আছে:
"শুধু ছাত্রদের জন্য"
তুমি ছাত্র হলে, তুমি উঠতে পারবে।
ছাত্র না হলে, গেটম্যান তোমাকে বলবে:
❌ "শুধু ছাত্রদের জন্য!"

এই বলাটাই হচ্ছে raise ValueError(...)
আর সেই গেটম্যানের বদলে কেউ politely বোঝায় দিলে, সেটা হচ্ছে try ও except 😄

✅ অতিশয় সংক্ষেপে:
Python কোড	বাস্তব উদাহরণ
try	চেষ্টা করা
raise	সমস্যায় চিৎকার করা
except	সেই সমস্যা সুন্দরভাবে সামলানো
"""
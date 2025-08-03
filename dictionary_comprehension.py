nums = list(range(0,11)) # 10 ta value

result = {i:"Even" if i%2 == 0 else "odd"for i in nums}

print(result)

a = list(range(1,21))
even =[]
odd =[]
for i in a:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
#even.append(i) → even list এ সেই সংখ্যা যোগ করবো।
# না হলে সেটা odd, তাই odd.append(i) করবো।
print("Even numbers:", even)
print("Odd numbers:", odd)
#append() method এর কাজ হলো — list-এর শেষে নতুন কোনো item (value) যোগ করা।


#  এটা হলো dictionary comprehension।
# মানে:
# প্রতিটি i নাম্বার nums লিস্ট থেকে নেওয়া হবে
# যদি i % 2 == 0 হয় (মানে even number), তাহলে value হবে "Even"
# না হলে (মানে odd number) value হবে "odd"
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

students = {
    1: {
        "Name": "Karim",
        "Birth_year": 1999,
        "Department_Name": "CSE",
        "Location": "Mohamadpur, Dhaka"
    },
    2: {
        "Name": "Rahim",
        "Birth_year": 1998,
        "Department_Name": "Math",
        "Location": "Mirpur, Dhaka"
    },
    3: {
        "Name": "Fahim",
        "Birth_year": 1996,
        "Department_Name": "BBA",
        "Location": "Shamoli, Dhaka"
    },
    4: {
        "Name": "Hamza",
        "Birth_year": 2000,
        "Department_Name": "Computer Science",
        "Location": "Mirpur-10, Dhaka"
    },
    5: {
        "Name": "Satu",
        "Birth_year": 1999,
        "Department_Name": "Business Management",
        "Location": "Mohamadpur, Dhaka"
    },
    6: {
        "Name": "Harim",
        "Birth_year": 1999,
        "Department_Name": "Agriculture",
        "Location": "Mirpur-11, Dhaka"
    },
    7: {
        "Name": "Kobita",
        "Birth_year": 1999,
        "Department_Name": "CSE",
        "Location": "Uttara, Dhaka"
    }
}

search_id = int(input("Please Enter your student ID(1 to 7):"))

if search_id in students:
    print("student Found")
    for key, value in students[search_id].items():
        print(f"{key}: {value}")

else:
    print("Sorry No student found with this ID")

# এখন তোমার কোড:
# ✅ 1. if search_id in students:
# এই লাইনটা দেখে:

# search_id নামে যেই ID ইনপুট নিছো,

# সেটা students dictionary-র ভিতরে আছে কি না, সেটা চেক করে।

# যদি থাকে, তাহলে নিচের লাইনগুলো চালাবে।

# ✅ 2. print("student Found")
# এই লাইনটা simply প্রিন্ট করে:

# nginx
# Copy
# Edit
# student Found
# ✅ 3. for key, value in students[search_id].items():
# এখানে students[search_id] হলো ওই student-এর details:

# যেমন, যদি search_id = 2, তাহলে students[2] = {"Name": "Rahim", "Birth_year": 1998}

# .items() method key আর value জোড়ায় জোড়ায় দেয়

# তাই for key, value দিয়ে তুমি ধরতে পারো:


a = [1, 2, 3, 4, "a", 5, 6, 7]

print(type('b'))  # এটা শুধু দেখাচ্ছে 'b' এর টাইপ => <class 'str'>

for i in a:
    if type(i) == type('b'):
        break  # যদি কোন এলিমেন্টের টাইপ str হয়, তাহলে লুপ থেমে যাবে
    else:
        print(i)
print("-------------------------------")
for i in a:
    if type(i) == type('a'):
        continue  # যদি টাইপ হয় string, তাহলে ওইটা স্কিপ করে পরেরটার দিকে যাবে a bade baki sob print korbe
    else:
        print(i)

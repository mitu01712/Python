# # jokhon amra janbo na koto bar loop cholbe kokhon amra while loop chalabo
# a = [1, 2, 3, 4, 5]
# result = 0
# i = 0 
# n = len(a)
# while i<n: # 0<5, 1<5, 2<5, 3<5, 4<5 
#     #while loop infynite loop e use hoye thake
#     result = result + a[i]#0+1, 1+2, 3+3, 6+4, 10+5 
#     i+=1# i = i + 1
#     print(result)

a = [-10,2,19,-3,-5] #[0, 2, 19, 0, 0]eta korte chaschi

i = 0
while i<len(a):
    if a[i] < 0: # list er jei index er man 0 theke choto
        a[i] = 0 # sei index er number ke replace kore 0 bosay dao
    i += 1 # ekhane i er increment always loop er baire hobe
print(a)

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
print(i)

# With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")


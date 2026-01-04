num1 = float(input("প্রথম সংখ্যা লিখুন: "))
num2 = float(input("দ্বিতীয় সংখ্যা লিখুন: "))

# ব্যবহারকারীর কাছে অপারেশন নেওয়া
print("কোনটি করতে চান?")
print("1. যোগ")
print("2. বিয়োগ")
print("3. গুণ")
print("4. ভাগ")
choice = input("নির্বাচন করুন (1/2/3/4): ")

# শর্ত ব্যবহার করে অপারেশন করা
if choice == '1':
    result = num1 + num2
    print("ফলাফল:", result)
elif choice == '2':
    result = num1 - num2
    print("ফলাফল:", result)
elif choice == '3':
    result = num1 * num2
    print("ফলাফল:", result)
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print("ফলাফল:", result)
    else:
        print("ত্রুটি: শূন্য দিয়ে ভাগ করা যায় না!")
else:
    print("সঠিক অপশন বেছে নিন।")

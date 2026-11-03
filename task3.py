name = input("Enter your name: ")
valid = True

# أحذف المسافات من بداية ونهاية الاسم
name = name.strip()

# أرتب المسافات بين الكلمات
while "  " in name:
    name = name.replace("  ", " ")

# أخلي أول حرف من كل كلمة كبير
name = name.title()

# أتحقق من صحة الاسم
if name.startswith("@") or not name:
    print("Invalid name")
    valid = False
else:
    print(name)


email = input("Enter your email: ")

# أحذف المسافات وأحول الحروف إلى صغيرة
email = email.replace(" ", "").lower()

# أتحقق من صحة البريد الإلكتروني
if "@" in email and "." in email:
    print(email)
else:
    print("Invalid email")
    valid = False


phone = input("Enter your phone: ")

# أحذف المسافات من رقم الجوال
phone = phone.replace(" ", "")

# أتحقق من صحة رقم الجوال
if phone.isdigit() and phone.startswith("05") and len(phone) == 10:
    print(phone)
else:
    print("Invalid phone")
    valid = False


# أنشئ اسم المستخدم إذا كانت البيانات صحيحة
if valid:
    # أستخرج الاسم الأول
    dot_position = name.find(" ")

    if dot_position == -1:
        first_name = name.lower()
    else:
        first_name = name[:dot_position].lower()

    # آخذ آخر رقمين من الجوال
    last_digits = phone[-2:]

    # أنشئ اسم المستخدم
    username = first_name + "." + last_digits

    print("Username:", username)

    # أطبع سجل العميل
    print(name, "|", email, "|", phone, "OK")  

    # في هذه المهمة تعلمت كيف أنظف بيانات العميل وأتأكد من صحتها
# رتبت الاسم وحذفت المسافات الزائدة.
# حولت البريد الإلكتروني إلى حروف صغيرة وتأكدت من وجود @ والنقطة
# تحققت من رقم الجوال وأنه يبدأ بـ 05 ويتكون من 10 أرقام
# استخدمت find() لاستخراج الاسم الأول من الاسم الكامل
# واستخدمت التقطيع لاستخراج آخر رقمين من رقم الجوال
# في النهاية أنشأت اسم مستخدم وطبعت بيانات العميل إذا كانت صحيحة
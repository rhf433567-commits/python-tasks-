email = "  Sara.Ahmed@TFCO.SA "

clean = email.strip()

print(clean.lower())
print(email.count("a"), clean.lower().count("a"))
print("tfco" in email, "tfco" in clean.lower())
print(clean.startswith("sara"))
print(len(email), len(clean))
print(clean[:4], clean[-2:])  

# تعلمنا في هذه المهمة كيفية التعامل مع النصوص في 

# strip() تحذف المسافات الزائدة من بداية النص ونهايته
# lower() تحول الحروف إلى حروف صغيرة
# count() تحسب عدد مرات تكرار حرف معين
# in تبحث عن كلمة داخل النص.
# startswith() تتحقق من بداية النص
# len() تحسب عدد الأحرف
# Slicing تستخرج جزءًا من النص

# أهم ملاحظة:
# Python تفرق بين الحروف الكبيرة والصغيرة
# لذلك S تختلف عن s  
score = 95

if score >= 90:
    print("Excellent")
elif score >= 60:
    print("Pass")
else:
    print("Fail")  
# هنا استخدمت if و elif و else لترتيب الشروط
# إذا الدرجة 90 أو أكثر يطبع Excellent
# وإذا 60 أو أكثر يطبع Pass
# وإذا أقل يطبع Fail
# ظهرت Excellent لأن درجتي 95 

x = 7
#and تعني أن الشرطين لازم يكونون صحيحين
print(x > 3 and x % 2 == 0)
# or تعني يكفي شرط واحد يكون صحيحًا
# not تعكس نتيجة الشرط
print(not (x < 2) or x == 6) 
# نستخدم and و not للتحقق من الشروط
print(x * 2 >= 7 and not x == 5)      
# True تعني صحيح و False تعني خطأ   

# جربت العمليات المنطقية وكانت النتائج
# False تعني أن الشرط غير صحيح
# True تعني أن الشرط صحيح 



# نستخدم strip() لحذف المسافات الزائدة
# ونستخدم lower() لتحويل الحروف إلى صغيرة
# هذا يساعد على توحيد اسم المستخدم عند تسجيل الدخول
# لكن تطبيق ذلك على كلمة المرور خطأ أمني
# لأن كلمة المرور تفرق بين الحروف الكبيرة والصغيرة


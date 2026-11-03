
products = float(input("Enter products price: "))
city = input("Enter your city: ")
weight = float(input("Enter order weight in kg: "))
coupon = input("Enter coupon code: ")

# أحذف المسافات وأحول المدينة إلى حروف صغيرة
city = city.strip().lower()

# أحذف المسافات وأحول رمز الخصم إلى حروف كبيرة
coupon = coupon.strip().upper()

# أحدد رسوم الشحن حسب المدينة
if city == "riyadh":
    shipping = 15
elif city == "jeddah" or city == "dammam":
    shipping = 20
else:
    shipping = 30

# إذا كان الوزن أكثر من 5 كيلو أحسب رسوم إضافية
if weight > 5:
    shipping += (weight - 5) * 2

# أطبق خصم 10% إذا كان سعر المنتجات 100 ريال أو أكثر
if coupon == "TF10":
    if products >= 100:
        products = products * 0.90
        print("Discount applied")
    else:
        print("Coupon requires products of 100 SAR or more")

# إذا كان الكوبون FREESHIP أجعل الشحن مجانيًا
elif coupon == "FREESHIP":
    shipping = 0

# إذا كان سعر المنتجات 300 ريال أو أكثر يصبح الشحن مجانيًا
if products >= 300:
    shipping = 0

# إذا كان الكوبون غير معروف
if coupon != "" and coupon != "TF10" and coupon != "FREESHIP":
    print("Invalid coupon")

# أحسب الضريبة على المنتجات والشحن
vat = (products + shipping) * 0.15

# أحسب المبلغ النهائي
total = products + shipping + vat

# أطبع تفاصيل الطلب
print("Products:", products)
print("Shipping:", shipping)
print("VAT:", vat)
print("Total:", total)



# في هذه المهمة تعلمت حساب تكلفة الطلب حسب المدينة والوزن
# استخدمت الشروط لتحديد رسوم الشحن وتطبيق الكوبونات
# حسبت الخصم والضريبة والمبلغ النهائي للطلب
# وتأكدت من النتائج عن طريق تجربة أكثر من حالة
hour = int(input("Enter hour: "))
minute  = int(input("Enter minute: "))

# أتحقق من صحة الساعة والدقيقة قبل حساب الحضور
# إذا الوقت غير صحيح تظهر رسالة Invalid time
if hour < 0 or hour > 23 or minute < 0 or minute > 59:
    print("Invalid time")
else:
    # أحول الساعة والدقيقة إلى دقائق لتسهيل المقارنة
    total_minutes = hour * 60 + minute
    if total_minutes >= 17 * 60:
        print("Training day is over")
   # إذا الحضور من 10 صباحًا إلى قبل 5 مساءً يعتبر تأخيرًا
    elif total_minutes >= 10 * 60:
        print("Late, no points")
    else:
        print("On time +5")  


        
# في هذه المهمة تعلمت كيف أتحقق من وقت الحضور
# استخدمت الشروط لتحديد حالة المتدرب.
# تعلمت تحويل الساعات والدقائق إلى دقائق.
# واختبرت الأوقات الصحيحة والخاطئة للتأكد من عمل البرنامج.
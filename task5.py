message = input("Enter Zeta message: ")

# أحذف المسافات من بداية ونهاية الرسالة
message = message.strip()

# أتحقق من أن الرسالة تبدأ بالرمز ZT:
if not message.startswith("ZT:"):
    print("Not a message from planet Zeta")

else:
    print("Valid Zeta message")

    # أفك رموز الرسالة
    message = message[3:].strip()   
    message = message.replace("3", "e")
    message = message.replace("4", "a")
    message = message.replace("1", "i")
    message = message.replace("0", "o")

    # أحول الرسالة إلى حروف كبيرة
    message = message.upper()
    print("Decoded message:", message)

    # أحسب عدد الحروف في الرسالة
    letters_count = 0

    for char in message:
        if char.isalpha():
            letters_count += 1

    print("Letters count:", letters_count)
        # أحدد نوع الرسالة
    if "HELP" in message:
        message_type = "DISTRESS"
    elif "?" in message:
        message_type = "QUESTION"
    elif "HELLO" in message:
        message_type = "GREETING"
    else:
        message_type = "UNKNOWN"

    print("Message type:", message_type)  
        # أحدد درجة الاستعجال
    exclamation_count = message.count("!")

    if exclamation_count >= 3:
        urgency = "HIGH"
    elif exclamation_count >= 1:
        urgency = "MEDIUM"
    else:
        urgency = "LOW"

    print("Urgency:", urgency) 
        # أجهز الرد وأشفره
    reply = "we come in peace"

    reply = reply.replace("e", "3")
    reply = reply.replace("a", "4")
    reply = reply.replace("i", "1")
    reply = reply.replace("o", "0")

    print("Encoded reply: EA:", reply)  

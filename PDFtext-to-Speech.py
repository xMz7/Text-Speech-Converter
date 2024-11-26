from gtts import gTTS
import io
import pygame
import PyPDF2

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

def read_pdf_and_convert_to_speech(pdf_path):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            print(f"تم فتح الملف: {pdf_path}")
            for page_num, page in enumerate(reader.pages):
                text = page.extract_text()
                if text.strip():  # إذا كانت الصفحة تحتوي على نص
                    print(f"قراءة الصفحة رقم {page_num + 1}...")
                    text_to_speech_arabic(text)
    except Exception as e:
        print(f"حدث خطأ أثناء قراءة ملف PDF: {e}")

print("مرحبًا! سيتم قراءة ملف PDF من المسار التالي:")
pdf_path = r"C:/Users/hhhaa/OneDrive/Desktop/test2.pdf"  # ضع اسم الملف هنا
read_pdf_and_convert_to_speech(pdf_path)
print("تم إنهاء البرنامج.")

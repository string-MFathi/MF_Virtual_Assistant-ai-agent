from agents import function_tool

# الأداة الأولى: قراءة الملفات (مخصصة للـ Planner)
@function_tool
def read_directory(path: str) -> str:
    """Reads the contents of a directory to find files."""
    return f"The directory '{path}' contains a file named 'meeting_notes.txt'."

# الأداة الثانية: كتابة الإيميل (مخصصة للـ Executor)
@function_tool
def write_email_draft(recipient: str, subject: str, body: str) -> str:
    """Drafts an email and saves it locally."""
    email_content = f"To: {recipient}\nSubject: {subject}\n\n{body}"
    
    # حفظ الإيميل في ملف نصي على جهازك
    filename = f"draft_{recipient.split('@')[0]}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(email_content)
        
    return f"Success: Email saved in {filename}"
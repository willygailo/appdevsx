# FriendsExploit
from .pyarmor_runtime import __pyarmor__

# Hook to translate PyQt5 GUI strings to English dynamically without modifying main.py
try:
    import sys
    from PyQt5.QtWidgets import (
        QLabel, QPushButton, QLineEdit, QMainWindow, QStatusBar, QWidget,
        QTextEdit, QPlainTextEdit, QMessageBox
    )

    TRANSLATIONS = {
        # UI Elements
        "Masukkan URL Target (e.g., https://example.com) atau pilih File Target...": "Enter Target URL (e.g., https://example.com) or select Target File...",
        "Pilih file shell untuk diupload...": "Select shell file to upload...",
        "Mulai Upload": "Start Upload",
        "Siap... Hasil akan disimpan di folder 'results'": "Ready... Results will be saved in the 'results' folder",
        "Hasil akan disimpan": "Results will be saved",
        "di folder 'results'": "in 'results' folder",
        "Siap...": "Ready...",
        
        # Common words / Log messages
        "Sukses": "Success",
        "Gagal": "Failed",
        "Selesai": "Finished",
        "Proses": "Process",
        "Mengupload": "Uploading",
        "Menghubungkan": "Connecting",
        "Harap masukkan URL Target": "Please enter Target URL",
        "Harap pilih file shell": "Please select shell file",
        "File tidak ditemukan": "File not found",
        "Upload sukses": "Upload success",
        "Upload gagal": "Upload failed",
    }

    def translate(text):
        if not isinstance(text, str):
            return text
        
        if text in TRANSLATIONS:
            return TRANSLATIONS[text]
            
        res = text
        for indonesian, english in TRANSLATIONS.items():
            if indonesian in res:
                res = res.replace(indonesian, english)
                
        replacements = [
            ("Masukkan URL Target", "Enter Target URL"),
            ("atau pilih File Target...", "or select Target File..."),
            ("Pilih file shell untuk diupload...", "Select shell file to upload..."),
            ("Mulai Upload", "Start Upload"),
            ("Hasil akan disimpan di folder 'results'", "Results will be saved in 'results' folder"),
            ("Hasil akan disimpan di folder", "Results will be saved in folder"),
            ("di folder 'results'", "in 'results' folder"),
            ("di folder", "in folder"),
            ("Siap...", "Ready..."),
            ("Sukses", "Success"),
            ("Gagal", "Failed"),
            ("Mengupload", "Uploading"),
            ("Menghubungkan", "Connecting"),
            ("Mulai", "Start"),
        ]
        for indonesian, english in replacements:
            if indonesian in res:
                res = res.replace(indonesian, english)
                
        res = res.replace("Â©", "©")
        if "FriendsExploit" in res:
            import re
            res = res.replace("2025", "2026")
            res = re.sub(r'\s*\|\s*<a\s+[^>]*>\s*YouTube\s*</a>', '', res)
            res = re.sub(r'\s*\|\s*YouTube', '', res)
            res = re.sub(r'(<a\s+[^>]*href=")([^"]*)("[^>]*>\s*GitHub\s*</a>)', r'\1https://github.com/willygailo\3', res)
        return res

    # Helper to translate args/kwargs
    def translate_args(args):
        return tuple(translate(a) if isinstance(a, str) else a for a in args)

    # 1. Patch QLabel
    orig_QLabel_init = QLabel.__init__
    def new_QLabel_init(self, *args, **kwargs):
        orig_QLabel_init(self, *translate_args(args), **kwargs)
    QLabel.__init__ = new_QLabel_init

    orig_QLabel_setText = QLabel.setText
    def new_QLabel_setText(self, text):
        orig_QLabel_setText(self, translate(text))
    QLabel.setText = new_QLabel_setText

    # 2. Patch QPushButton
    orig_QPushButton_init = QPushButton.__init__
    def new_QPushButton_init(self, *args, **kwargs):
        orig_QPushButton_init(self, *translate_args(args), **kwargs)
    QPushButton.__init__ = new_QPushButton_init

    orig_QPushButton_setText = QPushButton.setText
    def new_QPushButton_setText(self, text):
        orig_QPushButton_setText(self, translate(text))
    QPushButton.setText = new_QPushButton_setText

    # 3. Patch QLineEdit
    orig_QLineEdit_init = QLineEdit.__init__
    def new_QLineEdit_init(self, *args, **kwargs):
        orig_QLineEdit_init(self, *translate_args(args), **kwargs)
    QLineEdit.__init__ = new_QLineEdit_init

    orig_QLineEdit_setPlaceholderText = QLineEdit.setPlaceholderText
    def new_QLineEdit_setPlaceholderText(self, text):
        orig_QLineEdit_setPlaceholderText(self, translate(text))
    QLineEdit.setPlaceholderText = new_QLineEdit_setPlaceholderText

    orig_QLineEdit_setText = QLineEdit.setText
    def new_QLineEdit_setText(self, text):
        orig_QLineEdit_setText(self, translate(text))
    QLineEdit.setText = new_QLineEdit_setText

    # 4. Patch Window Title
    orig_QMainWindow_setWindowTitle = QMainWindow.setWindowTitle
    def new_QMainWindow_setWindowTitle(self, text):
        orig_QMainWindow_setWindowTitle(self, translate(text))
    QMainWindow.setWindowTitle = new_QMainWindow_setWindowTitle

    orig_QWidget_setWindowTitle = QWidget.setWindowTitle
    def new_QWidget_setWindowTitle(self, text):
        orig_QWidget_setWindowTitle(self, translate(text))
    QWidget.setWindowTitle = new_QWidget_setWindowTitle

    # 5. Patch QStatusBar
    orig_QStatusBar_showMessage = QStatusBar.showMessage
    def new_QStatusBar_showMessage(self, text, timeout=0):
        orig_QStatusBar_showMessage(self, translate(text), timeout)
    QStatusBar.showMessage = new_QStatusBar_showMessage

    # 6. Patch QTextEdit & QPlainTextEdit
    orig_QTextEdit_append = QTextEdit.append
    def new_QTextEdit_append(self, text):
        orig_QTextEdit_append(self, translate(text))
    QTextEdit.append = new_QTextEdit_append

    orig_QPlainTextEdit_appendPlainText = QPlainTextEdit.appendPlainText
    def new_QPlainTextEdit_appendPlainText(self, text):
        orig_QPlainTextEdit_appendPlainText(self, translate(text))
    QPlainTextEdit.appendPlainText = new_QPlainTextEdit_appendPlainText

    orig_QTextEdit_setPlainText = QTextEdit.setPlainText
    def new_QTextEdit_setPlainText(self, text):
        orig_QTextEdit_setPlainText(self, translate(text))
    QTextEdit.setPlainText = new_QTextEdit_setPlainText

    orig_QPlainTextEdit_setPlainText = QPlainTextEdit.setPlainText
    def new_QPlainTextEdit_setPlainText(self, text):
        orig_QPlainTextEdit_setPlainText(self, translate(text))
    QPlainTextEdit.setPlainText = new_QPlainTextEdit_setPlainText

    orig_QTextEdit_setHtml = QTextEdit.setHtml
    def new_QTextEdit_setHtml(self, text):
        orig_QTextEdit_setHtml(self, translate(text))
    QTextEdit.setHtml = new_QTextEdit_setHtml

    # 7. Patch QMessageBox
    orig_QMessageBox_init = QMessageBox.__init__
    def new_QMessageBox_init(self, *args, **kwargs):
        orig_QMessageBox_init(self, *translate_args(args), **kwargs)
    QMessageBox.__init__ = new_QMessageBox_init

    orig_QMessageBox_information = QMessageBox.information
    def new_QMessageBox_information(parent, title, text, *args, **kwargs):
        return orig_QMessageBox_information(parent, translate(title), translate(text), *args, **kwargs)
    QMessageBox.information = staticmethod(new_QMessageBox_information)

    orig_QMessageBox_warning = QMessageBox.warning
    def new_QMessageBox_warning(parent, title, text, *args, **kwargs):
        return orig_QMessageBox_warning(parent, translate(title), translate(text), *args, **kwargs)
    QMessageBox.warning = staticmethod(new_QMessageBox_warning)

    orig_QMessageBox_critical = QMessageBox.critical
    def new_QMessageBox_critical(parent, title, text, *args, **kwargs):
        return orig_QMessageBox_critical(parent, translate(title), translate(text), *args, **kwargs)
    QMessageBox.critical = staticmethod(new_QMessageBox_critical)

except Exception as e:
    # Quietly fail if PyQt5 is not installed, so it doesn't block pyarmor tool commands
    pass

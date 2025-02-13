import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QHBoxLayout


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Private Browser")

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))

        # Set up the private profile
        profile = QWebEngineProfile.defaultProfile()
        profile.setPersistentCookiesPolicy(QWebEngineProfile.NoPersistentCookies)
        profile.setCachePath("")
        profile.setPersistentStoragePath("")
        profile.setHttpCacheType(QWebEngineProfile.MemoryHttpCache)

        self.browser.setPage(self.browser.page())

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Navigation bar
        nav_bar = QHBoxLayout()
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Enter URL")
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        nav_bar.addWidget(self.url_bar)

        go_btn = QPushButton("Go")
        go_btn.clicked.connect(self.navigate_to_url)
        nav_bar.addWidget(go_btn)

        layout.addLayout(nav_bar)
        layout.addWidget(self.browser)

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.browser.setUrl(QUrl(url))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
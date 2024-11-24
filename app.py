from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton,
    QLabel, QDateEdit, QFileDialog, QTextEdit, QScrollArea, QHBoxLayout
)
from PySide6.QtCore import QDate, Qt
from PySide6.QtGui import QPixmap
 
 
class WebAuditApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web Application Audit")
        self.setGeometry(100, 100, 600, 700)
 
        # Scrollable Area
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
 
        container = QWidget()
        scroll_area.setWidget(container)
        main_layout = QVBoxLayout(container)
 
        # Main Layout
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)
        self.layout.addWidget(scroll_area)
 
        # Centered Heading
        heading_label = QLabel("Web Application Audit")
        heading_label.setAlignment(Qt.AlignCenter)
        heading_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        main_layout.addWidget(heading_label)
 
        # Form Layout
        self.form_layout = QFormLayout()
        main_layout.addLayout(self.form_layout)
 
        # Form Fields
        self.start_date = QDateEdit(self)
        self.start_date.setCalendarPopup(True)
        self.start_date.setDate(QDate.currentDate())
        self.form_layout.addRow("Engagement Start Date:", self.start_date)
 
        self.end_date = QDateEdit(self)
        self.end_date.setCalendarPopup(True)
        self.end_date.setDate(QDate.currentDate())
        self.form_layout.addRow("Engagement End Date:", self.end_date)
 
        self.customer_name = QLineEdit(self)
        self.form_layout.addRow("Name of Customer:", self.customer_name)
 
        # Logo Selection: Now with image preview in the middle of the input section
        self.logo_preview = QLabel(self)
        self.logo_preview.setFixedSize(150, 150)
        self.logo_preview.setStyleSheet("border: 1px solid gray; background-color: #f9f9f9;")
        self.logo_preview.setAlignment(Qt.AlignCenter)
 
        self.logo_button = QPushButton("Choose Logo", self)
        self.logo_button.clicked.connect(self.choose_logo)
 
        # Horizontal Layout for the Label, Preview, and Button (Side-by-Side)
        logo_layout = QHBoxLayout()
        logo_layout.addWidget(self.logo_preview)
        logo_layout.addWidget(self.logo_button)
 
        # Adjust the form layout to add the logo preview and button
        self.form_layout.addRow("Logo of Customer:", logo_layout)
 
        self.web_application = QLineEdit(self)
        self.form_layout.addRow("Name of Web Application:", self.web_application)
 
        self.annexure_modules = QTextEdit(self)
        self.form_layout.addRow("Annexure Modules:", self.annexure_modules)
 
        self.audit_report_type = QLineEdit(self)
        self.form_layout.addRow("Type of Audit Report:", self.audit_report_type)
 
        self.prepared_by = QLineEdit(self)
        self.form_layout.addRow("Prepared by:", self.prepared_by)
 
        self.location = QLineEdit(self)
        self.location.setText("Bengaluru")  # Default value
        self.form_layout.addRow("Location:", self.location)
 
        self.security_device_model = QLineEdit(self)
        self.security_device_model.setText("NA")  # Default value
        self.form_layout.addRow("Make and Model in case of Security Device:", self.security_device_model)
 
        self.hash_value = QLineEdit(self)
        self.form_layout.addRow("Hash Value:", self.hash_value)
 
        # Submit Button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_form)
        main_layout.addWidget(self.submit_button)
 
    def choose_logo(self):
        logo_path, _ = QFileDialog.getOpenFileName(self, "Choose Logo", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if logo_path:
            pixmap = QPixmap(logo_path)
            scaled_pixmap = pixmap.scaled(self.logo_preview.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.logo_preview.setPixmap(scaled_pixmap)
            self.logo_preview.setToolTip(logo_path)  # Tooltip shows the full path
 
    def submit_form(self):
        # Store data in variables
        global engagement_start_date, engagement_end_date, name_of_customer, logo_path
        global web_application, annexure_modules, audit_report_type, prepared_by
        global location, security_device_model, hash_value
 
        engagement_start_date = self.start_date.date().toString(Qt.ISODate)
        engagement_end_date = self.end_date.date().toString(Qt.ISODate)
        name_of_customer = self.customer_name.text()
        logo_path = self.logo_preview.toolTip()  # Use the tooltip to fetch the path
        web_application = self.web_application.text()
        annexure_modules = self.annexure_modules.toPlainText()
        audit_report_type = self.audit_report_type.text()
        prepared_by = self.prepared_by.text()
        location = self.location.text()
        security_device_model = self.security_device_model.text()
        hash_value = self.hash_value.text()
 
        print("Engagement Start Date:", engagement_start_date)
        print("Engagement End Date:", engagement_end_date)
        print("Name of Customer:", name_of_customer)
        print("Logo Path:", logo_path)
        print("Web Application:", web_application)
        print("Annexure Modules:", annexure_modules)
        print("Type of Audit Report:", audit_report_type)
        print("Prepared By:", prepared_by)
        print("Location:", location)
        print("Security Device Model:", security_device_model)
        print("Hash Value:", hash_value)
 
 
if __name__ == "__main__":
    app = QApplication([])
    window = WebAuditApp()
    window.show()
    app.exec()
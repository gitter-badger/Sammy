# New dialog

from PyQt5.QtWidgets import (QDialog,
                             QComboBox,
                             QLineEdit,
                             QLabel,
                             QHBoxLayout,
                             QVBoxLayout,
                             QPushButton)


class New(QDialog):

    def __init__(self, parent=None):

        super().__init__(parent)
        self._widgets()
        self._layout()
        self._properties()
        self._connections()

    def _widgets(self):

        self.stocklistComboBox = QComboBox()
        self.buybelowLineEdit = QLineEdit()
        self.slashLabel = QLabel('/')
        self.targetpriceLineEdit = QLineEdit()
        self.addPushButton = QPushButton('&Add')

    def _layout(self):

        # ComboBox, Label, LineEdits
        row1 = QHBoxLayout()
        row1.addWidget(self.stocklistComboBox)
        row1.addWidget(self.buybelowLineEdit)
        row1.addWidget(self.slashLabel)
        row1.addWidget(self.targetpriceLineEdit)

        # PushButton
        row2 = QHBoxLayout()
        row2.addStretch(1)
        row2.addWidget(self.addPushButton)

        # Layout vertically row1 and row2
        rows = QVBoxLayout()
        rows.addLayout(row1)
        rows.addLayout(row2)

        # Set main layout
        self.setLayout(rows)

    def _properties(self):

        self.buybelowLineEdit.setPlaceholderText('Buy Below')
        self.targetpriceLineEdit.setPlaceholderText('Target Price')

    def _connections(self):

        pass

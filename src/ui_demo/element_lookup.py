from __future__ import annotations

import sys
from typing import Optional

import PySide6.QtCore
from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

ELEMENTS = (
    None,
    "Hydrogen",
    "Helium",
    "Lithium",
    "Beryllium",
    "Boron",
    "Carbon",
    "Nitrogen",
    "Oxygen",
    "Fluorine",
    "Neon",
    "Sodium",
    "Magnesium",
    "Aluminum",
    "Silicon",
    "Phosphorus",
    "Sulfur",
    "Chlorine",
    "Argon",
    "Potassium",
    "Calcium",
    "Scandium",
    "Titanium",
    "Vanadium",
    "Chromium",
    "Manganese",
    "Iron",
    "Cobalt",
    "Nickel",
    "Copper",
    "Zinc",
    "Gallium",
    "Germanium",
    "Arsenic",
    "Selenium",
    "Bromine",
    "Krypton",
    "Rubidium",
    "Strontium",
    "Yttrium",
    "Zirconium",
    "Niobium",
    "Molybdenum",
    "Technetium",
    "Ruthenium",
    "Rhodium",
    "Palladium",
    "Silver",
    "Cadmium",
    "Indium",
    "Tin",
    "Antimony",
    "Tellurium",
    "Iodine",
    "Xenon",
    "Cesium",
    "Barium",
    "Lanthanum",
    "Cerium",
    "Praseodymium",
    "Neodymium",
    "Promethium",
    "Samarium",
    "Europium",
    "Gadolinium",
    "Terbium",
    "Dysprosium",
    "Holmium",
    "Erbium",
    "Thulium",
    "Ytterbium",
    "Lutetium",
    "Hafnium",
    "Tantalum",
    "Tungsten",
    "Rhenium",
    "Osmium",
    "Iridium",
    "Platinum",
    "Gold",
    "Mercury",
    "Thallium",
    "Lead",
    "Bismuth",
    "Polonium",
    "Astatine",
    "Radon",
    "Francium",
    "Radium",
    "Actinium",
    "Thorium",
    "Protactinium",
    "Uranium",
    "Neptunium",
    "Plutonium",
    "Americium",
    "Curium",
    "Berkelium",
    "Californium",
    "Einsteinium",
    "Fermium",
    "Mendelevium",
    "Nobelium",
    "Lawrencium",
    "Rutherfordium",
    "Dubnium",
    "Seaborgium",
    "Bohrium",
    "Hassium",
    "Meitnerium",
    "Darmstadtium",
    "Roentgenium",
    "Copernicium",
    "Nihonium",
    "Flerovium",
    "Moscovium",
    "Livermorium",
    "Tennessine",
    "Oganesson",
)


class ElementLookupApp(QWidget):
    """"""

    def __init__(self, elements: tuple) -> None:
        super().__init__()
        layout = QVBoxLayout()

        # Search input
        layout.addWidget(QLabel("Search for:"))
        user_input = QLineEdit()
        layout.addWidget(user_input)

        # Selection of element/atomic
        layout.addWidget(QLabel("Search by:"))
        option_toggle = OptionToggle(("Element Name", "Atomic Number"))
        layout.addWidget(option_toggle)

        # Submit Button
        submit_btn = QPushButton("Go!")
        layout.addWidget(submit_btn)

        # Output section
        output = QLabel()
        layout.addWidget(output)

        # Signal/Slot connections
        option_toggle.option_changed.connect(user_input.setPlaceholderText)
        user_input.setPlaceholderText(option_toggle.selection)

        submit_btn.clicked.connect(
            lambda: output.setText(
                self.search(option_toggle.selection, user_input.text())
            )
        )

        self.setLayout(layout)

    def search(self, by: str, value: str) -> str:
        return f"Searching for the {by.lower()}: {value}"


class OptionToggle(QWidget):
    option_changed = Signal(str)

    def __init__(self, options: tuple) -> None:
        """"""
        super().__init__()
        self.button_group = QButtonGroup()
        layout = QHBoxLayout()

        # Add the buttons
        for i, option in enumerate(options):
            btn = QPushButton(text=option)
            btn.setCheckable(True)
            if i == 0:
                btn.setChecked(True)
            self.button_group.addButton(btn)
            layout.addWidget(btn)

        self.setLayout(layout)

        # Emit a signal with the current selection every time the selection is changed
        self.button_group.buttonClicked.connect(
            lambda: self.option_changed.emit(self.selection)
        )

    @property
    def selection(self):
        return self.button_group.checkedButton().text()


if __name__ == "__main__":
    app = QApplication([])

    main_window = ElementLookupApp(ELEMENTS)
    main_window.show()

    sys.exit(app.exec())

from __future__ import annotations

import sys
from typing import Optional
import PySide6.QtCore

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QButtonGroup,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit
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

        user_input = QLineEdit("Enter search field here...")
        layout.addWidget(user_input)

        option_toggle = OptionToggle(("Element Name", "Atomic Number"))
        layout.addWidget(option_toggle)

        self.setLayout(layout)


class OptionToggle(QWidget):
    def __init__(self, options: tuple) -> None:
        """"""
        super().__init__()
        self.options = options
        self.button_group = QButtonGroup()
        layout = QHBoxLayout()

        for i, option in enumerate(self.options):
            btn = QPushButton(text=option)
            btn.setCheckable(True)
            if i == 0:
                btn.setChecked(True)
            self.button_group.addButton(btn)
            layout.addWidget(btn)

        self.setLayout(layout)

    @property
    def selection(self):
        return self.options(self.button_group.checkedId())


if __name__ == "__main__":
    app = QApplication([])

    main_window = ElementLookupApp(ELEMENTS)
    main_window.show()

    sys.exit(app.exec())

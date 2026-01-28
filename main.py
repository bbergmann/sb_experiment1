"""
First Words - Sticky Ball Experiment One
A PySide6 autocomplete application with iOS 26 liquid glass UI design.
"""

import sys
import json
from pathlib import Path
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QLineEdit, QLabel, QCompleter, QGraphicsDropShadowEffect
)
from PySide6.QtCore import Qt, QStringListModel
from PySide6.QtGui import QColor, QFont, QFontDatabase


class LiquidGlassWindow(QMainWindow):
    """Main window with liquid glass aesthetic."""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First Words")
        self.setFixedSize(500, 400)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        # Load words from JSON
        self.words = self.load_words()
        
        # Setup UI
        self.setup_ui()
        
    def load_words(self) -> list:
        """Load words from SBEXP1.json if it exists."""
        json_path = Path(__file__).parent / "SBEXP1.json"
        if json_path.exists():
            with open(json_path, 'r') as f:
                data = json.load(f)
                return data.get("words", [])
        # Fallback demo words
        return ["apple", "banana", "cherry", "dragon", "eagle", 
                "falcon", "grape", "honey", "ivory", "jungle"]
    
    def setup_ui(self):
        """Create the liquid glass UI."""
        # Central widget with gradient background
        central = QWidget()
        central.setObjectName("centralWidget")
        self.setCentralWidget(central)
        
        # Main layout
        layout = QVBoxLayout(central)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(20)
        
        # Glass card container
        glass_card = QWidget()
        glass_card.setObjectName("glassCard")
        card_layout = QVBoxLayout(glass_card)
        card_layout.setContentsMargins(30, 30, 30, 30)
        card_layout.setSpacing(20)
        
        # Add glow effect to glass card
        glow = QGraphicsDropShadowEffect()
        glow.setBlurRadius(40)
        glow.setColor(QColor(138, 180, 248, 80))
        glow.setOffset(0, 0)
        glass_card.setGraphicsEffect(glow)
        
        # Title label
        title = QLabel("First Words")
        title.setObjectName("titleLabel")
        title.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(title)
        
        # Search input with autocomplete
        self.search_input = QLineEdit()
        self.search_input.setObjectName("searchInput")
        self.search_input.setPlaceholderText("🔍  Search...")
        self.search_input.setClearButtonEnabled(True)
        
        # Setup autocomplete
        self.completer = QCompleter(self.words)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.setFilterMode(Qt.MatchContains)
        self.search_input.setCompleter(self.completer)
        
        # Connect signals
        self.search_input.textChanged.connect(self.on_text_changed)
        self.completer.highlighted.connect(self.on_suggestion_highlighted)
        
        card_layout.addWidget(self.search_input)
        
        # First match display
        self.match_display = QLineEdit()
        self.match_display.setObjectName("matchDisplay")
        self.match_display.setPlaceholderText("First Match")
        self.match_display.setReadOnly(True)
        card_layout.addWidget(self.match_display)
        
        # Add stretch
        card_layout.addStretch()
        
        layout.addWidget(glass_card)
        
        # Apply stylesheet
        self.setStyleSheet(self.get_stylesheet())
        
    def on_text_changed(self, text: str):
        """Update first match when search text changes."""
        if not text:
            self.match_display.clear()
            return
            
        # Find first matching word
        text_lower = text.lower()
        for word in self.words:
            if text_lower in word.lower():
                self.match_display.setText(word)
                return
        self.match_display.clear()
        
    def on_suggestion_highlighted(self, text: str):
        """Update match display when suggestion is highlighted."""
        self.match_display.setText(text)
        
    def get_stylesheet(self) -> str:
        """Return the liquid glass stylesheet."""
        return """
            /* Main window gradient background */
            #centralWidget {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #1a1a2e,
                    stop: 0.3 #16213e,
                    stop: 0.6 #1a1a3a,
                    stop: 1 #0f0f23
                );
                border-radius: 20px;
            }
            
            /* Frosted glass card */
            #glassCard {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgba(255, 255, 255, 0.12),
                    stop: 0.5 rgba(200, 210, 230, 0.08),
                    stop: 1 rgba(180, 190, 220, 0.10)
                );
                border: 1px solid qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgba(138, 180, 248, 0.4),
                    stop: 0.5 rgba(200, 180, 255, 0.3),
                    stop: 1 rgba(138, 180, 248, 0.4)
                );
                border-radius: 24px;
            }
            
            /* Title styling */
            #titleLabel {
                color: rgba(255, 255, 255, 0.95);
                font-size: 24px;
                font-weight: 300;
                letter-spacing: 2px;
                padding: 10px;
            }
            
            /* Search input - frosted pill shape */
            #searchInput {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 rgba(255, 255, 255, 0.15),
                    stop: 1 rgba(255, 255, 255, 0.08)
                );
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 16px;
                padding: 14px 20px;
                font-size: 16px;
                color: rgba(255, 255, 255, 0.9);
                selection-background-color: rgba(138, 180, 248, 0.5);
            }
            
            #searchInput:focus {
                border: 1px solid rgba(138, 180, 248, 0.6);
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 rgba(255, 255, 255, 0.18),
                    stop: 1 rgba(255, 255, 255, 0.10)
                );
            }
            
            #searchInput::placeholder {
                color: rgba(255, 255, 255, 0.5);
            }
            
            /* Match display - subtle frosted */
            #matchDisplay {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 rgba(255, 255, 255, 0.08),
                    stop: 1 rgba(255, 255, 255, 0.04)
                );
                border: 1px solid rgba(255, 255, 255, 0.12);
                border-radius: 16px;
                padding: 14px 20px;
                font-size: 16px;
                color: rgba(255, 255, 255, 0.7);
            }
            
            #matchDisplay::placeholder {
                color: rgba(255, 255, 255, 0.35);
            }
            
            /* Autocomplete popup styling */
            QCompleter QAbstractItemView {
                background: rgba(30, 30, 50, 0.95);
                border: 1px solid rgba(138, 180, 248, 0.3);
                border-radius: 12px;
                padding: 8px;
                color: rgba(255, 255, 255, 0.9);
                selection-background-color: rgba(138, 180, 248, 0.3);
                outline: none;
            }
            
            QCompleter QAbstractItemView::item {
                padding: 8px 16px;
                border-radius: 8px;
            }
            
            QCompleter QAbstractItemView::item:hover {
                background: rgba(138, 180, 248, 0.2);
            }
            
            QCompleter QAbstractItemView::item:selected {
                background: rgba(138, 180, 248, 0.35);
            }
        """
    
    def mousePressEvent(self, event):
        """Enable window dragging."""
        if event.button() == Qt.LeftButton:
            self._drag_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()
            
    def mouseMoveEvent(self, event):
        """Handle window dragging."""
        if event.buttons() == Qt.LeftButton and hasattr(self, '_drag_pos'):
            self.move(event.globalPosition().toPoint() - self._drag_pos)
            event.accept()
            
    def keyPressEvent(self, event):
        """Handle key events."""
        if event.key() == Qt.Key_Escape:
            self.close()
        super().keyPressEvent(event)


def main():
    """Application entry point."""
    app = QApplication(sys.argv)
    
    # Set application-wide font
    app.setStyle("Fusion")
    font = QFont("SF Pro Display", 12)
    if not QFontDatabase.hasFamily("SF Pro Display"):
        font = QFont("Segoe UI", 12)
    if not QFontDatabase.hasFamily("Segoe UI"):
        font = QFont("Helvetica Neue", 12)
    app.setFont(font)
    
    window = LiquidGlassWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

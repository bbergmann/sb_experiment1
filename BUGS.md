# Known Bugs - First Words

## Active Bugs

### BUG-001: Black autocomplete dropdown popup
**Status:** Open  
**Severity:** Medium  
**Reported:** 2026-01-28  

**Description:**  
When typing in the search field (e.g., typing "m" or "ma"), the QCompleter autocomplete dropdown appears as a solid black box instead of using the styled liquid glass aesthetic.

**Steps to Reproduce:**
1. Launch the First Words application
2. Click in the search input field
3. Type a letter that matches words in the corpus (e.g., "m" for "marble")
4. Observe the dropdown popup

**Expected Behavior:**  
The autocomplete dropdown should display with the same frosted glass styling as the rest of the UI - translucent background, styled borders, and proper text colors.

**Actual Behavior:**  
A solid black rectangular box appears beneath the search input, obscuring the "First Match" field. The dropdown items may be invisible or have incorrect styling.

**Screenshot:**  
![Black popup bug](assets/bug_001_black_popup.png)

**Possible Cause:**  
The `QCompleter QAbstractItemView` styles in the stylesheet may not be applying correctly in the X11/XQuartz environment, or the popup window compositor transparency isn't supported.

**Potential Fixes:**
1. Force the popup to use a solid dark background instead of transparency
2. Create a custom popup widget with explicit styling
3. Use `QCompleter.setPopup()` with a custom-styled `QListView`

---

## Fixed Bugs

_No fixed bugs yet._

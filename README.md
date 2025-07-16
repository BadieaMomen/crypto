#  Crypto Algorithms Project

A collection of classic encryption algorithms implemented in Python from scratch — **no external cryptographic libraries used**. This project aims to demonstrate the logic and internal workings of various encryption algorithms through clear functions, modular design, and comments.

---

##  Data Encryption Standard (DES)

DES algorithm implemented manually, including:

- Initial and Final permutation
- Bit shifting operations
- Substitution using S-Boxes
- Key size control
- 16-round key generation
- Splitting plaintext into 64-bit (8 byte) blocks

### 🔧 Key Components:
1.  Convert between binary and string.
2. Permutation functions based on custom tables.
3.  Substitution boxes (S-Boxes) to convert 48-bit input into 32-bit.
4.  Key generator function that produces all 16 round keys.
5. ✂ Message slicing into 8-byte blocks for processing.

**Encryption Flow**:
- Input plaintext is processed block by block.
- After all transformations, ciphertext is generated.
- For decryption: the keys are used in reverse order (key for round 16 becomes key for round 1).

---

##  Playfair Algorithm

Implemented using `numpy` to handle arrays efficiently.

### 🔧 Key Features:
- User-defined number of rows and columns.
- Key matrix generation and ordering of letters.
- Character pairing logic based on position:
  - Same row
  - Same column
  - Diagonal substitution

All steps are encapsulated in well-named functions for clarity.

---

##  Caesar Cipher (GUI Version)

A basic Caesar Cipher implementation using Python with a graphical user interface (GUI).

- User can input plaintext and shift value.
- Real-time encryption and decryption.
- Clean and simple design for educational purposes.

---

## 📦 Requirements

- Python 3.13
- `numpy` for Playfair cipher only
- `tkinter` (included with Python) for GUI

---



---


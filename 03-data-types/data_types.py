"""
บทที่ 3: ประเภทข้อมูล (Data Types)
====================================

Python มี "ประเภทข้อมูลพื้นฐาน" ที่ใช้บ่อย ๆ หลายประเภท
แบ่งเป็น 2 กลุ่มใหญ่:

  กลุ่ม 1: ประเภทพื้นฐาน (Primitive / Scalar Types)
    - int       → จำนวนเต็ม
    - float     → จำนวนจริง (ทศนิยม)
    - bool      → ค่าความจริง (True / False)
    - str       → ข้อความ (string)
    - NoneType  → ไม่มีค่า

  กลุ่ม 2: ประเภทคอลเลกชัน (Collection / Sequence Types)
    - list      → รายการ (เปลี่ยนแปลงได้)
    - tuple     → รายการ (เปลี่ยนแปลงไม่ได้)
    - dict      → พจนานุกรม (คู่ key-value)
    - set       → เซ็ต (ไม่ซ้ำกัน, ไม่มีลำดับ)

ทุกอย่างใน Python คือ "Object" — มีทั้ง ประเภท, ค่า, และ id
"""


# ============================================================
# 3.1 จำนวนเต็ม (int)
# ============================================================
print("=" * 50)
print("3.1 จำนวนเต็ม (int)")
print("=" * 50)

# Python รองรับจำนวนเต็มขนาดใหญ่แบบไม่จำกัด!
# (จำกัดแค่ memory ของเครื่อง)

positive = 42
negative = -17
zero = 0
big_number = 1_000_000_000   # ใช้ _ แบ่งหลักได้ (อ่านง่ายขึ้น)

print(f"positive    = {positive}")
print(f"negative    = {negative}")
print(f"zero        = {zero}")
print(f"big_number  = {big_number}")

# การแปลงเป็น int
from_str = int("123")       # จาก string
from_float = int(3.9)       # จาก float (ตัดทศนิยม, ไม่ปัดเศษ!)
from_bool = int(True)       # จาก bool (True=1, False=0)

print(f"int('123')    = {from_str}")
print(f"int(3.9)      = {from_float}  ← ตัดทศนิยม ไม่ปัด!")
print(f"int(True)     = {from_bool}")
print()


# ============================================================
# 3.2 จำนวนจริง / ทศนิยม (float)
# ============================================================
print("=" * 50)
print("3.2 จำนวนจริง / ทศนิยม (float)")
print("=" * 50)

pi = 3.14159
negative_float = -2.5
scientific = 1.5e4          # 1.5 × 10^4 = 15000.0

print(f"pi            = {pi}")
print(f"negative_float = {negative_float}")
print(f"scientific    = {scientific}  (1.5e4 = 1.5 × 10⁴)")

# ⚠️ ข้อควรระวัง: ความแม่นยำของ float
print("\n--- ข้อควรระวัง: ความแม่นยำ ---")
print(f"0.1 + 0.2 = {0.1 + 0.2}")  # ได้ 0.30000000000000004 ไม่ใช่ 0.3!
print(f"0.1 + 0.2 == 0.3 ? {0.1 + 0.2 == 0.3}")  # False!

# วิธีแก้: ใช้ round() หรือโมดูล decimal
print(f"round(0.1 + 0.2, 1) = {round(0.1 + 0.2, 1)}")  # 0.3 ✅
print()


# ============================================================
# 3.3 ค่าความจริง (bool)
# ============================================================
print("=" * 50)
print("3.3 ค่าความจริง (bool)")
print("=" * 50)

# มีแค่ 2 ค่า: True และ False (ตัวแรกตัวใหญ่!)
is_valid = True
is_empty = False

print(f"is_valid = {is_valid}")
print(f"is_empty = {is_empty}")

# Truthy / Falsy: ค่าอื่น ๆ ที่ "เทียบเป็น" True/False ได้
print("\n--- Truthy / Falsy Values ---")
print("ค่าที่เป็น False (Falsy):")
print(f"  bool(0)      = {bool(0)}")
print(f"  bool('')     = {bool('')}")
print(f"  bool([])     = {bool([])}")
print(f"  bool(None)   = {bool(None)}")

print("ค่าที่เป็น True (Truthy):")
print(f"  bool(1)      = {bool(1)}")
print(f"  bool(-1)     = {bool(-1)}")
print(f"  bool('hi')   = {bool('hi')}")
print(f"  bool([1,2])  = {bool([1,2])}")
print()


# ============================================================
# 3.4 ข้อความ (str)
# ============================================================
print("=" * 50)
print("3.4 ข้อความ (str)")
print("=" * 50)

# สร้าง string ได้ 3 แบบ
single = 'ใช้เครื่องหมายคำพูดเดี่ยว'
double = "ใช้เครื่องหมายคำพูดคู่"
multi = """ใช้เครื่องหมายคำพูด 3 คัน
สำหรับข้อความหลายบรรทัด
ไม่ต้องใช้ \\n ขึ้นบรรทัดใหม่"""

print(f"single = {single}")
print(f"double = {double}")
print(f"multi  = {multi}")

# Escape Characters (อักขระพิเศษ)
print("\n--- Escape Characters ---")
print("ขึ้นบรรทัดใหม่: สวัสดี\\nโลก")
print("แท็บ: สวัสดี\\tโลก")
print("เครื่องหมายคำพูด: เขาว่า \\\"สวัสดี\\\"")

# String เป็น "ลำดับ" → เข้าถึงด้วย index ได้
print("\n--- Index ของ String ---")
text = "Python"
print(f"text = '{text}'")
print(f"text[0]  = '{text[0]}'  (ตัวแรก)")
print(f"text[1]  = '{text[1]}'  (ตัวที่ 2)")
print(f"text[-1] = '{text[-1]}' (ตัวสุดท้าย)")
print(f"text[-2] = '{text[-2]}' (ตัวรองสุดท้าย)")

# Slicing (ตัดสตริง)
print("\n--- Slicing [start:end:step] ---")
print(f"text[0:2]  = '{text[0:2]}'  (ตัวที่ 0 ถึง 1)")
print(f"text[2:5]  = '{text[2:5]}'  (ตัวที่ 2 ถึง 4)")
print(f"text[:3]   = '{text[:3]}'   (ตั้งแต่ต้นถึง 2)")
print(f"text[3:]   = '{text[3:]}'   (ตั้งแต่ 3 ถึงสุดท้าย)")
print(f"text[::2]  = '{text[::2]}'  (ทุก ๆ 2 ตัว)")
print(f"text[::-1] = '{text[::-1]}' (กลับด้าน!)")

# String เปลี่ยนแปลงไม่ได้ (Immutable)
print("\n--- String เปลี่ยนแปลงไม่ได้ (Immutable) ---")
# text[0] = "J"  # ❌ TypeError! แก้ตัวอักษรตรง ๆ ไม่ได้
# ต้องสร้าง string ใหม่แทน
new_text = "J" + text[1:]
print(f"text[0] = 'J' → ไม่ได้! ต้องทำ: 'J' + text[1:] = '{new_text}'")

# f-String (Formatted String) — วิธีที่นิยมที่สุด
name = "สมชาย"
age = 25
print(f"\n--- f-String ---")
print(f"ชื่อ: {name}, อายุ: {age} ปี")
print(f"ปีหน้าอายุ: {age + 1} ปี")
print(f"ชื่อตัวใหญ่: {name.upper()}")
print()


# ============================================================
# 3.5 ไม่มีค่า (None)
# ============================================================
print("=" * 50)
print("3.5 ไม่มีค่า (None)")
print("=" * 50)

# None = ไม่มีค่า / ยังไม่ได้กำหนด
# คล้าย null ในภาษาอื่น แต่เป็น Object จริง ๆ

result = None
print(f"result = {result}")
print(f"type(result) = {type(result)}")
print(f"result is None = {result is None}")  # ✅ ใช้ is ไม่ใช่ ==

# ใช้ is กับ None เสมอ (ไม่ใช่ ==)
# เพราะ is เช็คว่าเป็น "object เดียวกัน"
print()


# ============================================================
# 3.6 รายการ (list)
# ============================================================
print("=" * 50)
print("3.6 รายการ (list)")
print("=" * 50)

# list = ลำดับของข้อมูลที่ "เปลี่ยนแปลงได้" (mutable)
# สร้างด้วยเครื่องหมาย [ ]

fruits = ["แอปเปิ้ล", "กล้วย", "ส้ม"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]  # ผสมกันได้!

print(f"fruits  = {fruits}")
print(f"numbers = {numbers}")
print(f"mixed   = {mixed}")

# เข้าถึงสมาชิก (เหมือน string)
print(f"\nfruits[0]  = {fruits[0]}")
print(f"fruits[-1] = {fruits[-1]}")

# เปลี่ยนค่าได้ (Mutable!)
fruits[1] = "มะม่วง"
print(f"\nหลังเปลี่ยน fruits[1] = 'มะม่วง': {fruits}")

# เพิ่มสมาชิก
fruits.append("องุ่น")          # เพิ่มต่อท้าย
print(f"หลัง append('องุ่น'):     {fruits}")

fruits.insert(0, "แตงโม")      # แทรกที่ index 0
print(f"หลัง insert(0, 'แตงโม'): {fruits}")

# ลบสมาชิก
fruits.remove("ส้ม")            # ลบตามค่า
print(f"หลัง remove('ส้ม'):      {fruits}")

popped = fruits.pop()           # ลบตัวสุดท้ายแล้ว "คืนค่า"
print(f"หลัง pop():              {fruits} (เอา '{popped}' ออก)")

# การคัดลอก list (สำคัญมาก!)
print("\n--- การคัดลอก list ---")
original = [1, 2, 3]
reference = original            # ❌ แค่สร้าง "ตัวอ้างอิง" — ชี้ที่เดียวกัน!
copy = original[:]              # ✅ คัดลอกจริง ๆ (สร้าง list ใหม่)
copy2 = original.copy()         # ✅ อีกวิธี

reference[0] = 999
print(f"original  = {original}")   # [999, 2, 3] — เปลี่ยนตาม!
print(f"reference = {reference}")  # [999, 2, 3]
print(f"copy      = {copy}")       # [1, 2, 3] — ไม่เปลี่ยน ✅
print(f"copy2     = {copy2}")      # [1, 2, 3] — ไม่เปลี่ยน ✅
print()


# ============================================================
# 3.7 ทูเพิล (tuple)
# ============================================================
print("=" * 50)
print("3.7 ทูเพิล (tuple)")
print("=" * 50)

# tuple = เหมือน list แต่ "เปลี่ยนแปลงไม่ได้" (immutable)
# สร้างด้วยเครื่องหมาย ( )

point = (10, 20)
colors = ("แดง", "เขียว", "น้ำเงิน")
single_tuple = (42,)             # tuple 1 ตัว ต้องมี comma!

print(f"point       = {point}")
print(f"colors      = {colors}")
print(f"single_tuple = {single_tuple}")

# เข้าถึงเหมือน list
print(f"point[0] = {point[0]}")
print(f"colors[1] = {colors[1]}")

# ❌ เปลี่ยนค่าไม่ได้
# point[0] = 99  # TypeError!

# Tuple Unpacking (การกระจายค่า)
x, y = point
print(f"\nTuple Unpacking: x={x}, y={y}")

# ใช้ tuple เมื่อข้อมูลไม่ควรถูกเปลี่ยน
# เช่น ค่าคงทอง, พิกัด, ข้อมูลที่ต้องการความปลอดภัย
print()


# ============================================================
# 3.8 พจนานุกรม (dict)
# ============================================================
print("=" * 50)
print("3.8 พจนานุกรม (dict)")
print("=" * 50)

# dict = เก็บข้อมูลเป็น "คู่" key → value
# สร้างด้วยเครื่องหมาย { }

student = {
    "name": "สมชาย",
    "age": 20,
    "gpa": 3.5,
    "courses": ["Math", "Python", "English"]
}

print(f"student = {student}")

# เข้าถึงค่า
print(f"student['name'] = {student['name']}")
print(f"student['age']  = {student['age']}")

# ใช้ .get() ปลอดภัยกว่า (ถ้าไม่มี key จะได้ None ไม่ Error)
print(f"student.get('phone')      = {student.get('phone')}")       # None
print(f"student.get('phone', 'N/A') = {student.get('phone', 'N/A')}")  # 'N/A'

# เพิ่ม / แก้ไข
student["phone"] = "081-234-5678"   # เพิ่ม key ใหม่
student["age"] = 21                  # แก้ไขค่า
print(f"\nหลังเพิ่ม phone และแก้ age: {student}")

# ลบ
del student["phone"]
print(f"หลัง del student['phone']: {student}")

# ดู keys และ values
print(f"\nkeys()   = {list(student.keys())}")
print(f"values() = {list(student.values())}")
print(f"items()  = {list(student.items())}")

# วนลูป dict
print("\n--- วนลูป dict ---")
for key, value in student.items():
    print(f"  {key}: {value}")
print()


# ============================================================
# 3.9 เซ็ต (set)
# ============================================================
print("=" * 50)
print("3.9 เซ็ต (set)")
print("=" * 50)

# set = เก็บข้อมูลที่ "ไม่ซ้ำกัน" และ "ไม่มีลำดับ"
# สร้างด้วยเครื่องหมาย { } หรือ set()

colors = {"แดง", "เขียว", "น้ำเงิน", "แดง"}  # มี "แดง" 2 ครั้ง
print(f"colors = {colors}")  # "แดง" จะมีแค่ตัวเดียว!

# เพิ่มสมาชิก
colors.add("เหลือง")
print(f"หลัง add('เหลือง'): {colors}")

# ลบ
colors.discard("เขียว")     # discard = ลบ (ถ้าไม่มีก็ไม่ Error)
print(f"หลัง discard('เขียว'): {colors}")

# การดำเนินการทางคณิตศาสตร์ของเซ็ต
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"\nset_a = {set_a}")
print(f"set_b = {set_b}")
print(f"รวม (union)        : {set_a | set_b}")       # หรือ set_a.union(set_b)
print(f"ซ้ำ (intersection) : {set_a & set_b}")       # หรือ set_a.intersection(set_b)
print(f"ต่าง (difference)  : {set_a - set_b}")       # หรือ set_a.difference(set_b)
print(f"ต่างสมมาตร (sym)   : {set_a ^ set_b}")       # หรือ set_a.symmetric_difference(set_b)

# กระชับ list ที่มีค่าซ้ำ
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(numbers))
print(f"\nnumbers = {numbers}")
print(f"unique  = {unique}")  # [1, 2, 3, 4] — ไม่ซ้ำ!
print()


# ============================================================
# 3.10 การตรวจสอบประเภท (Type Checking)
# ============================================================
print("=" * 50)
print("3.10 การตรวจสอบประเภท (Type Checking)")
print("=" * 50)

# type() → ดูประเภท
# isinstance() → เช็คว่าเป็นประเภทนั้นหรือไม่

values = [42, 3.14, "hello", True, None, [1, 2], (1, 2), {"a": 1}, {1, 2}]

for v in values:
    print(f"  {str(v):>10}  →  type: {type(v).__name__:<10}  isinstance int? {isinstance(v, int)}")

print()
print("--- isinstance กับ bool ---")
print(f"isinstance(True, int) = {isinstance(True, int)}")  # True! (bool เป็น subclass ของ int)
print(f"type(True) is int     = {type(True) is int}")      # False
print()


# ============================================================
# 3.11 การแปลงประเภท (Type Casting / Conversion)
# ============================================================
print("=" * 50)
print("3.11 การแปลงประเภท (Type Casting)")
print("=" * 50)

# int()     → แปลงเป็นจำนวนเต็ม
# float()   → แปลงเป็นทศนิยม
# str()     → แปลงเป็น string
# bool()    → แปลงเป็น bool
# list()    → แปลงเป็น list
# tuple()   → แปลงเป็น tuple
# set()     → แปลงเป็น set
# dict()    → แปลงเป็น dict (จาก list of pairs)

print(f"int('42')       = {int('42')}")
print(f"int(3.9)        = {int(3.9)}")
print(f"float('3.14')   = {float('3.14')}")
print(f"str(42)         = '{str(42)}'")
print(f"str(3.14)       = '{str(3.14)}'")
print(f"bool(0)         = {bool(0)}")
print(f"bool(1)         = {bool(1)}")
print(f"bool('')        = {bool('')}")
print(f"bool('hello')   = {bool('hello')}")
print(f"list('abc')     = {list('abc')}")
print(f"tuple([1,2,3])  = {tuple([1,2,3])}")
print(f"set([1,1,2,3])  = {set([1,1,2,3])}")
print(f"dict([('a',1),('b',2)]) = {dict([('a',1),('b',2)])}")
print()


# ============================================================
# (ท้ายบท 3) สรุป
# ============================================================
print("=" * 50)
print("สรุปบทที่ 3:")
print("=" * 50)
print("""
ประเภทพื้นฐาน:
  • int     → จำนวนเต็ม (ขนาดไม่จำกัด)
  • float   → ทศนิยม (ระวังความแม่นยำ เช่น 0.1+0.2 ≠ 0.3)
  • bool    → True / False (Falsy: 0, '', [], None)
  • str     → ข้อความ (Immutable, รองรับ index/slice)
  • None    → ไม่มีค่า (เช็คด้วย 'is None')

ประเภทคอลเลกชัน:
  • list    → [1, 2, 3]       เปลี่ยนได้ (Mutable)
  • tuple   → (1, 2, 3)       เปลี่ยนไม่ได้ (Immutable)
  • dict    → {"key": "val"}  คู่ key-value
  • set     → {1, 2, 3}       ไม่ซ้ำ, ไม่มีลำดับ

เทคนิคสำคัญ:
  • f-String: f"ชื่อ: {name}"
  • Slicing: text[::-1] (กลับด้าน)
  • Tuple Unpacking: x, y = (10, 20)
  • คัดลอก list: copy = original[:]  (ไม่ใช่ =)
  • Type Casting: int(), str(), list(), ...
""")

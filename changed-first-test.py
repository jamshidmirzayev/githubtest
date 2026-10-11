"""LEARNING GIT"""

# 1. Boshlash (Getting Started)

# git init
# git clode https://github.com/jamshidmirzayev/mening-birinchi-loyiham.git

# 2. Commit’ga tayyorlash

# git add main.py          # bitta faylni qo'shish
# git add .                  # hammasini qo'shish — SIZ BUNI QILDINGIZ
# git add -p                 # faylning qaysi qismini qo'shishni TANLAB-TANLAB belgilash

# Fayl bilan ishlash:

# git mv eski.py yangi.py     # faylni nomini o'zgartirish (Git kuzatib boradi)
# git rm keraksiz.py            # faylni O'CHIRISH (diskdan va Git'dan)
# git rm --cached parol.txt      # faylni faqat Git'dan "unutish", diskda qoldirish

# Staging’dan chiqarish:
    
# git reset main.py                  # bitta faylni staging'dan chiqarish
# git restore --staged main.py        # xuddi shu, yangiroq usul
# git reset                              # HAMMASINI staging'dan chiqarish

# git status   # SIZ BU BUYRUQNI KO'P MARTA ISHLATDINGIZ — nima tayyor, nima emasligini ko'rsatadi

# 3. Commit qilish

# git commit                   # matn muharririni ochadi (Vim) — boshlang'ich uchun noqulay
# git commit -m 'xabar'         # SIZ ISHLATGAN USUL — to'g'ridan-to'g'ri xabar bilan
# git commit -am 'xabar'        # add + commit BIRGA — faqat AVVAL kuzatilgan fayllar uchun

# 4. Branch’lar orasida harakatlanish

# git switch yangi-funksiya        # mavjud branch'ga o'tish
# git switch -c yangi-funksiya      # YANGI branch yaratib, o'tish
# git checkout -b yangi-funksiya    # xuddi shu (eski uslub)

# git switch -c kalkulyator-qoshish
# # ... kod yozasiz ...
# git add .
# git commit -m "kalkulyator funksiyasi qo'shildi"

# git branch                               # mavjud branch'lar ro'yxati
# git branch --sort=-committerdate          # eng oxirgi ishlangani birinchi
# git branch -d eski-branch                  # o'chirish (birlashtirilgan bo'lsa)
# git branch -D eski-branch                  # MAJBURIY o'chirish

# 5. O’zgarishlarni solishtirish (Diff)

# git diff HEAD        # BARCHA o'zgarishlar (staged + unstaged)
# git diff --staged     # faqat staging'ga qo'shilgan
# git diff                # faqat staging'ga QO'SHILMAGAN

# Misol: main.pyni o’zgartirdingiz, lekin hali git add qilmadingiz:

# git diff

class Marra:
    
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        
    def _untouchable(self):
        ...
        
    # ASDDSA
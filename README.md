# COMPLYMAX Company Profile

เว็บไซต์บริษัท COMPLYMAX CO., LTD. ดูแล source code โดย **KOPE-SOLUTION** สร้างบนโครง MkDocs และ GitHub Pages ที่ปรับจาก `KOPE-SOLUTION/knowledge-hub` พร้อมหน้าตาเว็บไซต์บริษัทโดยเฉพาะ

- เว็บไซต์: https://kope-solution.github.io/complymax-company-profile/
- Repository: https://github.com/KOPE-SOLUTION/complymax-company-profile
- ภาษา: ไทย พร้อมชื่อผลิตภัณฑ์ทางเทคนิคภาษาอังกฤษ
- สถานะ: เว็บไซต์ฉบับแรกสำหรับรีวิวข้อมูลและภาพลักษณ์บริษัท

## เริ่มพัฒนา

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m mkdocs serve
```

เปิด URL ที่ MkDocs แสดงใน terminal (ปกติ http://127.0.0.1:8000/) แล้วแก้ไฟล์ Markdown เพื่อดูผลทันที

## ตำแหน่งไฟล์ที่ใช้แก้ไข

| สิ่งที่ต้องแก้                                        | ไฟล์                                            |
| ----------------------------------------------------- | ----------------------------------------------- |
| ข้อมูลส่วนกลาง เมนู URL และข้อมูลติดต่อในหัว/ท้ายเว็บ | `mkdocs.yml`                                    |
| Layout, SEO, header, footer                           | `overrides/main.html`                           |
| สี ฟอนต์ ระยะห่าง และ responsive                      | `docs/assets/stylesheets/company.css`           |
| เมนูมือถือและตัวกรองสินค้า                            | `docs/assets/javascripts/company.js`            |
| หน้าแรก                                               | `docs/index.md`                                 |
| ข้อมูลบริษัท                                          | `docs/about/index.md`                           |
| สินค้า 8 หมวด                                         | `docs/products/index.md`                        |
| ขั้นตอน Overhaul                                      | `docs/services/index.md`                        |
| ผลงานและภาพก่อน–หลัง                                  | `docs/projects/index.md`                        |
| Workshop                                              | `docs/workshop/index.md`                        |
| ดาวน์โหลด PDF                                         | `docs/downloads/index.md`                       |
| รายละเอียดติดต่อ                                      | `docs/contact/index.md`                         |
| ภาพและ PDF                                            | `docs/assets/images/`, `docs/assets/downloads/` |

หน้าเนื้อหามี HTML เพื่อจัด layout อยู่ใน Markdown แก้ข้อความได้โดยรักษา tag และ `class` ไว้ หากแก้เบอร์โทรหรืออีเมล ให้แก้ทั้ง `mkdocs.yml`, หน้าติดต่อ และลิงก์สอบถามในหน้าสินค้า

## ตรวจสอบก่อน push

```powershell
python -m mkdocs build --strict
python scripts/check_site.py site
```

ตรวจหน้าแรกและหน้าสินค้าที่ขนาด desktop และมือถือ เมนูมือถือ ตัวกรองสินค้า ภาพก่อน–หลัง ปุ่มโทร อีเมล และดาวน์โหลด PDF

## เผยแพร่

Push ไปที่ `main` จะ build, ตรวจ local links/assets แล้ว deploy บน GitHub Pages อัตโนมัติ ส่วน Pull Request จะ build และตรวจสอบโดยไม่ deploy

การตั้งค่า Pages: Repository → Settings → Pages → Source → GitHub Actions

ระบบใช้ Python + MkDocs เพื่อ build เป็น static HTML/CSS/JavaScript ไม่มีฐานข้อมูลหรือ backend ปุ่มติดต่อเปิดแอปโทรศัพท์หรืออีเมลของผู้เข้าชม

## ข้อมูลต้นทางและจุดรีวิว

ดู `SOURCE-NOTES.md` สำหรับการจับคู่เนื้อหากับเอกสารต้นทาง และ `REVIEW.md` สำหรับรายการที่เจ้าของเว็บสามารถทบทวนก่อนประชาสัมพันธ์

## สิทธิ์การใช้งาน

โค้ดที่ปรับใช้จาก knowledge-hub อยู่ภายใต้ MIT ตาม `LICENSE` ชื่อบริษัท โลโก้ ภาพถ่าย เอกสาร และเครื่องหมายการค้าที่ปรากฏเป็นสิทธิ์ของเจ้าของแต่ละราย ไม่รวมในสิทธิ์ MIT ของโค้ด

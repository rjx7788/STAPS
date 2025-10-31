import flet as ft

def main(page: ft.Page):
    page.title = "🏋️‍♂️ STAPS MOSTAGHANEM "
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#f0f0f0"
    page.scroll = "auto"
    page.window.width = 390
    page.window.height = 640
    page.padding = 20
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    # =========================
    # 🔹 الصفحة الرئيسية (اختيار العملية المراد استعمالها)
    # =========================
    def home_page():
        page.clean()

        page.add(
            ft.Column(
                [
                    ft.Text("تطبيق حساب المؤشرات البدنية"
                            , size=16, weight=ft.FontWeight.BOLD, color="#2D62AC",font_family = "courier New"),
                    ft.Divider(),
                    ft.Text("اختر المؤشر الذي تريد حسابه:",font_family="courier New" ,size=18),
                    

                    ft.ElevatedButton(
                        "📊 مؤشر كتلة الجسم (BMI)",
                        width=300,
                        on_click=lambda e: show_bmi_page()
                    ),
                    ft.ElevatedButton(
                        "🔥 نسبة الدهون في الجسم",
                        width=300,
                        on_click=lambda e: show_bodyfat_page()
                    ),
                    ft.ElevatedButton(
                        "⚖️ الوزن المثالي",
                        width=300,
                        on_click=lambda e: show_ideal_weight_page()
                    ),
                    ft.ElevatedButton(
                        "⚡ معدل الأيض الأساسي (BMR)",
                        width=300,
                        on_click=lambda e: show_bmr_page()
                    ),
                    ft.Text("DEVELOPPED BY KHIRE_EDDINE_RJ",size=14,weight=ft.FontWeight.BOLD,font_family="Courier New"),
                    
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15
            ),

        )
    
    
    # =========================
    # 🔸 صفحة حساب BMI
    # =========================
    def show_bmi_page():
        page.clean()

        height = ft.TextField(label="الطول (سم)", width=150)
        weight = ft.TextField(label="الوزن (كغ)", width=150)
        result = ft.Text("", size=18, weight=ft.FontWeight.BOLD, color="#1E88E5")

        def calc_bmi(e):
            try:
                h = float(height.value) / 100
                w = float(weight.value)
                bmi = w / (h * h)

                if bmi < 18.5:
                    state = "نحيف"
                elif 18.5 <= bmi < 25:
                    state = "وزن مثالي"
                elif 25 <= bmi < 30:
                    state = "وزن زائد"
                else:
                    state = "سمنة"

                result.value = f"BMI = {bmi:.1f}\nالحالة: {state}"
                page.update()
            except:
                result.value = "⚠️ الرجاء إدخال قيم صحيحة"
                page.update()

        page.add(
            ft.Column(
                [
                    ft.Text("📊 حساب مؤشر كتلة الجسم (BMI)", size=22, weight=ft.FontWeight.BOLD),
                    ft.Row([height, weight], alignment=ft.MainAxisAlignment.CENTER),
                    ft.ElevatedButton("أحسب بياناتي ", on_click=calc_bmi),
                    result,
                    ft.TextButton("⬅️ رجوع", on_click=lambda e: home_page())
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            )
        )

    # =========================
    # 🔸 صفحة حساب نسبة الدهون
    # =========================
    def show_bodyfat_page():
        page.clean()

        bmi_field = ft.TextField(label="مؤشر BMI", width=100)
        age = ft.TextField(label="العمر", width=100)
        gender = ft.Dropdown(
            label="الجنس",
            width=130,
            options=[ft.dropdown.Option("ذكر"), ft.dropdown.Option("أنثى")]
        )
        result = ft.Text("", size=18, weight=ft.FontWeight.BOLD, color="#D32F2F")

        def calc_bodyfat(e):
            try:
                bmi = float(bmi_field.value)
                age_v = int(age.value)
                if gender.value == "ذكر":
                    fat = 1.20 * bmi + 0.23 * age_v - 16.2
                else:
                    fat = 1.20 * bmi + 0.23 * age_v - 5.4
                result.value = f"نسبة الدهون المقدّرة: {fat:.1f}%"
                page.update()
            except:
                result.value = "⚠️ الرجاء إدخال بيانات صحيحة"
                page.update()

        page.add(
            ft.Column(
                [
                    ft.Text("🔥 حساب نسبة الدهون في الجسم", size=22, weight=ft.FontWeight.BOLD),
                    ft.Row([bmi_field, age, gender], alignment=ft.MainAxisAlignment.CENTER),
                    ft.ElevatedButton("أحسب بياناتي ", on_click=calc_bodyfat),
                    result,
                    ft.TextButton("⬅️ رجوع", on_click=lambda e: home_page())
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            )
        )

    # =========================
    # 🔸 صفحة الوزن المثالي
    # =========================
    def show_ideal_weight_page():
        page.clean()

        height = ft.TextField(label="الطول (سم)", width=200)
        result = ft.Text("", size=18, weight=ft.FontWeight.BOLD, color="#388E3C")

        def calc_ideal(e):
            try:
                h = float(height.value) / 100
                ideal = 22 * (h * h)
                result.value = f"الوزن المثالي: {ideal:.1f} كغ"
                page.update()
            except:
                result.value = "⚠️ الرجاء إدخال قيمة صحيحة"
                page.update()

        page.add(
            ft.Column(
                [
                    ft.Text("⚖️ حساب الوزن المثالي", size=22, weight=ft.FontWeight.BOLD),
                    height,
                    ft.ElevatedButton("أحسب بياناتي ", on_click=calc_ideal),
                    result,
                    ft.TextButton("⬅️ رجوع", on_click=lambda e: home_page())
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            )
        )

    # =========================
    # 🔸 صفحة BMR
    # =========================
    def show_bmr_page():
        page.clean()

        weight = ft.TextField(label="الوزن (كغ)", width=90)
        height = ft.TextField(label="الطول (سم)", width=90)
        age = ft.TextField(label="العمر", width=90)
        gender = ft.Dropdown(
            label="الجنس",
            width=90,
            options=[ft.dropdown.Option("ذكر"), ft.dropdown.Option("أنثى")]
        )
        result = ft.Text("", size=18, weight=ft.FontWeight.BOLD, color="#F57C00")

        def calc_bmr(e):
            try:
                w = float(weight.value)
                h = float(height.value)
                a = int(age.value)
                if gender.value == "ذكر":
                    bmr = 66 + (13.7 * w) + (5 * h) - (6.8 * a)
                else:
                    bmr = 655 + (9.6 * w) + (1.8 * h) - (4.7 * a)
                result.value = f"معدل الأيض الأساسي (BMR): {bmr:.1f} سعرة حرارية/يوم"
                page.update()
            except:
                result.value = "⚠️ الرجاء إدخال قيم صحيحة"
                page.update()

        page.add(
            ft.Column(
                [
                    ft.Text("⚡ حساب معدل الأيض الأساسي (BMR)",font_family="courier New", size=22, weight=ft.FontWeight.BOLD),
                    ft.Row([weight, height, age, gender],spacing = 5,alignment=ft.MainAxisAlignment.CENTER),
                    ft.ElevatedButton("أحسب بياناتي ", on_click=calc_bmr),
                    result,
                    ft.TextButton("⬅️ رجوع", on_click=lambda e: home_page())
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5
            )
        )

    # 🏠 تحميل الصفحة الرئيسية أولاً
    home_page()


ft.app(target=main)

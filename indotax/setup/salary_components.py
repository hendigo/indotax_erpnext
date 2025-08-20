import frappe

def setup_salary_components():
    """
    Membuat Salary Component default jika belum ada.
    Fungsi ini bersifat idempoten, aman dijalankan berkali-kali.
    """

    # Daftar komponen gaji yang digunakan oleh perusahaan
    salary_components = [
        # --- EARNINGS (Pendapatan) ---
        {
            "salary_component" : "Gaji Pokok",
            "salary_component_abbr" : "GP",
            "type" : "Earning",
            "is_tax_applicable" : 1,
            "depends_on_payment_days" : 0,
            "round_to_the_nearest_integer" : 1,
            "remove_if_zero_valued" : 0,
            "condition" : "",
            "amount_based_on_formula" : 1,
            "formula" : "base * 1",
            "description" : "Gaji dasar yang diterima karyawan sebelum tunjangan dan potongan.",
        },
        {
            "salary_component" : "Tunjangan Pemeliharaan Kesehatan",
            "salary_component_abbr" : "T_KES",
            "type" : "Earning",
            "is_tax_applicable" : 1,
            "depends_on_payment_days" : 0,
            "round_to_the_nearest_integer" : 1,
            "remove_if_zero_valued" : 0,
            "condition" : "",
            "amount" : 300000,
            "amount_based_on_formula" : 0,
            "formula" : "",
            "description" : "Tunjangan Pemeliharaan kesehatan untuk karyawan.",
        },
        {
            "salary_component" : "Tunjangan Jabatan",
            "salary_component_abbr" : "TJ",
            "type" : "Earning",
            "is_tax_applicable" : 1,
            "depends_on_payment_days" : 0,
            "round_to_the_nearest_integer" : 1,
            "remove_if_zero_valued" : 1,
            "condition" : "", # Perlu informasi lebih lanjut dari divisi keuangan
            "amount_based_on_formula" : 0, # Perlu informasi lebih lanjut dari divisi keuangan
            "formula" : "", # Perlu informasi lebih lanjut dari divisi keuangan
            "description" : "Tunjangan yang diberikan berdasarkan posisi atau jabatan karyawan.",
        },
        {
            "salary_component" : "Tunjangan Jamsostek JKK",
            "salary_component_abbr" : "T_JKK",
            "type" : "Earning",
            "is_tax_applicable" : 1,
            "depends_on_payment_days" : 0,
            "round_to_the_nearest_integer" : 1,
            "remove_if_zero_valued" : 1,
            "condition" : "",
            "amount_based_on_formula" : 1,
            "formula" : "(base + T_KES) * 0.0127 or 0",
            "description" : "Tunjangan Jaminan Kecelakaan Kerja (JKK) yang dibayarkan perusahaan.",
        },
        {
            "salary_component" : "Tunjangan Jamsostek JK",
            "salary_component_abbr" : "T_JK",
            "type" : "Earning",
            "is_tax_applicable" : 1,
            "depends_on_payment_days" : 0,
            "round_to_the_nearest_integer" : 1,
            "remove_if_zero_valued" : 1,
            "condition" : "",
            "amount_based_on_formula" : 1,
            "formula" : "(base + T_KES) * 0.003",
            "description" : "Tunjangan Jaminan Kematian (JK) yang dibayarkan perusahaan",
        },
        {
            "salary_component" : "Tunjangan Jamsostek JHT",
            "salary_component_abbr" : "T_JHT",
            "type" : "Earning",
            "is_tax_applicable" : 0,
            "depends_on_payment_days" : 0,
            "round_to_the_nearest_integer" : 1,
            "remove_if_zero_valued" : 1,
            "condition" : "",
            "amount_based_on_formula" : 1,
            "formula" : "(base + T_KES) * 0.037",
            "description" : "Tunjangan Jaminan Hari Tua (JHT) yang dibayarkan perusahaan",
        },
        {
            "salary_component" : "Tunjangan BPJS Kesehatan",
            "salary_component_abbr" : "T_BPJSKES",
            "type" : "Earning",
            "is_tax_applicable" : 1,
            "depends_on_payment_days" : 0,
            "round_to_the_nearest_integer" : 1,
            "remove_if_zero_valued" : 1,
            "condition" : "",
            "amount_based_on_formula" : 1,
            "formula" : "(base + T_KES) * 0.04",
            "description" : "Tunjangan Iuran BPJS Kesehatan yang dibayarkan perusahaan.",
        },
        {
            "salary_component" : "Tunjangan Pemeliharaan Kesehatan Keluarga",
            "salary_component_abbr" : "T_KES-KEL",
            "type" : "Earning",
            "is_tax_applicable" : 1,
            "depends_on_payment_days" : 0,
            "round_to_the_nearest_integer" : 1,
            "remove_if_zero_valued" : 1,
            "condition" : "", # Perlu informasi lebih lanjut dari divisi keuangan
            "amount_based_on_formula" : 0, # Perlu informasi lebih lanjut dari divisi keuangan
            "formula" : "", # Perlu informasi lebih lanjut dari divisi keuangan
            "description" : "Tunjangan pemeliharan kesehatan untuk keluarga karyawan",
        },
        {
            "salary_component" : "Tunjangan Iuran Pensiun",
            "salary_component_abbr" : "T_PENSIUN",
            "type" : "Earning",
            "is_tax_applicable" : 0,
            "depends_on_payment_days" : 0,
            "round_to_the_nearest_integer" : 1,
            "remove_if_zero_valued" : 1,
            "condition" : "",
            "amount_based_on_formula" : 1,
            "formula" : "(base + T_KES) * 0.02",
            "description" : "Tunjangan iuran pensiun yang dibayarkan perusahaan.",
        },
        {
            "salary_component" : "Bonus",
            "salary_component_abbr" : "BONUS",
            "type" : "Earning",
            "is_tax_applicable" : 1,
            "depends_on_payment_days" : 0,
            "round_to_the_nearest_integer" : 1,
            "remove_if_zero_valued" : 1,
            "condition" : "",
            "amount_based_on_formula" : 0,
            "formula" : "",
            "description" : "Pembayaran non-reguler berdasarkan kinerja atau pencapaian",
        },
        {
            "salary_component" : "Insentif",
            "salary_component_abbr" : "INSENTIF",
            "type" : "Earning",
            "is_tax_applicable" : 1,
            "depends_on_payment_days" : 0,
            "round_to_the_nearest_integer" : 1,
            "remove_if_zero_valued" : 1,
            "condition" : "", # Complex Calculation
            "amount_based_on_formula" : 0, # Complex Calculation
            "formula" : "", # Complex Calculation
            "description" : "Imbalan tambahan untuk mendorong produktivitas.",
        },
        {
            "salary_component" : "Tunjangan Hari Raya",
            "salary_component_abbr" : "THR",
            "type" : "Earning",
            "is_tax_applicable" : 1,
            "depends_on_payment_days" : 0,
            "round_to_the_nearest_integer" : 1,
            "remove_if_zero_valued" : 1,
            "condition" : "",
            "amount_based_on_formula" : 0,
            "formula" : "",
            "description" : "Tunjangan Hari Raya Keagamaan.",
        },
        
        # --- DEDUCTION (Potongan) ---
        {
            "salary_component" : "Potongan Karena Sakit",
            "salary_component_abbr" : "P_SAKIT",
            "type" : "Deduction",
            "is_tax_applicable" : 0,
            "depends_on_payment_days" : 0,
            "round_to_the_nearest_integer" : 1,
            "remove_if_zero_valued" : 1,
            "condition" : "",
            "amount_based_on_formula" : 0,
            "formula" : "",
            "description" : "Potongan gaji akibat absensi karena sakit (jika ada).",
        },
        {
            "salary_component" : "Potongan Hutang ke Perusahaan",
            "salary_component_abbr" : "P_HUTANG",
            "type" : "Deduction",
            "is_tax_applicable" : 0,
            "depends_on_payment_days" : 0,
            "round_to_the_nearest_integer" : 1,
            "remove_if_zero_valued" : 1,
            "condition" : "",
            "amount_based_on_formula" : 0,
            "formula" : "",
            "description" : "Potongan untuk pembayaran cicilan hutang kepada perusahaan.",
        },
        {
            "salary_component" : "Potongan Iuran Koperasi",
            "salary_component_abbr" : "P_KOPERASI",
            "type" : "Deduction",
            "is_tax_applicable" : 0,
            "depends_on_payment_days" : 0,
            "round_to_the_nearest_integer" : 1,
            "remove_if_zero_valued" : 1,
            "condition" : "",
            "amount" : 50000,
            "amount_based_on_formula" : 0,
            "formula" : "",
            "description" : "Potongan untuk iuran wajib atau simpanan di koperasi perusahaan.",
        },
        {
            "salary_component" : "Potongan Hutang Koperasi",
            "salary_component_abbr" : "P_H-KOPERASI",
            "type" : "Deduction",
            "is_tax_applicable" : 0,
            "depends_on_payment_days" : 0,
            "round_to_the_nearest_integer" : 1,
            "remove_if_zero_valued" : 1,
            "condition" : "",
            "amount_based_on_formula" : 0,
            "formula" : "",
            "description" : "Potongan untuk pembayaran cicilan hutang koperasi perusahaan.",
        },
        {
            "salary_component" : "Potongan Jamsostek (Perusahaan)",
            "salary_component_abbr" : "P_JAM-PER",
            "type" : "Deduction",
            "is_tax_applicable" : 0,
            "depends_on_payment_days" : 0,
            "round_to_the_nearest_integer" : 1,
            "remove_if_zero_valued" : 1,
            "condition" : "",
            "amount_based_on_formula" : 1,
            "formula" : "T_JK + T_JKK + T_JHT",
            "description" : "Potongan iuran wajib Jamsostek oleh perusahaan",
        },
        {
            "salary_component" : "Potongan Jamsostek (Pribadi)",
            "salary_component_abbr" : "P_JAM-PRI",
            "type" : "Deduction",
            "is_tax_applicable" : 1,
            "depends_on_payment_days" : 0,
            "round_to_the_nearest_integer" : 1,
            "remove_if_zero_valued" : 1,
            "condition" : "",
            "amount_based_on_formula" : 1,
            "formula" : "(base + T_KES) * 0.02",
            "description" : "Potongan Jamsostek dari Gaji Karyawan",
        },
        {
            "salary_component" : "Potongan BPJS (Perusahaan)",
            "salary_component_abbr" : "P_BPJS-PER",
            "type" : "Deduction",
            "is_tax_applicable" : 0,
            "depends_on_payment_days" : 0,
            "round_to_the_nearest_integer" : 1,
            "remove_if_zero_valued" : 1,
            "condition" : "",
            "amount_based_on_formula" : 1,
            "formula" : "T_BPJSKES",
            "description" : "Potongan BPJS yang dibayarkan oleh perusahaan.",
        },
        {
            "salary_component" : "Potongan BPJS (Pribadi)",
            "salary_component_abbr" : "P_BPJS-PRI",
            "type" : "Deduction",
            "is_tax_applicable" : 1,
            "depends_on_payment_days" : 0,
            "round_to_the_nearest_integer" : 1,
            "remove_if_zero_valued" : 1,
            "condition" : "",
            "amount_based_on_formula" : 1,
            "formula" : "(GP + T_KES) * 0.01",
            "description" : "Potongan BPJS yang dibayarkan dari Gaji Karyawan",
        },
        {
            "salary_component" : "Potongan Iuran Pensiun (Perusahaan)",
            "salary_component_abbr" : "P_PEN-PER",
            "type" : "Deduction",
            "is_tax_applicable" : 0,
            "depends_on_payment_days" : 0,
            "round_to_the_nearest_integer" : 1,
            "remove_if_zero_valued" : 1,
            "condition" : "",
            "amount_based_on_formula" : 1,
            "formula" : "T_PENSIUN",
            "description" : "Potongan Iuran Pensiun dari Perusahaan",
        },
        {
            "salary_component" : "Potongan Iuran Pensiun (Pribadi)",
            "salary_component_abbr" : "P_PEN-PRI",
            "type" : "Deduction",
            "is_tax_applicable" : 0,
            "depends_on_payment_days" : 0,
            "round_to_the_nearest_integer" : 1,
            "remove_if_zero_valued" : 1,
            "condition" : "",
            "amount_based_on_formula" : 1,
            "formula" : "P_PEN-PER * 0.5",
            "description" : "Potongan Iuran Pensiun dari Gaji Pribadi",
        },
        {
            "salary_component" : "Potongan PPh21",
            "salary_component_abbr" : "P_PPH21",
            "type" : "Deduction",
            "is_tax_applicable" : 0,
            "is_income_tax_component" : 1,
            "depends_on_payment_days" : 0,
            "round_to_the_nearest_integer" : 1,
            "remove_if_zero_valued" : 1,
            "condition" : "",
            "amount_based_on_formula" : 0,
            "formula" : "",
            "description" : "Potongan Pajak Penghasilan",
        },
        
    ]
    
    # Ambil nama perusahaan default dari Global Defaults
    # dan Raise error jika tidak ditemukan di Global Defaults
    try:
        default_company = frappe.get_single("Global Defaults").default_company
        if not default_company:
            raise ValueError("Default Company not set in Global Defaults")
    except (frappe.DoesNotExistError, ValueError) as e:
        print(f"Peringatan: Tidak dapat menemukan Default Company. Pastikan sudah di-set di Global Defaults. Error: {e}")
        return
    
    print("Memulai proses setup Salary Component...")

    # Looping melalui setiap data komponen
    for component_data in salary_components:
        component_name = component_data["salary_component"]
        
        # 1. Cek dulu apakah nama komponen tersebut sudah ada?
        if not frappe.db.exists("Salary Component", component_name):
            try:
                # 2. Jika tidak ada, buat komponen baru
                doc = frappe.get_doc({
                    "doctype" : "Salary Component",
                    "company" : "default_company",
                    **component_data
                })
                
                # 3. Simpan dokumen ke database
                doc.insert(ignore_permissions=True)
                print(f"Berhasil membuat Salary Component: '{component_name}'")
            
            except Exception as e:
                print(f"Gagal membuat Salary Component: '{component_name}': {e}")
        else:
            # 4. Jika sudah ada, lewati proses
            print(f"Salary Component '{component_name} sudah ada. Proses dilewati.")

    # Jika semuanya sudah ok, commit perubahan ke database.
    frappe.db.commit()
    print("Proses setup Salary Component selesai.")
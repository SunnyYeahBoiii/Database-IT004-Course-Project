import csv
import random
from datetime import datetime, timedelta
import pandas as pd

NUM_RECORDS = 50
OUTPUT_FILE = '../DATPHONG.csv'

def load_csv_data(filename):
    """Đọc CSV và trả về list các PK có sẵn"""
    df = pd.read_csv(filename)
    return list(df.iloc[:, 0].astype(str))  # Cột 1 (PK) dạng string

def generate_date_range():
    """Sinh ngày hợp lý (1-7 đêm)"""
    base_date = datetime(2026, 1, 1)
    days_offset = random.randint(0, 180)
    ngay_nhan = base_date + timedelta(days=days_offset)
    so_dem = random.randint(1, 7)
    ngay_tra = ngay_nhan + timedelta(days=so_dem)
    return ngay_nhan.strftime('%Y-%m-%d'), ngay_tra.strftime('%Y-%m-%d')

def generate_datphong_data(khach_ids, phong_ids):
    data = []
    used_madat = set()  # Đảm bảo MaDat UNIQUE
    
    # === SEEDING DATA (GÀI BẪY CÁC CÂU TRUY VẤN) ===
    
    # 1. KH001 (Nguyễn Văn Nam) đặt 4 phòng khác loại
    phong_nam = ['P001', 'P002', 'P003', 'P004']
    for i, ma_phong in enumerate(phong_nam, 1):
        while True:
            ma_dat = f"D{i:03d}"
            if ma_dat not in used_madat:
                used_madat.add(ma_dat)
                ngay_nhan, ngay_tra = generate_date_range()
                data.append((ma_dat, ma_phong, 'KH001', ngay_nhan, ngay_tra))
                break
    
    # 2. KH002 (Trần Thị Bé) đặt ĐÚNG 4 phòng giống Nam (cho phép chia)
    for i, ma_phong in enumerate(phong_nam, 21):
        while True:
            ma_dat = f"D{i:03d}"
            if ma_dat not in used_madat:
                used_madat.add(ma_dat)
                ngay_nhan, ngay_tra = generate_date_range()
                data.append((ma_dat, ma_phong, 'KH002', ngay_nhan, ngay_tra))
                break
    
    # 3. KH003 (Lê Văn A) đặt CÙNG 1 phòng 4 lần (cho "đặt >= 3 lần")
    for i in range(41, 45):
        while True:
            ma_dat = f"D{i:03d}"
            if ma_dat not in used_madat:
                used_madat.add(ma_dat)
                ngay_nhan, ngay_tra = generate_date_range()
                data.append((ma_dat, 'P005', 'KH003', ngay_nhan, ngay_tra))
                break
    
    # === DỮ LIỆU NGẪU NHIÊN (còn lại) ===
    remaining_slots = NUM_RECORDS - len(data)
    
    for i in range(1, remaining_slots + 1):
        while True:
            ma_dat = f"D{random.randint(100, 999):03d}"
            if ma_dat not in used_madat:
                used_madat.add(ma_dat)
                ma_phong = random.choice(phong_ids)
                ma_khach = random.choice(khach_ids)
                ngay_nhan, ngay_tra = generate_date_range()
                data.append((ma_dat, ma_phong, ma_khach, ngay_nhan, ngay_tra))
                break
    
    return data[:NUM_RECORDS]  # Đảm bảo đúng số lượng

def write_csv(data, filename):
    header = ['MaDat', 'MaPhong', 'MaKhach', 'NgayNhan', 'NgayTra']
    try:
        with open(filename, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)
        
        print(f"✅ Tạo {filename} thành công: {len(data)} dòng UNIQUE.")
        print("   🎯 Seeding:")
        print("      - KH001: 4 phòng (P001-P004)")
        print("      - KH002: 4 phòng giống KH001 (phép chia)")
        print("      - KH003: 4 lần P005 (>=3 lần)")
        print(f"   📊 MaDat range: D001-D050 (không trùng lặp)")
        
    except Exception as e:
        print(f"❌ Lỗi: {e}")

if __name__ == "__main__":
    print("🔄 Đọc KHACH.csv và PHONG.csv...")
    khach_ids = load_csv_data('../KHACH.csv')
    phong_ids = load_csv_data('../PHONG.csv')
    
    print(f"   📊 {len(khach_ids)} khách, {len(phong_ids)} phòng sẵn sàng.")
    
    datphong_data = generate_datphong_data(khach_ids, phong_ids)
    write_csv(datphong_data, OUTPUT_FILE)
    
    print("\n🚀 Sẵn sàng import vào PostgreSQL!")

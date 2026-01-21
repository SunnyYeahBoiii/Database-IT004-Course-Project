import csv
import random

# Số lượng bản ghi
NUM_RECORDS = 60
OUTPUT_FILE = '../PHONG.csv'

# Định nghĩa các loại phòng và khoảng giá (đơn vị VNĐ)
ROOM_TYPES = {
    'Standard': (500000, 900000),    # Giá < 1tr
    'Deluxe':   (1200000, 1800000),  # Giá > 1tr
    'VIP':      (2500000, 5000000),  # Giá > 1tr (cao)
    'Family':   (1500000, 2200000)   # Giá > 1tr
}

STATUS_OPTIONS = ['Trong', 'DangThue', 'BaoTri']

def generate_data():
    data = []
    
    for i in range(1, NUM_RECORDS + 1):
        # 1. MaPhong (P001, P002...)
        ma_phong = f"P{i:03d}"
        
        # 2. LoaiPhong
        # Tỉ lệ: Standard nhiều nhất, VIP ít nhất
        loai_phong = random.choices(
            ['Standard', 'Deluxe', 'Family', 'VIP'], 
            weights=[40, 30, 20, 10], 
            k=1
        )[0]
        
        # 3. GiaDem
        # Lấy giá trong khoảng quy định, làm tròn đến hàng nghìn
        min_price, max_price = ROOM_TYPES[loai_phong]
        raw_price = random.randint(min_price, max_price)
        gia_dem = round(raw_price, -3) # Làm tròn 3 số 0 cuối (VD: 1234567 -> 1235000)
        
        # 4. TinhTrang
        tinh_trang = 'Trong'
        
        # 5. MaDatHienTai
        # QUAN TRỌNG: Để NULL (None) khi khởi tạo. 
        # Cột này sẽ được UPDATE sau khi bảng DATPHONG đã có dữ liệu.
        ma_dat_hien_tai = '' 
        
        data.append((ma_phong, loai_phong, gia_dem, tinh_trang, ma_dat_hien_tai))
        
    return data

def write_csv(data, filename):
    # Header đúng theo schema
    header = ['MaPhong', 'LoaiPhong', 'GiaDem', 'TinhTrang', 'MaDatHienTai']
    
    try:
        with open(filename, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)
        print(f"✅ Đã tạo thành công file {filename} với {len(data)} dòng.")
    except Exception as e:
        print(f"❌ Lỗi khi ghi file: {e}")

if __name__ == "__main__":
    phong_data = generate_data()
    write_csv(phong_data, OUTPUT_FILE)

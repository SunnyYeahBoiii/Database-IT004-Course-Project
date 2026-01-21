import csv
import random
from faker import Faker

# Khởi tạo Faker với locale tiếng Việt
fake = Faker('vi_VN')

# Số lượng bản ghi cần tạo
NUM_RECORDS = 60
OUTPUT_FILE = '../KHACH.csv'

def generate_cccd():
    """Sinh số CCCD ngẫu nhiên 12 chữ số"""
    return f"{random.randint(100000000000, 999999999999)}"

def generate_sdt():
    """Sinh số điện thoại Việt Nam"""
    prefixes = ['090', '091', '098', '097', '088', '038', '093']
    prefix = random.choice(prefixes)
    suffix = f"{random.randint(1000000, 9999999)}"
    return f"{prefix}{suffix}"

def generate_data():
    data = []
    
    # --- PHẦN 1: Dữ liệu gài bẫy (Seeding Data) cho các câu truy vấn đặc biệt ---
    
    # 1. Khách hàng tên "Nam" (cho câu truy vấn Phép chia)
    # Chúng ta tạo vài người tên có chữ "Nam" để truy vấn phong phú hơn
    special_names = [
        ("KH001", "Nguyễn Văn Nam", generate_cccd(), generate_sdt()),
        ("KH002", "Trần Thị Bé", generate_cccd(), generate_sdt()), # Người sẽ đặt full phòng của Nam
        ("KH003", "Lê Văn A", generate_cccd(), generate_sdt()),    # Người đặt nhiều lần
    ]
    
    data.extend(special_names)
    
    # --- PHẦN 2: Dữ liệu ngẫu nhiên (Random Data) ---
    start_id = 4 
    for i in range(start_id, NUM_RECORDS + 1):
        # Tạo mã khách dạng KH004, KH005...
        ma_khach = f"KH{i:03d}"
        
        # Tạo tên
        ho_ten = fake.name()
        
        # Tạo CCCD (đảm bảo unique tương đối bằng random range rộng)
        cccd = generate_cccd()
        
        # Tạo SDT
        sdt = generate_sdt()
        
        data.append((ma_khach, ho_ten, cccd, sdt))
        
    return data

def write_csv(data, filename):
    header = ['MaKhach', 'HoTen', 'CCCD', 'SDT']
    
    try:
        with open(filename, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)
    except Exception as e:
        print(f"❌ Lỗi khi ghi file: {e}")

if __name__ == "__main__":
    # Cài đặt thư viện nếu chưa có: pip install faker
    khach_data = generate_data()
    write_csv(khach_data, OUTPUT_FILE)

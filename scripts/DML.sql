DELETE
FROM KHACH;
DELETE
FROM PHONG;
DELETE
FROM DATPHONG;

-- Xóa tất cả dữ liệu trong bảng trước khi insert

\copy KHACH FROM 'mock-data/KHACH.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',', ENCODING 'UTF8');
\copy PHONG FROM 'mock-data/PHONG.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',', ENCODING 'UTF8');
\copy DATPHONG FROM 'mock-data/DATPHONG.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',', ENCODING 'UTF8');

UPDATE PHONG p
SET MaDatHienTai = (
    SELECT d.MaDat
    FROM DATPHONG d
    WHERE d.MaPhong = p.MaPhong
    ORDER BY d.NgayTra DESC  -- Chọn  phòng gần nhất làm phòng đặt
    LIMIT 1
)


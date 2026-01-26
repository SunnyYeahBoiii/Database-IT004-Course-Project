DROP VIEW IF EXISTS view_phong_co_ban CASCADE;
DROP VIEW IF EXISTS view_phong_so_luot_dat CASCADE;
DROP VIEW IF EXISTS view_datphong_daydu CASCADE;

-- VIEW 1: Mã phòng, loại phòng, giá/đêm
CREATE OR REPLACE VIEW view_phong_co_ban AS
SELECT MaPhong, LoaiPhong, GiaDem
FROM PHONG;

-- VIEW 2: Phòng + số lượt đặt
CREATE OR REPLACE VIEW view_phong_so_luot_dat AS
SELECT 
    p.MaPhong,
    p.LoaiPhong,
    COALESCE(COUNT(d.MaDat), 0) as SoLuotDat
FROM PHONG p
LEFT JOIN DATPHONG d ON p.MaPhong = d.MaPhong
GROUP BY p.MaPhong, p.LoaiPhong
ORDER BY SoLuotDat DESC, p.MaPhong;

-- VIEW 3: Đặt phòng đầy đủ
CREATE OR REPLACE VIEW view_datphong_daydu AS
SELECT 
    d.MaDat,
    k.HoTen,
    d.MaPhong,
    p.LoaiPhong,
    d.NgayNhan,
    d.NgayTra
FROM DATPHONG d
JOIN KHACH k ON d.MaKhach = k.MaKhach
JOIN PHONG p ON d.MaPhong = p.MaPhong
ORDER BY d.NgayNhan DESC, d.MaDat;


--- TEST VIEWS
SELECT 'VIEW 1 - 5 phòng đầu' as Test;
SELECT * FROM view_phong_co_ban LIMIT 5;

SELECT 'VIEW 2 - Top 5 phòng hot nhất' as Test;
SELECT * FROM view_phong_so_luot_dat LIMIT 5;

SELECT 'VIEW 3 - 5 booking gần nhất' as Test;
SELECT * FROM view_datphong_daydu LIMIT 5;
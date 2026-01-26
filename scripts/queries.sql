-- Test 1: Giá >= 1tr
SELECT MaPhong, LoaiPhong, GiaDem 
FROM PHONG 
WHERE GiaDem >= 1000000;

-- Test 2: Khách đặt >= 3 lần
SELECT k.MaKhach, k.HoTen, COUNT(*) as SoLan
FROM KHACH k
JOIN DATPHONG d ON k.MaKhach = d.MaKhach
GROUP BY k.MaKhach, k.HoTen
HAVING COUNT(*) >= 3;

-- Test 3: Mã đặt hiện tại
SELECT p.MaPhong, p.MaDatHienTai
FROM PHONG p
LEFT JOIN DATPHONG d ON p.MaDatHienTai = d.MaDat;
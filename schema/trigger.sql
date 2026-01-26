

-- TRIGGER 1 – DATPHONG
-- NgayTra >= NgayNhan

CREATE OR REPLACE FUNCTION trg_check_ngay_datphong()
RETURNS trigger AS $$
BEGIN
    IF NEW.NgayTra IS NOT NULL
       AND NEW.NgayTra < NEW.NgayNhan THEN
        RAISE EXCEPTION 'NgayTra khong duoc nho hon NgayNhan';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_ngay_datphong
BEFORE INSERT OR UPDATE ON DATPHONG
FOR EACH ROW
EXECUTE FUNCTION trg_check_ngay_datphong();

-- TRIGGER 2 – PHONG
-- MaDatHienTai phai thuoc dung phong

CREATE OR REPLACE FUNCTION trg_check_madat_hientai()
RETURNS trigger AS $$
BEGIN
    IF NEW.MaDatHienTai IS NOT NULL THEN
        IF NOT EXISTS (
            SELECT 1
            FROM DATPHONG
            WHERE MaDat = NEW.MaDatHienTai
              AND MaPhong = NEW.MaPhong
        ) THEN
            RAISE EXCEPTION
            'MaDatHienTai khong thuoc phong nay';
        END IF;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_madat_hientai
BEFORE UPDATE OF MaDatHienTai ON PHONG
FOR EACH ROW
EXECUTE FUNCTION trg_check_madat_hientai();

-- TRIGGER 3 – KHACH
-- Khong cho DELETE neu con DATPHONG
ALTER TABLE DATPHONG
DROP CONSTRAINT fk_dp_khach;

CREATE OR REPLACE FUNCTION trg_block_delete_khach()
RETURNS trigger AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM DATPHONG
        WHERE MaKhach = OLD.MaKhach
    ) THEN
        RAISE EXCEPTION
        'Khach dang co don dat phong, khong the xoa';
    END IF;
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER block_delete_khach
BEFORE DELETE ON KHACH
FOR EACH ROW
EXECUTE FUNCTION trg_block_delete_khach();
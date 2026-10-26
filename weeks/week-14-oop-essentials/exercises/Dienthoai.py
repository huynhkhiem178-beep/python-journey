class DienThoai:
  def _init_(self, MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan):
      self.MaMay = MaMay
      self.TenMay = TenMay
      self.HangSanXuat = HangSanXuat
      self.DungLuongPin = DungLuongPin
      self.GiaBan = GiaBan

  def thongtindienthoai(self):
      print("Ma may:", self.MaMay)
      print("Ten may:", self.TenMay)
      print("Hang san xuat:", self.HangSanXuat)
      print("Dung luong pin:" self.DungLuongPin, "mAh")
      print("Gia ban:" self.GiaBan, "VND")
      print("--------------------------")

dt1 = DienThoai("DT01", "iphone 15 Pro", "Apple", 3274, 28990000)
dt2 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)

dt1.thongtindienthoai()
dt2.thongtindienthoai()

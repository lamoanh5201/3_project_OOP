import argparse

parser = argparse.ArgumentParser() #tạo bộ đọc lệnh từ dòng lệnh
parser.add_argument("--msg", type=str, help="Message to print") 
# --msg là đối số người dùng nhập vào, --help dùng để in ra khi người dùng cần trợ giúp
args = parser.parse_args() #lấy giá trị người dùng đã nhập từ dòng lệnh

print("Bạn vừa nhập:", args.msg)

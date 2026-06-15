player_stats_list = [
    ("Faker", "10", "2", "8"),      
    ("ShowMaker", "15", "0", "10"), 
    ("Chovy", "12", "ba", "5")      
]


def calculate_kda(kills: str, deaths: str, assists: str) -> float:
    """Tính KDA theo công thức chuẩn"""
    return (int(kills) + int(assists)) / int(deaths)


def process_kda_stats(stats_list):
    """Hàm chính xử lý danh sách thống kê"""
    print("--- BẢNG XẾP HẠNG KDA ---")
    
    for player in stats_list:
        name = player[0]
        kills = player[1]
        deaths = player[2]
        assists = player[3]
        
        try:
            kda = calculate_kda(kills, deaths, assists)
            print(f"Tuyển thủ {name} có chỉ số KDA là: {kda:.2f}")
            
        except ZeroDivisionError:
            print(f"{name}: KDA Hoàn hảo (Perfect Game)!")
            
        except ValueError:
            print(f"{name}: Lỗi dữ liệu không hợp lệ!")
            


process_kda_stats(player_stats_list)
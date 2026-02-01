def format_name(full_name: str) -> str:
    full_name = "Aliyev, Vali, G'aniyevich"
    qismlar = full_name.split()
    print(f"{qismlar[1]} {qismlar[2]}, {qismlar[0]}") 
    
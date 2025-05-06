from models.auto_model import AutoModel

def poblar_autos():
    autos = [
        ("NUEVO", "NISSAN", 6),
        ("USADOS", "NISSAN", 4),
        ("NUEVO", "CHEVROLET", 6),
        ("USADOS", "VOLKSWAGEN", 4),
        ("USADOS", "HONDA", 8),
        ("NUEVO", "TOYOTA", 4),
        ("USADOS", "FORD", 4),
        ("NUEVO", "HYUNDAI", 6),
        ("USADOS", "KIA", 6),
        ("USADOS", "HONDA", 4),
        # Agrega más si lo necesitas...
    ]

    auto_model = AutoModel()
    for estado, marca, cilindros in autos:
        result = auto_model.add(estado, marca, cilindros)
        print(result)

if __name__ == "__main__":
    poblar_autos()

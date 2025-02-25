
while True:
    try:
        money = float(input("Enter amount: "))


        source = input("Enter source currency code (usd, eur, jpy, gbp, aud, cad, chf, cny, sek, nzd, php, krw, sgd, inr, rub, try, brl, zar, hkd): ").lower()
        target = input("Enter target currency code (usd, eur, jpy, gbp, aud, cad, chf, cny, sek, nzd, php, krw, sgd, inr, rub, try, brl, zar, hkd): ").lower()

        dict = {
            "usd": 1,
            "eur": 0.84,
            "jpy": 110.17,
            "gbp": 0.72,
            "aud": 1.29,
            "cad": 1.25,
            "chf": 0.92,
            "cny": 6.46,
            "sek": 8.41,
            "nzd": 1.39,
            "php": 48.51,
            "krw": 1130.10,
            "sgd": 1.35,
            "inr": 74.13,
            "rub": 74.13,
            "try": 8.63,
            "brl": 5.29,
            "zar": 14.68,
            "hkd": 7.75,
        }

        if source not in dict or target not in dict:
            print("Invalid currency code")
            continue
        else:
            break
    except: 
        KeyboardInterrupt
        ValueError
        print("Invalid input")
        continue


print("Currency Converter")


target_money = money / dict[source] * dict[target]

print(f"{money} {source.upper()} = {target_money} {target.upper()}")

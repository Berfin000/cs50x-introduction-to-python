from datetime import date
import sys
import inflect

p = inflect.engine()


def main():
    user_input = input("Date of Birth: ")
    try:
        # Doğum tarihini alıp nesneye dönüştürüyoruz
        birth_date = get_date(user_input)
    except ValueError:
        sys.exit("Invalid date")

    # Bugünün tarihiyle arasındaki dakika farkını hesaplıyoruz
    today = date.today()
    minutes = calculate_minutes(birth_date, today)

    # Dakikayı kelimelere döküyoruz
    output_text = minutes_to_words(minutes)
    print(output_text)


def get_date(date_str):
    # ISO formatına (YYYY-MM-DD) uygun mu kontrol eder ve date nesnesi döner
    return date.fromisoformat(date_str)


def calculate_minutes(birth_date, current_date):
    # İki tarih arasındaki gün farkını alıp dakikaya çevirir
    # date nesnelerinin birbirinden çıkarılması bize timedelta nesnesi döndürür (__sub__ overload)
    delta = current_date - birth_date
    return delta.days * 24 * 60


def minutes_to_words(minutes):
    # Sayıyı kelimelere döker ve aradaki "and" bağlaçlarını temizler
    words = p.number_to_words(minutes, wantlist=False)
    # "and" kelimesini kaldırıyoruz
    words = words.replace(" and", "")
    # İlk harfi büyük yapıp sonuna " minutes" ekliyoruz
    return f"{words.capitalize()} minutes"


if __name__ == "__main__":
    main()

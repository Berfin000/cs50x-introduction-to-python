class Jar:
    def __init__(self, capacity=12):
        # Kapasite doğrulaması setter metodu aracılığıyla yapılacak
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0  # Başlangıçta kavanoz boş

    def __str__(self):
        # size sayısı kadar kurabiye emojisi döner
        return "🍪" * self.size

    def deposit(self, n):
        # Eklemek istediğimiz miktar negatif olamaz
        if n < 0:
            raise ValueError("Cannot deposit a negative number of cookies")
        # Kapasite aşımı kontrolü
        if self.size + n > self.capacity:
            raise ValueError("Exceeds jar capacity")
        self._size += n

    def withdraw(self, n):
        # Almak istediğimiz miktar negatif olamaz
        if n < 0:
            raise ValueError("Cannot withdraw a negative number of cookies")
        # Yeterli kurabiye var mı kontrolü
        if self.size - n < 0:
            raise ValueError("Not enough cookies in the jar")
        self._size -= n

    @property
    def capacity(self):
        # Kapasiteyi okumak için getter metodu
        return self._capacity

    @property
    def size(self):
        # Mevcut kurabiye sayısını okumak için getter metodu
        return self._size

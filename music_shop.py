

class MusicalInstrumentShopManager:
    def __init__(self) -> None:
        self.wind_instruments = MusicInstrumentBox("wind")
        self.percussion_instruments = MusicInstrumentBox("percussion")
        self.string_instruments = MusicInstrumentBox("string")

    def add_instrument(self, type: str, name: str, brand: str, country: str, price: float, material: str) -> None:
        if type == "wind":
            self.wind_instruments.add_instrument(name, brand, country, price, material)
        elif type == "percussion":
            self.percussion_instruments.add_instrument(name, brand, country, price, material)
        elif type == "string":
            self.string_instruments.add_instrument(name, brand, country, price, material)

    def get_music_band_instruments(self):
        music_band_instruments = []
        if "guitar" in self.string_instruments.instruments:
            music_band_instruments.append(self.string_instruments.instruments["guitar"][0])
        if "drums" in self.percussion_instruments.instruments:
            music_band_instruments.append(self.percussion_instruments.instruments["drums"][0])
        if "flute" in self.wind_instruments.instruments:
            music_band_instruments.append(self.wind_instruments.instruments["flute"][0])
        return music_band_instruments

    def get_all_instruments_in_one_list(self):
        all_wind_instruments_info = []
        for type in self.wind_instruments.instruments:
            for temp in self.wind_instruments.instruments[type]:
                all_wind_instruments_info.append(temp)
        all_percussion_instruments_info = []
        for type in self.percussion_instruments.instruments:
            for temp in self.percussion_instruments.instruments[type]:
                all_percussion_instruments_info.append(temp)
        all_string_instruments_info = []
        for type in self.string_instruments.instruments:
            for temp in self.string_instruments.instruments[type]:
                all_string_instruments_info.append(temp)
        self.all_instruments = all_string_instruments_info + all_percussion_instruments_info + all_wind_instruments_info

    def get_instruments_sorted_by_price(self, is_reversed = False):
        
        if is_reversed:
            self.all_instruments.sort(key = lambda x:x[3], reverse = True)
        else:
            self.all_instruments.sort(key = lambda x:x[3])
        return self.all_instruments

    def get_instruments_sorted_by_material(self, is_reversed = False):
        if is_reversed:
            self.all_instruments.sort(key = lambda x:x[4], reverse = True)
        else:
            self.all_instruments.sort(key = lambda x:x[4])
        return self.all_instruments

class MusicInstrumentBox:

    def __init__(self, type: str) -> None:
        self.type = type
        self.instruments = {}       #key - name, value - list of MusicInstumentInfo objects

    def add_instrument(self, name: str, brand: str, country: str, price: float, material: str) -> None:
        new_instrument = MusicInstrumentInfo(name, brand, country, price, material)
        if name in self.instruments:
            self.instruments[name].append(new_instrument)
        else:
            self.instruments[name] = [new_instrument,]

class MusicInstrumentInfo:
    def __init__(self, type: str, name: str, brand: str, country: str, price: float, material: str) -> None:
        self.type = type
        self.name = name
        self.brand = brand
        self.country = country
        self.price = price
        self.material = material


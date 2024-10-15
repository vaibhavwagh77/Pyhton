class URLShortener:
    def __init__(self):  
        self.url_dict = {}
        self.base_url = "http://short.url/"
        self.url_count = 1  

    def add_url(self, original_url):
        if original_url in self.url_dict:
            print(f"URL already exists: {self.url_dict[original_url]}")
            return self.url_dict[original_url]
        
        short_url = self.base_url + "v" + str(self.url_count)
        self.url_dict[original_url] = short_url
        self.url_count += 1  

        return short_url

    def display_urls(self):
        for original, short in self.url_dict.items():
            print(f"{original} -> {short}")

shortener = URLShortener()
print(shortener.add_url("https://www.example.com"))
print(shortener.add_url("https://www.python.com"))
print(shortener.add_url("https://www.pandas.com"))
shortener.display_urls()

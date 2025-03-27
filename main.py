meme_sozlugu = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "ROFL bir şakaya karşılıktır, LOL gibidir"
            "UWU":UWU bir sevimli bir kelimedir             
            "OWO":OWO uwuya benzeyen bir sevimli tatlı daha çirkin kelimedir                              
            "ANİME":ANİME bir çinli animasyonundaki kişilere denir                                        }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if kelime in nem_sozlugu.keys():
    print(nem_sozlugu[kelime])
else:
    print("Henüz bu kelimeye sahip değiliz... Ama üzerinde çalışıyoruz!")

import discord
import random

# Botun ayrıcalıklarını tanımlayalım
intents = discord.Intents.default()
intents.message_content = True

# Bot oluşturalım ve ayrıcalıkları aktaralım
client = discord.Client(intents=intents)

# Plastik el işleri fikirleri içeren bir liste oluşturalım
plastik_el_isleri = [
    "Boş plastik şişeleri dekoratif vazolara dönüştürün.",
    "Yakacak olarak kullanabilirsin ama soba,ocak gibi şeylerden bahsetmedim. Ormanda ateş yakarken plastikler petrolden olduğu için ateşi güzel yakabilirsin ve ateş şovu olur.",
    "Tutacak yapabilirsin!(telefon tutacağı vs.)",
    "Yerden bulduğun çöplerle istediğin bir şeyi yap. Böylece geri dönüşüm yapmış olursun",
    "Pet şişeden erik toplayıcı yapabilirsin!",
    "Plastiklerle duvara ses yalıtımı yapabilirsin belki..."
]

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!plastik_el_isleri'):
        # Rastgele bir plastik el işi fikri seçelim
        fikir = random.choice(plastik_el_isleri)
        await message.channel.send(f"İşte bir plastik el işi fikri: {fikir}")

# Botu çalıştıralım
client.run("MTE5Njg1NTMxMzkwMzY2MTE0Nw.GIZfsu.yjV1S_7zWsryEML3XNPs2W4cOn-4EHPBSm6SqU")

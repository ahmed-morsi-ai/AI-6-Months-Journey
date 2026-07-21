import requests

print("--- 💰 اعرف سعر البيتكوين الحالي ---")
url = "https://api.coindesk.com/v1/bpi/currentprice.json"

print("\nجاري الاتصال بقاعدة البيانات العالمية...")

try:
    response = requests.get(url)
    data = response.json()
    expected_price = data["bpi"]["USD"]["rate"]
    
    print("-" * 30)
    print(f"✅ سعر البيتكوين (Bitcoin) الآن هو: {expected_price} دولار")

except requests.exceptions.ConnectionError:
    print("-" * 30)
    print("❌ عذراً: يبدو أن هناك مشكلة في الاتصال بالإنترنت، أو أن السيرفر لا يستجيب.")
    print("يرجى التحقق من اتصالك والمحاولة لاحقاً.")
    
except KeyError:
    print("-" * 30)
    print("❌ عذراً: السيرفر أرسل بيانات غير متوقعة أو تم تغيير شكل واجهة برمجة التطبيقات (API).")
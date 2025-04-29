import yfinance as yf
import feedparser

def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    todays_data = stock.history(period='1d')
    return todays_data['Close'].iloc[-1]

print(get_stock_price('AAPL'))  # Exemple : prix Apple



def get_rss_feed(url):
    feed = feedparser.parse(url)
    for entry in feed.entries[:5]:  # Juste les 5 premiers
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}\n")

get_rss_feed("https://www.lesechos.fr/rss/finance-marches.xml")
get_rss_feed("https://www.latribune.fr/rss/rubrique/finance.xml")

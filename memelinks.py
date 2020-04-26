#! /bin/python3
'''`memelinks` module contains `memelinks()` module which displays list of \
Twitter hashtag links in browser.'''
from flask import Flask
from flask import render_template


APP = Flask(__name__)


@APP.route('/popular')
def popular():
    '''Displays popular Twitter hashtag links in browser.'''
    POP_HASHTAGS = [
        'Medicaid', 'Ethereum', 'Crypto', 'Crowdfunding', 'Giveaway', 'TBT',
        'Contest', 'BlackHistoryMonth', 'WomensHistoryMonth', 'Cryptocurrency',
        'WomensDay', 'HappyBirthday', 'Authentication', 'Win', 'Medicare',
        'InternationalWomensDay', 'InfluencerMarketing', 'Opioid',
        'HealthInsurance', 'QA', 'Funny', 'WomenInSTEM', 'IWD2019',
        'Photography', 'MondayMotivation', 'OOTD', 'Vegan', 'TravelTuesday']
    POP_DICT = {}
    for ht in POP_HASHTAGS:
        POP_DICT[ht] = f'https://twitter.com/hashtag/{ht}?f=live'
    return render_template('pop.htm', pop_hashtags=POP_HASHTAGS,
                           pop_dict=POP_DICT)


@APP.route('/crypto')
def crypto():
    '''Displays Twitter crypto hashtag links in browser.'''
    CRYPTO_HASH = [
        'Crypto', 'Cryptocurrency', 'CryptoNews', 'CryptoContest',
        'CryptoPayments', 'CryptoTrading', 'CryptoCurrencies',
        'CryptoMonday', 'CryptoGiveaway', 'Altcoin', 'Altcoins',
        'ICO', 'Ripple', 'Ethereum', 'Bitcoin', 'EthereumClassic',
        'Blockchain', 'BitcoinMining', 'Mining', 'Coinbase', 'Binance']
    CRYPTO_FIN = [
        'ETH', 'XRP', 'LTC', 'BTC', 'BCH', 'ETC', 'Doge', 'EOS']
    DICT_HASH = {}
    DICT_FIN = {}
    for ht1 in CRYPTO_HASH:
        DICT_HASH[ht1] = f'https://twitter.com/search?q=%23{ht1}&f=live'
    for ht2 in CRYPTO_FIN:
        DICT_FIN[ht2] = f'https://twitter.com/search?q=%24{ht2}&f=live'
    return render_template('crypto.htm',
                           crypto_hash=CRYPTO_HASH, crypto_fin=CRYPTO_FIN,
                           dict_hash=DICT_HASH, dict_fin=DICT_FIN)

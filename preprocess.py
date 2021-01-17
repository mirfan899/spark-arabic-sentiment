import re


def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)


def clean_tweet_ar(tweet=None):
    tweet = ' '.join(re.sub("(@[A-Za-z0–9]+)|([0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    punctuations = '''!()-![]{};:+'"\,<>./?@#$%^&*_~…،'''
    tweet = ''.join([i for i in tweet if not i in punctuations])
    tweet = remove_emoji(tweet)
    tweet = [(tweet, "")]
    return tweet


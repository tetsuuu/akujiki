from google_play_scraper import Sort, reviews, reviews_all
import pandas as pd


# YouTubeのapp_id
APP_ID = 'com.google.android.youtube'


all_result = reviews_all(
    APP_ID, # YouTubeのapp_id
    sleep_milliseconds=0,
    lang='ja',
    country='jp',
    sort=Sort.NEWEST,
)


result, continuation_token = reviews(
    APP_ID,
    lang='ja',
    country='jp',
    sort=Sort.NEWEST,
    count=20,
)


result, _ = reviews(
    APP_ID,
    continuation_token=continuation_token
)


print(result)


# 全件のデータをDataFrameに変換
# df_jp = pd.DataFrame(all_result)


# df_jp
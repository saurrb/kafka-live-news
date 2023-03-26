from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Load news records from CSV file
    news_df = pd.read_csv('news.csv', error_bad_lines=False, parse_dates=['publishedAt'])

    # Drop duplicate rows based on 'title' column
    # news_df = news_df.drop_duplicates(subset=['title'])

    # Format date and time
    news_df['publishedAt'] = pd.to_datetime(news_df['publishedAt']).dt.strftime('%Y-%m-%d %I:%M:%S %p')

    # Create a new column with HTML for the image
    news_df['image_html'] = news_df['urlToImage'].apply(lambda x: f'<img src="{x}" width="150" height="100">')

    # Sort news records by date in descending order
    # news_df = news_df.sort_values(by='publishedAt', ascending=False)

    # Render the news template with the news dataframe
    return render_template('news.html', news=news_df)

if __name__ == '__main__':
    app.run(debug=True)

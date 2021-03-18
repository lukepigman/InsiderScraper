# InsiderScraper
This is a small project to scrape OpenInsiders for its most recent stock filing.

The program will hit openinsider every 30 seconds to see if any new filings have been added.
When a new filing is added, the program will buy the stock using the percent of your buying power that you specify

<h1>How to use</h1>

1. Clone this repository
2. Sign up for Alpaca account
3. Copy your credentials over to the cred file
4. <b>Edit the values in the utils file to match the amount you want to spend per trade (order types coming soon!)</b>
5. Open your favorite python enabled terminal
6. Run py insiderProd.py or insiderPaper.py, depending on whether you want to run it on your paper account or live trading account
7. Sit back and watch the gains

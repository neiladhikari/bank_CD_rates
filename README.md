### My first successful web scraping project.
The objective was to get the current bank CD rates for various terms and names of the respective banks offering these rates. After searching a bit online, I found the website bankrate.com has the most updated and reader-friendly display of bank CD rates for various terms, 6-month, 1-year, 2-years, 3-years, 5-years. The website looked simple enough, but upon inspecting the html code, it was very long and complex. Took a LOT of trial and error, and lot of minute observations to figure out how to get to the information I was interested in.
I used BeautifulSoup for the scraping (as compared to Scrapy), because I like to view my output in the jupyter notebook cell rather than the terminal, and also because this seemed like a fairly simple and light project that didn't require the horsepower of Scrapy.

The initial steps are pretty straightforward and intuitive. These include loading the libraries and reading in the webpage:

<pre><code>
from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.bankrate.com/banking/cds/current-cd-interest-rates/")

soup = BeautifulSoup(page.content, 'html.parser')
</code></pre>

I discovered some cool functions such as "prettify", get_text, print(i.text) and so on.

eg. We can now print out the HTML content of the page, formatted nicely, using the prettify method on the BeautifulSoup object.

<pre><code>
print(soup.prettify())
</code></pre>

I used commands like below to see the output under various elements:

<pre><code>
soup.find_all('p') #p=paragraph
soup.find_all('ul') #ul=unlisted
soup.find_all('li') #li=lists
soup.find_all('div') #div=division
</code></pre>

After a lot of trial and error with these commands, and Chrome's Inspect module and seeing where things correspond on the webpage, I discovered that the main data for the website was embedded in a section or element called "div", under a class called "article__content". The function "find" (remember, use "find", not "find_all" in case of div, otherwise we cannot run further loops or searches on this object) found all occurrences of "article__content" under div. There was still a lot of unwanted information, and the information I was interested in was all spread out. First, I saved the results from this loop in an object called article_content. Next, by running the following loop, I found that the information I was interested in was under the h3 header (there were about 8 h3 headers).

<pre><code>
for i in article_content.find_all("h3"):
    print(i.text)
</code></pre>

I wanted the CD rates under the term headers, which described the duration of the CDs. I had figured out how to get the headers, now to figure out how to get the bank names and CD rates, which were contained in the "li" element under "ul". After doing some searches online, I got an idea to try something like this:

<pre><code>
for header in article_content.find_all(['h3']):
    print(header.get_text())
    for elem in header.next_siblings:
        if elem.name and elem.name.startswith('h3'):
            break
        if elem.name == 'ul':
            print(elem.get_text())
</code></pre>

So pretty much, for this kind of complex situation, writing a script is absolutely necessary. This worked great! And pulled up all the information I wanted, in exactly the format I wanted.

*This is also my first markdown script. Learnt how to insert code blocks, change heading sizes, and italicize letters.*

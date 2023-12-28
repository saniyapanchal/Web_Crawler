import { get } from 'axios';
import { load } from 'cheerio';

async function crawl(url) {
    const response = await get(url);
    const $ = load(response.data);

    $('a').each((i, link) => {
        console.log($(link).attr('href'));
    });
}

crawl('http://example.com');
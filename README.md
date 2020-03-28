# feedfetcher

News aggregator application, which collects summary of news from different categories from given RSS feed urls. It processes the RSS feeds asynchronously to get news content. Built using Python, Django, Django Rest framework & Celery. 


## Setup 

After running server on a terminal 

run one more terminal tab, go to root run 
`redis-server`

open another terminal tab, go to root and run 
`celery -A proj worker -l info -B`


### Screenshots

![Api-Result](https://github.com/lalit97/feedfetcher/blob/master/result.png)
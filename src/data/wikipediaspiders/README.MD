To populate the interim data folder, the following commands were run using scrapy from the 'src\data\wikipedia' directory

scrapy crawl prisch -O ../../../../data/interim/prisch.json
scrapy crawl postsec -O ../../../../data/interim/postsec.json
scrapy crawl secsch -O ../../../../data/interim/secsch.json
scrapy crawl unis -O ../../../../data/interim/unis.json
scrapy crawl jcs -O ../../../../data/interim/jcs.json
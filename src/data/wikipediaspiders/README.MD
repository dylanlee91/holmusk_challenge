To populate the external data folder, the following commands were run using scrapy from the 'src\data\wikipedia' directory

scrapy crawl prisch -O ../../../../../data/external/prisch.json
scrapy crawl postsec -O ../../../../../data/external/postsec.json
scrapy crawl secsch -O ../../../../../data/external/secsch.json
scrapy crawl unis -O ../../../../../data/external/unis.json
scrapy crawl jcs -O ../../../../../data/external/jcs.json
import scrapy
import datetime


class NoticiasSpider(scrapy.Spider):
    name = "noticias"
    allowed_domains = ["dataprev.gov.br"]
    start_urls = ["https://dataprev.gov.br/maisnoticias"]

    def parse(self, response):
        print("🚀 Página carregada:", response.url)

        # Guardando todas as noticias numa lista
        noticias = response.css('.view-content .views-row') # Parametros retirados da analise HTML
        print("📰 Total de notícias encontradas:", len(noticias))

        # Retirando informações de cada noticia em noticias
        for noticia in noticias:
            try:
                titulo = noticia.css(".field-name-title h2 a::text").get()
                link = noticia.css(".field-name-title h2 a::attr(href)").get()
                descricao = noticia.css(".field-name-body .field-item p::text").get()
                data_str = noticia.css(".field-name-post-date .field-item::text").get()

                print("🔍 Notícia encontrada:", titulo)

                # Converte a string para datetime
                data_obj = datetime.datetime.strptime(data_str, "%d/%m/%Y")

                # Filtra datas a partir de 09/04/2010
                if data_obj >= datetime.datetime(2010, 4, 9):
                    yield {
                        'titulo': titulo,
                        'link': link,
                        'descricao': descricao,
                        'data': data_obj.strftime("%Y-%m-%d")
                    }
            except Exception as e:
                print("⚠️ Erro ao processar notícia:", e)
                continue

        # Paginação: extrai o link da próxima página
        proxima_pagina = response.css('li.next a::attr(href)').get()
        if proxima_pagina:
            yield response.follow(proxima_pagina, callback=self.parse)



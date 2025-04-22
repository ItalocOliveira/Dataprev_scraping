# Scrapy - Coletando Notícias do Site da Dataprev

Este projeto utiliza o framework [Scrapy](https://scrapy.org/) para fazer scraping da aba de notícias do site oficial da [Dataprev](https://www.dataprev.gov.br/). O objetivo foi praticar técnicas de raspagem de dados, incluindo paginação, extração seletiva e tratamento de erros.

## 📌 Sobre o Projeto

O spider percorre todas as páginas da seção de notícias, extraindo:
- **Título**
- **Link da notícia**
- **Descrição**
- **Data de publicação**

As notícias extraídas são filtradas por uma data mínima (09/04/2010) e impressas no terminal ou salvas conforme o formato de saída escolhido.

---

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repo.git
   cd seu-repo
2. Execute o Crawler a partir da pasta principal do projeto:
   ```bash
   scrapy crawl noticia -o noticias.csv
   scrapy crawl noticia (caso não queira uma saída em .csv)

## [Explicação detalhada no Notion](https://www.notion.so/Web-Crawling-Web-Scraping-1dc2ff4aeac78059bfe7c6b77784e003)
